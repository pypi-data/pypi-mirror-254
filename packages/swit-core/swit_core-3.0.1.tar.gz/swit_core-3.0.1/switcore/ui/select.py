from enum import Enum
from typing import Any

from pydantic import root_validator, validator

from switcore.pydantic_base_model import SwitBaseModel
from switcore.ui.element_components import Tag
from switcore.ui.image import Image
from switcore.ui.select_item import SelectItem


class NoOptionsReason(SwitBaseModel):
    message: str


class Option(SelectItem):
    """
        https://devdocs.swit.io/docs/user-actions/ref/schemas/select
    """
    icon: Image | None = None
    tag: Tag | None = None


class OptionGroup(SwitBaseModel):
    label: str
    options: list[Option]

    # add validator to check if options is not empty
    @validator('options')
    def options_must_not_be_empty(cls, v):
        if len(v) == 0:
            raise ValueError("options must not be empty")
        return v


class SelectStyleTypes(str, Enum):
    filled = "filled"
    outlined = "outlined"
    ghost = "ghost"


class Style(SwitBaseModel):
    variant: SelectStyleTypes = SelectStyleTypes.outlined


class SelectQuery(SwitBaseModel):
    query_server: bool = True
    disabled: bool = False
    placeholder: str | None = None
    value: str | None = None
    action_id: str | None = None


class Select(SwitBaseModel):
    type: str = 'select'
    placeholder: str | None = None
    multiselect: bool = False
    trigger_on_input: bool = False
    value: list[str] | None = None
    options: list[Option] = []
    option_groups: list[OptionGroup] = []
    no_options_reason: NoOptionsReason | None = None
    style: Style | None = None
    query: SelectQuery | None = None

    @root_validator
    def validate_options_exclusivity(cls, values: dict[str, Any]):
        options: list[Option] = values.get('options', [])
        option_groups: list[OptionGroup] = values.get('option_groups', [])
        if len(options) > 0 and len(option_groups) > 0:
            raise ValueError("Only one of 'options' or 'option_groups' should be provided.")
        return values
