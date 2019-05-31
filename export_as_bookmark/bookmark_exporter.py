from typing import List

import html

_ = """
<!DOCTYPE NETSCAPE-Bookmark-file-1>

<META HTTP-EQUIV="Content-Type" CONTENT="text/html; charset=UTF-8">
<TITLE>Bookmarks</TITLE>
<H1>Bookmarks</H1>

<DL><p>
    <DT><H3 ADD_DATE="1559279096" LAST_MODIFIED="1559279096" PERSONAL_TOOLBAR_FOLDER="true">Buku bookmarks</H3>
    <DL><p>
        <DT><A HREF="http://google.com" ADD_DATE="1559279096" LAST_MODIFIED="1559279096">Google</A>
        <DD>世界中のあらゆる情報を検索するためのツールを提供しています。さまざまな検索機能を活用して、お探しの情報を見つけてください。
    </DL><p>
</DL><p>

"""
class BookmarkExporter:
    # Mod from https://github.com/bdesham/chrome-export/blob/master/export-chrome-bookmarks
    # Copyright © 2011, 2017–2018 Benjamin D. Esham. This program is released under the ISC license
    # Use django template?
    _TEMPLATE = """<!DOCTYPE NETSCAPE-Bookmark-file-1>

<meta http-equiv='Content-Type' content='text/html; charset=UTF-8' />
<title>Bookmarks</title>
<h1>{name}</h1>
<dl><p>
<dl>
{bookmarks}
</dl>

"""

    _TEMPLATE_A = """<dt><a href="{title}">{url}</a>\n"""

    urls: List[str]

    def __init__(self, urls: List[str]):
        self.urls = list(urls)
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
