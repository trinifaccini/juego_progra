import pygame

ANCHO_VENTANA = 800
ALTO_VENTANA = 800
FPS = 15
TAMANIO_PANTALLA = (ANCHO_VENTANA, ALTO_VENTANA)

pygame.init()
RELOJ = pygame.time.Clock()

# Pantalla
PANTALLA = pygame.display.set_mode(TAMANIO_PANTALLA)
pygame.display.set_caption("Primer ventana")

fondo = pygame.image.load("Recursos/fondo_casa.jpg")
fondo = pygame.transform.scale(fondo, TAMANIO_PANTALLA)

# HOMERO
imagen_homero_der = pygame.image.load("Recursos/derecha.png") #donde se encuentra la imagen
imagen_homero_der  = pygame.transform.scale(imagen_homero_der, (200,250))

#imagen_homero_izq = pygame.image.load("Recursos/izquieda.png") #donde se encuentra la imagen
imagen_homero_izq = pygame.transform.flip(imagen_homero_der, True, False)
imagen_homero_izq = pygame.transform.scale(imagen_homero_izq, (200,250))

imagen_homero = imagen_homero_der

rectangulo_homero = imagen_homero.get_rect()
rectangulo_homero.x = 400
rectangulo_homero.y = 570
rectangulo_homero.width = 200
rectangulo_homero.height = 200


flag = True
while flag:

    RELOJ.tick(FPS)

    lista_eventos = pygame.event.get()
    for evento in lista_eventos:
        if evento.type == pygame.QUIT:
            flag = False

    lista_teclas = pygame.key.get_pressed()

    if lista_teclas[pygame.K_RIGHT]:
        nueva_x = rectangulo_homero.x + 10
        if nueva_x < ANCHO_VENTANA - rectangulo_homero.width:
            rectangulo_homero.x += 10
            imagen_homero = imagen_homero_der
    if lista_teclas[pygame.K_LEFT]:
        nueva_x = rectangulo_homero.x - 10
        if nueva_x > 0:
            rectangulo_homero.x -= 10
            imagen_homero = imagen_homero_izq


    PANTALLA.blit(fondo, (0, 0))
    PANTALLA.blit(imagen_homero, rectangulo_homero)

    pygame.display.update()
