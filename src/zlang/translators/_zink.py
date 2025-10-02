from .t import T as Template
from ..logger import print_info, print_warn, print_error

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
    
    class ellipsis(none):
        def __init__(self):
            super().__init__()
        def __repr__(self):
            return f"<...>"

    class bool(obj):
        def __init__(self, value):
            super().__init__(bool(value))
        def __repr__(self):
            return f"<bool {self.value}>"
            
    class int(obj):
        def __init__(self, value):
            super().__init__(int(value))
        def __repr__(self):
            return f"<int {self.value}>"

    class str(obj):
        def __init__(self, value):
            super().__init__(str(value))
        def __repr__(self):
            return f"<str \"{self.value}\">"

    class bytes(obj):
        def __init__(self, value):
            super().__init__(bytes(value, "utf-8"))
        def __repr__(self):
            return f"<bytes {self.value}>"
    
    class list(obj):
        def __init__(self, value):
            super().__init__(list(value))
        def __repr__(self):
            return f"<list [{", ".join([repr(v) for v in self.value])}]>"
    
    class tuple(obj):
        def __init__(self, value):
            super().__init__(tuple(value))
        def __repr__(self):
            return f"<tuple [{", ".join([repr(v) for v in self.value])}]>"
        
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
                    var.set(value)
                    break
        def get(self, name: str):
            for var in self.value:
                if var.name == name:
                    return var
        def __repr__(self):
            return f"<vars [{", ".join([repr(v) for v in self.value])}]>"
    
    class pyfunc(obj):
        def __init__(self, func):
            super().__init__(func)
        def __call__(self, *args, **kwargs):
            self.value(*args, **kwargs)
        def __repr__(self):
            return f"<python func {self.value}>"

g = types.vars()
g.set("test", types.pyfunc(lambda: print("Hello, World")))

class T(Template):

    def __init__(self):
        super().__init__("Zink")
    
    # TODO: self.vars
    #def __call__(self, node: tuple[str, ...], dollar: str = "", indent: int = 0, vars: types.vars = g):
    #    pass
    
    def error(self, s):
        print_error(s)
        exit(8)

    def _program(s):
        out = []
        for stmt in s.n[1]:
            if (walked := s.wt(stmt)) != None: out.append((" "*s.indent)+str(walked))
        return out
    
    def _var(s):
        if s.n[1] == "$": return s.dollar
        return types.var_ref(s.n[1])
    
    def _NUMBER(s):                                                                 return types.int(s.n[1])
    def _STRING(s):                                                                 return types.str(s.n[1])
    def _BSTRING(s):                                                                return types.bytes(s.n[1])
#   def _RSTRING(s):                                                                return 
    def _TRUE(s):                                                                   return types.bool(True)
    def _FALSE(s):                                                                  return types.bool(False)
    def _NONE(s):                                                                   return types.none()
    def _ellipsis(s):                                                               return types.ellipsis()

    def _set(s):
        s.dollar = s.jwt(s.n[1], ", ")
        vars = [s.wt(node) for node in s.n[1]]
        vals = [s.wt(node) for node in s.n[2]]
        print(vars, vals)
        if len(vars) == 1:
            ... # set vars with self.vars
        else:
            if len(vars) != len(vals):
                s.error(f"Cannot unpack {len(vals)} value{"" if len(vals) == 1 else "s"} to {len(vars)} variables")
            for i, var in enumerate(vars):
                print(var, "=", vals[i])
                ... # set vars with self.vars