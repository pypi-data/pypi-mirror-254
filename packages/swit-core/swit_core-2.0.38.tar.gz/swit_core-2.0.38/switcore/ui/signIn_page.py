from switcore.pydantic_base_model import SwitBaseModel
from switcore.ui.Icon import Icon
from switcore.ui.button import Button


class IntegratedService(SwitBaseModel):
    icon: Icon


class SignInPage(SwitBaseModel):
    id: str | None = None
    type: str = "sign_in_page"
    integrated_service: IntegratedService
    title: str
    description: str
    button: Button
