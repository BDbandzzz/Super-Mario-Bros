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
        self.hongo = None
        self.hongoVida = None
        
    # Atributos para animar:     
        self.frame_actual = 0
        self.frame_tiempo = pygame.time.get_ticks()
      
      
    def animacion(self,lista,framerate,fotogramas):
        now = pygame.time.get_ticks()
        if now - self.frame_tiempo > framerate:
            self.frame_tiempo = now
            self.frame_actual = (self.frame_actual + 1) % fotogramas
            self.image = lista[self.frame_actual]
           
        
        # Cargar sprites al crear el objeto    
  
class Bonus(Poderes):
    def __init__(self, nombre, posicionX, posicionY):
        super().__init__(nombre, posicionX, posicionY)
        self.coins = cargar_sprites(3,COIN_PATH,False,escala=None,div=9)
        self.image = self.coins[0] 
        self.rect = self.image.get_rect()
        self.rect.x = self.posicionX
        self.rect.y = self.posicionY
        
    def update(self):
        self.animacion(self.coins, 300, 3)
        
        
        
class Hongo(Poderes):
    pass
    
    
    

        
        





