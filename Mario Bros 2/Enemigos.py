import pygame
from Constantes import *
from Funciones import cargar_sprites

class Enemigo(pygame.sprite.Sprite):
    
    def __init__(self, nombre, posicionX, posicionY,vida=1):
        super().__init__()
        
        self.nombre = nombre
        self.posicionX = posicionX 
        self.posicionY = posicionY
        self.vida = vida
        
        self.sprites_goomba = cargar_sprites(2,ENEMY_IMAGE,False,escala=3)
        self.image = self.sprites_goomba[0]
        
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
        self.frame_actual = 0
        self.frame_tiempo = pygame.time.get_ticks()
        self.frame_carga = 300
        self.image = self.sprites_goomba[0]
        self.animaciones_ticks = 2
    
    def mover_goomba(self):
        direccion = 3 * self.movimiento
        self.mover(dx = direccion)
        if self.posicionX <= 0:
            direccion *= -1
    
    
    def animaciones(self):
        now = pygame.time.get_ticks()
        if now - self.frame_tiempo > self.frame_carga:
            self.frame_tiempo = now
            self.frame_actual = (self.frame_actual+ 1 ) % self.animaciones_ticks
            self.image = self.sprites_goomba[self.frame_actual]
            
    def update(self):
        self.mover_goomba()
        self.animaciones()
      
    


    

        
        
        