import pygame
from Personaje import cargar_imagenes

class Enemigo(pygame.sprite.Sprite):
    def __init__(self, nombre, posicionX, posicionY,vida):
        
        self.nombre = nombre
        self.posicionX = posicionX 
        self.posicionY = posicionY
        self.vida = vida
    
    def mover(self, dx=0, dy=0):
        self.posicionX += dx
        self.posicionY += dy    
    

        
        
        