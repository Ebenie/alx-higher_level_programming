import unittest
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):

    def test_rectangle_creation(self):
        r1 = Rectangle(3, 4)
        self.assertEqual(r1.width, 3)
        self.assertEqual(r1.height, 4)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)
        self.assertEqual(r1.id, 1)

    def test_rectangle_area(self):
        r1 = Rectangle(3, 4)
        self.assertEqual(r1.area(), 12)

    def test_rectangle_display(self):
        r1 = Rectangle(2, 3)
        expected_output = "  ##\n  ##\n  ##\n"
        with self.assertLogs() as logs:
            r1.display()
        self.assertEqual(logs.output, [expected_output])

    def test_rectangle_update(self):
        r1 = Rectangle(2, 3)
        r1.update(5, 6, 7, 8, 9)
        self.assertEqual(r1.to_dictionary(), {'id': 5, 'width': 6, 'height': 7, 'x': 8, 'y': 9})

if __name__ == '__main__':
    unittest.main()

