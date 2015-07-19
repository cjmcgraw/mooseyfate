from math import sqrt
import unittest

from ...lib.HelperFunctions import euclidean_distance

class HelperFunctionsTest(unittest.TestCase):

    def test_euclidean_distance_1dimension(self):
        """Tests the euclidean distance in one dimension"""
        dist_from_origin = lambda v: euclidean_distance([0], v)

        self.assertEqual(100, dist_from_origin([100]))
        self.assertEqual(100, dist_from_origin([-100]))

        self.assertEqual(123, dist_from_origin([123]))
        self.assertEqual(123, dist_from_origin([-123]))

        self.assertEqual(0,   dist_from_origin([0]))
        self.assertEqual(0,   dist_from_origin([0]))

        self.assertEqual(1,   dist_from_origin([-1]))
        self.assertEqual(1,   dist_from_origin([1]))

        dist_from_initial = lambda v: euclidean_distance([77], v)

        self.assertEqual(33, dist_from_initial([77 + 33]))
        self.assertEqual(33, dist_from_initial([77 - 33]))

        self.assertEqual(11, dist_from_initial([77 + 11]))
        self.assertEqual(11, dist_from_initial([77 - 11]))

        self.assertEqual(123, dist_from_initial([77 + 123]))
        self.assertEqual(123, dist_from_initial([77 - 123]))

    def test_euclidean_distance_2dimension(self):
        """Tests the euclidean distance in 2 dimensions"""
        dist_from_origin = lambda v: euclidean_distance([0, 0], v)

        # Do it first with known whole numbers
        self.assertEqual(5,  dist_from_origin([3, 4]))
        self.assertEqual(5,  dist_from_origin([-3, -4]))

        self.assertEqual(13, dist_from_origin([5, 12]))
        self.assertEqual(13, dist_from_origin([-5, -12]))

        self.assertEqual(15, dist_from_origin([9, 12]))
        self.assertEqual(15, dist_from_origin([-9, -12]))

        self.assertEqual(52, dist_from_origin([20, 48]))
        self.assertEqual(52, dist_from_origin([-20, -48]))

        # Next we will do it with a couple doubles, but we need
        # to round
        self.assertEqual(8.6023,  round(dist_from_origin([5, 7]),     4))
        self.assertEqual(8.6023,  round(dist_from_origin([-5, -7]),   4))

        self.assertEqual(13.0384, round(dist_from_origin([7, 11]),    4))
        self.assertEqual(13.0384, round(dist_from_origin([-7, -11]),  4))

        self.assertEqual(17.0294, round(dist_from_origin([11, 13]),   4))
        self.assertEqual(17.0294, round(dist_from_origin([-11, -13]), 4))

        dist_from_initial = lambda v: euclidean_distance([7, 23], v)

        # Do it first with known whole numbers
        self.assertEqual(5,  dist_from_initial([7 + 3, 23 + 4]))
        self.assertEqual(5,  dist_from_initial([7 - 3, 23 - 4]))

        self.assertEqual(13, dist_from_initial([7 + 5, 23 + 12]))
        self.assertEqual(13, dist_from_initial([7 - 5, 23 - 12]))

        self.assertEqual(15, dist_from_initial([7 + 9, 23 + 12]))
        self.assertEqual(15, dist_from_initial([7 - 9, 23 - 12]))

        self.assertEqual(52, dist_from_initial([7 + 20, 23 + 48]))
        self.assertEqual(52, dist_from_initial([7 + 20, 23 + 48]))

        # Next we do it with some doubles which require rounding
        self.assertEqual(8.6023, round(dist_from_initial([7 + 5, 23 + 7]), 4))
        self.assertEqual(8.6023, round(dist_from_initial([7 - 5, 23 - 7]), 4))

        self.assertEqual(13.0384, round(dist_from_initial([7 + 7, 23 + 11]), 4))
        self.assertEqual(13.0384, round(dist_from_initial([7 - 7, 23 - 11]), 4))

        self.assertEqual(17.0294, round(dist_from_initial([7 + 11, 23 + 13]), 4))
        self.assertEqual(17.0294, round(dist_from_initial([7 - 11, 23 - 13]), 4))

    def test_euclidean_distance_Ndimension(self):
        """Tests the euclidean distance in 2+ dimensions"""

        self.assertEqual(15, euclidean_distance([0, 0, 0], [10, 10, 5]))
        self.assertEqual(15, euclidean_distance([0, 0, 0], [-10, -10, -5]))

        self.assertEqual(17, euclidean_distance([0, 0, 0, 0], [10, 10, 8, 5]))
        self.assertEqual(17, euclidean_distance([0, 0, 0, 0], [-10, -10, -8, -5]))

        self.assertEqual(8,  euclidean_distance([0, 0, 0, 0, 0], [5, 1, 1, 1, 6]))
        self.assertEqual(8,  euclidean_distance([0, 0, 0, 0, 0], [-5, -1, -1, -1, -6])) 

if __name__ == '__main__':
    unittest.main()
