from switcore.pydantic_base_model import SwitBaseModel
from switcore.ui.item import Item


class InfoCard(SwitBaseModel):
    type: str = 'info_card'
    items: list[Item]
    action_id: str | None = None
    draggable: bool = False
