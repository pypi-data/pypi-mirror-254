"""Definitions for Netlify widgets"""

from __future__ import annotations
from typing import TypeVar, Optional, Union, Tuple, List

from pydantic import BaseModel


Hint = Union[Tuple[str, str], str]  # is this confused with pattern?


class Widget(BaseModel):
    """Base Widget that any other widget inherits from"""

    # common widget options
    name: str
    label: Optional[str] = None  # if None, name will be sluggified
    required: bool = False
    hint: Optional[Hint] = None

    def dict(self, exclude_none=True, **kwargs):
        return super().dict(exclude_none=exclude_none, **kwargs)


W = TypeVar('W', bound=Widget)
Widgets = List[W]


class StringWidget(Widget):
    """Widget that takes a string"""

    widget: str = 'string'


class NumberWidget(Widget):
    """Widget that takes a number"""

    widget: str = 'number'


class BooleanWidget(Widget):
    """Widget that represents a boolean (true or false) value"""

    widget: str = 'boolean'


class ColorWidget(Widget):
    """Widget that allows input of a color"""

    widget: str = 'color'


class MarkdownWidget(Widget):
    """Widget that allows input of markdown"""

    widget: str = 'markdown'


class ListWidget(Widget):
    """Widget that allows for a list of Widgets"""

    widget: str = 'list'
    fields: Widgets
    summary: Optional[str] = None


class SelectWidget(Widget):
    """Widget that allows for selection of various predefined (string) options"""

    widget: str = 'select'
    options: List[str]
    default: Union[List[str], str, None] = None


class ObjectWidget(Widget):
    """Widget that represents an object represented with fields as other widgets"""

    widget: str = 'object'
    summary: Optional[str] = None
    collapsed: Optional[bool] = None
    fields: Widgets


class ImageWidget(Widget):
    """Widget that allows selection of an image"""

    widget: str = 'image'
    choose_url: Optional[bool] = None


class RelationWidget(Widget):
    """Widget that allows drawing relations with other collections"""

    widget: str = 'relation'
    multiple: Optional[bool] = None
    collection: str
    search_fields: List[str]
    value_field: str
    display_fields: Optional[List[str]] = None


class DateTimeWidget(Widget):
    """Widget that allows the input of a date field"""

    widget: str = 'datetime'
    date_format: Optional[str] = None
    time_format: Optional[bool] = None
