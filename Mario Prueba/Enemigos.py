import pygame
from Constantes import * 

class Enemigo(pygame.sprite.Sprite):
    def __init__(self, nombre, posicionX, posicionY, vida, id):
        super().__init__()
        self.nombre = nombre
        self.posicionX = posicionX 
        self.posicionY = posicionY
        self.vida = vida
        self.id = id
        self.direccion = -1

        self.image = pygame.image.load(ENEMIGO_IMAGE)
        self.image = pygame.transform.scale(self.image, (self.image.get_width() * 3, self.image.get_height() * 3))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = self.posicionX
        self.rect.y = self.posicionY

    def mover(self, dx=0, dy=0):
        self.posicionX += dx
        self.posicionY += dy    
        self.rect.x = self.posicionX
        self.rect.y = self.posicionY

   

