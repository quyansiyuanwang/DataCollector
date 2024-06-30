import unittest
from typing import Protocol

from core import RunConfig
from core.SupportLibs.Gather import Gather
from utils.ProjectPath import GatherRunResultsPath


class GatherTests(unittest.TestCase):
    def test_normalFunctionOfFilter(self):
        class _Box(Protocol):
            _id: int

        r: RunConfig = RunConfig(
            _id=0
        )
        r_1: RunConfig = RunConfig(
            _id=1
        )
        r_2: RunConfig = RunConfig(
            _id=2
        )

        g_1: Gather = Gather([
            n_0 := r,
            r_1,
            r_2,
            r
        ])
        compare_1: Gather = Gather([
            r,
            r
        ])

        def Box_filter(one: '_Box', another: '_Box'):
            return getattr(one, '_id') == getattr(another, '_id')

        g_1.add_filter(_Box, Box_filter)
        g_2 = g_1[n_0]

        self.assertEqual(g_2, compare_1)

    def test_normalFunctionDisplayInfo(self):
        r: RunConfig = RunConfig(
            _id=0
        )
        r_1: RunConfig = RunConfig(
            _id=1
        )
        r_2: RunConfig = RunConfig(
            _id=2
        )

        g_1: Gather = Gather([
            r,
            r_1,
            r_2,
            r
        ])

        with open(GatherRunResultsPath / "normalFunctionDisplayInfo", "r") as file:
            expected = file.read()

        self.assertEqual(expected, g_1.__str__())
