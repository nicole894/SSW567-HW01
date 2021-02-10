import unittest
from hw01 import classify_triangle


class TestTriangles(unittest.TestCase):

    def testDataTypes(self):
        print("Positive Test Case: For Invalid DataTypes (x, y, z)")
        self.assertEqual(classify_triangle('x', 'y', 'z'), 'Invalid Data')
        print("Test Case End\n")




    def testEquilateral(self):
        print("Positive Test Case: For Equilateral Triangle (5,5,5)")
        self.assertEqual(classify_triangle(5, 5, 5), 'Equilateral')
        print("Test Case End\n")

        print("Negative Test Case: For Equilateral Triangle (5, 6, 5)")
        self.assertNotEqual(classify_triangle(5, 6, 5), 'Equilateral', 'Should be Equilateral')
        print("Test Case End\n")

    def testIsosceles(self):
        print("Positive Test Case: For Isosceles Triangle (6,6,8)")
        self.assertEqual(classify_triangle(6, 6, 8), 'Isosceles')
        print("Test Case End\n")

        print("Negative Test Case: For Isosceles Triangle (6, 6, 6)")
        self.assertNotEqual(classify_triangle(6, 6, 6), 'Isosceles', 'Should be Isosceles')
        print("Test Case End\n")

    def testScalene(self):
        print("Positive Test Case: For Scalene Triangle (5, 6, 9)")
        self.assertEqual(classify_triangle(5, 6, 9), 'Scalene')
        print("Test Case End\n")

        print("Negative Test Case: For Scalene Triangle (5, 5, 9)")
        self.assertNotEqual(classify_triangle(5, 5, 9), 'Scalene', 'Should be Scalene')
        print("Test Case End\n")

    def testRightAngled(self):
        print("Positive Test Case: For Right Triangle (8, 10, 6)")
        self.assertEqual(classify_triangle(8, 10, 6), 'Right')
        print("Test Case End\n")

        print("Negative Test Case: For Right Triangle (8, 10, 7)")
        self.assertNotEqual(classify_triangle(8, 10, 7), 'Right', 'Should be Right')
        print("Test Case End\n")

    def testTriangle(self):

        print("Positive Test Case: For Not Triangle (2, 3, 7)")
        self.assertEqual(classify_triangle(2, 3, 7), 'NotATriangle')
        print("Test Case End\n")

        print("Negative Test Case: For Not Triangle (2, 2, 8)")
        self.assertNotEqual(classify_triangle(2, 7, 8), 'NotATriangle', 'Should not be a Triangle')
        print("Test Case End\n")

if __name__ == '__main__':
    unittest.main()
