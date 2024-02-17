"""Collections for file entries to be placed"""

from __future__ import annotations
from typing import Optional, List

from pydantic import BaseModel

from netlifyconfig.widgets import Widgets


class Collection(BaseModel):
    """Represents a collection in the netlify editor.
    For information on collections, see https://www.netlifycms.org/docs/configuration-options/#collections
    """

    name: str
    """unique identifier for the collection, used as the key when referenced in other contexts
    (like the relation widget)"""
    identifier_field: Optional[str] = None
    label: Optional[str]
    """label for the collection in the editor UI; defaults to the value of ``name``"""
    label_singular: Optional[str] = None
    """singular label for certain elements in the editor; defaults to the value of ``label``"""
    description: Optional[str] = None
    """optional text, displayed below the label when viewing a collection"""
    delete: Optional[bool] = None
    """``False`` prevents users from deleting items in a collection; defaults to ``True``"""
    format: Optional[str] = None
    fields: Widgets
    """The fields option maps editor UI widgets to field-value pairs in the saved file.
    The order of the fields in your Netlify CMS config.yml file determines their order in the editor UI
    and in the saved file."""
    media_folder: Optional[str] = None
    """Specifies the location for media files to be saved, relative to the base of the repo"""
    public_folder: Optional[str] = None
    """Specifies the location for media files to be accessed from the built site"""

    def __repr__(self) -> str:
        return f'<Collection:{self.__class__.__name__}>'

    def dict(self, exclude_none=True, **kwargs):
        """Overrides pydantic's ``dict`` function to omit Nonetype values

        :param exclude_none: include fields which are set to None, defaults to True
        :return: A python dictionary representation of the pydantic object
        """
        return super().dict(exclude_none=exclude_none, **kwargs)


class FolderCollection(Collection):
    """Represents a folder collection in the netlify editor.
    For information on Folder collections, see https://www.netlifycms.org/docs/collection-types#folder-collections"""

    folder: str
    """A path to a directory to create file(s) under"""
    # filter: TodoType = ???
    create: Optional[bool] = None  # set to true to allow creating new files; defaults to false
    """Set to True to allow creating new files; if undefined, this value is interpreted as False"""


class File(Collection):
    """Represents an individual file in a File Collection"""

    file: str
    """The path to the file to write"""


class FileCollection(Collection):
    """Represents a file collection in the netlify editor.
    For information on File collections, see https://www.netlifycms.org/docs/collection-types#file-collections"""

    # This feels like a dirty hack, but it does (in theory) get rid of the normal field requirement
    fields: Optional[Widgets] = None  # type: ignore
    files: List[File]
    """A list of netlifyconfig.collection.File objects"""
