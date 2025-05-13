import pygame
import os

# Configuración de la pantalla
screen = pygame.display.set_mode([800, 400])
clock = pygame.time.Clock()

done = False

# ruta para la imagen
background_path = os.path.join("asests", "fondo.png")

try:
    background = pygame.image.load(background_path).convert()
except FileNotFoundError:
    print(f"Error: No se encontró el archivo '{background_path}'. Verifica que exista en la carpeta 'assets'.")
    pygame.quit()
    exit()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.blit(background, [0, 0])

    pygame.display.flip()
    clock.tick(60)

pygame.quit()