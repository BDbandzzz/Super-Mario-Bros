import pygame
import os
from Constantes import *
from Personaje import Personaje

# Inicialización de Pygame
pygame.init()

# Pnatalla y fps
PANTALLA = pygame.display.set_mode([ANCHURA_PANTALLA, ALTURA_PANTALLA])
FPS = pygame.time.Clock()

# Cargar fondo
background = pygame.image.load(BACKGROUND_IMAGE).convert_alpha()


# Crear personaje, ubicarlo en la posiciones 
personaje = Personaje(id=1, nombre="Jugador", posicionX=0, posicionY=580)
all_lista_sprites = pygame.sprite.Group()
all_lista_sprites.add(personaje)

# Variable boleana para el bucle principal 
Juego = False
score = 0


# Bucle abnegado xddddd, a son de que 
while not Juego:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Juego = True
      
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        personaje.mover(dx = -5)
    if keys[pygame.K_RIGHT]:
        personaje.mover(dx = 5)
    if keys[pygame.K_UP]:
        pass # Aqui va la funcion de salto, o no se con que tecla se puede poner
    if keys[pygame.K_DOWN]:
        personaje.mover(dy = 5)      

    all_lista_sprites.update()

    # Dibujar en la pantalla
    PANTALLA.blit(background, (0, 0))  # Dibujar el fondo
    all_lista_sprites.draw(PANTALLA)
    pygame.display.flip()
    FPS.tick(60)

pygame.quit()

