from switcore.pydantic_base_model import SwitBaseModel
from switcore.ui.select_item import SelectItem


class Tabs(SwitBaseModel):
    """
        An element representing an array of tabs.
    """
    type: str = "tabs"
    tabs: list[SelectItem]
    value: str
