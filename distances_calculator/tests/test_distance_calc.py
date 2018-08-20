from unittest import TestCase
from calculator.distance_calc import get_distance

class TestDistanceCalc(TestCase):
    def test_is_zero(self):
        r = get_distance("125 Queen St, Auckland, 0620", "125 Queen St, Auckland, 0620")
        self.assertTrue(r==0)