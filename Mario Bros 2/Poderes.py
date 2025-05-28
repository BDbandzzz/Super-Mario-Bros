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
        self.direccion = -1
        
    # Atributos para animar:     
        self.frame_actual = 0
        self.frame_tiempo = pygame.time.get_ticks()
      
    def mover(self,dx=0,dy=0):
        self.rect.x += dx
        self.rect.y += dy
        self.rect.x = max(0, min(self.rect.x,  ANCHURA_PANTALLA- self.rect.width))
        self.rect.y = max(0, min(self.rect.y, (ALTURA_PANTALLA-82) - self.rect.height))
        
    
    def animacion(self,lista,framerate,fotogramas):
        now = pygame.time.get_ticks()
        if now - self.frame_tiempo > framerate:
            self.frame_tiempo = now
            self.frame_actual = (self.frame_actual + 1) % fotogramas
            self.image = lista[self.frame_actual]
    
    def movimiento_automatico(self):
        mover = self.direccion * 3
        self.mover(dx=mover)
        if self.rect.x <= 0:
         self.direccion *=-1 

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
        
        self.recogido = False
        self.tiempo_recogido = pygame.time.get_ticks()
         
    def update(self):
        self.animacion(self.hongo,400,2)     
        self.movimiento_automatico()


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
        self.movimiento_automatico()    
    


class Estrella(Poderes):
    def __init__(self, nombre, posicionX, posicionY):
        super().__init__(nombre, posicionX, posicionY) 
        self.estrella = cargar_sprites(4,ESTRELLA_PATH,False,escala=3, div= None)
        self.image = self.estrella[0]
        self.rect = self.image.get_rect()
        self.rect.x = self.posicionX
        self.rect.y = self.posicionY
        
        self.esta_saltando = False
        self.gravedad = 0.5
        self.altura_salto = 0
        self.direccion =-1
        
        
    def mover_estrella(self):
        mover_estrella = self.direccion * 3
        self.mover(dx=mover_estrella)
        if self.rect.x <= 0:
            self.direccion *=-1
            
                
    
    def salto(self,velocidad_inicial =-10):
        if not self.esta_saltando:
            self.altura_salto = velocidad_inicial
            self.esta_saltando = True
               
    def caer(self):
        if self.esta_saltando:
            self.altura_salto += self.gravedad
            self.mover(dy=self.altura_salto)
            limite_piso = (ALTURA_PANTALLA-82) - self.rect.height
            
            if self.rect.y >= limite_piso:
                self.rect.y = limite_piso
                self.esta_saltando = False   
                self.altura_salto = 0 
        
    def update(self):
        self.animacion(self.estrella,200,4)    
        if not self.esta_saltando:
            self.salto()
        else:
            self.caer()
        self.mover_estrella()
        


    


