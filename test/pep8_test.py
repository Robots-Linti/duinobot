import unittest
import pep8
from glob import glob
import os.path


def flatten(iterable):
    return (element for i in iterable for element in i)


class TestCodeFormat(unittest.TestCase):
    files = flatten(map(glob, [
        '*.py',
        os.path.join('ejemplos', '*.py'),
        os.path.join('test', '*.py')
    ]))

    def test_pep8_conformance(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=False)
        result = pep8style.check_files(TestCodeFormat.files)
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")
