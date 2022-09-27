from dataclasses import dataclass
from typing import ClassVar, Optional, List

@dataclass(frozen=True)
class APIModule(object):
    modules_dict: ClassVar[dict] = {}
    name: str
    classname: Optional[str]
    get_by: Optional[list]

    def __post_init__(self):
        self.modules_dict[self.name]=self

    @classmethod
    def get_module(cls, name: str) -> Optional['APIModule']:
        # potentiall raise a KeyError exception
        return cls.modules_dict[name]

    @classmethod
    def get_modules_list(cls,l) -> List['APIModule']:
        if not l:
            mod_list = cls.modules_dict.values()
        else:
            mod_list = list(map(cls.get_module, l))
        return mod_list
