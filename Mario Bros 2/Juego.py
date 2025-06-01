import pygame
import os
import random

from Sonidos import SoundEfects
from Colisiones  import recojer_monedas, chocar_enemigo, hongo_Rojo,inmunidad
from Constantes import *
from Personaje  import Mario
from Enemigos import Goomba, Koppa
from Poderes import Bonus, Hongo, HongoVida, Estrella
from Funciones import cargar_elementos, coins_random,cargar_sprites

class Juego:
    def __init__(self):
        
        # Inicialización de Pygame y mesclador de sonido 
        pygame.init()
        pygame.mixer.init()
        
        # Elementos de pantalla 
        self.PANTALLA = pygame.display.set_mode([ANCHURA_PANTALLA, ALTURA_PANTALLA])
        self.FPS = pygame.time.Clock()
        self.background = pygame.image.load(BACKGROUND_IMAGE).convert_alpha()
        self.fuente= pygame.font.Font(FONT_PATH, 50)
     
       
    
        
        
        # Grupos de sprites
        self.all_lista_enemigos = pygame.sprite.Group()
        self.all_lista_sprites = pygame.sprite.Group()
        self.hongos = pygame.sprite.Group()
        self.stars = pygame.sprite.Group()
        self.hongo_vida = pygame.sprite.Group()
        self.monedas = pygame.sprite.Group()

        # Instanciar elementos
        coins_random(9, "coin", Bonus, self.monedas, X=ANCHURA_PANTALLA-40, Y=320)
        cargar_elementos(1, "Hongo", Hongo, self.hongos, 400, Y=580)
        cargar_elementos(1, "HongoVida", HongoVida, self.hongo_vida, 600, 580)
        cargar_elementos(1, "Goomba", Goomba, self.all_lista_enemigos, X=1000, Y=580)
        cargar_elementos(1, "estrella", Estrella, self.stars, X=800, Y=580)
        cargar_elementos(1, "koopa",Koppa,self.all_lista_enemigos,X=1220,Y=0)

        # Instanciamos el personaje principal.    
        self.personaje = Mario("Mario", posicionX=0, posicionY=580)
        self.all_lista_sprites.add(self.personaje)

        
        # Se establece el sonido de fondo, "Nombre" 
        # indica el sonido que se va a reproducir dentro del diccionario "self.sonidos_fondo"
        self.sonido_Fondo = SoundEfects()
        self.sonido_Fondo.reproducir_musica_fondo(nombre="DonkeyK")
        self.juego_activo = True
        self.juego_pausado = False
        
        self.stats_images = cargar_sprites(2,STATS_PATH,False,escala=3)
        
        # Estados para imunidad y hongos recogidos 
        self.inmunidad_anterior = self.personaje.inmunidad
        self.hongos_recogidos = False
        self.vidas_recogidos = False
        self.contador = 0


    def manejar_personaje(self):
        movimiento_activo = False
        self.personaje.agachado = False
        self.personaje.running = False
        self.personaje.walking = False
    
        keys = pygame.key.get_pressed()
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            if self.personaje.estado_personaje == "grande":
                movimiento_activo = False
                self.personaje.agachado = True

        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            movimiento_activo = True
            self.personaje.direccion = False
            self.personaje.caminar()
            if keys[pygame.K_x] or keys[pygame.K_RSHIFT]:
                self.personaje.correr()

        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            movimiento_activo = True
            self.personaje.direccion = True
            self.personaje.caminar()
            if keys[pygame.K_x] or keys[pygame.K_RSHIFT]:
                self.personaje.correr()

        if keys[pygame.K_c] or keys[pygame.K_SPACE]:
            movimiento_activo = True
            self.personaje.saltar()

        if not movimiento_activo:
            self.personaje.detener()

    def actualizar_sprites(self, *groups): # Iteramos y actualizamos la lista de sprites o sprites individuales.
        for grupo in groups:
            grupo.update()

    def dibujar_en_pantalla(self, fondo, *groups): # Iteramos individualmente y dibujamos en pantalla.
        self.PANTALLA.blit(fondo, (0, 0)) #cosas a cambiar: 1 movimiento de pantalla 2: funciones que, segun el movimiento del personaje me permita
        # cambiar el movimiento en pantalla.))w
        # Dentro de pantalla.blit se inicia la superficie, es decir, el fondo de pantalla
        # La funcion itera y dibuja en la pantalla.
        for group in groups:
            group.draw(self.PANTALLA)

    def colisiones_coins(self):
        colisiones = pygame.sprite.spritecollide(self.personaje, self.monedas, dokill=True)
        if colisiones:
            self.sonido_Fondo.reproducir("Coin")
            for colision in colisiones:
                if isinstance(colision, Bonus):
                    recojer_monedas(self.personaje)

    def colisiones_enemigos(self):
        colisiones = pygame.sprite.spritecollide(self.personaje, self.all_lista_enemigos, dokill=False)
        if colisiones:
            for colision in colisiones:
                self.personaje.activar_salto_goomba = False
                if isinstance(colision, Goomba) or isinstance(colision,Koppa):
                    chocar_enemigo(self.personaje, colision,self.sonido_Fondo)
                  
    def colisiones_Hongo(self):
        colisiones = pygame.sprite.spritecollide(self.personaje, self.hongos, dokill=True)
        if colisiones:
            for colision in colisiones:
                if isinstance(colision, Hongo):
                    hongo_Rojo(self.personaje,self.hongos)
                    self.calcular_tiempo_drop = pygame.time.get_ticks()
                    self.hongos_recogidos = True
                    self.sonido_Fondo.reproducir("Hongo")

    def colisiones_hongoVidas(self):
        colisiones = pygame.sprite.spritecollide(self.personaje, self.hongo_vida, dokill=True)
        if colisiones:
            for colision in colisiones:
                if isinstance(colision, HongoVida):
                    self.calcular_hongo_vida_drop = pygame.time.get_ticks()
                    self.vidas_recogidos = True
                    self.personaje.obtener_vida()

    def colisiones_estrella(self):
        colisiones = pygame.sprite.spritecollide(self.personaje, self.stars, dokill=True)
        if colisiones:
            for colision in colisiones:
                if isinstance(colision, Estrella):
                    inmunidad(self.personaje,self.sonido_Fondo)

    def generar_texto(self, *groups):
        x_texto= 200 
        x_image = 200
        
        
        y = 20

        for texto in groups:
            superficie = self.fuente.render(f"x {texto}", True, WHITE)
            self.PANTALLA.blit(superficie, (x_texto, 20))
           
            x_texto += 400
           
        for i in range(2):
            self.PANTALLA.blit(self.stats_images[i],(x_image-120,y))  
            x_image += 400
            y -=20 
    
            
    
    def drop_hongos(self):
        x = random.randint(400,1000)
        y = 580 
      
        now = pygame.time.get_ticks()
        if len(self.hongos) == 0:
            if self.hongos_recogidos and (now - self.calcular_tiempo_drop) > 9000:
                nuevo_hongo = Hongo("hongo",x,y)
                self.hongos.add(nuevo_hongo) 
                self.hongos_recogidos = False
    
    def drop_vidas(self):
        x = random.randint(400,1000)
        y = 580
        now = pygame.time.get_ticks()
        if self.vidas_recogidos and (now- self.calcular_hongo_vida_drop) > 9000:
            nueva_vida = HongoVida("Vida{",x,y)
            self.hongo_vida.add(nueva_vida) 
            self.vidas_recogidos = False
            
    def drop_enemigos(self):
     xkoopa = random.choice([0,1220])
     y = 580 
     
     ykoopa = 0
     xgoomba = random.randint(700,900)       
     
     if len(self.all_lista_enemigos) == 0:
                self.contador += 2 
                new_enemy = Koppa("Koppa",xkoopa,ykoopa)
                new_goomba = Goomba("Goomba", xgoomba,y)
                self.all_lista_enemigos.add(new_enemy)
                self.all_lista_enemigos.add(new_goomba)
                
                
    def drop_coins(self):
     x = random.randint(0,1000)  
     y = random.randint(320,580)
     if len(self.monedas) < 9:
        coin = Bonus("MONEDAS",x,y)
        self.monedas.add(coin)
             
             
    def detectar_cambio_cancion(self):       
        if self.inmunidad_anterior and not self.personaje.inmunidad:
                self.sonido_Fondo.reproducir_musica_fondo("DonkeyK")
        self.inmunidad_anterior = self.personaje.inmunidad
        

        

    
    def bucle_principal(self):
        while self.juego_activo:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: 
                    self.juego_activo = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:
                        self.juego_pausado = not self.juego_pausado
                        if self.juego_pausado:
                                pygame.mixer.music.pause()
                        else:
                            pygame.mixer.music.unpause()
                        


            
            self.dibujar_en_pantalla(
                self.background,
                self.all_lista_enemigos, self.all_lista_sprites,
                self.monedas, self.hongos, self.hongo_vida, self.stars
            )

            if not self.juego_pausado:
                self.manejar_personaje()
                self.actualizar_sprites(
                    self.all_lista_enemigos,
                    self.all_lista_sprites, self.monedas, self.stars,
                    self.hongos, self.hongo_vida)
                
                self.colisiones_enemigos()
                self.drop_hongos() if self.hongos_recogidos else None 
                self.drop_vidas() 
                self.drop_enemigos() if self.contador < 10 else None
                self.colisiones_Hongo()
                self.colisiones_hongoVidas()
                self.colisiones_coins()
                self.colisiones_estrella()
                self.detectar_cambio_cancion()
                self.generar_texto(f"{self.personaje.vida}", 
                                   f"{self.personaje.coin}",
                                   f"{self.personaje.puntos}")
            else:
                texto_pausa = self.fuente.render("Juego en pausa: Presione P para volver", True, (149, 165, 166 ))
                posicon_texto = texto_pausa.get_rect(center=(ANCHURA_PANTALLA/2, ALTURA_PANTALLA/2))
                self.PANTALLA.blit(texto_pausa, posicon_texto)
              

            if self.personaje.game_over:
                self.juego_activo = False

            pygame.display.flip()
            self.FPS.tick(60)

        pygame.quit()



