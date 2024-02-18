from switcore.pydantic_base_model import SwitBaseModel


class SearchInput(SwitBaseModel):
    type: str = 'search_input'
    action_id: str
    placeholder: str | None
    value: str | None
    disabled: bool = False
