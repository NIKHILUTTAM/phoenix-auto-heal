import unittest
from app import power_level


class TestPhoenixSystem(unittest.TestCase):
    def test_power_level(self):
        # The system is only healthy if power is 100
        current_level = power_level()
        self.assertEqual(current_level, 100, "CRITICAL: Power level dropped below 100!")


if __name__ == "__main__":
    unittest.main()
