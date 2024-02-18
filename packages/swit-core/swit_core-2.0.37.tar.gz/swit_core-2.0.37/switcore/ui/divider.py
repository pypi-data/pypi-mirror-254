from switcore.pydantic_base_model import SwitBaseModel


class Divider(SwitBaseModel):
    type: str = "divider"
