from enum import Enum

from pydantic import root_validator

from switcore.pydantic_base_model import SwitBaseModel


class TagColorTypes(str, Enum):
    primary = "primary"
    secondary = "secondary"
    danger = "danger"


class TagShapeTypes(str, Enum):
    rectangular = "rectangular"
    rounded = "rounded"


class TagStyle(SwitBaseModel):
    color: TagColorTypes = TagColorTypes.secondary
    shape: TagShapeTypes = TagShapeTypes.rectangular

    class Config:
        use_enum_values = True

    @root_validator
    def check_color_and_shape(cls, values):
        color: TagColorTypes | None = values.get('color')
        shape: TagShapeTypes | None = values.get('shape')
        if color is None and shape is None:
            raise ValueError("color and shape cannot be None at the same time")
        return values


class Tag(SwitBaseModel):
    type: str = "tag"
    content: str
    style: TagStyle | None = None


class SubText(SwitBaseModel):
    type: str = "subtext"
    content: str


class OpenOauthPopup(SwitBaseModel):
    action_type: str = "open_oauth_popup"
    link_url: str


class OpenLink(SwitBaseModel):
    action_type: str = "open_link"
    link_url: str


class CloseView(SwitBaseModel):
    action_type: str = "close_view"


class WriteToClipboard(SwitBaseModel):
    action_type: str = "write_to_clipboard"
    content: str


StaticAction = OpenOauthPopup | OpenLink | WriteToClipboard | CloseView
