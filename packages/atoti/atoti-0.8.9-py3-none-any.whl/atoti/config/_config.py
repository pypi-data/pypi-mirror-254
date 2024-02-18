from collections.abc import Mapping
from typing import Any, Optional, TypeVar

from .._path_utils import to_absolute_path

ConfigClass = TypeVar("ConfigClass")


class Config:
    @classmethod
    def _from_mapping(
        cls: type[ConfigClass], mapping: Mapping[str, Any]
    ) -> ConfigClass:
        """Take a mapping and return an instance of the class."""
        return cls(**mapping)


SubConfig = TypeVar("SubConfig", bound=Config)


def pop_optional_sub_config(
    data: dict[str, Any], *, attribute_name: str, sub_config_class: type[SubConfig]
) -> Optional[SubConfig]:
    return (
        sub_config_class._from_mapping(data.pop(attribute_name))
        if data.get(attribute_name) is not None
        else None
    )


def convert_path_to_absolute_string(config: Config, *attribute_names: str) -> None:
    for attribute_name in attribute_names:
        attribute_value = getattr(config, attribute_name)
        if attribute_value is not None:
            config.__dict__[attribute_name] = to_absolute_path(attribute_value)
