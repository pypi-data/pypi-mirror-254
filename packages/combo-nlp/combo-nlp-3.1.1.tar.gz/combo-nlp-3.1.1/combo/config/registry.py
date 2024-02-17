from typing import Optional, Type, Dict, Tuple

from combo.config.exceptions import RegistryException


class Registry:
    __classes: Dict[str, Tuple[Type, str]] = {}
    __class_names: Dict[Tuple[Type[object], str], str] = {}

    @classmethod
    def classes(cls) -> Dict[str, Tuple[Type, str]]:
        return cls.__classes

    @classmethod
    def register(cls, registry_name: str, constructor_method: Optional[str] = None):
        def decorator(clz):
            nonlocal registry_name, constructor_method
            if constructor_method is None:
                constructor_method = '__init__'
            cls.__classes[registry_name.lower()] = (clz, constructor_method)
            cls.__class_names[(clz, constructor_method)] = registry_name.lower()
            return clz

        return decorator

    @classmethod
    def resolve(cls, class_name: str) -> Optional[Tuple[Type, str]]:
        try:
            return cls.__classes[class_name.lower()]
        except KeyError:
            raise RegistryException('No registered name ' + class_name.lower())

    @classmethod
    def get_class_name(cls, clz: Type[object], constructor_method: Optional[str] = None) -> Optional[str]:
        try:
            if constructor_method is None:
                constructor_method = '__init__'
            return cls.__class_names[(clz, constructor_method)]
        except KeyError:
            raise RegistryException('Class ' + str(clz) + ' is not registered!')
