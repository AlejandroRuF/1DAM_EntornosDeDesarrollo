from Coche import Coche
from Garaje import Garaje

c1 = [Coche("BBC1234", "Skoda", "Octavia", 2010, "E"), Coche("BBC1234", "Skoda", "Octavia", 2015, "G"),
      Coche("BBC1234", "Skoda", "Octavia", 2000, "D")]
c2 = Coche("BBC1234", "Skoda", "Octavia", 2015, "G")
c3 = Coche("BBC1234", "Skoda", "Octavia", 2015, "G")
g1 = Garaje("Garaje Godelleta", 30, 10)
g1.setCoches(c1)
g1.resumen()
g1.agregarCoches(c2)
g1.agregarCoches(c3)
g1.resumen()
g1.estadistica()
