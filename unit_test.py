import unittest
from math import pi

class TestShapes(unittest.TestCase):
    def test_circle_area(self):
        circle = Circle(5)
        self.assertAlmostEqual(circle.area(), pi * 25)
        
    def test_circle_invalid_radius(self):
        with self.assertRaises(ValueError):
            Circle(-1)
            
    def test_triangle_area(self):
        triangle = Triangle(3, 4, 5)
        self.assertAlmostEqual(triangle.area(), 6)
        
    def test_triangle_invalid_sides(self):
        with self.assertRaises(ValueError):
            Triangle(1, 2, 5)
            
    def test_right_angled_triangle(self):
        self.assertTrue(Triangle(3, 4, 5).is_right_angled())
        self.assertFalse(Triangle(3, 4, 6).is_right_angled())
        
    def test_calculate_area_function(self):
        circle = Circle(2)
        triangle = Triangle(5, 12, 13)
        self.assertAlmostEqual(calculate_area(circle), pi * 4)
        self.assertAlmostEqual(calculate_area(triangle), 30)
        
    def test_is_right_angled_function(self):
        self.assertTrue(is_right_angled(Triangle(3, 4, 5)))
        self.assertFalse(is_right_angled(Circle(5)))

if __name__ == "__main__":
    unittest.main()
