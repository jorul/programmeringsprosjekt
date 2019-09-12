from tilfeldig import Tilfeldig
from testSpiller import TestSpiller1
from sekvensiell import Sekvensiell
from mestVanlig import MestVanlig
from historiker import Historiker
from mangeSpill import MangeSpill


s2 = Tilfeldig()
s1 = Tilfeldig()

testing = MangeSpill(s1, s2, 100)
testing.arranger_turnering()
testing.plott_graf()