import unittest
import statistics ; from statistics import *
from math import isnan


class StatsTest(unittest.TestCase):
    def test_report_min_max_avg(self):
        computedStats = statistics.calculateStats([1.5, 8.9, 3.2, 4.5])
        epsilon = 0.001
        self.assertAlmostEqual(computedStats["avg"], 4.525, delta=epsilon)
        self.assertAlmostEqual(computedStats["max"], 8.9, delta=epsilon)
        self.assertAlmostEqual(computedStats["min"], 1.5, delta=epsilon)

    def test_avg_is_nan_for_empty_input(self):
        computedStats = statistics.calculateStats([])
        self.assertTrue(isnan(computedStats["avg"]))
        self.assertTrue(isnan(computedStats["max"]))
        self.assertTrue(isnan(computedStats["min"]))

    def test_raise_alerts_when_max_above_threshold(self):
        emailAlert = EmailAlert()
        ledAlert = LEDAlert()
        maxThreshold = 10.5
        statsAlerter = StatsAlerter(maxThreshold, [emailAlert, ledAlert])
        statsAlerter.checkAndAlert([22.6, 12.5, 3.7])
        self.assertTrue(emailAlert.emailSent)
        self.assertTrue(ledAlert.ledGlows)


if __name__ == "__main__":
    unittest.main()
