import pygame
class SoundEfects():
    def __init__(self):
        self.sonidos = { "Salto":pygame.mixer.Sound("Assets//soundEfect//salto.wav"),
                        "Coin" : pygame.mixer.Sound("Assets//soundEfect//coin.wav"),     
                        "Muerte": pygame.mixer.Sound("Assets//soundEfect//death.wav")
        }
    def reproducir(self, nombre):
        if nombre in self.sonidos:
            self.sonidos[nombre].play()
            
    def reproducir_musica_fondo(self,nombre, volumen =0.5,loop=True):
       self.sonidos_fondo = { "DonkeyK":"Assets//soundEfect//DonkeyK.wav",
                                "MarioB":"Assets//soundEfect//MarioBros.waw"
        }
       if nombre in self.sonidos_fondo:
        pygame.mixer_music.load(self.sonidos_fondo[nombre])
        pygame.mixer_music.set_volume(volumen)
        pygame.mixer_music.play(-1 if loop else 0)