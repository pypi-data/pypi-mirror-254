from switcore.pydantic_base_model import SwitBaseModel


class Image(SwitBaseModel):
    type: str = "image"
    image_url: str
    alt: str | None = None
    style: dict | None = None
