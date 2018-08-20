from unittest import TestCase
from calculator.distance_calc import get_distance

class TestDistanceCalc(TestCase):
    def test_is_zero(self):
        r = get_distance("20 Queent St, Auckland", "20 Queen St, Auckland")
        self.assertTrue(r==0)