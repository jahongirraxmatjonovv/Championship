
class Driver:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

class GP:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

class Championship:
    def __init__(self):
        self._drivers = []
        self._grandPrix = None

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
        self._grandPrix = grandPrix
        return grandPrix

    def getGrandPrix(self):
        return self._grandPrix
