import unittest

class TestA(unittest.TestCase):

    def test_does_a_thing(self):
        self.assertTrue(True)

if __name__ == "__main__":
    unittest.main()