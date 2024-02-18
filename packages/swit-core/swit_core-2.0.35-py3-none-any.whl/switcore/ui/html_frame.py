from switcore.pydantic_base_model import SwitBaseModel


class HtmlFrame(SwitBaseModel):
    type: str = 'html_frame'
    html_content: str
