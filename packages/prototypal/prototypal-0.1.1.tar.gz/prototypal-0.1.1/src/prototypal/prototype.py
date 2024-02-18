import types
import inspect


def _getattr(obj, name):
    try:
        return object.__getattribute__(obj, name)
    except AttributeError:
        return None


def _setattr(obj, name, val):
    object.__setattr__(obj, name, val)


def _proto_getattr(obj, name):
    val = _getattr(obj, name)
    if val is None:
        parent = _getattr(obj, '__proto__')
        val = _getattr(parent, name)
    return val


class ObjectMetaClass(type):
    def __repr__(cls):
        return "<constructor '%s'>" % cls.__name__


class Object(metaclass=ObjectMetaClass):
    prototype = None

    def __init__(self):
        self.__proto__ = self.prototype
        self.constructor = self.__class__

    def __getattribute__(self, name):
        # First, try to get the attribute normally
        try:
            return object.__getattribute__(self, name)
        except AttributeError:
            pass

        # If normal attribute access fails, try to get it from the prototype
        val = _proto_getattr(self, name)
        if val is not None:
            if isinstance(val, property):
                if val.fget is not None:
                    # If it's a property with a getter, call the getter
                    return val.fget(self)
            elif inspect.isfunction(val):
                # If it's a function, return a bound method
                return types.MethodType(val, self)
            else:
                # If it's a regular value, return it as is
                return val
        # If the attribute is not found even in the prototype, return None
        return None

    def __setattr__(self, name, val):
        # Check if we're defining a property on the prototype, not on an instance
        if isinstance(val, property) or not hasattr(self, '__dict__'):
            # Set the property on the class (which affects the prototype)
            cls = type(self)
            setattr(cls, name, val)
        else:
            # Try to get the attribute or property from the prototype
            prop = _proto_getattr(self, name)
            if isinstance(prop, property):
                if prop.fset is not None:
                    # If it's a property with a setter, call the setter
                    prop.fset(self, val)
                else:
                    # If it's a read-only property, raise an AttributeError
                    raise AttributeError(f"can't set attribute '{name}'")
            else:
                # If it's not a property, set the attribute normally
                object.__setattr__(self, name, val)

    def __delattr__(self, name):
        val = _proto_getattr(self, name)
        if isinstance(val, property) and val.fdel:
            val.fdel(self)
        else:
            object.__delattr__(self, name)

    def __repr__(self):
        return f"<{type(self).__name__} object at {hex(id(self))}>"


Object.prototype = Object()


def constructor(func):
    ret = type(func.__name__, (Object,), {})
    ret.prototype = ret()

    def init(self, *vargs, **kwargs):
        Object.__init__(self)
        func(self, *vargs, **kwargs)

    ret.__init__ = init
    return ret


# New feature: Simpler Syntax for Creating Prototypes
def create_prototype(**attrs):
    class Proto(Object):
        pass

    for name, value in attrs.items():
        setattr(Proto.prototype, name, value)
    return Proto()


# New feature: Chaining and Inheritance
def chain_prototypes(base, *others):
    class Chained(Object):
        pass

    for other in [base] + list(others):
        for name in dir(other.prototype):
            if not name.startswith('_'):
                setattr(Chained.prototype, name, getattr(other.prototype, name))
    return Chained()


# New feature: Cloning
def clone_prototype(original):
    return chain_prototypes(original)



