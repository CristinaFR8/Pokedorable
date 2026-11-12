class Pokemon:
    def __init__(self, id, nombre, altura, peso,
                 estadisticas, sprites, tipos, ataques):
        self.id = id
        self.nombre = nombre
        self.altura = altura
        self.peso = peso
        self.estadisticas = estadisticas
        self.sprites = sprites
        self.tipos = tipos
        self.ataques = ataques

    def clasificar_peso(self):
        if self.peso < 20:
            return "Ligero"
        elif self.peso <= 60:
            return "Medio"
        else:
            return "Pesado"

    def calcular_total_estadisticas(self):
        total = 0

        for estadistica in self.estadisticas:
            total += estadistica["value"]

        return total