import os
import random

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
ENEMY_IMAGE      = os.path.join(ASSETS_PATH,"Sprites//SpritesEnemigos//Goomba00")
KOOPA_PATH       = os.path.join(ASSETS_PATH,"Sprites//SpritesEnemigos//Koopa//koopa")
DEATH_ENEMY      = os.path.join(ASSETS_PATH,"Sprites//SpritesEnemigos//death")
DEATH_KOOPA      = os.path.join(ASSETS_PATH,"Sprites//SpritesEnemigos//Koopa//death")

# Imagenes del personaje inicial
PLAYER_IMAGE = os.path.join(ASSETS_PATH,"Sprites//SpritesMario//basePequeno//mario")
JUMP_PATH    = os.path.join(ASSETS_PATH,"Sprites//SpritesMario//saltoPequeno//mario")
RUNNING_PATH = os.path.join(ASSETS_PATH,"Sprites//SpritesMario//caminarPequeno//mario")
DEATH_PATH   = os.path.join(ASSETS_PATH,"Sprites//SpritesMario//morir//mario")

# Imagenes para mario grande 
BASE_GRANDE    = os.path.join(ASSETS_PATH,"Sprites//SpritesMario//baseGrande//mario")
RUNNING_GRANDE = os.path.join(ASSETS_PATH,"Sprites//SpritesMario//caminarGrande//mario")
JUMP_GRANDE    = os.path.join(ASSETS_PATH,"Sprites//SpritesMario//saltoGrande//mario")
DOWN_GRANDE    = os.path.join(ASSETS_PATH,"Sprites//SpritesMario//agacharseGrande//mario")

# Imagenes para los poderes y bonus:
HONGO_VIDA_PATH = os.path.join(ASSETS_PATH,"Sprites//SpritesPowers//hongoVida//hongo")
COIN_PATH       = os.path.join(ASSETS_PATH,"Sprites//SpritesPowers//Coins//coins")
HONGO_PATH      = os.path.join(ASSETS_PATH,"Sprites//SpritesPowers//hongoRojo//hongo")
ESTRELLA_PATH   = os.path.join(ASSETS_PATH,"Sprites//SpritesPowers//estrella//estrella")

# Acceso y eleccion de fondo aleatorio
fondos_paralelos = ["fondo1","fondo2"]
opcion_fondo = random.choice(fondos_paralelos)

BACKGROUND_IMAGE = os.path.join(ASSETS_PATH,"background", "Fondo1.png")
PARALAX_IMAGES   = os.path.join(ASSETS_PATH,f"background//{opcion_fondo}//font")
GROUND_IMAGE     = os.path.join(ASSETS_PATH,f"background//{opcion_fondo}//ground.png")


# Acceso a la fuente de letra 
FONT_PATH  = os.path.join(ASSETS_PATH,"font//SMW.ttf")

#Acceso a las imagenes de la lista de stats 
STATS_PATH = os.path.join(ASSETS_PATH,"Sprites//statsList//stats")

#Acceso al muro invisible
WALL_PATH = os.path.join(ASSETS_PATH,"Sprites//wall//wall.png")



#Imagenes random
MENU_VIDAS_IMAGE = os.path.join(ASSETS_PATH,"Sprites//SpritesMario//basePequeno//mario0.png")
GAME_OVER_IMAGE = os.path.join(ASSETS_PATH,"Sprites//SpritesMario//morir//mario0.png")