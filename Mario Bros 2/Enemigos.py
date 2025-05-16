import pygame
from Personaje import Personaje

class Enemigo(Personaje):
    def __init__(self, nombre, posicionX, posicionY,vida=1):
        
        self.nombre = nombre
        self.posicionX = posicionX 
        self.posicionY = posicionY
        self.vida = vida
    
    def mover(self, dx=0, dy=0):
        self.posicionX += dx
        self.posicionY += dy
        
class Goomba(Enemigo):
    pass    
    

        
        
        