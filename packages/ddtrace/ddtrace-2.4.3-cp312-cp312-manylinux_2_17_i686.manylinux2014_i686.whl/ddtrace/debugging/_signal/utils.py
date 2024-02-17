from itertools import islice
from itertools import takewhile
from types import FrameType
from typing import Any
from typing import Callable
from typing import Dict
from typing import Iterable
from typing import List
from typing import Optional
from typing import Tuple
from typing import Type

from ddtrace.debugging._probe.model import MAXFIELDS
from ddtrace.debugging._probe.model import MAXLEN
from ddtrace.debugging._probe.model import MAXLEVEL
from ddtrace.debugging._probe.model import MAXSIZE
from ddtrace.debugging._redaction import REDACTED_PLACEHOLDER
from ddtrace.debugging._redaction import redact
from ddtrace.debugging._redaction import redact_type
from ddtrace.debugging._safety import get_fields
from ddtrace.internal.compat import BUILTIN_CONTAINER_TYPES
from ddtrace.internal.compat import BUILTIN_MAPPNG_TYPES
from ddtrace.internal.compat import BUILTIN_SIMPLE_TYPES
from ddtrace.internal.compat import CALLABLE_TYPES
from ddtrace.internal.compat import Collection
from ddtrace.internal.compat import ExcInfoType
from ddtrace.internal.compat import NoneType
from ddtrace.internal.safety import _isinstance
from ddtrace.internal.utils.cache import cached


EXCLUDED_FIELDS = frozenset(["__class__", "__dict__", "__weakref__", "__doc__", "__module__", "__hash__"])


@cached()
def qualname(_type: Type) -> str:
    try:
        return _type.__qualname__
    except AttributeError:
        try:
            return _type.__name__
        except AttributeError:
            return repr(_type)


def _serialize_collection(
    value: Collection, brackets: str, level: int, maxsize: int, maxlen: int, maxfields: int
) -> str:
    o, c = brackets[0], brackets[1]
    ellipsis = ", ..." if len(value) > maxsize else ""
    return "".join(
        (o, ", ".join(serialize(_, level - 1, maxsize, maxlen, maxfields) for _ in islice(value, maxsize)), ellipsis, c)
    )


def serialize(
    value: Any, level: int = MAXLEVEL, maxsize: int = MAXSIZE, maxlen: int = MAXLEN, maxfields: int = MAXFIELDS
) -> str:
    """Python object serializer.

    We provide our own serializer to avoid any potential side effects of calling
    ``str`` directly on arbitrary objects.
    """

    if _isinstance(value, CALLABLE_TYPES):
        return object.__repr__(value)

    if type(value) in BUILTIN_SIMPLE_TYPES:
        r = repr(value)
        return "".join((r[:maxlen], "..." + ("'" if r[0] == "'" else "") if len(r) > maxlen else ""))

    if not level:
        return repr(type(value))

    if type(value) not in BUILTIN_CONTAINER_TYPES:
        return "%s(%s)" % (
            type(value).__name__,
            ", ".join(
                (
                    "=".join((k, serialize(v, level - 1, maxsize, maxlen, maxfields)))
                    for k, v in islice(get_fields(value).items(), maxfields)
                    if not redact(k)
                )
            ),
        )

    if type(value) is dict:
        return "{%s}" % ", ".join(
            (
                ": ".join(
                    (
                        serialize(_, level - 1, maxsize, maxlen, maxfields)
                        for _ in (k, v if not (_isinstance(k, str) and redact(k)) else REDACTED_PLACEHOLDER)
                    )
                )
                for k, v in islice(value.items(), maxsize)
            )
        )
    elif type(value) is list:
        return _serialize_collection(value, "[]", level, maxsize, maxlen, maxfields)
    elif type(value) is tuple:
        return _serialize_collection(value, "()", level, maxsize, maxlen, maxfields)
    elif type(value) is set:
        return _serialize_collection(value, r"{}", level, maxsize, maxlen, maxfields) if value else "set()"

    msg = f"Unhandled type: {type(value)}"
    raise TypeError(msg)


def capture_stack(top_frame: FrameType, max_height: int = 4096) -> List[dict]:
    frame: Optional[FrameType] = top_frame
    stack = []
    h = 0
    while frame and h < max_height:
        code = frame.f_code
        stack.append(
            {
                "fileName": code.co_filename,
                "function": code.co_name,
                "lineNumber": frame.f_lineno,
            }
        )
        frame = frame.f_back
        h += 1
    return stack


def capture_exc_info(exc_info: ExcInfoType) -> Optional[Dict[str, Any]]:
    _type, value, tb = exc_info
    if _type is None or value is None:
        return None

    top_tb = tb
    if top_tb is not None:
        while top_tb.tb_next is not None:
            top_tb = top_tb.tb_next

    return {
        "type": _type.__name__,
        "message": ", ".join([serialize(v) for v in value.args]),
        "stacktrace": capture_stack(top_tb.tb_frame) if top_tb is not None else None,
    }


def redacted_value(v: Any) -> dict:
    return {"type": qualname(type(v)), "notCapturedReason": "redactedIdent"}


def redacted_type(t: Any) -> dict:
    return {"type": qualname(t), "notCapturedReason": "redactedType"}


def capture_pairs(
    pairs: Iterable[Tuple[str, Any]],
    level: int = MAXLEVEL,
    maxlen: int = MAXLEN,
    maxsize: int = MAXSIZE,
    maxfields: int = MAXFIELDS,
    stopping_cond: Optional[Callable[[Any], bool]] = None,
) -> Dict[str, Any]:
    return {
        n: (capture_value(v, level, maxlen, maxsize, maxfields, stopping_cond) if not redact(n) else redacted_value(v))
        for n, v in pairs
    }


def capture_value(
    value: Any,
    level: int = MAXLEVEL,
    maxlen: int = MAXLEN,
    maxsize: int = MAXSIZE,
    maxfields: int = MAXFIELDS,
    stopping_cond: Optional[Callable[[Any], bool]] = None,
) -> Dict[str, Any]:
    cond = stopping_cond if stopping_cond is not None else (lambda _: False)

    _type = type(value)

    if _type in BUILTIN_SIMPLE_TYPES:
        if _type is NoneType:
            return {"type": "NoneType", "isNull": True}

        if cond(value):
            return {
                "type": qualname(_type),
                "notCapturedReason": cond.__name__,
            }

        value_repr = serialize(value)
        value_repr_len = len(value_repr)
        return (
            {
                "type": qualname(_type),
                "value": value_repr,
            }
            if value_repr_len <= maxlen
            else {
                "type": qualname(_type),
                "value": value_repr[:maxlen],
                "truncated": True,
                "size": value_repr_len,
            }
        )

    if _type in BUILTIN_CONTAINER_TYPES:
        if level < 0:
            return {
                "type": qualname(_type),
                "notCapturedReason": "depth",
                "size": len(value),
            }

        if cond(value):
            return {
                "type": qualname(_type),
                "notCapturedReason": cond.__name__,
                "size": len(value),
            }

        collection: Optional[List[Any]] = None
        if _type in BUILTIN_MAPPNG_TYPES:
            # Mapping
            collection = [
                (
                    capture_value(
                        k,
                        level=level - 1,
                        maxlen=maxlen,
                        maxsize=maxsize,
                        maxfields=maxfields,
                        stopping_cond=cond,
                    ),
                    capture_value(
                        v,
                        level=level - 1,
                        maxlen=maxlen,
                        maxsize=maxsize,
                        maxfields=maxfields,
                        stopping_cond=cond,
                    )
                    if not (_isinstance(k, str) and redact(k))
                    else redacted_value(v),
                )
                for k, v in takewhile(lambda _: not cond(_), islice(value.items(), maxsize))
            ]
            data = {
                "type": qualname(_type),
                "entries": collection,
                "size": len(value),
            }

        else:
            # Sequence
            collection = [
                capture_value(
                    v,
                    level=level - 1,
                    maxlen=maxlen,
                    maxsize=maxsize,
                    maxfields=maxfields,
                    stopping_cond=cond,
                )
                for v in takewhile(lambda _: not cond(_), islice(value, maxsize))
            ]
            data = {
                "type": qualname(_type),
                "elements": collection,
                "size": len(value),
            }

        if len(collection) < min(maxsize, len(value)):
            data["notCapturedReason"] = cond.__name__
        elif len(value) > maxsize:
            data["notCapturedReason"] = "collectionSize"

        return data

    # Arbitrary object
    if level < 0:
        return {
            "type": qualname(_type),
            "notCapturedReason": "depth",
        }

    if redact_type(qualname(_type)):
        return redacted_type(_type)

    if cond(value):
        return {
            "type": qualname(_type),
            "notCapturedReason": cond.__name__,
        }

    fields = get_fields(value)
    captured_fields = {
        n: (
            capture_value(v, level=level - 1, maxlen=maxlen, maxsize=maxsize, maxfields=maxfields, stopping_cond=cond)
            if not redact(n)
            else redacted_value(v)
        )
        for n, v in takewhile(lambda _: not cond(_), islice(fields.items(), maxfields))
    }
    data = {
        "type": qualname(_type),
        "fields": captured_fields,
    }
    if len(captured_fields) < min(maxfields, len(fields)):
        data["notCapturedReason"] = cond.__name__
    elif len(fields) > maxfields:
        data["notCapturedReason"] = "fieldCount"

    return data
