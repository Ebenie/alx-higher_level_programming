import unittest
from models.square import Square

class TestSquare(unittest.TestCase):

    def test_square_creation(self):
        s1 = Square(3)
        self.assertEqual(s1.size, 3)
        self.assertEqual(s1.x, 0)
        self.assertEqual(s1.y, 0)
        self.assertEqual(s1.id, 1)

    def test_square_size_property(self):
        s1 = Square(3)
        s1.size = 5
        self.assertEqual(s1.size, 5)
        self.assertEqual(s1.width, 5)
        self.assertEqual(s1.height, 5)

    def test_square_update(self):
        s1 = Square(2)
        s1.update(5, 6, 7, 8)
        self.assertEqual(s1.to_dictionary(), {'id': 5, 'size': 6, 'x': 7, 'y': 8})

if __name__ == '__main__':
    unittest.main()

