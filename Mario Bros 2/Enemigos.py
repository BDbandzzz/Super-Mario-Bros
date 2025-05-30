import pygame
from Constantes import *
from Funciones import cargar_sprites,voltear_sprites

class Enemigo(pygame.sprite.Sprite):
    
    def __init__(self, nombre, posicionX, posicionY,vida=1):
        super().__init__()
        
        self.nombre = nombre
        self.posicionX = posicionX 
        self.posicionY = posicionY
        self.vida = vida
        self.gravedad = 4
        self.limite_suelo = 580
    def mover(self, dx=0, dy=0):
        self.rect.x += dx
        self.rect.y += dy
        
   
        
        
class Goomba(Enemigo):
    def __init__(self, nombre, posicionX, posicionY, vida=1):
        super().__init__(nombre, posicionX, posicionY, vida)
    
        self.movimiento = -1
        self.frame_actual = 0
        self.frame_tiempo = pygame.time.get_ticks()
        self.tiempo_muerte = pygame.time.get_ticks()
        self.muerte = False
        self.frame_carga = 300
        
        
        self.direccion = True
        self.sprites_goomba = cargar_sprites(2,ENEMY_IMAGE,False,escala=3)
        self.goomba_muerto = cargar_sprites(1,DEATH_ENEMY,False,escala=3)
        self.image = self.sprites_goomba[0]
        self.inverso = voltear_sprites(self.sprites_goomba)
        self.rect = self.image.get_rect()
        self.rect.x = posicionX
        self.rect.y = posicionY

        self.animaciones_ticks = 2
    
   # Si quieres que se active el movimiento del hongo, llama la funcion dentro del update o del bucle principal 
    def movimiento_enemigo(self):
        direccion = 3 * self.movimiento
        self.mover(dx = direccion)
        if self.rect.x <= 0:
            self.movimiento *= -1
            self.direccion = False

        elif self.rect.x >= ANCHURA_PANTALLA-40:
            self.movimiento *=-1
            self.direccion = True
    
    def animaciones(self,imagenes,inverso):
        now = pygame.time.get_ticks()
        if not self.muerte and now - self.frame_tiempo > self.frame_carga:
            self.frame_tiempo = now
            self.frame_actual = (self.frame_actual+ 1 ) % self.animaciones_ticks
            self.image = imagenes[self.frame_actual] if self.direccion else inverso[self.frame_actual]
    
    def morir(self,image):
        tiempo = pygame.time.get_ticks()
        if self.muerte:
            self.image = image[0]
            if tiempo - self.tiempo_muerte > 1000:
                self.kill()
    
    def update(self):
        self.movimiento_enemigo() if not self.muerte else self.morir(self.goomba_muerto)
        self.animaciones(self.sprites_goomba,self.inverso)
        
class Koppa(Goomba):
    def __init__(self, nombre, posicionX, posicionY, vida=1):
        super().__init__(nombre, posicionX, posicionY, vida)
        self.sprites_koopa = cargar_sprites(2,KOOPA_PATH,False,escala=3)
        self.death_koopa = cargar_sprites(1,DEATH_KOOPA,False,escala=3)
        self.image = self.sprites_koopa[0]    
        self.rect = self.image.get_rect()
        self.rect.x = posicionX
        self.rect.y = posicionY
        self.inverso = voltear_sprites(self.sprites_koopa)
        
    def caer(self):
        if self.rect.y < self.limite_suelo:
            if self.rect.x == 0:
                self.direccion = False
                self.movimiento *=-1
            self.mover(dy=+self.gravedad)
        
         
    
    def update(self):
        self.caer()
        self.animaciones(self.sprites_koopa,self.inverso)
        if self.rect.y == self.limite_suelo:
            self.movimiento_enemigo() if not self.muerte else self.morir(self.death_koopa)
             
    
            

    

        
        
        