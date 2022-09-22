from dataclasses import dataclass
import inspect
from .core import Dataclass
from typing import Optional, Any, Union

# dicts and Dataclass type are valid types
Meta = Union[dict, Dataclass]

#dict[Meta, Union[Any, tuple[Any, ...]], dict[Meta, Union[Any, tuple[Any, ...]]]]
SpecificationField = Union[tuple[Union[tuple[str, Any], tuple[str, tuple[Any, ...]]]], Meta]

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
        self.checked_success: bool = True

    # TODO: сделать различный уровень вложенности для Specification
    # поэтому mypy будет ругаться, если с помощью него протестировать этот код
    @staticmethod
    def verify(meta: Meta,
               specification: Optional[Specification] = None) -> "MetaVerification":
        # Prepare function returns in advance
        res_success = MetaVerification()
        res_success.checked_success = True
        res_unsuccess = MetaVerification()
        res_unsuccess.checked_success = False

        if specification == None:
            return res_success

        # Make dict of specification
        if isinstance(specification, tuple):
            specification_dict = dict(specification)
        elif isinstance(specification, dict):
            specification_dict = specification
        else:
            attributes = inspect.getmembers(specification, lambda a: not (inspect.isroutine(a)))
            attributes = [a for a in attributes if not(a[0].startswith('__') and a[0].endswith('__'))]
            specification_dict = {key_i: type(val_i) for key_i, val_i in attributes}

        # Make dict of meta
        if isinstance(meta, dict):
            meta_dict = meta
        else:
            attributes_meta = inspect.getmembers(meta, lambda a: not (inspect.isroutine(a)))
            attributes_meta = [a for a in attributes_meta if not (a[0].startswith('__') and a[0].endswith('__'))]
            meta_dict = {key_i: val_i for key_i, val_i in attributes_meta}

        #Compare specification_dict with meta_dict
        for key_i in specification_dict.keys():
            if key_i not in meta_dict:
                return res_unsuccess
            if not isinstance(specification_dict[key_i], tuple):
                type_i = specification_dict[key_i]
                if not isinstance(meta_dict[key_i], type_i):
                    return res_unsuccess
            else:
                found_attrib_type = False
                for type_i in specification_dict[key_i]:
                    if isinstance(meta_dict[key_i], type_i):
                        found_attrib_type = True
                        break
                if not found_attrib_type:
                    return res_unsuccess

        return res_success


def get_meta_attr(meta : Meta, key : str, default : Optional[Any] = None) -> Optional[Any]:
    if hasattr(meta, key):
        return getattr(meta, key)
    return default


def update_meta(meta: Meta, **kwargs):
    for key in kwargs:
        setattr(meta, key, kwargs[key])