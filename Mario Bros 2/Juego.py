import pygame
import os
import random

from SoundPlayer import SoundEfects
from Colisiones  import recojer_monedas, chocar_enemigo, hongo_Rojo,inmunidad
from Constantes import *
from Personaje  import Mario
from Enemigos import Goomba, Koppa
from Poderes import Bonus, Hongo, HongoVida, Estrella
from Funciones import cargar_elementos, coins_random

class Juego:
    def __init__(self):
        # Inicialización de Pygame
        pygame.init()
        pygame.mixer.init()
        self.PANTALLA = pygame.display.set_mode([ANCHURA_PANTALLA, ALTURA_PANTALLA])
        self.FPS = pygame.time.Clock()
        self.background = pygame.image.load(BACKGROUND_IMAGE).convert_alpha()

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
        cargar_elementos(1, "koopa",Koppa,self.all_lista_enemigos,X=700,Y=580)

        self.personaje = Mario("Mario", posicionX=0, posicionY=580)
        self.all_lista_sprites.add(self.personaje)

        self.sonido_Fondo = SoundEfects()
        self.sonido_Fondo.reproducir_musica_fondo(nombre="DonkeyK")

        self.juego_activo = True

    def manejar_personaje(self):
        movimiento_activo = False
        self.personaje.agachado = False
        self.personaje.running = False
        self.personaje.walking = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_DOWN]:
            if self.personaje.estado_personaje == "grande":
                movimiento_activo = False
                self.personaje.agachado = True

        if keys[pygame.K_LEFT]:
            movimiento_activo = True
            self.personaje.direccion = False
            self.personaje.caminar()
            if keys[pygame.K_x]:
                self.personaje.correr()

        if keys[pygame.K_RIGHT]:
            movimiento_activo = True
            self.personaje.direccion = True
            self.personaje.caminar()
            if keys[pygame.K_x]:
                self.personaje.correr()

        if keys[pygame.K_c]:
            movimiento_activo = True
            self.personaje.saltar()

        if not movimiento_activo:
            self.personaje.detener()

    def actualizar_sprites(self, *groups):
        for grupo in groups:
            grupo.update()

    def dibujar_en_pantalla(self, fondo, *groups):
        self.PANTALLA.blit(fondo, (0, 0))
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
                    hongo_Rojo(self.personaje)
                    self.sonido_Fondo.reproducir("Hongo")

    def colisiones_hongoVidas(self):
        colisiones = pygame.sprite.spritecollide(self.personaje, self.hongo_vida, dokill=True)
        if colisiones:
            for colision in colisiones:
                if isinstance(colision, HongoVida):
                    self.personaje.obtener_vida()

    def colisiones_estrella(self):
        colisiones = pygame.sprite.spritecollide(self.personaje, self.stars, dokill=True)
        if colisiones:
            for colision in colisiones:
                if isinstance(colision, Estrella):
                    inmunidad(self.personaje,self.sonido_Fondo)

    def generar_texto(self, *groups):
        fuente = pygame.font.Font(FONT_PATH, 60)
        x = 200
        for texto in groups:
            superficie = fuente.render(f"{texto}: ", True, WHITE)
            self.PANTALLA.blit(superficie, (x, 0))
            x += 600

    def bucle_principal(self):
        inmunidad_anterior = self.personaje.inmunidad
        
        while self.juego_activo:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.juego_activo = False
            self.manejar_personaje()
            self.actualizar_sprites(
                self.all_lista_enemigos,
                self.all_lista_sprites, self.monedas, self.stars,
                self.hongos, self.hongo_vida
            )
            self.dibujar_en_pantalla(
                self.background,
                self.all_lista_enemigos, self.all_lista_sprites,
                self.monedas, self.hongos, self.hongo_vida, self.stars
            )
            self.colisiones_Hongo()
            self.colisiones_hongoVidas()
            self.colisiones_coins()
            self.colisiones_enemigos()
            self.colisiones_estrella()
            
            if inmunidad_anterior and not self.personaje.inmunidad:
                self.sonido_Fondo.reproducir_musica_fondo("DonkeyK")
            inmunidad_anterior = self.personaje.inmunidad
            
            
            contador_vidas = self.personaje.vida 
            if self.personaje.game_over:
                self.juego_activo = False
                print("done")

            self.generar_texto(f"vidas: {contador_vidas}", f" coins: {self.personaje.coin}")

            pygame.display.flip()
            self.FPS.tick(60)

        pygame.quit()

if __name__ == "__main__":
    
    juego = Juego()
    juego.bucle_principal()

#o