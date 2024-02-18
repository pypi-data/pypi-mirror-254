from switcore.pydantic_base_model import SwitBaseModel


class DatePicker(SwitBaseModel):
    type: str = "datepicker"
    action_id: str
    placeholder: str | None = None
    trigger_on_input: bool = False
    value: str | None = None
