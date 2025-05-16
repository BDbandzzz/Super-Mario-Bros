# Clase Personaje
import pygame
from Constantes import *


class Personaje(pygame.sprite.Sprite):
    def __init__(self, id, nombre, posicionX, posicionY, vida=3):
        super().__init__()
        self.id = id
        self.nombre = nombre
        self.posicionX = posicionX
        self.posicionY = posicionY
        self.vida = vida
        self.esta_saltando = bool
        self.velocidad_salto = 0
        self.gravedad = 0

        #Aqui se carga la imagen principal //"Puede cambiarse por una funcion que lo haga con
        # los sprites con los que se va a trabajar despues"
        
        self.image = pygame.image.load(PLAYER_IMAGE).convert_alpha()
        # Escalar la imagen del personaje
        self.image = pygame.transform.scale(self.image, (self.image.get_width() * 3, self.image.get_height() * 3))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = self.posicionX
        self.rect.y = self.posicionY

    #Se añade una funcion para mover el personaje y se la asigna un limite
    # maximo para no sobrepasar los limites del suelo y la pantalla 
    
    def mover(self, dx=0, dy=0):
        self.rect.x += dx
        self.rect.y += dy
        self.rect.x = max(0, min(self.rect.x,  ANCHURA_PANTALLA- self.rect.width))
        self.rect.y = max(0, min(self.rect.y, (ALTURA_PANTALLA-82) - self.rect.height))
    
    def saltar(self,velocidad_salto= 0):
        self.velocidad_salto = velocidad_salto
        self.esta_saltando = True


    def update(self,gravedad = 0):  
        self.gravedad = 0.5 
        self.velocidad_salto += self.gravedad 
        self.mover(dy = self.velocidad_salto)
        self.esta_saltando = False



class Mario(Personaje):
    def __init__(self, id, nombre, posicionX, posicionY, estado="Vivo", vida=3):
        super().__init__(id, nombre, posicionX, posicionY, estado, vida)
        
     
     