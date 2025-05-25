import pygame
import os
import random

from SoundPlayer import SoundEfects
from Colisiones  import recojer_monedas,chocar_enemigo,hongo_Rojo
from Constantes import *
from Personaje import Mario
from Enemigos import Goomba
from Poderes import Bonus,Hongo,HongoVida,Estrella
from Funciones import cargar_elementos,coins_random



# Inicialización de Pygame
pygame.init()

# Pantalla y fps
PANTALLA = pygame.display.set_mode([ANCHURA_PANTALLA, ALTURA_PANTALLA])
FPS = pygame.time.Clock()
# Cargar fondo
background = pygame.image.load(BACKGROUND_IMAGE).convert_alpha()



all_lista_poderes = pygame.sprite.Group()
all_lista_enemigos = pygame.sprite.Group()
all_lista_sprites = pygame.sprite.Group()

hongos = pygame.sprite.Group()
stars = pygame.sprite.Group()
hongo_vida = pygame.sprite.Group()
monedas = pygame.sprite.Group()




# Funcion para cargar elementos de las listas
# Los nombres son las variables que se ultilizan dentro de la funcion.


            
            
# Se instancian los elementos             
coin = coins_random(10, "coin", Bonus, monedas, X=ANCHURA_PANTALLA-40, Y=320)
hongo = cargar_elementos(1,"Hongo",Hongo,hongos,200,Y=580)
hongoVerde =cargar_elementos(1,"HongoVida",HongoVida,hongo_vida,400,580)
enemigos = cargar_elementos(1,"Goomba",Goomba,all_lista_enemigos,X=600,Y=580)






personaje = Mario("Mario",posicionX= 0,posicionY=580)
all_lista_sprites.add(personaje)


sonido_Fondo = SoundEfects()
sonido_Fondo.reproducir_musica_fondo(nombre="DonkeyK")


def manejar_personaje(personaje): 
    # Reiniciamos el estado de movimiento en cada frame
    movimiento_activo = False
    personaje.agachado =False
    personaje.running = False
    personaje.walking = False
    
    # Manejo de teclas
    keys = pygame.key.get_pressed()
    
    
    if keys[pygame.K_DOWN]:
        if personaje.estado_personaje == "grande": 
            movimiento_activo = False
            personaje.agachado = True
        else:
            None
    
    if keys[pygame.K_LEFT]:
        movimiento_activo = True
        personaje.direccion = False
        personaje.caminar()
        
        if keys[pygame.K_x]:
            personaje.correr()
        
    if keys[pygame.K_RIGHT]:
        movimiento_activo = True
        personaje.direccion = True
        personaje.caminar()
        
        if keys[pygame.K_x]:
            personaje.correr()
            
    if keys[pygame.K_c]:
        movimiento_activo = True
        personaje.saltar()
    
    
    # Solo detener si no hay teclas de movimiento presionadas
    if not movimiento_activo:
        personaje.detener()

def actualizar_sprites(*groups):
    for grupo in groups:
        grupo.update()

def dibujar_en_pantalla(pantalla,fondo,*groups):
    pantalla.blit(fondo,(0,0))
    for group in groups:
        group.draw(pantalla)
    pygame.display.flip()
    
def colisiones_coins():
    colisiones = pygame.sprite.spritecollide(personaje,monedas,dokill=True)
    if colisiones:
        sonido_Fondo.reproducir("Coin")
        for colision in colisiones:
             if isinstance(colision, Bonus):
               recojer_monedas(personaje)
                    
def colisiones_enemigos():
    colisiones = pygame.sprite.spritecollide(personaje,all_lista_enemigos,False)
    if colisiones:
        sonido_Fondo.reproducir("Antonio")
        for colision in colisiones:
            personaje.activar_salto_goomba = False
            if isinstance(colision, Goomba):
                sonido_Fondo.reproducir("Antonio")
                chocar_enemigo(personaje=personaje)
                
                  
def colisiones_Hongo():
    colisiones = pygame.sprite.spritecollide(personaje,hongos,dokill=True)
    if colisiones:
        for colision in colisiones:
            if isinstance(colision,Hongo):
                personaje.estado_personaje = "grande"
                personaje.actualizar_estados()
    

def colisiones_hongoVidas():
    colisiones = pygame.sprite.spritecollide(personaje,hongo_vida,dokill=True)
    if colisiones:
        for colision in colisiones:
            if isinstance(colision,HongoVida):
                personaje.obtener_vida()
       


Juego = False
while not Juego:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  
            Juego = True
   
   # Se cargan las funiones que antes estaban dentro del bucle de una manera mas organizada
    manejar_personaje(personaje)
    
    actualizar_sprites(all_lista_enemigos,
                       all_lista_poderes,
                       all_lista_sprites,
                       monedas,hongos,hongo_vida)
    
    dibujar_en_pantalla(PANTALLA,background,
                        all_lista_enemigos,
                        all_lista_poderes,
                        all_lista_sprites,
                        monedas,hongos,hongo_vida)
    colisiones_Hongo()
    colisiones_hongoVidas()
    colisiones_coins() 
    colisiones_enemigos()
 
    
    pygame.display.flip()
    FPS.tick(60)

pygame.quit()

