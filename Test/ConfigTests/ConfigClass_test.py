import unittest
from typing import Union

from core import DisplayConfig
from core.SupportLibs.DataConfig import VariableNotMatch
from utils import get_raises_info

Digit = Union[int, float]


class ConfigTests(unittest.TestCase):
    def test_VNMErrorToMuchVar(self):
        cfg = DisplayConfig()

        def c():
            cfg["display_doc"] = False, True

        self.assertRaises(VariableNotMatch, c)

        print(get_raises_info(c))

    def test_VNMErrorVarNumNotEnough(self):
        cfg = DisplayConfig()

        def c():
            cfg[
                "display_doc",
                "display_func_name",
                "display_args"
            ] = False, True

        self.assertRaises(VariableNotMatch, c)

        print(get_raises_info(c))

    def test_setitemMethod(self):
        cfg = DisplayConfig()
        cfg["display_doc"] = False

        comparison_1 = DisplayConfig()
        comparison_1.display_doc = False

        self.assertEqual(cfg.display_doc, False)
        self.assertEqual(comparison_1, cfg)

        comparison_2 = DisplayConfig()

        cfg[
            "display_doc",
            "display_args"
        ] = True

        self.assertEqual(comparison_2, cfg)

        print(cfg)
