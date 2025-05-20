import pygame
import os
from Constantes import *
from Personaje import Mario
from Enemigos import Goomba

# Inicialización de Pygame
pygame.init()

# Pnatalla y fps
PANTALLA = pygame.display.set_mode([ANCHURA_PANTALLA, ALTURA_PANTALLA])
FPS = pygame.time.Clock()

# Cargar fondo
background = pygame.image.load(BACKGROUND_IMAGE).convert_alpha()


# Crear personaje, ubicarlo en la posiciones 
personaje = Mario(id=1, nombre="Jugador", posicionX=0, posicionY=580)
enemigo = Goomba(nombre="Goomba",posicionX = 600,posicionY=580)
all_lista_sprites = pygame.sprite.Group()

all_lista_sprites.add(personaje)
all_lista_sprites.add(enemigo)

# Variable boleana para el bucle principal 
Juego = False
score = 0


# Bucle abnegado xddddd, a son de que 



while not Juego:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Juego = True
      
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and keys[pygame.K_x]:
        personaje.correr(derecha=False)
        
    if keys[pygame.K_LEFT]:
        personaje.mover(dx= -4)
        personaje.direccion = False
    
    if keys[pygame.K_RIGHT] and keys[pygame.K_x]: 
        personaje.correr(derecha=True)
        
    if keys[pygame.K_RIGHT]:
        personaje.mover(dx = 4)
        personaje.direccion = True
        
    if keys[pygame.K_c]:
        personaje.saltar()
        
    if keys[pygame.K_DOWN]:
        personaje.mover(dy = 4)      
    
    
    all_lista_sprites.update()

    
    PANTALLA.blit(background, (0, 0))
    all_lista_sprites.draw(PANTALLA)
    
    pygame.display.flip()
    FPS.tick(60) 

pygame.quit()

