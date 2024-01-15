import unittest
from models.base import Base

class TestBase(unittest.TestCase):

    def test_base_creation(self):
        b1 = Base()
        b2 = Base()
        b3 = Base(5)
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 5)

if __name__ == '__main__':
    unittest.main()

