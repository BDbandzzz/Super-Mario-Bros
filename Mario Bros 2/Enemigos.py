import pygame
from Constantes import *

class Enemigo(pygame.sprite.Sprite):
    def __init__(self, nombre, posicionX, posicionY,vida=1):
        super().__init__()
        
        self.nombre = nombre
        self.posicionX = posicionX 
        self.posicionY = posicionY
        self.vida = vida
        self.image = pygame.image.load(ENEMY_IMAGE).convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.image.get_width() * 3, self.image.get_height() * 3))
        self.image.set_colorkey(BLACK)
        
        self.rect = self.image.get_rect()
        self.rect.x = posicionX
        self.rect.y = posicionY
    
    def mover(self, dx=0, dy=0):
        self.rect.x += dx
        self.rect.y += dy

        
class Goomba(Enemigo):
    def __init__(self, nombre, posicionX, posicionY, vida=1):
        super().__init__(nombre, posicionX, posicionY, vida)
    
        self.movimiento = -1
    
    def mover_goomba(self):
        direccion = 3 * self.movimiento
        self.mover(dx = direccion)
        if self.posicionX == ANCHURA_PANTALLA - 40:
            self.direccion *= -1
            
            
    def update(self):
        self.mover_goomba()
      
    


    

        
        
        