from Constantes import *
import pygame
import random

def cargar_sprites(cantidad, path,del_fondo,escala=None,div=None):
    imagenes = []
    for i in range(cantidad):
        ruta = f"{path}{i}.png"
        try:
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
        except Exception as e:
            print(f" Error en el archivo {ruta}: {e}")
    
    return imagenes


def voltear_sprites(imagenes):
   return [pygame.transform.flip(imagen,True,False) for imagen in imagenes]


def cargar_elementos(cantidad,nombre,clase,lista,X,Y):
    if cantidad is not None:
        for i in range (cantidad):
            nombre = clase(nombre=f"{nombre}",posicionX= X, posicionY= Y)
            lista.add(nombre)  
    else:
        nombre = clase(nombre=f"{nombre}",posicionX= X, posicionY= Y)
        lista.add(nombre)

def coins_random(cantidad,nombre,clase,lista,X,Y):
      if cantidad is not None:
        for i in range (cantidad):
            nombre = clase(nombre=f"{nombre}",posicionX= random.randint(20,X), posicionY= random.randint(Y,580))
            lista.add(nombre)
        else:
            nombre = clase(nombre=f"{nombre}",posicionX= X, posicionY= Y)
            lista.add(nombre)


