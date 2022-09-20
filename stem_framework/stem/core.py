from typing import Optional
from typing_extensions import Protocol

def pascal_case_to_snake_case(name: str) -> str:
    ... # TODO()



class Named:
    _name: Optional[str] = None

    @property
    def name(self):
        ... # TODO()




class Dataclass(Protocol):
    a: int
    b: float
    c: list
