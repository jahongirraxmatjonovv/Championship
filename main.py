from formula1 import Championship

championship = Championship()

driver1 = championship.createDriver("Name 1")
driver2 = championship.createDriver("Name 2")

all_drivers = championship.getDrivers()
for driver in all_drivers:
    print(driver.name)

grandPrix = championship.defineGrandPrix("Uzbekistan Grand Prix")

grandPrixName = grandPrix.name
print("Grand Prix Nomi:", grandPrixName)

championshipGrandPrix = championship.getGrandPrix()
if championshipGrandPrix:
    print("Chempionat Gran-prisiga nomzod:", championshipGrandPrix.name)
else:
    print("Chempionat Gran-prisi hali aniqlanmagan.")
