import random
import pygame

def crear_dona(ancho, alto, path_imagen, pos_x, pos_y) -> dict:
    '''
    * Brief: Devuelve un diccionario que representa una dona
    '''
    imagen_dona = pygame.image.load(path_imagen)
    imagen_dona = pygame.transform.scale(imagen_dona, (ancho, alto))
    rectangulo_dona = imagen_dona.get_rect()
    rectangulo_dona.x = pos_x
    rectangulo_dona.y = pos_y

    diccionario_dona = {}
    diccionario_dona = {
        "superficie": imagen_dona,
        "rectangulo": rectangulo_dona,
        "velocidad": random.randint(1, 5)
    }

    return diccionario_dona

def crear_lista_donas(cantidad) -> list:
    """
    * Brief: crea una lista de donas
    """
    donas = []
    for i in range(cantidad):
        x = random.randrange(0,740,60)
        y = random.randrange(-1000, 0, 60)
        dona = crear_dona(60,60, "Recursos/dona.png", x, y)
        donas.append(dona)

    return donas

def update_donas(lista_donas: list) -> None:

    """
    * Brief: Actualiza la posicion de las donas
    """

    for dona in lista_donas:
        rectangulo = dona['rectangulo']
        rectangulo.y += dona['velocidad']

def desaparecer_dona(dona: dict) -> None:
    """
    * 
    """
    dona['rectangulo'].x = random.randrange(0,740,60)
    dona['rectangulo'].y = random.randrange(-1000, 0, 60)

def verificar_colision(lista_donas: list, personaje: dict) -> bool:

    """
    * Brief: Verifica si cada dona en la lista de donas colisionó con el personaje
    """

    for dona in lista_donas:
        rectangulo_dona = pygame.Rect(dona['rectangulo'])
        rectangulo_colision = pygame.Rect(personaje['rectangulo_boca'])
        if rectangulo_colision.colliderect(rectangulo_dona):
            personaje['puntos'] += 100
            desaparecer_dona(dona)
        if rectangulo_dona.y > 720:
            desaparecer_dona(dona)
      