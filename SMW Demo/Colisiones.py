from Personaje import Mario
from Poderes import Bonus, Hongo,HongoVida
from Enemigos import Goomba
import pygame

pygame.mixer.init()

def recojer_monedas(personaje):
     personaje.contador += 1
     personaje.coin += 1
     personaje.puntos +=1000
      
     if personaje.contador == 10:
        personaje.resetear_contador = True
        personaje.obtener_vida()
        
def chocar_enemigo(personaje, enemigo, efecto_sonido):
    if not enemigo.muerte and personaje.inmunidad:
        enemigo.muerte = True
        personaje.puntos +=400
    
    
    if not enemigo.muerte and (personaje.rect.bottom <= enemigo.rect.top + 10 and
        personaje.rect.right > enemigo.rect.left and 
        personaje.rect.left < enemigo.rect.right):
        
        # Pisa al enemigo
        personaje.activar_salto_goomba = True
        enemigo.tiempo_muerte = pygame.time.get_ticks()
        personaje.saltar(velocidad_inicial=6)
        personaje.puntos += 600
        enemigo.muerte = True
    
    else:
     if not personaje.game_over:   
        if (personaje.rect.right > enemigo.rect.left and 
            personaje.rect.left < enemigo.rect.right and
            personaje.rect.bottom > enemigo.rect.top and 
            personaje.rect.top < enemigo.rect.bottom):
            
            if (personaje.estado_personaje == "grande" and 
                not personaje.inmunidad and not enemigo.muerte) and not personaje.inmunidad_por_daño:
                personaje.estado_personaje = "pequeño"
                personaje.daño_inmunidad = pygame.time.get_ticks()
                personaje.inmunidad_por_daño = True  
                personaje.actualizar_estados()
                efecto_sonido.reproducir("Pequeño")
            
            elif(personaje.estado_personaje == "pequeño" 
                 and not personaje.inmunidad and not enemigo.muerte) and not personaje.inmunidad_por_daño:
                
                personaje.inmunidad_por_daño = True
                personaje.daño_inmunidad = pygame.time.get_ticks()
                personaje.vida -=1
                personaje.game_over = True
                personaje.actualizar_estados()
                personaje.time_death = pygame.time.get_ticks()
                pygame.mixer_music.pause()
                efecto_sonido.reproducir_musica_fondo("Muerte",loop=False)  
                
       
               

def hongo_Rojo(personaje,hongo):
    if personaje.estado_personaje == "pequeño":
        personaje.estado_personaje = "grande"
        personaje.puntos += 100
        personaje.actualizar_estados() 

def inmunidad(personaje, efecto_sonido):
    if not personaje.inmunidad:
        personaje.puntos +=300
        personaje.inmunidad = True
        personaje.inmunidad_time = pygame.time.get_ticks()
        efecto_sonido.reproducir_musica_fondo("Estrella", loop=False)
       
