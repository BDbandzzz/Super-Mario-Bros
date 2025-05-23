import os


# Archivo de constantes, aqui se añaden todas las variables necesarias
# para no sobrecargar el codigo principal.

#Direccion de la carpeta
ASSETS_PATH = "Assets"
BLACK = (0, 0, 0)

# Configuración de la pantalla
ANCHURA_PANTALLA = 1280
ALTURA_PANTALLA = 720


#Acceso a las imagenes
PLAYER_IMAGE = os.path.join(ASSETS_PATH,"SpritesMario//basePequeno//mario")
BACKGROUND_IMAGE = os.path.join(ASSETS_PATH,"Font", "Fondo1.png")
ENEMY_IMAGE = os.path.join(ASSETS_PATH,"SpritesEnemigos//Goomba00")
JUMP_PATH = os.path.join(ASSETS_PATH,"SpritesMario//saltoPequeno//mario")
RUNNING_PATH = os.path.join(ASSETS_PATH,"SpritesMario//caminarPequeno//mario")
COIN_PATH = os.path.join(ASSETS_PATH,"Coins//coins")



#Acceso a los efectos de sonido 
SOUND_PATH = os.path.join(ASSETS_PATH,"soundEfect")
