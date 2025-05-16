import pygame
import os
from Constantes import *
from Personaje import Personaje
from Enemigos import Enemigo
# Inicialización de Pygame
pygame.init()

# Pnatalla y fps
PANTALLA = pygame.display.set_mode([ANCHURA_PANTALLA, ALTURA_PANTALLA])
FPS = pygame.time.Clock()

# Cargar fondo
background = pygame.image.load(BACKGROUND_IMAGE).convert_alpha()


# Crear personaje, ubicarlo en la posiciones 
personaje = Personaje(id=1, nombre="Jugador", posicionX=0, posicionY=580)
Goomba = Enemigo(nombre="Goomba", posicionX=100, posicionY=580, vida=1, id=2)
personaje_volteado = pygame.transform.flip(personaje.image,True,False)
imagen_base = personaje.image
direccion = False



all_lista_sprites = pygame.sprite.Group()
all_lista_sprites.add(personaje)
all_lista_sprites.add(Goomba)

# Crear enemigo, ubicarlo en la posiciones




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
        if not direccion:
         direccion = True
         personaje.image = personaje_volteado
        personaje.mover(dx= -4)
    
    if keys[pygame.K_LEFT] and keys[pygame.K_x]:
        if not direccion:
         personaje.image = personaje_volteado
         direccion = True
        valor = + -1
        velocidad = max(-10, min(valor, -5))
        personaje.mover(dx = -5 + velocidad)  
        
    if keys[pygame.K_RIGHT] and keys[pygame.K_x]:
        if direccion:
         personaje.image = imagen_base
         direccion = False
        valor =+ 1
        velocidad = max(10, min(valor,5))
        personaje.mover(dx = 4 + velocidad)
        
    if keys[pygame.K_RIGHT]:
        
        if direccion:
            direccion = False  
            personaje.image = imagen_base
        personaje.mover(dx=4)   
           
    if keys[pygame.K_UP]:
        pass # Aqui va la funcion de salto, o no se con que tecla se puede poner
    if keys[pygame.K_DOWN]:
        personaje.mover(dy = 4)      

    all_lista_sprites.update()

    # Dibujar en la pantalla
    PANTALLA.blit(background, (0, 0))  # Dibujar el fondo
    all_lista_sprites.draw(PANTALLA)
    pygame.display.flip()
    FPS.tick(60)

pygame.quit()

