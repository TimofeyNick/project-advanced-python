import re
from typing import Optional
from typing_extensions import Protocol

def pascal_case_to_snake_case(name: str) -> str:
    out = name[0].lower()
    for i in range(1,len(name)-1):
        if name[i].islower():
            out += name[i]
        else:
            if name[i-1].islower():
                out += '_' + name[i].lower()
            else:
                if name[i+1].islower():
                    out += '_' + name[i].lower()
                else:
                    out += name[i].lower()
    out += name[len(name)-1]
    return out


class Named:
    _name: Optional[str] = None

    @property
    def name(self):
        if self._name is not None:
            return self._name
        else:
            return pascal_case_to_snake_case(self.__class__.__name__)



class Dataclass(Protocol):
    a: int
    b: float
    c: list
