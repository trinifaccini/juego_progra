import pygame
from Enumerados import Colores
from Donas import crear_lista_donas, update_donas, verificar_colision

ANCHO_VENTANA = 800
ALTO_VENTANA = 800
FPS = 60
TAMANIO_PANTALLA = (ANCHO_VENTANA, ALTO_VENTANA)

pygame.init()
RELOJ = pygame.time.Clock()

# Evento propio
user_tick = pygame.USEREVENT + 0
pygame.time.set_timer(user_tick, 50)


# Pantalla
PANTALLA = pygame.display.set_mode(TAMANIO_PANTALLA)
pygame.display.set_caption("Primer ventana")

# Fondo 
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

## boca homero
x = 493
y = 658
rectangulo_boca = pygame.Rect(x,y,40,40)

personaje = {}
personaje = {
    "superficie": imagen_homero,
    "rectangulo_homero": rectangulo_homero,
    "puntos": 0,
    "rectangulo_boca": rectangulo_boca
}

# DONAS
donas = crear_lista_donas(10)

# PUNTAJE
fuente = pygame.font.SysFont("Arial", 60)

flag = True
while flag:

    RELOJ.tick(FPS)

    lista_eventos = pygame.event.get()
    for evento in lista_eventos:
        if evento.type == pygame.QUIT:
            flag = False
        if evento.type == user_tick:
            update_donas(donas)

    lista_teclas = pygame.key.get_pressed()

    if lista_teclas[pygame.K_RIGHT]:
        nueva_x = rectangulo_homero.x + 10
        if nueva_x < ANCHO_VENTANA - rectangulo_homero.width:
            personaje["rectangulo_homero"].x += 10
            personaje["rectangulo_boca"].x += 10
            imagen_homero = imagen_homero_der
    if lista_teclas[pygame.K_LEFT]:
        nueva_x = rectangulo_homero.x - 10
        if nueva_x > 0:
            personaje["rectangulo_homero"].x -= 10
            personaje["rectangulo_boca"].x -= 10
            imagen_homero = imagen_homero_izq

    PANTALLA.blit(fondo, (0, 0)) # CAPA 0
    PANTALLA.blit(imagen_homero, rectangulo_homero) # CAPA 1

    for d in donas:
        PANTALLA.blit(d['superficie'], d['rectangulo']) # CAPA 2

    pygame.draw.rect(PANTALLA, Colores.ROJO.value, personaje["rectangulo_homero"],5)
    pygame.draw.rect(PANTALLA, Colores.AZUL.value, personaje["rectangulo_boca"],5)

    verificar_colision(donas, personaje)

    texto = fuente.render(f"Score: {personaje['puntos']}", False, Colores.VERDE.value, Colores.AZUL_CLARO.value)
    PANTALLA.blit(texto, (0,0))

    pygame.display.update()
