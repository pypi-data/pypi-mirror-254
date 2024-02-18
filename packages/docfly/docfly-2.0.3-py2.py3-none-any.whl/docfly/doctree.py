# -*- coding: utf-8 -*-

"""
Create doc tree if you follows

:ref:`Sanhe Sphinx standard <en_sphinx_doc_style_guide>`.
"""

from __future__ import print_function
import json

from pathlib_mate import PathCls as Path

from .template import TC
from .pkg import textfile


class ArticleFolder(object):
    """
    Represent an ``index.rst`` or ``index.ipynb`` file with a Title in a directory.

    :param index_file: the index file name (no file extension)
    :param dir_path: A folder contains single rst file. The rst file path

    **中文文档**

    一篇 Article 代表着文件夹中有一个 ``index.rst`` 或 ``index.ipynb`` 文件的文件夹.
    其中必然有至少一个标题元素.
    """

    DEFAULT_INDEX_FILE = "index"

    def __init__(self, index_file=None, dir_path=None):
        if index_file is None:
            index_file = self.DEFAULT_INDEX_FILE
        self.index_file = index_file
        self.dir_path = dir_path
        self._title = None

    @property
    def rst_path(self):
        """
        The actual rst file absolute path.
        """
        return Path(self.dir_path, self.index_file + ".rst").abspath

    @property
    def ipynb_path(self):
        """
        The actual ipynb file absolute path.
        """
        return Path(self.dir_path, self.index_file + ".ipynb").abspath

    @property
    def rel_path(self):
        """
        File relative path from the folder.
        """
        return "{}/{}".format(Path(self.dir_path).basename, self.index_file)

    @property
    def title(self):
        """
        Title for the first header.
        """
        if self._title is None:
            if Path(self.rst_path).exists():
                self._title = self.get_title_from_rst()
            elif Path(self.ipynb_path).exists():
                self._title = self.get_title_from_ipynb()
            else:
                pass
        return self._title

    def get_title_from_rst(self):
        """
        Get title line from .rst file.

        **中文文档**

        从一个 ``_filename`` 所指定的 .rst 文件中, 找到顶级标题.
        也就是第一个 ``====`` 或 ``----`` 或 ``~~~~`` 上面一行.
        """
        header_bar_char_list = "=-~+*#^"

        lines = list()
        for cursor_line in textfile.readlines(
            self.rst_path, strip="both", encoding="utf-8"
        ):
            if cursor_line.startswith(".. include::"):
                relative_path = cursor_line.split("::")[-1].strip()
                included_path = Path(Path(self.rst_path).parent.abspath, relative_path)
                if included_path.exists():
                    cursor_line = included_path.read_text(encoding="utf-8")
            lines.append(cursor_line)
        rst_content = "\n".join(lines)

        cursor_previous_line = None
        for cursor_line in rst_content.split("\n"):
            for header_bar_char in header_bar_char_list:
                if cursor_line.startswith(header_bar_char):
                    flag_full_bar_char = cursor_line == header_bar_char * len(
                        cursor_line
                    )
                    flag_line_length_greather_than_1 = len(cursor_line) >= 1
                    flag_previous_line_not_empty = bool(cursor_previous_line)
                    if (
                        flag_full_bar_char
                        and flag_line_length_greather_than_1
                        and flag_previous_line_not_empty
                    ):
                        return cursor_previous_line.strip()
            cursor_previous_line = cursor_line

        msg = (
            "Warning, this document doesn't have any %s header!" % header_bar_char_list
        )
        return None

    def get_title_from_ipynb(self):
        """
        Get title line from .ipynb file.

        **中文文档**

        从一个 ``_filename`` 所指定的 .ipynb 文件中, 找到顶级标题.
        也就是第一个 ``#`` 后面的部分.

        有的时候我们会用 raw RestructuredText 来做顶级标题.
        """
        header_bar_char_list = "=-~+*#^"

        data = json.loads(Path(self.ipynb_path).read_text())
        for row in data["cells"]:
            if len(row["source"]):
                if row.get("cell_type") == "markdown":
                    content = row["source"][0]
                    line = content.split("\n")[0]
                    if "# " in line:
                        return line[2:].strip()
                elif (
                    row.get("cell_type") == "raw"
                    and row.get("metadata", {}).get("raw_mimetype", "unknown")
                    == "text/restructuredtext"
                ):
                    try:
                        line = row["source"][3].strip()
                    except IndexError:
                        continue
                    try:
                        title_line = row["source"][2].strip()
                    except IndexError:
                        continue

                    for header_bar_char in header_bar_char_list:
                        if line.startswith(header_bar_char):
                            flag_full_bar_char = line == header_bar_char * len(line)
                            flag_line_length_greather_than_1 = len(line) >= 1
                            flag_previous_line_not_empty = bool(title_line)
                            if (
                                flag_full_bar_char
                                and flag_line_length_greather_than_1
                                and flag_previous_line_not_empty
                            ):
                                return title_line
                else:
                    pass

        msg = "Warning, this document doesn't have any level 1 header!"
        return None

    @property
    def sub_article_folders(self):
        """
        Returns all valid ArticleFolder sitting inside of
        :attr:`ArticleFolder.dir_path`.
        """
        l = list()
        for p in Path.sort_by_fname(Path(self.dir_path).select_dir(recursive=False)):
            af = ArticleFolder(index_file=self.index_file, dir_path=p.abspath)
            try:
                if af.title is not None:
                    l.append(af)
            except:
                pass
        return l

    def toc_directive(self, maxdepth=1):
        """
        Generate toctree directive text.

        :param table_of_content_header:
        :param header_bar_char:
        :param header_line_length:
        :param maxdepth:
        :return:
        """
        articles_directive_content = TC.toc.render(
            maxdepth=maxdepth,
            article_list=self.sub_article_folders,
        )
        return articles_directive_content

    def __repr__(self):
        return "Article(index_file=%r, title=%r)" % (
            self.index_file,
            self.title,
        )
