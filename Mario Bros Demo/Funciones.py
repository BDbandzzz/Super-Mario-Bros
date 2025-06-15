from Constantes import *
import pygame
import random

""" Funcion de cargar los sprites, segun los parametros que se pasan haran las funciones designadas
Si quieres que se elimine el fondo, pasa del_fondo = True
Si quieres que se amplie la imagen, pasa un parametro a escala
Si quieres que se reduzca la imagen, pasa parametro a div
Si quieres que se carguen varias imagenes, pasa la cantidad de imagenes en cantidad."""

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
            

            imagenes.append(image)
        except Exception as e:
            print(f" Error en el archivo {ruta}: {e}")
    return imagenes

"""Solo voltea las imagenes a la izquierda, retorna una lista
Por la cantidad de sprites que se maneja o se planea ultilizar mas adelante."""

def voltear_sprites(imagenes):
   return [pygame.transform.flip(imagen,True,False) for imagen in imagenes]



""" Me permite instanciar los elementos y agregarlos a la lista de sprites"""
def cargar_elementos(cantidad,nombre,clase,lista,X,Y):
        for i in range(cantidad):
            nombre = clase(nombre=f"{nombre}",posicionX= X, posicionY= Y)
            lista.add(nombre)  


"""Me permite generar coins en posiciones aleatorias."""
def coins_random(cantidad,nombre,clase,lista,X,Y):
        for i in range (cantidad):
            
            nombre = clase(nombre=f"{nombre}",
                           posicionX= random.randint(20,X),
                           posicionY= random.randint(Y,580))
            lista.add(nombre)
        return lista

      
""" Funcion para renderizar el texto en pantalla, 
segun los parametros y la cantidad de transparencia
Fuente = Tipo de fuente, pantalla = Superficie de la paantalla, 
texto = Texto que se va a ultilizar para poner en pantalla 
Por el momento esta funcion solo puede poner texto 
en un fondo negro o transparente, con un color en especifico."""


def renderizar_texto(fuente, pantalla, texto=str,transparencia=bool,alpha=int):
    if not transparencia:
        fondo = pygame.Surface((ANCHURA_PANTALLA,ALTURA_PANTALLA))
        fondo.fill(BLACK)
    
    else:
        fondo = pygame.Surface((ANCHURA_PANTALLA,ALTURA_PANTALLA),pygame.SRCALPHA)
        fondo.fill((0,0,0,alpha))
    
    texto_pantalla = fuente.render(texto,False,WHITE)
    posicion_texto = texto_pantalla.get_rect(center=(ANCHURA_PANTALLA//2,
                                                        ALTURA_PANTALLA//2))        
    pantalla.blit(fondo,(0,0))
    pantalla.blit(texto_pantalla,posicion_texto)
        