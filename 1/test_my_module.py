import unittest
from my_module import add, subtract

class TestMyModule(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)

    def test_subtract(self):
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(1, -1), 2)

if __name__ == '__main__':
    unittest.main()