import unittest

if __name__ == "__main__":
    loader = unittest.TestLoader()
    suite = loader.discover(start_dir="./app", pattern="*_test.py")
    unittest.TextTestRunner(verbosity=2).run(test=suite)
    


