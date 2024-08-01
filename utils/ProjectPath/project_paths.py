from pathlib import Path


RootPath = '\\'.join(Path.cwd().__str__().split('\\')[:-1])

ConfigRunResultsPath = Path("Test\\ConfigTests\\ConfigRunResults")
GatherRunResultsPath = Path("Test\\GatherTests\\GatherRunResults")
TestTogetherRunResultsPath = Path("Test\\AwaitTestTogetherTests\\AwaitTestTogetherRunResults")

ConfigWorkPath = Path("Test\\ConfigTests")
GatherWorkPath = Path("Test\\GatherTests")
TestTogetherWorkPath = Path("Test\\AwaitTestTogetherTests")

__all__ = [
    "ConfigRunResultsPath",
    "GatherRunResultsPath",
    "TestTogetherRunResultsPath",
    "ConfigWorkPath",
    "GatherWorkPath",
    "TestTogetherWorkPath",
    "RootPath"
]
