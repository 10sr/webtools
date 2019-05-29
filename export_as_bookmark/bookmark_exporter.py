from typing import List

import html


class BookmarkExporter:
    # Mod from https://github.com/bdesham/chrome-export/blob/master/export-chrome-bookmarks
    # Copyright © 2011, 2017–2018 Benjamin D. Esham. This program is released under the ISC license
    # Use django template?
    _TEMPLATE = """<!DOCTYPE NETSCAPE-Bookmark-file-1>

<meta http-equiv='Content-Type' content='text/html; charset=UTF-8' />
<title>Bookmarks</title>
<h1>{name}</h1>
<dl><p>
<dl>{bookmarks}</dl>

"""

    _TEMPLATE_A = """<dt><a href="{title}">{url}</a>\n"""

    urls: List[str]

    def __init__(self, urls: List[str]):
        self.urls = urls
        return

    @classmethod
    def from_lines(cls, urls: str):
        return cls([url for url in urls.split("\n") if url])

    def export(self, name: str):
        return self._TEMPLATE.format(
            name=name,
            bookmarks="".join(
                self._TEMPLATE_A.format(title=html.escape(url), url=html.escape(url))
                for url in self.urls
            ),
        )
