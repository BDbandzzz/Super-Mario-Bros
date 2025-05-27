from Personaje import Mario
from Poderes import Bonus, Hongo,HongoVida
from Enemigos import Goomba
import pygame

now = pygame.time.get_ticks 

def recojer_monedas(personaje):
     personaje.contador += 1
     personaje.coin += 1
     if personaje.contador == 10:
        personaje.resetear_contador = True
        personaje.obtener_vida()
        
def chocar_enemigo(personaje, enemigo, efecto_sonido):
    if (personaje.rect.bottom <= enemigo.rect.top + 10 and
        personaje.rect.right > enemigo.rect.left and personaje.rect.left < enemigo.rect.right):
        # Pisa al enemigo
        personaje.activar_salto_goomba = True
        personaje.saltar(velocidad_inicial=6)
        enemigo.muerte = True
    else:
        if (personaje.rect.right > enemigo.rect.left and personaje.rect.left < enemigo.rect.right and
            personaje.rect.bottom > enemigo.rect.top and personaje.rect.top < enemigo.rect.bottom):
            if personaje.estado_personaje == "grande" and not personaje.inmunidad:
                personaje.estado_personaje = "pequeño"
                personaje.actualizar_estados()
                efecto_sonido.reproducir("Pequeño")
            elif personaje.estado_personaje == "pequeño" and not personaje.inmunidad:
                personaje.actualizar_estados()
                personaje.vida -=1
                 
def hongo_Rojo(personaje,hongo):
    if personaje.estado_personaje == "pequeño":
        personaje.estado_personaje = "grande"
        personaje.actualizar_estados() 
        hongo.recogido = True
        

def inmunidad(personaje,efecto_sonido):
    personaje.inmunidad = True
    efecto_sonido.reproducir_musica_fondo("Estrella",loop=False)