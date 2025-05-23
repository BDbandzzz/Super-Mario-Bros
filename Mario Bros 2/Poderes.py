import pygame
from Constantes import * 
from Funciones import cargar_sprites


# Clase poderes
class Poderes(pygame.sprite.Sprite):
    def __init__(self, nombre, posicionX, posicionY):
        super().__init__()
        self.nombre = nombre
        self.posicionX = posicionX
        self.posicionY = posicionY
        self.contador = 0
        self.coins = cargar_sprites(3,COIN_PATH,False,escala=None,div=9)
        self.hongo = None
        self.hongoVida = None
        
        # Cargar sprites al crear el objeto    
        self.image = self.coins[0]
        self.rect = self.image.get_rect()
        self.rect.x = self.posicionX
        self.rect.y = self.posicionY


 
class Bonus(Poderes):
    def __init__(self, nombre, posicionX, posicionY):
        super().__init__(nombre, posicionX, posicionY)
        
        self.frame_actual = 0
        self.frame_tiempo = pygame.time.get_ticks()
        self.frame_carga = 300
        self.fotogramas = 3
        self.image = self.coins[0]
        
    def animacion(self):
        now = pygame.time.get_ticks()
        if now - self.frame_tiempo > self.frame_carga:
            self.frame_tiempo = now
            self.frame_actual = (self.frame_actual + 1) % self.fotogramas
            self.image = self.coins[self.frame_actual]
    
    
    def update(self):
        self.animacion()





