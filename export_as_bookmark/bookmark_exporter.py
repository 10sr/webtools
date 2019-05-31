from typing import List

import html


class BookmarkExporter:
    _TEMPLATE = """<!DOCTYPE NETSCAPE-Bookmark-file-1>

<META HTTP-EQUIV="Content-Type" CONTENT="text/html; charset=UTF-8">
<TITLE>Bookmarks</TITLE>
<H1>ExportAsBookmark</H1>

<DL><p>
    <DT><H3 ADD_DATE="1559279096" LAST_MODIFIED="1559279096" PERSONAL_TOOLBAR_FOLDER="true">{name}</H3>
    <DL><p>
{bookmarks}
    </DL><p>
</DL><p>

"""

    _TEMPLATE_A = """<DT><A HREF="{url}" ADD_DATE="1559279096" LAST_MODIFIED="1559279096">{title}</A>\n"""

    urls: List[str]

    def __init__(self, urls: List[str]):
        self.urls = list(urls)
        return

    @classmethod
    def from_lines(cls, urls: str):
        return cls([url.strip() for url in urls.split("\n") if url.strip()])

    def export(self, name: str):
        return self._TEMPLATE.format(
            name=name,
            bookmarks="".join(
                self._TEMPLATE_A.format(title=html.escape(url), url=html.escape(url))
                for url in self.urls
            ),
        )
