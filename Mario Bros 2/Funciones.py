from Constantes import *
import pygame

def cargar_sprites(cantidad, path,del_fondo, escala=None,div = None):
    imagenes = []
    
    for i in range(cantidad):
        ruta = f"{path}{i}.png"
        if del_fondo:
            image = pygame.image.load(ruta).convert_alpha()
        else:
            image = pygame.image.load(ruta)

        if escala is not None:
            ancho = int(image.get_width() * escala)
            alto = int(image.get_height() * escala)
            image = pygame.transform.scale(image, (ancho, alto))
        elif div is not None:
            ancho = int(image.get_width() // div)
            alto = int(image.get_height() // div)
            image = pygame.transform.scale(image, (ancho, alto))

        if del_fondo:
            image.set_colorkey(BLACK)  # Color negro como transparente
        imagenes.append(image)

    return imagenes


def voltear_sprites(imagenes):
   return [pygame.transform.flip(imagen,True,False) for imagen in imagenes]
