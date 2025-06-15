import pygame
from Constantes import *

class Muro(pygame.sprite.Sprite):
    def __init__(self, nombre,posicionX,posicionY):
        super().__init__()
        self.nombre = nombre
        self.image = pygame.image.load(WALL_PATH).convert_alpha()
        self.rect = self.image.get_rect(topleft=(posicionX,posicionY))
        self.activar = False
    
    def update(self):
        if self.activar:
            self.kill()
        