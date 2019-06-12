"""Bookmark exporter."""


from __future__ import annotations

import html

from typing import List


class BookmarkExporter:
    """Export bookmark into Netscape Bookmark file.."""

    _TEMPLATE = """<!DOCTYPE NETSCAPE-Bookmark-file-1>

<META HTTP-EQUIV="Content-Type" CONTENT="text/html; charset=UTF-8">
<TITLE>Bookmarks</TITLE>
<H1>ExportAsBookmark</H1>

<DL><p>
<DT><H3>{name}</H3>
<DL><p>
{bookmarks}
</DL><p>
</DL><p>

"""

    _TEMPLATE_A = """<DT><A HREF="{url}">{title}</A>\n"""

    urls: List[str]

    def __init__(self, urls: List[str]) -> None:
        """Initialize."""
        self.urls = list(urls)
        return

    @classmethod
    def from_lines(cls, urls: str) -> BookmarkExporter:
        """Create bookmark exporter from list of urls."""
        return cls([url.strip() for url in urls.split("\n") if url.strip()])

    def export(self, name: str) -> str:
        """Export bookmark file."""
        return self._TEMPLATE.format(
            name=name,
            bookmarks="".join(
                self._TEMPLATE_A.format(title=html.escape(url), url=html.escape(url))
                for url in self.urls
            ),
        )
