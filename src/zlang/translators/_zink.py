from .t import T as Template
from ..logger import print_info, print_warn, print_error
import inspect

class errors:
    class BaseError(BaseException):
        def __init__(self, desc: str):
            self.desc = desc
        def __str__(self):
            return f"{type(self).__name__}: {self.desc}"
    class OperatorError(BaseError):
        def __init__(self, op: str, this: str, other: str | None):
            super().__init__(f"Cannot {op} \"{this}\" and \"{other}\"")
    class ArgumentError(BaseError):
        pass
    class ArgumentPositionError(ArgumentError):
        def __init__(self):
            super().__init__("Cannot have a positional argument after a keyword argument")

class types:
    class obj:
        def __init__(self, value):
            self.value = value
        def __repr__(self):
            return f"<obj {self.value}>"

    class none(obj):
        def __init__(self):
            super().__init__(None)
        def __repr__(self):
            return f"<none>"
        def __str__(self):
            return "None"
    
    class ellipsis(none):
        def __init__(self):
            super().__init__()
        def __repr__(self):
            return f"<...>"
        def __str__(self):
            return "..."

    class bool(obj):
        def __init__(self, value):
            super().__init__(bool(value))
        def __repr__(self):
            return f"<bool {self.value}>"
        def __str__(self):
            return "True" if self.value else "False"
        def __add__(self, other, error):
            match type(other):
                case types.int: return other.value + (1 if self.value else 0)
            raise error
        def __sub__(self, other, error):
            match type(other):
                case types.int: return other.value - (1 if self.value else 0)
            raise error
        def __radd__(self, other, error): return self.__add__(other, error)
        def __rsub__(self, other, error): return self.__sub__(other, error)

    class int(obj):
        def __init__(self, value):
            super().__init__(int(value))
        def __repr__(self):
            return f"<int {self.value}>"
        def __str__(self):
            return str(self.value)
        def __add__(self, other, error):
            match type(other):
                case types.int: return self.value + other.value
            raise error
        def __sub__(self, other, error):
            match type(other):
                case types.int: return self.value - other.value
            raise error
        def __radd__(self, other, error): return self.__add__(other, error)
        def __rsub__(self, other, error): return self.__sub__(other, error)

    class str(obj):
        def __init__(self, value):
            super().__init__(str(value))
        def __repr__(self):
            return f"<str \"{self.value}\">"
        def __str__(self):
            return self.value

    class bytes(obj):
        def __init__(self, value):
            super().__init__(bytes(value, "utf-8"))
        def __repr__(self):
            return f"<bytes {self.value}>"
    
    class pair(obj):
        def __init__(self, key, value):
            self.key = key
            super().__init__(value)
        def __repr__(self):
            return f"<pair {self.key} = {self.value}>"

    class tuple(obj):
        def __init__(self, value):
            super().__init__(tuple(value))
        def __repr__(self):
            return f"<tuple [{", ".join([repr(v) for v in self.value])}]>"
        def __str__(self):
            return f"[{", ".join([str(v) for v in self.value])}]"

    class list(obj):
        def __init__(self, value):
            super().__init__(list(value))
        def __repr__(self):
            return f"<list [{", ".join([repr(v) for v in self.value])}]>"
        def __str__(self):
            return f"[{", ".join([str(v) for v in self.value])},]"

    class dict(obj):
        def from_pairs(p):
            d = []
            for pair in p:
                d[pair.name] = pair.value
        def __init__(self, value):
            super().__init__(dict(value))

    class var_ref(obj):
        def __init__(self, name: str):
            super().__init__(name)
        def __repr__(self):
            return f"<var {self.value}>"

    class var(obj):
        def __init__(self, name: str, value = None):
            super().__init__(value)
            self.name = name
        def __repr__(self):
            return f"<var {self.name} = {self.value}>"
    
    class vars(list):
        def __init__(self):
            super().__init__([])
        def set(self, name: str, value):
            for var in self.value:
                if var.name == name:
                    var.value = value
                    break
            else:
                self.value.append(types.var(name, value))
        def get(self, name: str):
            for var in self.value:
                if var.name == name:
                    return var
        def overlay(self, base):
            for var in base.value:
                if not self.get(var.name):
                    self.set(var.name, var.value)
        def __repr__(self):
            return f"<vars [{", ".join([repr(v) for v in self.value])}]>"
    
    class pyfunc(obj):
        def __init__(self, func):
            super().__init__(func)
        def __repr__(self):
            return f"<python func {self.value}>"
    
    class func(obj):
        def __init__(self, args, body):
            self.args = args
            super().__init__(body)
        def __repr__(self):
            return f"<func {self.args}>"

class T(Template):
    g = types.vars()
    g.set("test", types.pyfunc(lambda: print("Hello, World")))

    def __init__(self, top: bool = True):
        super().__init__("Zink")
        self.top = top
    
    def __call__(self, node: tuple[str, ...], dollar: str = "", indent: int = 0, vars: types.vars = g):
        self.vars = vars
        return super().__call__(node, dollar, indent)
    
    def wt(self, node, dollar: str = None, indent: int = None, vars: types.vars = None):
        return type(self)(top=False)(node, dollar if dollar else self.dollar, indent if indent else self.indent, vars if vars else self.vars)
    def wtl(self, nodes, dollar: str = None, indent: int = None, vars: types.vars = None):
        return [self.wt(node, dollar, indent, vars) for node in nodes]
    def jwt(self, nodes, sep: str, dollar: str = None, indent: int = None, vars: types.vars = None):
        return sep.join(str(self.wt(node, dollar, indent, vars)) for node in nodes)
    def jfwt(self, nodes, func, sep: str, dollar: str = None, indent: int = None, vars: types.vars = None):
        return self.jwt(filter(func, nodes), sep, dollar, indent, vars)
    def sv(self, node, vars: types.vars = None):
        #if type(node) == list:
        if hasattr(node, "__iter__"):
            return [self.sv(x, vars) for x in node]
        if type(node) == types.var_ref:
            if (val := (vars if vars else self.vars).get(node.value)) == None:
                self.error(f"Variable \"{node.value}\" is not defined")
            return self.sv(val, vars)
        if type(node) == types.var:
            return self.sv(node.value, vars)
        return node
    def swt(self, node, dollar: str = None, indent: int = None, vars: types.vars = None):
        return self.sv(self.wt(node, dollar, indent, vars), vars)
    def swtl(self, nodes, dollar: str = None, indent: int = None, vars: types.vars = None):
        return self.sv(self.wtl(nodes, dollar, indent, vars), vars)
    
    def error(self, s):
        print_error(s)
        exit(8)

    def add(self, this, other):
        print(repr(this), repr(other))
        error = errors.OperatorError("add", type(this).__name__, type(other).__name__)
        try:
            if (attr := getattr(this, "__add__", None)):
                return attr(other, error)
        except type(error):
            try:
                if (attr := getattr(other, "__radd__", None)):
                    return attr(this, error)
            except type(error):
                raise error

    def _program(s):
        try:
            print("PROGRAM:", s.swtl(s.n[1]))
        except errors.BaseError as e:
            s.error(str(e))
    
    def _var(s):
        if s.n[1] == "$": return s.dollar
        return types.var_ref(s.n[1])
    
    def _NUMBER(s):
        return types.int(s.n[1])
    def _STRING(s):
        return types.str(s.n[1])
    def _BSTRING(s):
        return types.bytes(s.n[1])
#   def _RSTRING(s):
    def _TRUE(s):
        return types.bool(True)
    def _FALSE(s):
        return types.bool(False)
    def _NONE(s):
        return types.none()
    def _ellipsis(s):
        return types.ellipsis()
    def _output(s):
        o = s.swt(s.n[1])
        os = None
        if not (os := getattr(o, "__str__", None)):
            if not (os := getattr(o, "__repr__", None)):
                os = lambda: f"<{type(o).__name__}>"
        print(f">> {os()}")
            
    def _func(s):
        f = s.swt(s.n[1])
        a = s.wtl(s.n[2])
        if type(f) == types.pyfunc:
            fs = inspect.signature(f.value)
            fp_pos = sum(1 for p in fs.parameters if p.kind == p.POSITIONAL_ONLY)
            # TODO: remake function parameter checking to support T._default_arg()
            # if len(a) != fp_pos:
                # TODO: make error specify function name
                # s.error(f"Function required {fp_pos} parameters, called with {len(a)}")
            return f.value(*a)
        elif type(f) == types.func:
            l = types.vars()
            # TODO: add function argument handling
            for i, arg in enumerate(a):
                if type(arg) == types.pair: break
                l.set(f.args[i].value, s.sv(arg))
            for arg in a[len(l.value):]:
                if type(arg) != types.pair: errors.ArgumentPositionError()
                if l.get(arg.key): s.error(f"Multiple values for argument \"{arg.key}\"")
                l.set(arg.key, arg.value)
            l.overlay(s.vars)
            return s.wt(f.value, vars=l)
        else:
            s.error(f"Cannot call a non-callable object")
    
    def _tuple(s):
        return types.tuple(s.swtl(s.n[1]))
    def _list(s):
        return types.list(s.swtl(s.n[1]))
    def _dict(s):
        return types.dict(s.swtl(s.n[1]))
    
#   def _arg(s):                                                                    return f"*{s.n[1]}"
#   def _kwarg(s):                                                                  return f"**{s.n[1]}"
#   def _true_arg(s):                                                               return f"{s.n[1]} = True"
#   def _false_arg(s):                                                              return f"{s.n[1]} = False"
#   def _typed_arg(s):                                                              return f"{s.n[1]}: {s.wt(s.n[2])}"
    def _default_arg(s):
        return types.pair(s.n[1], s.wt(s.n[2]))
#   def _default_typed_arg(s):                                                      return f"{s.n[1]}: {s.wt(s.n[2])} = {s.wt(s.n[3])}"
    
    def _set(s):
        s.dollar = s.jwt(s.n[1], ", ")
        vars = [s.wt(node) for node in s.n[1]]
        vals = [s.wt(node) for node in s.n[2]]
        if len(vars) == 1:
            s.vars.set(vars[0].value, s.sv(vals if len(vals) > 1 else vals[0]))
        else:
            if len(vars) != len(vals):
                s.error(f"Cannot unpack {len(vals)} value{"" if len(vals) == 1 else "s"} to {len(vars)} variables")
            for i, var in enumerate(vars):
                s.vars.set(var.value, s.sv(vals[i]))

    def _add(s):
        return s.add(s.swt(s.n[1]), s.swt(s.n[2]))
    def _subtract(s):
        return s.subtract(s.swt(s.n[1]), s.swt(s.n[2]))

    def _func_def_untyped(s):
        s.vars.set(s.wt(s.n[1]), types.func(s.wtl(s.n[2]), s.n[3]))