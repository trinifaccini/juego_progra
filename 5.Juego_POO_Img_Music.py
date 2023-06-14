import sys
import pygame
from Imagen import Imagen
from Enumerados import Orientaciones

ANCHO = 1000
ALTO = 500
FPS = 18

pygame.init()
screen_size = (ANCHO,ALTO)
PANTALLA = pygame.display.set_mode(screen_size)
pygame.display.set_caption("HOMEROLAND")

icono = pygame.image.load("Recursos/icono_homero.png") #donde se encuentra la imagen
pygame.display.set_icon(icono)

#FONDO
fondo = pygame.image.load("Recursos/fondo_casa.jpg")
fondo = pygame.transform.scale(fondo, screen_size)

#MUSICA
pygame.mixer.music.load("Recursos/intro.mp3")
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.2)

imagen_vertical = Imagen((100,100), (ANCHO//2, ALTO//2), "Recursos/dona.png")
imagen_horizontal = Imagen((150,250), (ANCHO-50, ALTO//2), "Recursos/homero.png")

clock = pygame.time.Clock()

while True:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    PANTALLA.blit(fondo, (0, 0))

    PANTALLA.blit(imagen_vertical.imagen, imagen_vertical.rectangulo)
    PANTALLA.blit(imagen_horizontal.imagen, imagen_horizontal.rectangulo)

    imagen_vertical.mover_imagen(Orientaciones.VERTICAL, 10, (ANCHO,ALTO))
    imagen_horizontal.mover_imagen(Orientaciones.HORIZONTAL, 10, (ANCHO,ALTO))

    imagen_horizontal.detectar_colision(imagen_vertical)

    pygame.display.update()
    pygame.display.flip()