import collections.abc
import inspect
import typing


def validate(ttype) -> bool:
    def __false(msg) -> bool:
        print(f"Type {ttype} is not deser-compatible because: {msg}")
        return False

    if ttype == int:
        return True
    if ttype == float:
        return True
    if ttype == str:
        return True
    if ttype == bool:
        return True

    if isinstance(ttype, typing._GenericAlias):
        origin = typing.get_origin(ttype)
        if origin == list:
            inner_type = ttype.__args__[0]
            if validate(inner_type):
                return True
            else:
                return __false(f"list type {inner_type} is not a deser-compatible type")
        elif origin == dict:
            key_type = ttype.__args__[0]
            value_type = ttype.__args__[1]
            if key_type != str:
                return __false(f"dict key type {key_type} is not str")
            if validate(value_type):
                return True
            else:
                return __false(f"dict value type {value_type} is not a deser-compatible type")
        else:
            return __false(f"unsupported type {ttype}")

    spec = inspect.getfullargspec(ttype.__init__)
    constructor_args = set(spec.args[1:])
    if len(constructor_args) == 0:
        return __false("constructor doesn't have arguments")

    annotation_names = set(spec.annotations.keys())
    if constructor_args != annotation_names:
        return __false("not every constructor argument has a type hint")

    for type_hint in spec.annotations.values():
        if not validate(type_hint):
            return __false(f"constructor argument {type_hint} is not a deser-compatible type")

    return True


def serialize(value):
    if value is None:
        return None
    elif isinstance(value, int):
        return value
    elif isinstance(value, str):
        return value
    elif isinstance(value, float):
        return value
    elif isinstance(value, bool):
        return value
    elif isinstance(value, collections.abc.Sequence):
        return [serialize(it) for it in value]
    elif isinstance(value, dict):
        return {k: serialize(v) for k, v in value.items()}
    elif hasattr(value, '__dict__'):
        return serialize(value.__dict__)
    else:
        raise TypeError("Can't serialize type: %s" % type(value))


def deserialize(value, ttype):
    if value is None:
        return None

    if ttype == int:
        return int(value)
    if ttype == float:
        return float(value)
    if ttype == str:
        return str(value)
    if ttype == bool:
        return bool(value)

    if isinstance(ttype, typing._GenericAlias):
        origin = typing.get_origin(ttype)
        if origin == list:
            inner_type = ttype.__args__[0]
            return [deserialize(it, inner_type) for it in value]
        elif origin == dict:
            value_type = ttype.__args__[1]
            return {k: deserialize(v, value_type) for k, v in value.items()}
        else:
            raise TypeError("Can't deserialize type: %s" % type(value))

    spec = inspect.getfullargspec(ttype.__init__)
    constructor_args = set(spec.args[1:])
    annotations = spec.annotations
    dict_keys = set(value.keys())
    if constructor_args != dict_keys:
        raise TypeError("Deserialization problem: dict keys (%s) doesn't match constructor argument names (%s)" % (
            dict_keys, constructor_args))
    result = ttype(**{k: deserialize(v, annotations.get(k)) for k, v in value.items()})
    return result


def describe(o):
    if o is None:
        return "(None)"
    elif isinstance(o, int) or isinstance(o, str) or isinstance(o, float) or isinstance(o, bool):
        return "(%s) %s" % (type(o).__name__, o)
    elif isinstance(o, collections.abc.Sequence):
        return "[%s]" % ",".join([describe(it) for it in o])
    elif isinstance(o, dict):
        return "{%s}" % ",".join(["%s: %s" % (k, describe(v)) for k, v in o.items()])
    elif hasattr(o, '__dict__'):
        return "(%s) %s" % (type(o).__name__, describe(o.__dict__))
    else:
        return "(%s) %s" % (type(o).__name__, str(o))
