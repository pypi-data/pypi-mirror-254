# -*- coding: utf-8 -*-

import pytest
import shutil
import docfly
from docfly.api_reference_doc import ApiReferenceDoc
from pathlib_mate import Path

package_name = docfly.__name__
DIR_HERE = Path(__file__).parent


def setup_module(module):
    dir_docfly_api_ref_doc = Path(DIR_HERE, package_name).abspath
    try:
        shutil.rmtree(dir_docfly_api_ref_doc)
    except:
        pass


class TestApiReferenceDoc(object):
    def test(self):
        doc = ApiReferenceDoc(
            conf_file=Path(__file__).change(new_basename="conf.py").abspath,
            package_name=package_name,
            ignored_package=[
                "{}.pkg".format(package_name),
                "{}.util.py".format(package_name),
            ]
        )
        doc.fly()

        assert Path(DIR_HERE, package_name, "api_reference_doc.rst").exists()
        assert Path(DIR_HERE, package_name, "doctree.rst").exists()

        assert not Path(DIR_HERE, package_name, "pkg").exists()
        assert not Path(DIR_HERE, package_name, "util").exists()


if __name__ == "__main__":
    import os

    basename = os.path.basename(__file__)
    pytest.main([basename, "-s", "--tb=native"])
