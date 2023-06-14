import pygame

from Enumerados import Colores

ANCHO_VENTANA = 800
ALTO_VENTANA = 800

pygame.init()

VENTANA = pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA))

pygame.display.set_caption("Primer ventana")

fuente = pygame.font.SysFont("Arial", 60)
texto = fuente.render("Hola estudiantes de 1BD", False, Colores.VERDE.value, Colores.AZUL_CLARO.value)

flag = True
while flag:
    lista_eventos = pygame.event.get()
    for evento in lista_eventos:
        if evento.type == pygame.QUIT:
            flag = False

    VENTANA.blit(texto, (100,200))
    pygame.display.update()
