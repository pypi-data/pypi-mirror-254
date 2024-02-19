from enum import Enum

from switcore.pydantic_base_model import SwitBaseModel


class InputVariant(str, Enum):
    text = 'text'
    select = 'select'


class Input(SwitBaseModel):
    type: str = 'text_input'
    action_id: str
    placeholder: str | None
    trigger_on_input: bool = False
    value: str | None
    variant: InputVariant = InputVariant.text
