# This file is used to test the simulation of the Gather class tests generate

from core.SupportLibs import *
from core import RunConfig
from utils.ProjectPath import GatherRunResultsPath


class TestSimulate:
    @staticmethod
    def test_normalFunctionDisplayInfo():
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

        with open(GatherRunResultsPath / "normalFunctionDisplayInfo", "w") as file:
            file.write(g_1.__str__())

        print(g_1.__str__())


def temp_simulation():
    pass


if __name__ == '__main__':
    # TestSimulate.test_normalFunctionDisplayInfo()
    # temp_simulation()
    pass
