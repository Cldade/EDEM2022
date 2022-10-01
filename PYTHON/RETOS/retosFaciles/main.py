from retosFaciles.reto13 import areaTriangulo
from retosFaciles.reto13 import areaCirculo
from retosFaciles.reto14 import volumenCilindro
from retosFaciles.reto17 import enc3y5, primerosSeis, desde5aFinal, muestraToda, desde2a9de2en2, salto4, de9a2

#comprarDisco()

areaT = areaTriangulo(2,4)
print(areaT)

areaC = areaCirculo(4)
print(areaC)

volumenC = volumenCilindro(4,4)
print(volumenC)

tupla = (2, 4, 3, 5, 4, 6, 7, 8, 6, 1)
print(*enc3y5(tupla))
print(*primerosSeis(tupla))
print(*desde5aFinal(tupla))
print(*muestraToda(tupla))
print(*desde2a9de2en2(tupla))
print(*salto4(tupla))
print(*de9a2(tupla))