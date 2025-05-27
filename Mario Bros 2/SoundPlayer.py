import pygame
class SoundEfects():
    def __init__(self):
        self.sonidos = { "Salto":pygame.mixer.Sound("Assets//soundEfect//salto.wav"),
                        "Coin" : pygame.mixer.Sound("Assets//soundEfect//coin.wav"),     
                        "Muerte": pygame.mixer.Sound("Assets//soundEfect//death.wav"),
                        "Antonio":pygame.mixer.Sound("Assets//soundEfect//OOH.mp3"),
                        "Vida": pygame.mixer.Sound("Assets//soundEfect//Up.wav"),
                        "Hongo": pygame.mixer.Sound("Assets//soundEfect//powerup.wav"),
                        "Pequeño": pygame.mixer.Sound("Assets//soundEfect//pequeño.wav"),
     
        }
    def reproducir(self, nombre):
        if nombre in self.sonidos:
            self.sonidos[nombre].play()
            
    def reproducir_musica_fondo(self,nombre, volumen =0.5,loop=True):
       self.sonidos_fondo = { "DonkeyK":"Assets//soundEfect//DonkeyK.wav",
                                "MarioB":"Assets//soundEfect//MarioBros.waw",
                                "MMX3": "Assets//SoundEfect//MMX3.wav",
                                "Estrella":"Assets//SoundEfect//estrella.mp3"
        }
       if nombre in self.sonidos_fondo:
        pygame.mixer_music.load(self.sonidos_fondo[nombre])
        pygame.mixer_music.set_volume(volumen)
        pygame.mixer_music.play(-1 if loop else 0)