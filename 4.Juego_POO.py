import pygame, sys
from ImagenColor import Imagen_Color
from Enumerados import *


ANCHO = 800
ALTO = 600

FPS = 30 

pygame.init() 
PANTALLA = pygame.display.set_mode((ANCHO,ALTO)) 

pygame.display.set_caption("Bienvenidos")

PANTALLA.fill(Colores.NEGRO.value) 

imagen_vertical = Imagen_Color((100,100), (ANCHO//2, ALTO//2), (Colores.VERDE.value, Colores.ROJO.value))
imagen_horizontal = Imagen_Color((100,100), (ANCHO-50, ALTO//2), (Colores.AZUL.value, Colores.BLANCO.value))

clock = pygame.time.Clock()

while True:
    
    clock.tick(FPS)
    
    for evento in pygame.event.get(): 
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    PANTALLA.fill(Colores.NEGRO.value)

    pygame.draw.line(PANTALLA,Colores.AZUL.value,(400,0),(400,800),1)
    pygame.draw.line(PANTALLA,Colores.AZUL.value,(0,300),(800,300),1)

    PANTALLA.blit(imagen_vertical.imagen, imagen_vertical.rectangulo)
    PANTALLA.blit(imagen_horizontal.imagen, imagen_horizontal.rectangulo)

    imagen_vertical.mover_imagen(Orientaciones.VERTICAL.value, 10, (ANCHO,ALTO))
    imagen_horizontal.mover_imagen(Orientaciones.HORIZONTAL.value, 10, (ANCHO,ALTO))

    #en caso de colisionar, que cambie de color (se deben crear funciones para esto)

    imagen_vertical.detectar_colision(imagen_horizontal)
    
    pygame.display.flip() 


