import unittest

from whiteboard import solution

class MatchTestCase(unittest.TestCase):
    def test_one(self):
        self.assertEqual(solution(10),"drink toddy")
    def test_two(self):
        self.assertEqual(solution(21),"drink whisky")
    def test_zero(self):
        self.assertEqual(solution(0),"drink toddy")
    def test_three(self):
        self.assertEqual(solution(14),"drink coke")
    def test_four(self):
        self.assertEqual(solution(19),"drink beer")
if __name__ == '__main__':
    unittest.main()