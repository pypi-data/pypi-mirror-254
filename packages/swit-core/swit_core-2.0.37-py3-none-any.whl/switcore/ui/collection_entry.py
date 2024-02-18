from enum import Enum

from switcore.pydantic_base_model import SwitBaseModel
from switcore.ui.element_components import SubText, Tag, StaticAction
from switcore.ui.image import Image
from switcore.ui.text_paragraph import TextParagraph


class TextStyle(SwitBaseModel):
    bold: bool = False
    color: str
    size: str
    max_lines: int


class BackgroundType(str, Enum):
    none = "none"
    lightblue = "lightblue"


class Background(SwitBaseModel):
    color: BackgroundType = BackgroundType.none


class MetadataItem(SwitBaseModel):
    type: str
    content: str | None = None
    style: dict | None = None
    image_url: str | None = None


class TextSection(SwitBaseModel):
    text: TextParagraph
    metadata_items: list[SubText | Image | Tag] | None = None


class VerticalAlignmentTypes(str, Enum):
    top = "top"
    middle = "middle"
    bottom = "bottom"


class CollectionEntry(SwitBaseModel):
    type: str = "collection_entry"
    start_section: Image | None = None
    text_sections: list[TextSection]
    vertical_alignment: VerticalAlignmentTypes = VerticalAlignmentTypes.top
    background: Background | None = None
    action_id: str | None = None
    static_action: StaticAction | None = None
    draggable: bool = False
