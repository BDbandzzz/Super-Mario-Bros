import os


# Archivo de constantes, aqui se añaden todas las variables necesarias
# para no sobrecargar el codigo principal.

#Direccion de la carpeta
ASSETS_PATH = "Assets"

# Colores: 
BLACK = (0, 0, 0)
WHITE = (255,255,255)

# Configuración de la pantalla
ANCHURA_PANTALLA = 1280
ALTURA_PANTALLA = 720


#Acceso a las imagenes
BACKGROUND_IMAGE = os.path.join(ASSETS_PATH,"Font", "Fondo1.png")
ENEMY_IMAGE = os.path.join(ASSETS_PATH,"SpritesEnemigos//Goomba00")
KOOPA_PATH = os.path.join(ASSETS_PATH,"SpritesEnemigos//Koopa//koopa")
DEATH_ENEMY = os.path.join(ASSETS_PATH,"SpritesEnemigos//death")
DEATH_KOOPA = os.path.join(ASSETS_PATH,"SpritesEnemigos//death")

# Imagenes del personaje inicial
PLAYER_IMAGE = os.path.join(ASSETS_PATH,"SpritesMario//basePequeno//mario")
JUMP_PATH = os.path.join(ASSETS_PATH,"SpritesMario//saltoPequeno//mario")
RUNNING_PATH = os.path.join(ASSETS_PATH,"SpritesMario//caminarPequeno//mario")
DEATH_PATH = os.path.join(ASSETS_PATH,"SpritesMario//morir//mario")

# Imagenes para mario grande 
BASE_GRANDE = os.path.join(ASSETS_PATH,"SpritesMario//baseGrande//mario")
RUNNING_GRANDE = os.path.join(ASSETS_PATH,"SpritesMario//caminarGrande//mario")
JUMP_GRANDE = os.path.join(ASSETS_PATH,"SpritesMario//saltoGrande//mario")
DOWN_GRANDE = os.path.join(ASSETS_PATH,"SpritesMario//agacharseGrande//mario")

# Imagenes para los poderes y bonus:
COIN_PATH = os.path.join(ASSETS_PATH,"SpritesPowers//Coins//coins")
HONGO_PATH = os.path.join(ASSETS_PATH,"SpritesPowers//hongoRojo//hongo")
HONGO_VIDA_PATH = os.path.join(ASSETS_PATH,"SpritesPowers//hongoVida//hongo")
ESTRELLA_PATH = os.path.join(ASSETS_PATH,"SpritesPowers//estrella//estrella")


#Acceso a los efectos de sonido 
SOUND_PATH = os.path.join(ASSETS_PATH,"soundEfect")



# Acceso a la fuente de letra 
FONT_PATH = os.path.join(ASSETS_PATH,"Letra//SMW.ttf")

