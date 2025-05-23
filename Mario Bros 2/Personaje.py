# Clase Personaje
import pygame
from Constantes import *
from Funciones import cargar_sprites,voltear_sprites
from SoundPlayer import SoundEfects


class Personaje(pygame.sprite.Sprite):
    def __init__(self,nombre, posicionX, posicionY, estado="Vivo", vida=3):
        super().__init__()
        self.nombre = nombre
        self.posicionX = posicionX
        self.posicionY = posicionY
        self.estado = estado
        self.vida = vida
   
        
        #Aqui se carga la imagen principal //"Puede cambiarse por una funcion que lo haga con
        # los sprites con los que se va a trabajar despues"  
        self.base = cargar_sprites(1,PLAYER_IMAGE,False,escala=3)
        self.caminando = cargar_sprites(3,RUNNING_PATH,True,escala=3)
        self.caminando_inverso = voltear_sprites(self.caminando)
        
        
        self.image = self.base[0]
        self.original = self.image 
        self.inverso = pygame.transform.flip(self.base[0],True,False)

        self.jump = cargar_sprites(1,JUMP_PATH,True,3)
        self.salto_inverso = pygame.transform.flip(self.jump[0],True,False)
        
        self.rect = self.image.get_rect()
        self.rect.x = self.posicionX
        self.rect.y = self.posicionY
    
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
        
        self.esta_saltando = False
        self.altura_salto = 0
        self.gravedad = 0.5
        self.velocidad = 0
        self.direccion = True  # True = derecha, False = izquierda
        self.running = False
        self.esta_quieto = True  # Nuevo atributo para controlar estado quieto
        self.walking = False
        self.sonidos = SoundEfects()
        
        
        # Atributos para animar 
        self.movimiento = -1
        self.frame_actual = 0
        self.frame_tiempo = pygame.time.get_ticks()
        self.frame_carga = 40
        self.fotogramas = 3
        
    def correr(self): 
        velocidad = 4 if self.direccion else -4
        self.running = True
        self.esta_quieto = False
        self.mover(dx=velocidad)
    
    def caminar(self):
        caminado = 4 if self.direccion else -4
        self.mover(dx=caminado)
        self.walking = True
        self.running = False
        self.esta_quieto = False
        
        
    
    def detener(self):
        self.running = False
        self.esta_quieto = True
        self.frame_actual = 0  # Resetear animación
        self.voltear_personaje()  # Asegurar dirección correcta
        
    def saltar(self, velocidad_inicial=-12):
        if not self.esta_saltando:
            self.esta_saltando = True
            self.esta_quieto = False
            self.sonidos.reproducir("Salto")
            self.altura_salto = velocidad_inicial
            
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
                # Al tocar el suelo, verificar si debe estar quieto
                if not self.running:
                    self.esta_quieto = True
                
    def isjumping(self):
        self.image = self.jump[0] if self.direccion else self.salto_inverso
    
    def voltear_personaje(self):
        # Actualizar tanto la imagen original como la inversa
        self.original = self.base[0]
        self.inverso = pygame.transform.flip(self.base[0], True, False)
        # Establecer la imagen correcta según dirección
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

    def update(self):
        self.caer()
         
        # Lógica de estados de animación
        if self.esta_saltando:
            self.isjumping()
        elif self.running or self.walking:
            frame = 40 if self.running else 150
            self.animar_personaje(frame_carga=frame,fotogramas=3)
        elif self.esta_quieto:
            self.voltear_personaje()
       