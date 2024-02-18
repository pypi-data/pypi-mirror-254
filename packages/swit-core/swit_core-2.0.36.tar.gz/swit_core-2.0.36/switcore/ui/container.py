from switcore.pydantic_base_model import SwitBaseModel
from switcore.ui.button import Button
from switcore.ui.datepicker import DatePicker
from switcore.ui.select import Select


class Container(SwitBaseModel):
    type: str = "container"
    elements: list[Select | Button | DatePicker]

    class Config:
        smart_union = True
