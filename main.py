import pygame
from random import *

pygame.init()

ANCHO, ALTO = 500, 500
COLOR_FONDO = (64, 201, 144)
BLACK = (0,0,0)
WHITE = (255,255,255)
FPS = 60

screen = pygame.display.set_mode((ANCHO, ALTO))
reloj = pygame.time.Clock()

# CLASES 
class Area():
    def __init__(self, x, y, ancho, alto, color=None):
        self.rect = pygame.Rect(x, y, ancho, alto)
        if color:
            self.color = color


    def fill(self):
        pygame.draw.rect(screen, self.color, self.rect)

    def change_color(self, new_color):
        self.color = new_color

class Label(Area):
    def set_text(self, text, size, text_color=BLACK):
        self.image = pygame.font.SysFont("Arial", size).render(text, 1, text_color)

    def draw(self, dist_x=10, dist_y=10):
        self.fill()
        screen.blit(self.image, (self.rect.x + dist_x, self.rect.y + dist_y))

class Picture(Area):
    def __init__(self, img_file, x, y, ancho, alto, color=None):
        super().__init__(x, y, ancho, alto, color)
        self.image = pygame.image.load(img_file) 

    def draw(self):
        screen.blit(self.image, (self.rect.x, self.rect.y))

# OBJETOS:
player = Picture('platform.png', 200, 400, 100, 20)
ball = Picture('ball.png', (ANCHO - 50) // 2, 200, 50, 50)

# LOGICA DE CREACION DE ENEMIGOS
monsters = [] # Lista para los sprites
inicio_x = 5
pos_y = 5
cantidad_enemigos = 9

for fila in range(3):
    pos_x = inicio_x
    
    for columna in range(cantidad_enemigos):
        enemy = Picture('enemy.png', pos_x, pos_y, 50, 50)
        monsters.append(enemy)
        pos_x = pos_x + 55
    # FINALIZAMOS LA PRIMERA FILA Y ASIGNAMOS PARAMETROS PARA LA 2DA
    inicio_x = inicio_x + 35
    cantidad_enemigos -= 1
    pos_y = pos_y + 60


finish = False

while True:
    screen.fill(COLOR_FONDO)

    if not finish:
        player.draw()
        ball.draw()

        for enemy in monsters:
            enemy.draw()


    pygame.display.update()
    reloj.tick(FPS)

pygame.quit()
