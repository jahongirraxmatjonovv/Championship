from formula1 import Championship
from formula1 import Time

championship = Championship()

driver1 = championship.createDriver("Name 1")
driver2 = championship.createDriver("Name 2")

grandPrix1 = championship.defineGrandPrix("Uzbekistan Grand Prix")
grandPrix2 = championship.defineGrandPrix("Kazakistan Grand Prix")

time1 = Time(grandPrix1, driver1, 1, 30, 15, 500)
time2 = Time(grandPrix1, driver2, 1, 30, 20, 200)
time3 = Time(grandPrix2, driver1, 1, 28, 45, 800)
time4 = Time(grandPrix2, driver2, 1, 29, 0, 500)

championshipRanking = championship.getChampionshipRanking()
print("Championship Ranking:", championshipRanking)
