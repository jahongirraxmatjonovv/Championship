class Driver:
    def __init__(self, name):
        self._name = name
        self._raced = []

    @property
    def name(self):
        return self._name

    def getRaced(self):
        return self._raced

    def getPoints(self):
        points_mapping = {1: 25, 2: 18, 3: 15, 4: 12, 5: 10, 6: 8, 7: 6, 8: 4, 9: 2, 10: 1}
        total_points = sum(points_mapping.get(pos, 0) for pos in self._raced)
        return total_points


class GP:
    def __init__(self, name):
        self._name = name
        self._participants = []
        self._results = {}

    @property
    def name(self):
        return self._name

    def setTime(self, driver, hours, minutes, seconds, ms):
        race_time = (hours, minutes, seconds, ms)
        self._results[driver] = race_time

    def toString(self):
        return f"{self._name} Grand Prix"

    def getGRanking(self):
        sorted_results = sorted(self._results.items(), key=lambda x: x[1])
        return [driver[0] for driver in sorted_results]

    def getPosition(self, driver):
        if driver in self._results:
            return sorted(self._results, key=lambda x: self._results[x]).index(driver) + 1
        else:
            return None


class Time:
    def __init__(self, gp, driver, hours, minutes, seconds, ms):
        self._gp = gp
        self._driver = driver
        self._time = (hours, minutes, seconds, ms)

    def __str__(self):
        return f"{self._gp.name} - {self._driver.name} - {':'.join(map(str, self._time))}"


class Championship:
    def __init__(self):
        self._drivers = []
        self._grandPrixList = []

    def createDriver(self, name):
        driver = Driver(name)
        self._drivers.append(driver)
        return driver

    def getDrivers(self):
        return self._drivers

    def getDriver(self, name):
        for driver in self._drivers:
            if driver.name == name:
                return driver
        return None

    def defineGrandPrix(self, name):
        grandPrix = GP(name)
        self._grandPrixList.append(grandPrix)
        return grandPrix

    def getGrandPrix(self, name):
        for grandPrix in self._grandPrixList:
            if grandPrix.name == name:
                return grandPrix
        return None

    def getChampionshipRanking(self):
        sorted_drivers = sorted(self._drivers, key=lambda x: x.getPoints(), reverse=True)
        return [driver.name for driver in sorted_drivers]