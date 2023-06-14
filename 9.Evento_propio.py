import pygame
from Enumerados import Colores

ANCHO_VENTANA = 800
ALTO_VENTANA = 800
FPS = 15

pygame.init()

VENTANA = pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA))

pygame.display.set_caption("Primer ventana")

reloj = pygame.time.Clock()

# Timer para el juego
timer_event = pygame.USEREVENT + 0
pygame.time.set_timer(timer_event, 1000)

contador = 0

flag = True
while flag:

    reloj.tick(FPS)

    lista_eventos = pygame.event.get()
    for evento in lista_eventos:
        if evento.type == pygame.QUIT:
            flag = False
        if evento.type == pygame.MOUSEBUTTONDOWN:
            print(evento.pos)
        if evento.type == timer_event:
            print(f"Tiempo de juego: {contador}" )
            contador += 1

    lista_teclas = pygame.key.get_pressed()

    if lista_teclas[pygame.K_ESCAPE]:
        flag = False

    VENTANA.fill(Colores.NEGRO.value)

    pygame.display.update()
