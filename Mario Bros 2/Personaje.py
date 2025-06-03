# Clase Personaje
import pygame
from Constantes import *
from Funciones import cargar_sprites,voltear_sprites
from Sonidos import SoundEfects

pygame.mixer.init()
class Personaje(pygame.sprite.Sprite):
    def __init__(self,nombre, posicionX, posicionY, estado="vivo", vida=3,coin=0,contador= 0):
        super().__init__()
        
        self.nombre = nombre
        self.posicionX = posicionX
        self.posicionY = posicionY
        self.estado = estado
        self.vida = vida
        self.coin = coin
        self.contador = contador 
        self.game_over = False
       
     
    #Se añade una funcion para mover el personaje y se la asigna un limite
    # maximo para no sobrepasar los limites del suelo y la pantalla 
    
    def mover(self, dx=0, dy=0):
        self.rect.x += dx
        self.rect.y += dy
        self.rect.x = max(0, min(self.rect.x,  ANCHURA_PANTALLA- self.rect.width))
        self.rect.y = max(0, min(self.rect.y, (ALTURA_PANTALLA-82) - self.rect.height))
        

class Mario(Personaje):
    def __init__(self, nombre, posicionX, posicionY, estado="Vivo", vida=3):
        super().__init__(nombre, posicionX, posicionY, estado, vida)
        
       
       # Estados de mario en logica booleana 
        self.esta_saltando = False 
        self.direccion = True  # True = derecha, False = izquierda
        self.running = False # Evalua si  esta caminando
        self.walking = False # Evaluar si esta corriendo
        self.esta_quieto = True  # Controla y evalua si el personaje esta moviendose o no
        self.agachado = False   # Detectar si el personaje esta agachado o no
        self.activar_salto_goomba = False  # Detectar colision con el goomba y generar rebote 
        self.inmunidad = False  # Para detectar la inmunidad
        self.daño = False
        
        
        # Funciones para calcular el tiempo
        self.frame_tiempo = pygame.time.get_ticks()
        self.daño_inmunidad = pygame.time.get_ticks()
        self.inmunidad_time = pygame.time.get_ticks()
        
                
        # Se cargan las imagenes para realizar animaciones.
        self.sprites_mario = {
            "pequeño": {
            "saltar": cargar_sprites(1, JUMP_PATH, False, 3),
            "caminar": cargar_sprites(3, RUNNING_PATH, False, escala=3),
            "Base": cargar_sprites(1, PLAYER_IMAGE, False, escala=3),
            "Reverso_caminar": voltear_sprites(
                cargar_sprites(3, RUNNING_PATH, False, escala=3)
            ),
            },
            "grande": {
            "saltar": cargar_sprites(1, JUMP_GRANDE, False, 3),
            "caminar": cargar_sprites(3, RUNNING_GRANDE, False, escala=3),
            "Base": cargar_sprites(1, BASE_GRANDE, False, escala=3),
            "Reverso_caminar": voltear_sprites(
                cargar_sprites(3, RUNNING_GRANDE, False, escala=3)
            ),
            "Agacharse": cargar_sprites(1, DOWN_GRANDE, False, escala=3),
            },
        }
    # Imagenes iniciales 
        self.estado_personaje = "pequeño"
        self.base = self.sprites_mario[self.estado_personaje]["Base"]
        self.image = self.base[0]
        self.rect = self.image.get_rect()
        self.rect.x = posicionX
        self.rect.y = posicionY
        
        self.actualizar_estados()
       
        # Atributos para velocidades, salto y efectos de sonido
        
        
        self.altura_salto = 0
        self.gravedad = 0.5
        self.velocidad = 0
        self.sonidos = SoundEfects()
        
     
       
        # Atributos para animar 
        self.frame_actual = 0
        self.fotogramas = 3   
        # Contador 
        self.resetear_contador = False
        self.contador = 0
        self.puntos = 0
        
    def actualizar_estados(self):
        sprites = self.sprites_mario[self.estado_personaje]
        self.base = sprites["Base"]
        self.caminando = sprites["caminar"]
        self.jump = sprites["saltar"]
        self.caminando_inverso = sprites["Reverso_caminar"]
        self.salto_inverso = pygame.transform.flip(self.jump[0],True,False)
        if self.estado_personaje =="grande": 
            self.abajo = sprites["Agacharse"]
            self.abajo_inverso = pygame.transform.flip(self.abajo[0],True,False)
            self.redimensionar()
        else:
            self.redimensionar()
      
    def redimensionar(self): # Guarda y ajusta el resize de la imagen al actualizar el estado de mario  
        # Guarda la posición de los pies antes de cambiar el rect
        base_y = self.rect.y + self.rect.height
        base_x = self.rect.x
        
        # Cambia la imagen y el rect 
        self.image = self.base[0]
        self.rect = self.image.get_rect()
        
        # Reasigna la posición para que mario siempre este en el suelo
        # Bug: Si te mantienes agachado y te vuelves pequeño, mario queda en el aire.
        self.rect.x = base_x
        self.rect.y = base_y - self.rect.height 
    
    def correr(self): 
        if not self.agachado: # Se hace para evitar que, por ejemplo el personaje corra agachado
            velocidad = 4 if self.direccion else -4
            self.running = True
            self.esta_quieto = False
            self.mover(dx=velocidad)
    
    def caminar(self):
        if not self.agachado:
            caminado = 4 if self.direccion else -4
            self.mover(dx=caminado)
            self.walking = True
            self.running = False
            self.esta_quieto = False
            
    def detener(self):
        self.running = False
        self.walking = False
        self.esta_quieto = True
        self.agacharse() if self.agachado else self.voltear_base()
        
    def saltar(self, velocidad_inicial=-15):
        if not self.esta_saltando:
            
            self.esta_saltando = True
            self.esta_quieto = False
            self.sonidos.reproducir("Salto")
            self.altura_salto = velocidad_inicial
            
        elif self.activar_salto_goomba:
            velocidad_inicial = -5
            
            self.sonidos.reproducir("KillGoomba")
            self.altura_salto = velocidad_inicial
            self.esta_saltando = True
            self.esta_quieto = False
            self.activar_salto_goomba = False
        
        self.image = self.jump[0] if self.direccion else self.salto_inverso
           
    def caer(self):
        if self.esta_saltando:
            self.altura_salto += self.gravedad
            self.mover(dy=self.altura_salto)
            limite_piso = (ALTURA_PANTALLA-82) - self.rect.height
            if self.rect.y >= limite_piso:
                self.rect.y = limite_piso
                self.esta_saltando = False
                self.altura_salto = 0
                
                if not self.running:
                    self.esta_quieto = True
                
    def isjumping(self):
        self.image = self.jump[0] if self.direccion else self.salto_inverso
    
    def voltear_base(self):
        self.original = self.base[0]
        self.inverso = pygame.transform.flip(self.base[0], True, False)
        if self.direccion:
            self.image = self.original
        else:
            self.image = self.inverso
    
    def animar_personaje(self,frame_carga,fotogramas):
        now = pygame.time.get_ticks()
        self.fotogramas = fotogramas
        if (self.running or self.walking) and not self.esta_saltando:
            if now - self.frame_tiempo > frame_carga:
                self.frame_tiempo = now
                self.frame_actual = (self.frame_actual + 1) % self.fotogramas
                # Usar la animación correcta según la dirección
                sprites = self.caminando if self.direccion else self.caminando_inverso
                self.image = sprites[self.frame_actual]
                
    def obtener_vida(self):
        self.sonidos.reproducir("Vida")
        self.vida +=1
        if self.resetear_contador:
         self.contador = 0
         self.resetear_contador = False
         
    def agacharse(self):
        if self.estado_personaje == "grande":
            self.image = self.abajo[0] if self.direccion else self.abajo_inverso            
            
    def actualizar_inmunidad(self):
        if self.inmunidad:
            inmunidad_time = pygame.time.get_ticks()
            if inmunidad_time - self.inmunidad_time > 14000:
                self.inmunidad = False
                
    def inmunidad_daño(self):
        if self.daño:
            daño = pygame.time.get_ticks()
            if daño - self.daño_inmunidad> 3000:
                self.daño = False
            
    def morir(self):
        if self.vida == 0:
            self.game_over = True
                  
    def update(self):
        self.actualizar_inmunidad()
        self.inmunidad_daño()
        self.caer()   
        self.morir()
      

        # Lógica de estados de animación
        if self.agachado:
            self.agacharse()
        elif self.esta_saltando:
            self.isjumping()
        elif self.running or self.walking:
            frame = 40 if self.running else 150
            self.animar_personaje(frame_carga=frame,fotogramas=3)
        elif self.esta_quieto:
            self.voltear_base()
