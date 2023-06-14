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

pygame.init() 

PANTALLA = pygame.display.set_mode((ANCHO,ALTO)) #pixeles px

pygame.display.set_caption("Mi primer juego")
 
PANTALLA.fill(NEGRO) 

imagen_vertical = pygame.Surface((100,100))
imagen_vertical.fill(VERDE)
rectangulo_vertical = imagen_vertical.get_rect()#toma el rect que representa superfice
rectangulo_vertical.center = (ANCHO//2, ALTO//2)

imagen_horizontal = pygame.Surface((100,100))
imagen_horizontal.fill(AZUL)
rectangulo_horizontal = imagen_horizontal.get_rect()
rectangulo_horizontal.center = (ANCHO-50, ALTO//2)

clock = pygame.time.Clock()

while True:

    clock.tick(FPS)
    
    for evento in pygame.event.get(): 
        if evento.type == pygame.QUIT: 
            pygame.quit()
            sys.exit()

    PANTALLA.fill(NEGRO) 
    
    PANTALLA.blit(imagen_vertical, rectangulo_vertical)
    PANTALLA.blit(imagen_horizontal, rectangulo_horizontal)

    # Para moverlas

    rectangulo_vertical.y += 10 
    rectangulo_horizontal.x += 10

    # Para devolverlas al inicio cuando se salen de la pantalla

    if rectangulo_vertical.top > ALTO:
        rectangulo_vertical.bottom = 0

    if rectangulo_horizontal.left > ANCHO:
        rectangulo_horizontal.right = 0

    pygame.draw.line(PANTALLA,VERDE,(400,0),(400,800),3)
    pygame.draw.line(PANTALLA,VERDE,(0,300),(800,300),3)

    pygame.display.flip() 
