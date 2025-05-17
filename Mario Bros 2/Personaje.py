# Clase Personaje
import pygame
from Constantes import *


class Personaje(pygame.sprite.Sprite):
    def __init__(self, id, nombre, posicionX, posicionY, estado="Vivo", vida=3):
        super().__init__()
        self.id = id
        self.nombre = nombre
        self.posicionX = posicionX
        self.posicionY = posicionY
        self.estado = estado
        self.vida = vida
        
        #Aqui se carga la imagen principal //"Puede cambiarse por una funcion que lo haga con
         # los sprites con los que se va a trabajar despues"
        
        self.image = pygame.image.load(PLAYER_IMAGE).convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.image.get_width() * 3, self.image.get_height() * 3))
        self.image.set_colorkey(BLACK)
        self.original = self.image
        self.inverso = pygame.transform.flip(self.image,True,False)
        self.rect = self.image.get_rect()
        self.rect.x = self.posicionX
        self.rect.y = self.posicionY


        def cargar_sprites():
            pass   
    
    #Se añade una funcion para mover el personaje y se la asigna un limite
    # maximo para no sobrepasar los limites del suelo y la pantalla 
    
    def mover(self, dx=0, dy=0):
        self.rect.x += dx
        self.rect.y += dy
        self.rect.x = max(0, min(self.rect.x,  ANCHURA_PANTALLA- self.rect.width))
        self.rect.y = max(0, min(self.rect.y, (ALTURA_PANTALLA-82) - self.rect.height))
    

class Mario(Personaje):
    def __init__(self, id, nombre, posicionX, posicionY, estado="Vivo", vida=3):
        super().__init__(id, nombre, posicionX, posicionY, estado, vida)
        
        self.esta_saltando = False
        self.altura_salto = 0
        self.gravedad = 0.5
        self.velocidad = 0
        self.direccion = bool
        
    def correr(self, derecha): 
        self.direccion = derecha
        velocidad = 4 if self.direccion == True  else -8
        self.mover(dx=velocidad)
        
    def voltear_personaje(self):
        if self.direccion:
            self.image = self.original
        else:
            self.image = self.inverso     

    def saltar(self, velocidad_inicial=-12):
        if not self.esta_saltando:
            self.esta_saltando = True
            self.altura_salto = velocidad_inicial
            
    def bajar(self):
        if self.esta_saltando:
            self.altura_salto += self.gravedad
            self.mover(dy=self.altura_salto)
            limite_piso = (ALTURA_PANTALLA-82) - self.rect.height
            if self.rect.y >= limite_piso:
                self.rect.y = limite_piso
                self.esta_saltando = False
                self.altura_salto = 0
      
    def update(self):
        self.bajar()
        self.voltear_personaje()