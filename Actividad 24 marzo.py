# =========================
# CLASE 1: TENISTA
# =========================
class Tenista:
    def __init__(self, nombre, anio, nacionalidad, ranking, altura):
        self.nombre = nombre
        self.anio = anio
        self.nacionalidad = nacionalidad
        self.ranking = ranking
        self.altura = altura

    def entrenar(self):
        print(self.nombre, "está entrenando")

    def competir(self):
        print(self.nombre, "está compitiendo")

    def viajar(self):
        print(self.nombre, "viaja a torneos")

    def descansar(self):
        print(self.nombre, "está descansando")

    def mostrar_info(self):
        print(self.nombre, self.nacionalidad)


# =========================
# CLASE 2: POOH
# =========================
class Pooh:
    def __init__(self, nombre, comida, felicidad, humor, amigos):
        self.nombre = nombre
        self.comida = comida
        self.felicidad = felicidad
        self.humor = humor
        self.amigos = amigos

    def comer(self):
        print("A Winnie Pooh le gusta mucho comer miel")
    
    def jugar(self):
        print(f"{self.nombre} está jugando con {self.amigos}")

    def dormir(self):
        print(f"{self.nombre} está durmiendo una siesta tranquila")
    
    def cantar(self):
        print(f"{self.nombre} está cantando una canción feliz")
    
    def pasear(self):
        print(f"{self.nombre} está paseando por el Bosque de los Cien Acres")


# =========================
# CLASE 3: PLANETA
# =========================
class Planeta:
    def __init__(self, nombre, diametro, masa, distancia_sol, tiene_lunas):
        self.nombre = nombre
        self.diametro = diametro
        self.masa = masa
        self.distancia_sol = distancia_sol
        self.tiene_lunas = tiene_lunas

    def mostrar_nombre(self):
        print(self.nombre)

    def mostrar_diametro(self):
        print(self.diametro)

    def mostrar_masa(self):
        print(self.masa)

    def mostrar_distancia(self):
        print(self.distancia_sol)

    def tiene_luna(self):
        print(self.tiene_lunas)


# =========================
# CLASE 4: BASQUETBOLISTA
# =========================
class Basquetbolista:
    def __init__(self, id, nombre, equipo, edad, posicion):
        self.id = id
        self.nombre = nombre
        self.equipo = equipo
        self.edad = edad
        self.posicion = posicion

    def entrenar(self):
        print(self.nombre, "está entrenando")

    def jugar(self):
        print(self.nombre, "está jugando un partido")

    def anotar(self):
        print(self.nombre, "anotó puntos")

    def defender(self):
        print(self.nombre, "está defendiendo")

    def descansar(self):
        print(self.nombre, "está descansando")


# =========================
# OBJETOS (UNO POR CLASE)
# =========================
tenista1 = Tenista("Carlos Alcaraz", 2003, "España", 2, 1.83)
pooh1 = Pooh("Winnie Pooh", "Miel", "Muy feliz", "Perezoso", "Tigger, Piglet, Conejo")
planeta1 = Planeta("Júpiter", 139820, 1898, 778.5, True)
basquet1 = Basquetbolista("B01", "LeBron James", "Lakers", 39, "Alero")

# =========================
# IMPRIMIR UN ATRIBUTO DE CADA UNO
# =========================
print(tenista1.nombre)
print(pooh1.nombre)
print(planeta1.nombre)
print(basquet1.nombre)

# =========================
# LLAMAR MÉTODOS
# =========================
tenista1.entrenar()
pooh1.jugar()
planeta1.mostrar_diametro()
basquet1.jugar()