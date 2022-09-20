from dataclasses import dataclass
from .core import Dataclass
from typing import Optional, Any, Union

# dicts and Dataclass type are valid types
Meta = Union[dict, Dataclass]

SpecificationField = dict[Meta, Union[Any, tuple[Any, ...]], dict[Meta, Union[Any, tuple[Any, ...]]]]

Specification = Union[Dataclass, tuple[SpecificationField, ...]]


class SpecificationError(Exception):
    pass


@dataclass
class MetaFieldError:
    required_key: str
    required_types: Optional[tuple[type]] = None
    presented_type: Optional[type] = None
    presented_value: Any = None


class MetaVerification:

    def __init__(self, *errors: Union[MetaFieldError, "MetaVerification"]):
        self.error = errors
        self.checked_success: bool = False

    @staticmethod
    def verify(meta: Meta,
               specification: Optional[Specification] = None) -> "MetaVerification":
        if specification == None:
            raise SpecificationError
        meta_keys = meta.__dict__.keys()
        if isinstance(specification, tuple):
            print('Turple')
        else:
            print('Meta type')
        #TODO: create the comparasion method



def get_meta_attr(meta : Meta, key : str, default : Optional[Any] = None) -> Optional[Any]:
    if hasattr(meta, key):
        return getattr(meta, key)
    return default


def update_meta(meta: Meta, **kwargs):
    for key in kwargs:
        setattr(meta, key, kwargs[key])