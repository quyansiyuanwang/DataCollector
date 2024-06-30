import unittest

from Test.ConfigTests.ConfigClass_test import ConfigTests
from Test.GatherTests.GatherClass_test import GatherTests
from Test.TestTogetherTests.RunResultCheck_test import TestTogetherResultCheckTests
from Test.TestTogetherTests.global_test import MainTests
from Test.TestTogetherTests.withConfig_test import WithConfigTests

ConfigTests: ConfigTests
MainTests: MainTests
WithConfigTests: WithConfigTests
GatherTests: GatherTests
TestTogetherResultCheckTests: TestTogetherResultCheckTests

if __name__ == "__main__":
    unittest.main()
