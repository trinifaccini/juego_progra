"""
CONFIGURACIONES DE IMAGEN

"""
#pylint: disable=missing-function-docstring
#pylint: disable=invalid-name
#pylint: disable=consider-using-enumerate

import pygame


def girar_imagenes(lista, flip_x, flip_y) -> list:
    lista_girada = []

    # aca puedo usar un foreach porque no estoy modificando la lista que estoy recorriendo
    for imagen in lista: 
        lista_girada.append(pygame.transform.flip(imagen, flip_x, flip_y))

    return lista_girada

# Escalar imagenes
def reescalar_imagenes(lista_imagenes, W,H):

    # Estos for son de solo lectura - no se pueden modificar
    # (los foreach suelen funcionar de lectura)
    # trabaja por instancia dentro de la lista
    # for lista in lista_imagenes:
    #     for imagen in lista:
    #         imagen = pygame.transform.scale(imagen, (W,H))

    for lista in lista_imagenes:
        for i in range(len(lista)): # en un rango, si modifica
            lista[i] = pygame.transform.scale(lista[i], (W,H))


# Definimos los fotogramas de cada animacion

personaje_quieto_derecha = [pygame.image.load("Recursos/Personajes/Esquiador/Quieto/esquiador_quieto_0.png"),
                            pygame.image.load("Recursos/Personajes/Esquiador/Quieto/esquiador_quieto_1.png"),
                            pygame.image.load("Recursos/Personajes/Esquiador/Quieto/esquiador_quieto_2.png"),
                            pygame.image.load("Recursos/Personajes/Esquiador/Quieto/esquiador_quieto_3.png"),
                            ]

personaje_quieto_izquierda = girar_imagenes(personaje_quieto_derecha, True, False)


personaje_camina_derecha = [pygame.image.load("Recursos/Personajes/Esquiador/Moviendose/esquiador_moviendose_0.png"),
                            pygame.image.load("Recursos/Personajes/Esquiador/Moviendose/esquiador_moviendose_1.png"),
                            pygame.image.load("Recursos/Personajes/Esquiador/Moviendose/esquiador_moviendose_2.png"),
                            pygame.image.load("Recursos/Personajes/Esquiador/Moviendose/esquiador_moviendose_3.png")
                            ]

personaje_camina_izquierda = girar_imagenes(personaje_camina_derecha, True, False)

personaje_salta_derecha = [pygame.image.load("Recursos/Personajes/Esquiador/Saltando/esquiador_saltando_0.png"),
                        #    pygame.image.load("Salta/1.png"),
                        #    pygame.image.load("Salta/2.png"),
                        #    pygame.image.load("Salta/3.png")
                           ]

personaje_salta_izquierda = girar_imagenes(personaje_salta_derecha, True, False)
