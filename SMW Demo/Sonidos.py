import pygame
from Constantes import * 

class SoundEfects():
    
    def __init__(self):
        self.sonidos = { "Salto":  pygame.mixer.Sound("Assets//Sonidos//salto.wav"),
                        "Coin" :   pygame.mixer.Sound("Assets//Sonidos//coin.wav"),     
                        "Antonio": pygame.mixer.Sound("Assets//Sonidos//OOH.mp3"),
                        "Vida":    pygame.mixer.Sound("Assets//Sonidos//Up.wav"),
                        "Hongo":   pygame.mixer.Sound("Assets//Sonidos//powerup.wav"),
                        "Pequeño": pygame.mixer.Sound("Assets//Sonidos//pequeño.wav"),
                    "KillGoomba":  pygame.mixer.Sound("Assets//Sonidos//Kick.wav")
     
        }
    def reproducir(self, nombre):
        if nombre in self.sonidos:
            self.sonidos[nombre].play()
            
    def reproducir_musica_fondo(self,nombre, volumen =0.5,loop=True):
        
       self.sonidos_fondo = {"DonkeyK": "Assets//Sonidos//DonkeyK.wav",
                            "MarioB":   "Assets//Sonidos//MarioBros.waw",
                            "MMX3":     "Assets//Sonidos//MMX3.wav",
                            "Estrella": "Assets//Sonidos//estrella.mp3",
                            "Muerte":   "Assets//Sonidos//death.wav"
                            
        }
       if nombre in self.sonidos_fondo:
        pygame.mixer_music.load(self.sonidos_fondo[nombre])
        pygame.mixer_music.set_volume(volumen)
        pygame.mixer_music.play(-1 if loop else 0)
        