class Personaje:
    def __init__(self, id, nombre, x, y, estado="Vivo", vida):
        self.id = id
        self.nombre = nombre
        self.posicionX = x
        self.posicionY = y
        self.estado = estado
        self.vida = 3

    def mover(self, dx=0, dy=0):
        self.posicionX += dx
        self.posicionY += dy