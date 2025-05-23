import pygame
import os
from Constantes import *
from Personaje import Mario
from Enemigos import Goomba
from Poderes import Bonus
from SoundPlayer import SoundEfects


# Inicialización de Pygame
pygame.init()

# Pantalla y fps
PANTALLA = pygame.display.set_mode([ANCHURA_PANTALLA, ALTURA_PANTALLA])
FPS = pygame.time.Clock()

# Cargar fondo
background = pygame.image.load(BACKGROUND_IMAGE).convert_alpha()

# Crear las listas de sprites 
personaje = Mario(nombre="Jugador", posicionX=0, posicionY=580)


all_lista_poderes = pygame.sprite.Group()
all_lista_enemigos = pygame.sprite.Group()
all_lista_sprites = pygame.sprite.Group()
# Funcion para cargar elementos de las listas
# Los nombres son las variables que se ultilizan dentro de la funcion.

def cargar_elementos(cantidad,nombre,clase,lista,X,Y):
    if cantidad is not None:
        for i in range (cantidad):
            nombre = clase(nombre=f"{nombre}",posicionX= X, posicionY= Y)
            lista.add(nombre)
    else:
        nombre = clase(nombre=f"{nombre}",posicionX= X, posicionY= Y)
        lista.add(nombre)

# Se cargan los elementos 
coin = cargar_elementos(1,"coin",Bonus,all_lista_poderes,X=320, Y=300)
enemigos = cargar_elementos(1,"Goomba",Goomba,all_lista_enemigos,X=600,Y=580)

personaje = Mario("Mario",posicionX= 0,posicionY=580)
all_lista_sprites.add(personaje)

sonido_Fondo = SoundEfects()
sonido_Fondo.reproducir_musica_fondo(nombre="DonkeyK")


def manejar_personaje(personaje):
             
    # Reiniciamos el estado de movimiento en cada frame
    movimiento_activo = False
    personaje.running = False
    personaje.walking = False
    
    # Manejo de teclas
    keys = pygame.key.get_pressed()
    
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
        
        
# Variables de control
Juego = False

while not Juego:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  
            Juego = True
   
   # Se cargan las funiones que antes estaban dentro del bucle de una manera mas organizada

    manejar_personaje(personaje)
    actualizar_sprites(all_lista_enemigos,all_lista_poderes,all_lista_sprites)
    dibujar_en_pantalla(PANTALLA,background,all_lista_enemigos,all_lista_poderes,all_lista_sprites)

    pygame.display.flip()
    FPS.tick(60)

pygame.quit()
