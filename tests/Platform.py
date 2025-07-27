import unittest
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from tools import Platform

class TestPlatform(unittest.TestCase):
    def test_something(self):

        platform_json = {
            "hw": {
                "name": "generic",
                "arch": "x86_64"
            },
            "os": {
                "name": "Linux",
                "version": "5.4.0-42-generic"
            }
        }

        platform = Platform.Platform.from_json(platform_json)
        self.assertIsNotNone(platform)
        self.assertEqual(platform.hardware.brand.value, "generic")
        self.assertEqual(platform.hardware.arch.value, "x86_64")
        self.assertEqual(platform.system.name.value, "Linux")
        self.assertEqual(platform.system.version, "5.4.0-42-generic")

        print(platform)

if __name__ == '__main__':
    unittest.main()
