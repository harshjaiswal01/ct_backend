from unittest import TestCase

from whiteboard import solution

class MatchTestCase2(TestCase):
    def test_general1(self):
        self.assertEqual(solution([1, 2, 3, 4, 5]), [2, 3, 4, 5])
    def test_general2(self):
         self.assertEqual(solution([5, 3, 2, 1, 4]), [5, 3, 2, 4])
    def test_multiple_mins(self):
        self.assertEqual(solution([1, 2, 3, 1, 1]), [2, 3, 1, 1])
    def test_empty(self):
        self.assertEqual(solution([]), [])