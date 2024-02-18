from typing import Optional

from switcore.pydantic_base_model import SwitBaseModel
from switcore.ui.Icon import Icon
from switcore.ui.element_components import StaticAction


class Button(SwitBaseModel):
    id: Optional[str] = None
    type: str = "button"
    label: str | None = None
    style: str | None = None
    disabled: bool | None = None
    action_id: str | None = None
    static_action: StaticAction | None = None
    icon: Icon | None = None
