"""
Creacion de animaciones
"""

#pylint: disable=global-statement
#pylint: disable=invalid-name
#pylint: disable=wildcard-import
#pylint: disable=unused-wildcard-import
#pylint: disable=missing-function-docstring
#pylint: disable=redefined-outer-name


import pygame,sys
from configuraciones import *
from modo import *

################################################################
def dibujar_borde_rectangulos(lados_rectangulo: dict, color: str):

    for lado in lados_rectangulo:
        pygame.draw.rect(PANTALLA, color, lados_rectangulo[lado], 2)

def obtener_rectangulos(principal: pygame.Rect) -> dict:
    diccionario = {}

    diccionario = {
        "main": principal,
        "bottom": pygame.Rect(principal.left, principal.bottom-10, principal.width, 10),
        "right": pygame.Rect(principal.right-2, principal.top, 2, principal.height),
        "left": pygame.Rect(principal.left, principal.top, 2, principal.height),
        "top": pygame.Rect(principal.left, principal.top, principal.width, 10)
    }

    return diccionario

def aplicar_gravedad(pantalla, plataformas, imagenes_accion, lados_personaje):
    
    global esta_saltando, desplazamiento_y

    if esta_saltando:
        animar_personaje(imagenes_accion, pantalla, lados_personaje['main'])

        for lado in lados_personaje:
            lados_personaje[lado].y += desplazamiento_y

        if desplazamiento_y + gravedad < limite_velocidad_caida:
            desplazamiento_y += gravedad

    #Verifica en cada iteracion con que plataforma esta colisionando
    for p in plataformas:
        if lados_personaje['bottom'].colliderect(p['top']):
            #rectangulo_personaje.bottom = p.top - 5 # si no lo ponemos queda un poco enterrado
            esta_saltando = False
            desplazamiento_y = 0
            lados_personaje["main"].bottom = p['main'].top + 5
            #Rompe cuando deja de verificar colision, entonces el personaje cae
            break
        else:
            esta_saltando = True


def mover_personaje(lados_personaje, velocidad):
    for lado in lados_personaje:
        lados_personaje[lado].x += velocidad

def animar_personaje(imagenes_accion, pantalla, rect_personaje):

    global contador_pasos # dentro de esta funcion, esta variable global puede ser modificada

    largo = len(imagenes_accion) # cuantas imagenes tengo para esa accion en particular

    if contador_pasos >= largo: # necesito saber si el contador de pasos es mayor a la cantidad de imagenes que tengo para la animacion
        contador_pasos = 0

    pantalla.blit(imagenes_accion[contador_pasos],rect_personaje)
    contador_pasos += 1


def actualizar_pantalla(pantalla, lista_plataformas, accion, velocidad, lista_animaciones, lados_personaje):

    global esta_saltando, desplazamiento_y

    pantalla.blit(fondo, (0,0))

    # Recorrer la lista de plataformas a partir de la 1
    pantalla.blit(plataforma, (lista_plataformas[1]['main'].x,lista_plataformas[1]['main'].y))

    match (accion):
        case "derecha":
            if not esta_saltando: # solo animo si no está saltando
                animar_personaje(lista_animaciones[2], pantalla, lados_personaje["main"])
            mover_personaje(lados_personaje,velocidad)
        case "izquierda":
            if not esta_saltando: # solo animo si no está saltando
                animar_personaje(lista_animaciones[3], pantalla, lados_personaje["main"])
            mover_personaje(lados_personaje,velocidad*-1)
        case "saltando":
            if not esta_saltando: # para no hacer doble salto
                esta_saltando = True
                desplazamiento_y = potencia_salto
        case "quieto":
            if not esta_saltando: # solo animo si no está saltando
                animar_personaje(lista_animaciones[0], pantalla, lados_personaje["main"])

    aplicar_gravedad(pantalla, lista_plataformas, lista_animaciones[4], lados_personaje) # se aplica siempre, no solo cuando salta

################################################################

W,H = 1300,700
TAMANIO_PANTALLA = (W,H)
FPS = 18

pygame.init()
RELOJ = pygame.time.Clock()
PANTALLA = pygame.display.set_mode(TAMANIO_PANTALLA)

# FONDO
fondo = pygame.image.load("Recursos/Fondos/fondo_nivel_1.png")
fondo = pygame.transform.scale(fondo, TAMANIO_PANTALLA)

# VARIABLES SALTO
gravedad = 1
potencia_salto = -15
limite_velocidad_caida = 15
esta_saltando = False
desplazamiento_y = 0


# PERSONAJE
contador_pasos = 0
x_inicial = W/2
y_inicial = 500 # Es el inicio del suelo del fondo que usa German
pos_actual_x = 0
pos_actual_y = 0
velocidad = 10 # Cuanto avanza o retrocede el personaje en pixeles

lista_animaciones_imagenes = [personaje_quieto_derecha,
                              personaje_quieto_izquierda,
                              personaje_camina_derecha,
                              personaje_camina_izquierda,
                              personaje_salta_derecha,
                              personaje_salta_izquierda] # lista de imagenes

reescalar_imagenes(lista_animaciones_imagenes, 150,180) # reescalamos

rectangulo_personaje = personaje_salta_derecha[0].get_rect() # puedo tomar cualquier imagen porque todas tienen el mismo tam
rectangulo_personaje.x = x_inicial
rectangulo_personaje.y = y_inicial

lados_personaje = obtener_rectangulos(rectangulo_personaje)

accion = "quieto"

# PISO
piso = pygame.Rect(0,0, W, 20)
piso.top = rectangulo_personaje.bottom # Hacemos coincidir el top del piso con el bottom del personaje 
lados_piso = obtener_rectangulos(piso)


# PLATAFORMA
plataforma = pygame.image.load("Recursos/Plataformas/plataforma_tierra_nieve.png")
plataforma = pygame.transform.scale(plataforma, (300,40))
rectangulo_plataforma = plataforma.get_rect()
rectangulo_plataforma.x = 500
rectangulo_plataforma.y = 550

lados_plataforma = obtener_rectangulos(rectangulo_plataforma)

lista_plataformas_lados = [lados_piso, lados_plataforma]

while True:

    RELOJ.tick(FPS)

    lista_eventos = pygame.event.get()
    for evento in lista_eventos:
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)

    keys = pygame.key.get_pressed()

    if keys[pygame.K_RIGHT]:
        accion = "derecha"
    elif keys[pygame.K_LEFT]:
        accion = "izquierda"
    elif keys[pygame.K_UP] or keys[pygame.K_SPACE]:
        accion = "saltando"
    elif keys[pygame.K_TAB]:
        change_mode()
    else:
        accion = "quieto"

    actualizar_pantalla(PANTALLA, lista_plataformas_lados, accion, velocidad, lista_animaciones_imagenes, lados_personaje)

    if get_mode() is True:
        # pygame.draw.rect(PANTALLA, "Blue", rectangulo_personaje, 2)
        # pygame.draw.rect(PANTALLA, "Green", piso, 2)
        dibujar_borde_rectangulos(lados_piso, "Green")
        dibujar_borde_rectangulos(lados_plataforma, "Blue")
        dibujar_borde_rectangulos(lados_personaje, "Red")

    pygame.display.update()
