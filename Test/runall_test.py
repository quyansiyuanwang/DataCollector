import unittest

from Test.ConfigTests.ConfigClass_test import ConfigTests
from Test.GatherTests.GatherClass_test import GatherTests
from Test.AwaitTestTogetherTests.RunResultCheck_test import TestTogetherResultCheckTests
from Test.AwaitTestTogetherTests.global_test import MainTests
from Test.AwaitTestTogetherTests.withConfig_test import WithConfigTests

ConfigTests: ConfigTests
MainTests: MainTests
WithConfigTests: WithConfigTests
GatherTests: GatherTests
TestTogetherResultCheckTests: TestTogetherResultCheckTests

if __name__ == "__main__":
    unittest.main()
