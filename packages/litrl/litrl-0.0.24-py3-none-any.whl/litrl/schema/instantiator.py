from __future__ import annotations

import inspect
from typing import TYPE_CHECKING, Any, Generic, TypeVar, cast

if TYPE_CHECKING:
    import sys

    if sys.version_info[:2] >= (3, 11):
        from typing import Self
    else:
        from typing_extensions import Self

import hydra
from loguru import logger
from pydantic import RootModel
from pydantic.dataclasses import dataclass as pydantic_dataclass
from pydantic.dataclasses import is_pydantic_dataclass

InstanceClass = TypeVar("InstanceClass")


@pydantic_dataclass(frozen=True)
class InstantiatorClass(Generic[InstanceClass]):
    _target_: str

    @classmethod
    def is_instantiable(cls: type[Self], obj: type) -> bool:
        if obj == InstantiatorClass or (inspect.isclass(object=obj) and issubclass(obj, InstantiatorClass)):
            return True
        return False

    @classmethod
    def process_dict(  # noqa: PLR0913
        cls: type[Self],
        key_type: type,
        key: str,
        val: Any,
        info_dict: dict[str, Any],
        *,
        instantiate_children: bool,
    ) -> None:
        if key_type == list and instantiate_children:
            for list_item in val:
                logger.info(f"instantiating list item {list_item}")
        if cls.is_instantiable(obj=key_type):
            schema: InstantiatorClass[Any] = key_type(**info_dict[key])
            if instantiate_children:
                schema = schema.instantiate()
            info_dict[key] = schema
        elif is_pydantic_dataclass(key_type):
            sub_info_dict = info_dict[key]
            cls.cast_type(
                pydantic=RootModel(root=val),
                info_dict=sub_info_dict,
                instantiate_children=instantiate_children,
            )
            info_dict[key] = key_type(**sub_info_dict)

    @classmethod
    def cast_type(
        cls: type[Self],
        pydantic: RootModel[Any],
        info_dict: dict[str, Any],
        *,
        instantiate_children: bool,
    ) -> None:
        for key in info_dict:
            val = pydantic.root.__getattribute__(key)
            key_type = type(val)
            if key_type == list:
                objs: list[Any] = []
                for list_item in val:
                    if cls.is_instantiable(type(list_item)):
                        objs.append(list_item.instantiate())
                    else:
                        objs.append(list_item)
                info_dict[key] = objs
            else:
                cls.process_dict(
                    key_type=key_type,
                    key=key,
                    val=val,
                    info_dict=info_dict,
                    instantiate_children=instantiate_children,
                )

    def to_dict(self, pydantic_model: RootModel[Any]) -> dict[str, Any]:
        return pydantic_model.model_dump(exclude="_target_")  # type: ignore[no-any-return]

    def instantiate(self, *, _recursive_: bool | None = None) -> InstanceClass:
        pydantic_model = RootModel(root=self)
        info_dict = self.to_dict(pydantic_model)
        if _recursive_ is None:
            _recursive_ = cast(bool, info_dict.pop("_recursive_", True))
        self.cast_type(
            pydantic=pydantic_model,
            info_dict=info_dict,
            instantiate_children=_recursive_,
        )
        fabric: type[InstanceClass] = hydra.utils.instantiate(
            config={"_target_": self._target_},
            _partial_=True,
        )
        return fabric(**info_dict)
