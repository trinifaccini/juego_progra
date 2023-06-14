import pygame
from Enumerados import * 

class Imagen:
    def __init__(self, tamanio, origen, path_imagen) -> None:
        self.imagen = pygame.image.load(path_imagen)
        self.imagen = pygame.transform.scale(self.imagen, tamanio)
        self.rectangulo = self.imagen.get_rect()
        self.rectangulo.center = origen
        self.sonido_colision = pygame.mixer.Sound('Recursos/ñam.mp3')
        self.sonido_colision.set_volume(1)

    def mover_imagen(self, sentido: str, desplazamiento: int, tamanio_pantalla: tuple):
        if sentido == Orientaciones.VERTICAL:
            self.rectangulo.y += desplazamiento
            if self.rectangulo.top > tamanio_pantalla[1]:
                self.rectangulo.bottom = 0

        else:
            self.rectangulo.x += desplazamiento
            if self.rectangulo.left > tamanio_pantalla[0]:
                self.rectangulo.right = 0

    def detectar_colision(self, otra_imagen):
        if self.rectangulo.colliderect(otra_imagen.rectangulo):
            self.sonido_colision.play()
