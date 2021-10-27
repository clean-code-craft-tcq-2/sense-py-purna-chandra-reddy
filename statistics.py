import math


class EmailAlert:
    def __init__(self):
        self.emailSent = False


class LEDAlert:
    def __init__(self):
        self.ledGlows = False


class StatsAlerter:
    def __init__(self, maxThreshold, Alerts):
        self.maxThreshold = maxThreshold
        self.Alerts = Alerts

    def checkAndAlert(self, array):
        computedStats = calculateStats(array)

        if computedStats["max"] > self.maxThreshold:
            self.Alerts[0].emailSent = True
            self.Alerts[1].ledGlows = True


def calculateStats(array):
    if len(array):
        avgNum = sum(array) / len(array)
        maxNum = max(array)
        minNum = min(array)
    else:
        avgNum = math.nan
        maxNum = math.nan
        minNum = math.nan
    computedStats = {"avg": avgNum, "max": maxNum, "min": minNum}

    return computedStats
