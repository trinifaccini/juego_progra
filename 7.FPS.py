import pygame
import random

from Enumerados import Colores

ANCHO_VENTANA = 800
ALTO_VENTANA = 800
FPS = 15

pygame.init()

VENTANA = pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA))

pygame.display.set_caption("Primer ventana")

# Generador aleatorio de enemigos
circulos = []
for i in range(500):
    x = random.randint(1, ANCHO_VENTANA-1)
    y = random.randint(1, ALTO_VENTANA-1)
    circulos.append([x,y]) # podria ser una tupla tb


reloj = pygame.time.Clock()

flag = True
while flag:

    reloj.tick(FPS)

    lista_eventos = pygame.event.get()
    for evento in lista_eventos:
        if evento.type == pygame.QUIT:
            flag = False

    VENTANA.fill(Colores.NEGRO.value)

    # MOVERLOS
    for c in circulos:
        c[0] += 1
        c[1] += 2

        if c[0] > ANCHO_VENTANA:
            c[0] = 0

        if c[1] > ALTO_VENTANA:
            c[1] = 0

    # DIBUJARLOS
    for c in circulos:
        pygame.draw.circle(VENTANA, Colores.ROJO.value, (c[0], c[1]), 5, 10)

    pygame.display.update()
