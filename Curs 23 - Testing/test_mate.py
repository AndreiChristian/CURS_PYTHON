import unittest
from mate import multiply

class TestMate(unittest.TestCase):

    def test_adunare(self):
        self.assertEqual(2+2, 4)
        self.assertRaises(multiply(2,2),4)



if __name__ == "__main__":
    unittest.main()
