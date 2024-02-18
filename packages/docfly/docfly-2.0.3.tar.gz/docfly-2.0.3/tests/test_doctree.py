# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import pytest
from docfly.doctree import ArticleFolder
from pathlib_mate import PathCls as Path

dir_here = Path(__file__).parent
dir_test_source = Path(dir_here, "test_source")


class TestArticleFolder(object):
    def test_title(self):
        af = ArticleFolder(dir_path=dir_test_source.abspath)
        assert af.title == "Welcome to the Document"
        af = ArticleFolder(dir_path=dir_test_source.append_parts("Section1").abspath)
        assert af.title == "Section1"

        af = ArticleFolder(index_file="index_cn", dir_path=dir_test_source.abspath)
        assert af.title == "欢迎来到此文档"
        af = ArticleFolder(index_file="index_cn", dir_path=dir_test_source.append_parts("Section1").abspath)
        assert af.title == "第1章"

    def test_sub_article_folders(self):
        af = ArticleFolder(dir_path=dir_test_source.abspath)
        assert len(af.sub_article_folders) == 3
        for ind, sub_af in enumerate(af.sub_article_folders):
            assert sub_af.title == "Section{}".format(ind + 1)

        af = ArticleFolder(index_file="index_cn", dir_path=dir_test_source.abspath)
        assert len(af.sub_article_folders) == 3
        for ind, sub_af in enumerate(af.sub_article_folders):
            assert sub_af.title == "第{}章".format(ind + 1)

    def test_toc_directive(self):
        af = ArticleFolder(dir_path=dir_test_source.abspath)
        rst_directive = af.toc_directive()
        assert "Section1 <Section1/index>" in rst_directive
        assert "Section2 <Section2/index>" in rst_directive
        assert "Section3 <Section3/index>" in rst_directive

        af = ArticleFolder(index_file="index_cn", dir_path=dir_test_source.abspath)
        rst_directive = af.toc_directive()
        assert "第1章 <Section1/index_cn>" in rst_directive
        assert "第2章 <Section2/index_cn>" in rst_directive
        assert "第3章 <Section3/index_cn>" in rst_directive


if __name__ == "__main__":
    import os

    basename = os.path.basename(__file__)
    pytest.main([basename, "-s", "--tb=native"])
