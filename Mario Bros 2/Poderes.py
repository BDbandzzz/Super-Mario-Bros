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
      
    def asignar_rect(self,imagen,X,Y):
        baseX = X
        baseY = Y
        self.image = imagen
        self.rect = self.image.get_rect()
        self.rect.x = baseX
        self.rect.y = baseY
    
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
        self.animacion(self.coins, 300, 2)
        
        
        
class Hongo(Poderes):
    def __init__(self, nombre, posicionX, posicionY):
        super().__init__(nombre, posicionX, posicionY) 
        self.hongo = cargar_sprites(2,HONGO_PATH,False,escala=3,div=None)
        self.image = self.hongo[0]
        self.rect = self.image.get_rect()
        self.rect.x = self.posicionX
        self.rect.y = self.posicionY
    
    def update(self):
        self.animacion(self.hongo,400,2)     



class HongoVida(Poderes):
    def __init__(self, nombre, posicionX, posicionY):
        super().__init__(nombre, posicionX, posicionY) 
        self.hongoVida = cargar_sprites(2,HONGO_VIDA_PATH,False,escala=3,div=None)        
        self.image = self.hongoVida[0]
        self.rect = self.image.get_rect()
        self.rect.x = self.posicionX
        self.rect.y = self.posicionY
    
    def update(self):
        self.animacion(self.hongoVida,200,2)     


class Estrella(Poderes):
    def __init__(self, nombre, posicionX, posicionY):
        super().__init__(nombre, posicionX, posicionY) 
        self.estrella = cargar_sprites(4,ESTRELLA_PATH,False,escala=3, div= None)
        self.image = self.estrella[0]
        self.rect = self.image.get_rect()
        self.rect.x = self.posicionX
        self.rect.y = self.posicionY
    def update(self):
        self.animacion(self.estrellaa,200,4)     


    


