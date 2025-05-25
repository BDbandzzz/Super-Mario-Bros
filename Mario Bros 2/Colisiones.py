from Personaje import Mario
from Poderes import Bonus, Hongo,HongoVida
from Enemigos import Goomba
from SoundPlayer import SoundEfects
    

def recojer_monedas(personaje):
     personaje.contador += 1
     personaje.coin += 1
     if personaje.contador == 10:
        personaje.resetear_contador = True
        personaje.obtener_vida()
        
        
def chocar_enemigo(personaje): # Corregir
    personaje.saltar(velocidad_inicial=6)
    personaje.activar_salto_goomba = True
    if personaje.estado_personaje == "grande":
        personaje.estado_personaje = "pequeño"
        personaje.actualizar_estados()
    else:
        None
    
def hongo_Rojo(personaje):
    if personaje.estado_personaje == "pequeño":
        personaje.estado_personaje = "grande"
        personaje.actualizar_estados() 

        
        
def hongo_Vida(personaje):
        personaje.obtener_vida()
    


def estrella(personaje):
    if personaje.estado_personaje == "pequeño":
        personaje.actualizar_estados() 
    elif personaje.estado_personaje == "grande":
        personaje.estado_personaje = "inmunidad"
        personaje.actualizar_estados()        
        
  
        