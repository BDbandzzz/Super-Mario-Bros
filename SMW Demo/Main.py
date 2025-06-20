import pygame
import os
import random

from Constantes import *
from Poderes    import Bonus, Hongo, HongoVida,Estrella
from Muro       import Muro
from Sonidos    import SoundEfects
from Enemigos   import Goomba, Koppa
from Personaje  import Mario
from EfectosVisuales import EfectoEstrella
from Funciones  import (cargar_elementos, coins_random,
                        cargar_sprites,renderizar_texto,gestor_tiempo,
                        dibujar_imagenes_aleatorias)

from Colisiones import (recojer_monedas, chocar_enemigo,
                        hongo_Rojo,inmunidad)

class Juego:
    
    def __init__(self):
        
        # Inicialización de Pygame y mesclador de sonido 
        pygame.init()
        pygame.mixer.init()
        
        # Elementos de pantalla 
        self.PANTALLA = pygame.display.set_mode([ANCHURA_PANTALLA, ALTURA_PANTALLA])
        pygame.display.set_caption("SMW Demo")
        self.FPS = pygame.time.Clock()
        self.suelo = pygame.image.load(GROUND_IMAGE)
        
        self.fondo_scroll = cargar_sprites(3,PARALAX_IMAGES,True)
        self.stats_images = cargar_sprites(2,STATS_PATH,False,escala=3)
        self.fuente= pygame.font.Font(FONT_PATH, 50)
       
        
        # Grupos de sprites
        self.all_lista_enemigos = pygame.sprite.Group()
        self.lista_sprites = pygame.sprite.Group()
        self.hongos = pygame.sprite.Group()
        self.stars = pygame.sprite.Group()
        self.hongo_vida = pygame.sprite.Group()
        self.monedas = pygame.sprite.Group()
        self.muros = pygame.sprite.Group()
        self.efectos_visuales = pygame.sprite.Group()


        # Instanciamos el personaje principal.    
        self.personaje = Mario("Mario", posicionX=0, posicionY=580)
        self.lista_sprites.add(self.personaje)

        # Instanciar elementos
        coins_random(5, "coin", Bonus, self.monedas, X=ANCHURA_PANTALLA-40, Y=320)
        cargar_elementos(1, "Hongo", Hongo, self.hongos, 400, Y=580)
        cargar_elementos(1, "HongoVida", HongoVida, self.hongo_vida, 600, 580)
        cargar_elementos(1, "Goomba", Goomba, self.all_lista_enemigos, X=1000, Y=580)
        cargar_elementos(1, "estrella", Estrella, self.stars, X=800, Y=580)
        cargar_elementos(1, "koopa",Koppa,self.all_lista_enemigos,X=1220,Y=0)
        cargar_elementos(1,"wall",Muro,self.muros,X=ANCHURA_PANTALLA//2,Y=400)
        cargar_elementos(1,"efectovisual",EfectoEstrella,self.efectos_visuales,X=self.personaje.rect.x,Y=self.personaje.rect.y)

        
        # Se establece el sonido de fondo, "Nombre" 
        # indica el sonido que se va a reproducir dentro del diccionario "self.sonidos_fondo"
        self.nombre_cancion = "DonkeyK" 
        self.sonido_Fondo = SoundEfects()
        self.sonido_Fondo.reproducir_musica_fondo(nombre=self.nombre_cancion)
        
        """ Gestor de Pantallas"""
        
        self.juego_activo = True
        self.juego_pausado = False
        self.juego_terminado = False
        self.menu = True
    
        
        # Estados para imunidad y hongos recogidos 
        self.inmunidad_anterior = self.personaje.inmunidad
        self.hongos_recogidos = False
        self.vidas_recogidos = False
        self.movimiento_activo = False
        self.esta_enlamitad = False
        self.pantalla_vidas = False
     
        self.tiempo_game_over = pygame.time.get_ticks()
        self.resetear_contador_vidas = False    
        self.contador_enemigos = 0
        self.movimiento_constante = 0

    
    
 
        
    def limpiar_listas(self):
        self.all_lista_enemigos.empty()
        self.lista_sprites.empty()
        self.hongos.empty()
        self.stars.empty()
        self.hongo_vida.empty()
        self.monedas.empty()
        self.muros.empty()
        self.efectos_visuales.empty()
    
    def resetear_elementos(self):
        self.vidas_actuales = self.personaje.vida
        coins_random(10, "coin", Bonus, self.monedas, X=ANCHURA_PANTALLA-40, Y=320)
        cargar_elementos(1, "Hongo", Hongo, self.hongos, 400, Y=580)
        cargar_elementos(1, "HongoVida", HongoVida, self.hongo_vida, 600, 580)
        cargar_elementos(1, "Goomba", Goomba, self.all_lista_enemigos, X=1000, Y=580)
        cargar_elementos(1, "estrella", Estrella, self.stars, X=800, Y=580)
        cargar_elementos(1, "koopa",Koppa,self.all_lista_enemigos,X=1220,Y=0)
        cargar_elementos(1,"efectovisual",EfectoEstrella,self.efectos_visuales,X=self.personaje.rect.x,Y=self.personaje.rect.y)

        # Instanciamos el personaje principal.    
        self.personaje = Mario("Mario", posicionX=0, posicionY=580,vida=self.vidas_actuales)
        self.lista_sprites.add(self.personaje)
        self.reset_stats()
     
        

            # // Funciones para el comportamiento del scroll //
    def reset_stats(self):
        if self.resetear_contador_vidas:
            self.personaje.vida = 3
            self.resetear_contador_vidas = False
        
        self.contador_enemigos = 0
        self.movimiento_constante = 0
        self.personaje.contador = 0
    
    
    def concatenar_listas(self,lista,*listas):
        for elementos in listas:
            lista.add(*elementos)
        return lista
    
    
    def manejar_scroll_sprites(self):
        self.lista_abs = pygame.sprite.Group()
        self.lista_abs = self.concatenar_listas(self.lista_abs,
                                                self.all_lista_enemigos,
                                                self.hongos,
                                                self.hongo_vida,
                                                self.monedas)
        for elementos in self.lista_abs:
            movimiento_elementos = 0 
            if self.personaje.running:
                movimiento_elementos +=6
            elif self.personaje.walking:
                movimiento_elementos +=2
            
            
            if self.esta_enlamitad:
                if self.personaje.direccion:
                    elementos.rect.x -= movimiento_elementos
                else:
                    elementos.rect.x += movimiento_elementos
                    
    
        
    
    def efecto_visual_inmunidad(self):        
        if self.personaje.inmunidad:
            self.dibujar_en_pantalla(self.efectos_visuales)
            self.actualizar_sprites(self.efectos_visuales)
            for efectos in self.efectos_visuales:
                efectos.mover(dx=self.personaje.rect.x,
                            dy=self.personaje.rect.y)
                if self.personaje.esta_agachado:
                    efectos.mover(dy=(self.personaje.rect.y),dx=self.personaje.rect.x)
                if self.personaje.estado_personaje == "grande":
                    efectos.activar = True
                else:
                    efectos.activar = False
                            

    def fondo_scrolling(self,fondo,suelo):
        for x in  range(5):
            self.velocidad = 0.2
            for scroll in fondo:
                self.PANTALLA.blit(scroll,(((x * ANCHURA_PANTALLA) -
                                            self.movimiento_constante *
                                            self.velocidad,0)))
                
                self.velocidad += 0.2
        
        """ Se blitea el suelo 2 veces y segun el movimiento y la velocidad se genera la sensacion de movimiento"""
        altura_suelo = suelo.get_height()
        for ground in range(2):
            self.PANTALLA.blit(suelo,((( ground * ANCHURA_PANTALLA) - self.movimiento_constante * self.velocidad
                                        , ALTURA_PANTALLA - altura_suelo)))
    
    def middle_wall(self):
        
        colisiones = pygame.sprite.spritecollide(self.personaje, self.muros, dokill=False)    
        if colisiones:
                x = -40 if self.personaje.rect.x <= ANCHURA_PANTALLA//2 else 30
                for muro in colisiones:
                    self.personaje.rect.x = (muro.rect.x) + x
                    self.esta_enlamitad = True
                    if self.movimiento_constante >= 1600 or self.movimiento_constante <= 0:
                        muro.activar = True                    
        else:
            self.esta_enlamitad = False
            
        if (len(self.muros) == 0 and (self.personaje.rect.x 
            >= (ANCHURA_PANTALLA//2)+60 or self.personaje.rect.x <= (ANCHURA_PANTALLA//2) - 60)) :
                
                new_muro = Muro("new_muro",ANCHURA_PANTALLA//2,400)
                self.muros.add(new_muro)
    
    def detectar_cambio_cancion(self):       
        if self.inmunidad_anterior and not self.personaje.inmunidad:
                self.sonido_Fondo.reproducir_musica_fondo(self.nombre_cancion)
        self.inmunidad_anterior = self.personaje.inmunidad
    

    def pausar_sonido (self):
        self.juego_pausado = not self.juego_pausado
        if self.juego_pausado:
            pygame.mixer_music.pause()
        else:
            pygame.mixer_music.unpause()
        
        
    def gestor_perdida_vidas(self):
        self.guardar_movimiento = self.movimiento_constante        
        self.tiempo_muerte = gestor_tiempo(parametro_tiempo=self.personaje.time_death,
                                           tiempo_transcurrido=5000)
        
        
        if self.personaje.perdida_vida:
            if self.tiempo_muerte and not self.personaje.vida <= 0:
                self.pantalla_vidas = True
                self.limpiar_listas()
                self.movimiento_constante = self.guardar_movimiento
        
        if self.personaje.vida <= 0 and self.tiempo_muerte:
            self.juego_terminado = True
            self.personaje.perdida_vida = False
            self.tiempo_game_over = pygame.time.get_ticks()
            self.limpiar_listas()
        
    
    def menu_perdida_vidas(self):
        while self.pantalla_vidas:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: 
                    self.pantalla_vidas = False
                    pygame.quit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        self.pantalla_vidas = False   
                
            renderizar_texto(fuente=self.fuente,
                         pantalla=self.PANTALLA,
                        texto=f"               x       {self.personaje.vida}",
                        transparencia= False
        )
        
            dibujar_imagenes_aleatorias(imagen=MENU_VIDAS_IMAGE,
                                        pantalla=self.PANTALLA,
                                        posX=-60,
                                        posY=0,escala=True)
    
    
    
    
            pygame.display.flip()
            self.FPS.tick(60)
        if not self.juego_terminado:    
            self.resetear_elementos()
        self.sonido_Fondo.reproducir_musica_fondo(self.nombre_cancion)
    
    def menu_game_over(self):
        self.tiempo_transcurrido = False 
        self.sonido_Fondo.reproducir("GameOver")

        while self.juego_terminado:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.juego_terminado = False
                    pygame.quit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN and self.tiempo_transcurrido:
                        self.juego_terminado = False

            # Verifica si han pasado 7000 ms desde el inicio del Game Over
            self.tiempo_transcurrido = gestor_tiempo(
                parametro_tiempo=self.tiempo_game_over,
                tiempo_transcurrido=7000)

            renderizar_texto(
                fuente=self.fuente,
                pantalla=self.PANTALLA,
                texto="Game Over.",
                transparencia=False
            )
            dibujar_imagenes_aleatorias(imagen=GAME_OVER_IMAGE,
                                        pantalla=self.PANTALLA,
                                        posX=0,
                                        posY=60,
                                        escala=True)
            
            
            pygame.display.flip()
            self.FPS.tick(60)

       
        self.resetear_contador_vidas = True
        self.resetear_elementos()
        self.sonido_Fondo.reproducir_musica_fondo(self.nombre_cancion)
    
    def menu_inicio(self):
        pygame.mixer_music.pause() 
      
        while self.menu:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: 
                    self.menu = False
                    pygame.quit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        self.menu = False   
        

            renderizar_texto(fuente=self.fuente,
                         pantalla=self.PANTALLA,
                        texto="Presiona Enter para iniciar",
                        transparencia= False)
            

           
            pygame.display.flip()
            self.FPS.tick(60)
        pygame.mixer_music.unpause()
    
    
            
    def movimiento_scroll(self):
        desplazamiento_derecha = 0
        desplazamiento_izquierda = 0
        
        self.salto_movimiento = self.personaje.esta_saltando and (self.personaje.running or self.personaje.walking)
        self.movimiento_personaje = self.personaje.walking or self.personaje.running
        
        if (self.salto_movimiento or self.movimiento_personaje) and not self.personaje.esta_agachado:            
            if self.movimiento_activo and self.movimiento_constante > 0:
                if not self.personaje.direccion:
                    desplazamiento_izquierda -= 5
                    if self.personaje.running:
                        desplazamiento_izquierda -= 4
                self.movimiento_constante += desplazamiento_izquierda
                        
            if self.movimiento_activo and self.movimiento_constante < 1600:
                if self.personaje.direccion:
                    desplazamiento_derecha += 5
                    if self.personaje.running:
                        desplazamiento_derecha += 4
                self.movimiento_constante += desplazamiento_derecha
                    
                
 # --------------------------------------------------------------------------------   
    

    
    def control_personaje(self):
        self.movimiento_activo = False
        self.personaje.esta_agachado = False
        self.personaje.running = False
        self.personaje.walking = False
  
        keys = pygame.key.get_pressed()
        
        
        if not self.personaje.perdida_vida:
            if keys[pygame.K_DOWN] or keys[pygame.K_s]:
                
                if self.personaje.estado_personaje == "grande":
                    self.movimiento_activo = False
                    self.personaje.esta_agachado = True
            
            if (keys[pygame.K_LEFT] or keys[pygame.K_a]):
                self.movimiento_activo = True
                self.personaje.direccion = False
                self.personaje.caminar()
                
                if keys[pygame.K_x] or keys[pygame.K_RSHIFT]:
                    self.personaje.correr()

            if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
                self.movimiento_activo = True
                self.personaje.direccion = True
                self.personaje.caminar()
                
                if keys[pygame.K_x] or keys[pygame.K_RSHIFT]:
                    self.personaje.correr()
                            
            if keys[pygame.K_c] or keys[pygame.K_SPACE]:
                self.movimiento_activo = True
                self.personaje.saltar()

            if not self.movimiento_activo:
                self.personaje.detener()

#         // Funciones para actualizar y dibujar en pantalla // 
    
    def actualizar_sprites(self, *groups): # Iteramos y actualizamos la lista de sprites.
        for grupo in groups:
            grupo.update()
            

    def dibujar_en_pantalla(self,*groups): #  Y dibujamos en pantalla.
        for group in groups:
            group.draw(self.PANTALLA)
#----------------------------------------------------------------------------------


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
        if  colisiones:
            for colision in colisiones:
                if isinstance(colision, Hongo):
                    hongo_Rojo(self.personaje,self.hongos)
                    self.calcular_tiempo_drop = pygame.time.get_ticks()
                    self.personaje.puntos += 200
                    self.hongos_recogidos = True
                    self.sonido_Fondo.reproducir("Hongo")

    def colisiones_hongoVidas(self):
        colisiones = pygame.sprite.spritecollide(self.personaje, self.hongo_vida, dokill=True)
        if colisiones:
            for colision in colisiones:
                if isinstance(colision, HongoVida):
                    self.calcular_hongo_vida_drop = pygame.time.get_ticks()
                    self.personaje.puntos += 500
                    self.vidas_recogidos = True
                    self.personaje.obtener_vida()

    def colisiones_estrella(self):
        colisiones = pygame.sprite.spritecollide(self.personaje, self.stars, dokill=True)
        if colisiones:
            for colision in colisiones:
                if isinstance(colision, Estrella):
                    inmunidad(self.personaje,self.sonido_Fondo)

    def generador_stats(self, *texto_pantalla): #Acomodado a las malas.
        x_texto= 200 
        x_image = 200
        y = 20
        
        for texto in texto_pantalla:
            superficie = self.fuente.render(f"x {texto}", True, WHITE)
            self.PANTALLA.blit(superficie, (x_texto, 20))
            x_texto += 400
           
        for i in range(2): # XDDDDD
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
        
            nueva_vida = HongoVida("Vida",x,y)
            self.hongo_vida.add(nueva_vida) 
            self.vidas_recogidos = False
            
    
    def drop_enemigos(self):
    # Reduce la frecuencia de checks
        if len(self.all_lista_enemigos) == 0 and self.contador_enemigos < 10:
            self.contador_enemigos += 2 
            xkoopa = random.choice([0,1220])
            ykoopa = 0
            xgoomba = random.randint(700,900)
            
            new_enemy = Koppa("Koppa",xkoopa,ykoopa)
            new_goomba = Goomba("Goomba", xgoomba,580)
            self.all_lista_enemigos.add(new_enemy, new_goomba)
    
    def drop_coins(self): 
     x = random.randint(0,1000)   
     y = random.randint(320,580)
     if len(self.monedas) < 9:
        coin = Bonus("MONEDAS",x,y)
        self.monedas.add(coin)


    def bucle_principal(self):
        while self.juego_activo:
            # Verificar si el personaje perdió una vida
            if self.personaje.perdida_vida:
                self.gestor_perdida_vidas()

            # Manejo de eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.juego_activo = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:
                        self.pausar_sonido()

            # Dibujar si no estamos en el menú
            if not self.menu:
                self.fondo_scrolling(
                    self.fondo_scroll,
                    suelo=self.suelo
                )

                self.dibujar_en_pantalla(
                    self.all_lista_enemigos,
                    self.lista_sprites,
                    self.monedas,
                    self.hongos,
                    self.hongo_vida,
                    self.stars
                )

            # Actualizar lógica del juego si no está pausado
            if not self.juego_pausado:
                self.actualizar_sprites(self.lista_sprites)

                if not self.personaje.perdida_vida:
                    self.actualizar_sprites(
                        self.muros,
                        self.all_lista_enemigos,
                        self.monedas,
                        self.stars,
                        self.hongos,
                        self.hongo_vida
                    )

                self.generador_stats(
                    f"{self.personaje.vida}",
                    f"{self.personaje.coin}",
                    f"{self.personaje.puntos}"
                )

                # Verificar condiciones para ejecutar lógica de juego activa
                if (not self.personaje.perdida_vida and
                    not self.juego_terminado and
                    not self.pantalla_vidas):

                    self.movimiento_scroll()
                    self.control_personaje()
                    self.colisiones_enemigos()
                    self.drop_hongos()
                    self.drop_vidas()
                    self.drop_enemigos()
                    self.colisiones_Hongo()
                    self.colisiones_hongoVidas()
                    self.colisiones_coins()
                    self.colisiones_estrella()
                    self.detectar_cambio_cancion()
                    self.middle_wall()
                    self.manejar_scroll_sprites()

            # Renderizado del mensaje de pausa
            else:
                renderizar_texto(
                    fuente=self.fuente,
                    pantalla=self.PANTALLA,
                    texto="Presione P para volver",
                    transparencia=True,
                    alpha=170
                )

            # Menú de vidas si se activa
            if self.pantalla_vidas:
                self.menu_perdida_vidas()

            # Menú de Game Over
            if self.juego_terminado:
                self.menu_game_over()
            
            if self.personaje.inmunidad:
                self.efecto_visual_inmunidad()
         
            # Control del framerate y actualización de pantalla
            self.FPS.tick(60)
            pygame.display.flip()


