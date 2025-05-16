import pygame
from Personaje import Personaje

class Enemigo(personaje):
    def __init__(self, nombre, posicionX, posicionY,vida):
        
        self.nombre = nombre
        self.posicionX = posicionX 
        self.posicionY = posicionY
        self.vida = vida
    
    def mover(self, dx=0, dy=0):
        self.posicionX += dx
        self.posicionY += dy    
    

        
        
        