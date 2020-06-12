import unittest


from src.main.data_structure.list_exercise import *


class TestList(unittest.TestCase):
    def test_appending(self):
        self.assertEqual(appended([1,2],[3,4]),[1,2,3,4])

        
if __name__ == '__main__':
    unittest.main()