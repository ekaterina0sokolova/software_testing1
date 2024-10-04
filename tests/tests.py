import unittest
from main import solve_quadratic_equation


class TestQuadraticEquationModule(unittest.TestCase):
    def test_positive_discr(self):
        self.assertEqual(solve_quadratic_equation(a=1, b=-4, c=-5), [5.0, -1.0])

    def test_zero_discr(self):
        self.assertEqual(solve_quadratic_equation(a=2, b=-4, c=2), [1.0])

    def test_negative_discr(self):
        self.assertEqual(solve_quadratic_equation(a=2, b=-1, c=1), ["нет корней"])

    def test_zero_a(self):
        self.assertEqual(solve_quadratic_equation(a=0, b=2, c=-4), [2.0])

    def test_zero_a_zero_b(self):
        self.assertEqual(solve_quadratic_equation(a=0, b=0, c=-4), ["не уравнение"])

    def test_incorrect_arguments_type(self):
        with self.assertRaises(TypeError):
            solve_quadratic_equation(a="hello", b=2, c=-4)

    def test_less_number_of_arguments(self):
        with self.assertRaises(TypeError):
            solve_quadratic_equation(b=2, c=-4)

    def test_more_number_of_arguments(self):
        with self.assertRaises(TypeError):
            solve_quadratic_equation(a=2, b=2, c=2, dicr=0)


if __name__ == '__main__':
    unittest.main()
