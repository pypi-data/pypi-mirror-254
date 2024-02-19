from enum import Enum

from switcore.pydantic_base_model import SwitBaseModel


class TextareaSizeTypes(str, Enum):
    small = "small"
    medium = "medium"
    large = "large"


class Textarea(SwitBaseModel):
    type: str = "textarea"
    action_id: str
    placeholder: str | None
    value: str | None
    height: TextareaSizeTypes = TextareaSizeTypes.small
    disabled: bool = False
