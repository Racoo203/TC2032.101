# Ejercicio 1: Clase de Listas en Python
# Raúl Correa Ocañas
# A01722401
# 08/08/2023

class Listas:
    MAX = 100
    size = 0 # Ningún elemento en la lista al inicio / funciona también como un indice
    data = [0 for i in range(MAX)] # Genera una lista de 100 ceros

    def insert(self, num):
        if self.size < self.MAX:
            self.data[self.size] = num
            self.size += 1
    def erase(self):
        if self.size > 0:
            self.size -= 1
            del self.data[self.size]
        else: print("NO HAY ELEMENTOS")
    def getData(self, index):
        if index >= 0 and index < self.size:
            print(self.data[index])
        else: print("ERROR EN EL INDICE")
    def getSize(self):
        return self.size
    def print(self):
        for i in range(self.size):
            print("[%d]" % (i),"-",self.data[i])

# Pruebas de funcionamiento

ob1 = Listas()
for i in range(42):
    ob1.insert(i*4%7)
ob1.erase()
ob1.print()
ob1.getData(40)
ob1.getData(41)
ob1.insert(2003)
ob1.getData(41)