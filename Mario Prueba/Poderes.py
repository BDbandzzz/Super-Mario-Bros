import pygame

# Clase poderes
class Poderes(pygame.sprite.Sprite):
    def __init__(self,nombre,posicionX,posicionY,estado,id,):
        
        self.nombre = nombre
        self.posicionX = posicionX
        self.posicionY = posicionY
        self.estado = estado
        self.id = id
        
        
        #creamos el poder hongo y lo indentamos con la clase poderes
class HongoRojo(Poderes):
    def __init__(self, nombre, posicionX, posicionY, estado, id, ):
            super().__init__(nombre, posicionX, posicionY, estado, id)
            self.tipo = "HongoRojo"
            pass

        #creamos el poder hongo y lo indentamos con la clase poderes
class HongoVerde(Poderes):
    def __init__(self, nombre, posicionX, posicionY, estado, id):
            super().__init__(nombre, posicionX, posicionY, estado, id)
            self.tipo = "HongoVerde"
            pass
            
           #creamos el poder estrella y lo indentamos con la clase poderes  
class estrella(Poderes):
    def __init__(self, nombre, posicionX, posicionY, estado, id):
            super().__init__(nombre, posicionX, posicionY, estado, id)
            self.tipo = "estrella eres invencible durante 5 segundos"
            pass    
 
    
            #creamos los coins y lo indentamos con la clase poderes
class coins(Poderes):
    def __init__(self, nombre, posicionX, posicionY, estado, id):
            super().__init__(nombre, posicionX, posicionY, estado, id)
            self.tipo = "bonus coins"
            pass 
        
    
    

