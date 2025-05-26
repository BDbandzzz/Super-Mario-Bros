from Personaje import Mario
from Poderes import Bonus, Hongo,HongoVida
from Enemigos import Goomba
import pygame



def recojer_monedas(personaje):
     personaje.contador += 1
     personaje.coin += 1
     if personaje.contador == 10:
        personaje.resetear_contador = True
        personaje.obtener_vida()
        
# YO NO HICE ESTO,ESTABA CANSADO Y USE EL STAND      
def chocar_enemigo(personaje, enemigo,efecto_sonido):
    # Colisión desde arriba (Mario pisa al enemigo
            if personaje.rect.bottom <= enemigo.rect.top + 10 and personaje.rect.right > enemigo.rect.left and personaje.rect.left < enemigo.rect.right:
                personaje.activar_salto_goomba = True
                personaje.saltar(velocidad_inicial=6)
                enemigo.muerte = True
                
            # Colisión por los lados (frente o atrás)
            elif not personaje.inmunidad:
                if (personaje.rect.right > enemigo.rect.left and personaje.rect.left < enemigo.rect.right and
                personaje.rect.bottom > enemigo.rect.top and personaje.rect.top < enemigo.rect.bottom):
                    if personaje.estado_personaje == "grande":
                        personaje.estado_personaje = "pequeño"
                        personaje.actualizar_estados()
                        efecto_sonido.reproducir("Pequeño")
                    else:
                        personaje.vida -=1
    
def hongo_Rojo(personaje):
    if personaje.estado_personaje == "pequeño":
        personaje.estado_personaje = "grande"
        personaje.actualizar_estados() 

def inmunidad(personaje,efecto_sonido):
    personaje.activar_inmunidad() 
    efecto_sonido.reproducir_musica_fondo("Estrella",loop=False)