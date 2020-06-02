import unittest
from main import camper_age_input


class MyTestCase(unittest.TestCase):
    def test_convert_to_months(self):
        self.assertEqual(camper_age_input.convert_to_months(12), 1)


if __name__ == '__main__':
    unittest.main()
