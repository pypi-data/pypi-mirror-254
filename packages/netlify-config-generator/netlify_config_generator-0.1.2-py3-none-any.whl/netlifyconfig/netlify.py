"""Definition of the base entrypoint into a netlify configuration file"""
from __future__ import annotations
from typing import Optional

from pydantic import BaseModel

from netlifyconfig.collection import Collection

# TODO: multiple inherited backends based off this
class Backend(BaseModel):
    """Represents backend config
    For more information, see https://www.netlifycms.org/docs/backends-overview/"""

    name: str
    """The backend type to use"""
    repo: Optional[str] = None
    """Required for ``github``, ``gitlab``, and ``bitbucket`` backends; ignored by ``git-gateway``.
    Follows the pattern ``[org-or-username]/[repo-name]``."""
    branch: Optional[str] = None
    """The branch where published content is stored. All CMS commits and PRs are made to this branch."""
    api_root: Optional[str] = None
    """The API endpoint. Only necessary in certain cases, like with GitHub Enterprise or self-hosted GitLab."""
    # site_domain: TodoType = ???
    base_url: Optional[str] = None
    """Sets the ``site_id`` query param sent to the API endpoint. Non-Netlify auth setups will often need to set
    this for local development to work properly."""
    auth_endpoint: Optional[str] = None
    """Path to append to ``base_url`` for authentication requests. Optional."""
    cms_label_prefix: Optional[str] = None
    """Pull (or Merge) Requests label prefix when using editorial workflow. Optional."""

    def dict(self, exclude_none=True, **kwargs):
        return super().dict(exclude_none=exclude_none, **kwargs)


class NetlifyConfig(BaseModel):
    """Represents a netlify-cms configuration file"""

    backend: Backend
    publish_mode: Optional[str] = None  # TODO: enum or some other validator?
    media_folder: str
    public_folder: str
    site_url: Optional[str] = None
    show_preview_links: Optional[bool] = None
    collections: list[Collection] = []
    local_backend: Optional[bool] = None

    def dict(self, exclude_none=True, **kwargs):
        return super().dict(exclude_none=exclude_none, **kwargs)
