import pygame
from Enumerados import Colores

ANCHO_VENTANA = 800
ALTO_VENTANA = 800
FPS = 15

pygame.init()

VENTANA = pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA))

pygame.display.set_caption("Primer ventana")

reloj = pygame.time.Clock()

flag = True
while flag:

    reloj.tick(FPS)

    lista_eventos = pygame.event.get()
    for evento in lista_eventos:
        if evento.type == pygame.QUIT:
            flag = False
        if evento.type == pygame.MOUSEBUTTONDOWN:
            print(evento.pos)

    lista_teclas = pygame.key.get_pressed()
    
    if lista_teclas[pygame.K_0]:
        print("PRESIONO 0")
    if lista_teclas[pygame.K_LEFT]:
        print("PRESIONO IZQUIERDA")
    if lista_teclas[pygame.K_ESCAPE]:
        flag = False

    VENTANA.fill(Colores.NEGRO.value)

    pygame.display.update()
