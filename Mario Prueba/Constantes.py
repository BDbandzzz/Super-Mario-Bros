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
PLAYER_IMAGE = os.path.join(ASSETS_PATH, "basePequeño.png")
BACKGROUND_IMAGE = os.path.join(ASSETS_PATH, "Fondo1.png")
ENEMIGO_IMAGE = os.path.join(ASSETS_PATH , "goobba.png")

# ENEMIGO_IMAGE = os.path.join(ASSETS_PATH, "goomba.png")
