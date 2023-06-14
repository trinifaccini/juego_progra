import pygame, sys

BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
ROJO = (255, 0, 0)
VERDE = (0, 255, 0)
AZUL=(0,0,255)
AZUL_CLARO=(0,150,255)

ANCHO = 800
ALTO = 600

FPS = 30 #fps por segundo

# Se inicializa - es una pantalla es como una superficie, que solapea cosas
# Primero se le indican el tamaño de la pantalla (en pyhton no existe una constante, para diferenciarlo lo usamos asi)
pygame.init() 

# ((500,400),pygame.FULLSCREEN) para ponerlo en pantalla completa
PANTALLA = pygame.display.set_mode((ANCHO,ALTO)) #pixeles px

# Para cambiar el titulo de la ventana:
pygame.display.set_caption("Mi primer juego")
 
PANTALLA.fill(NEGRO) 


# 1: VERTICAL
# Surface(ancho, alto) = superficie
imagen_vertical = pygame.Surface((100,100))
imagen_vertical.fill(VERDE)

# Crea el rectangulo asociado a esa superficie
rectangulo_vertical = imagen_vertical.get_rect()#toma el rect que representa superfice

# Ponemos una posicion relativa del rect
rectangulo_vertical.center = (ANCHO//2, ALTO//2)

# 2: HORIZONTAL
imagen_horizontal = pygame.Surface((100,100))
imagen_horizontal.fill(AZUL)
rectangulo_horizontal = imagen_horizontal.get_rect()
rectangulo_horizontal.center = (ANCHO-50, ALTO//2)

# desacelara la ejecucion del while, ya que va muy rapido y no se percibe
clock = pygame.time.Clock()

# como en arduino: en lugar de loop lo tenemos en un while
# toda accion que este para la pantalla tiene que estar actualizada en el while

while True:

    clock.tick(FPS)

    # Trabajamos con eventos
    
    for evento in pygame.event.get(): # Cada evento sucede por un disparó de algun boton precionado
        if evento.type == pygame.QUIT: # Si salio del programa
            pygame.quit()
            sys.exit()

    PANTALLA.fill(NEGRO)  # Llenar la pantalla, "limpia" 
    
    # Blit se propone en los programas para dibujar una imagen sobre otra
    PANTALLA.blit(imagen_vertical, rectangulo_vertical)
    PANTALLA.blit(imagen_horizontal, rectangulo_horizontal)

    pygame.draw.line(PANTALLA,VERDE,(400,0),(400,800),3)
    pygame.draw.line(PANTALLA,VERDE,(0,300),(800,300),3)

    pygame.display.flip() # flip() o update()

    # pygame.draw.rect(PANTALLA, AZUL, (100,50, 100, 50), 1)
    # pygame.draw.rect(PANTALLA, VERDE, (250, 100, 25, 50),3)
    #     # (tamaño,tamaño,tamaño,tamaño), tamaño del pixel)

    # pygame.draw.line(PANTALLA, VERDE, (120,105),(199,199),3)
    #                                     #(x,y), si es chico va hacia arriba
    # pygame.draw.circle(PANTALLA, ROJO, (120,50), 25,1)

    # pygame.draw.ellipse(PANTALLA, NEGRO, (270, 150, 80, 40),5)
    #                         # (x, x, tamaño en x, e Y)
    

#Mario Rampi — hoy a las 11:45: Para crear un nuevo env: python -m venv  nombre
#solo vamos a usar los rectangulos