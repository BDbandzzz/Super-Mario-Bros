import pygame
from Constantes import *
from Funciones import *

class Efectos(pygame.sprite.Sprite):   
    def __init__(self,nombre, posicionX, posicionY):
        super().__init__()
        self.frame_tiempo = pygame.time.get_ticks()
        self.frame_carga = 100
        self.frame_actual = 0
        self.animaciones_ticks = 3
        self.posicionX = posicionX
        self.posicionY = posicionY
        self.nombre = nombre

    def animaciones(self,imagenes):
        now = pygame.time.get_ticks()
        if now - self.frame_tiempo > self.frame_carga:
            self.frame_tiempo = now
            self.frame_actual = (self.frame_actual+ 1 ) % self.animaciones_ticks
            self.image = imagenes[self.frame_actual]
    
    def mover(self,dx,dy):
        self.rect.x = dx
        self.rect.y = dy
    
    
class EfectoEstrella(Efectos):
    def __init__(self, nombre, posicionX, posicionY):
        super().__init__(nombre,posicionX, posicionY)
        self.efecto_estrella_pequeño = cargar_sprites(3,ESTRELLA_EFFECT_PATH,False,escala=3)
        self.efecto_estrella_grande = cargar_sprites(3,ESTRELLA_EFFECT_GRANDE_PATH,False,escala=3)
        self.image = self.efecto_estrella_pequeño[0]
        self.activar = False
        
        self.rect = self.image.get_rect()
        self.rect.x = posicionX
        self.rect.y = posicionY
        
        
    
    def update(self):
        self.animaciones(imagenes=self.efecto_estrella_pequeño 
                         if not self.activar else self.efecto_estrella_grande)
       