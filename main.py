import pygame
from random import *

pygame.init()

ANCHO, ALTO = 500, 500
COLOR_FONDO = (64, 201, 144)
COLOR_CARD = (227, 172, 54)
COLOR_BORDER = (71, 11, 222)
BLACK = (0,0,0)
WHITE = (255,255,255)
FPS = 60

screen = pygame.display.set_mode((ANCHO, ALTO))
reloj = pygame.time.Clock()

# CLASES 
class Area():
    def __init__(self, x, y, ancho, alto, color=None):
        self.rect = pygame.Rect(x, y, ancho, alto)
        self.color = color
    
    def fill(self):
        pygame.draw.rect(screen, self.color, self.rect)

    def change_color(self, new_color):
        self.color = new_color

    def set_border(self, border_color, border_size):
        pygame.draw.rect(screen, border_color, self.rect, border_size)

class Label(Area):
    def set_text(self, text, size, text_color=BLACK):
        self.image = pygame.font.SysFont("Arial", size).render(text, 1, text_color)

    def draw(self, dist_x=10, dist_y=10):
        self.fill()
        screen.blit(self.image, (self.rect.x + dist_x, self.rect.y + dist_y))

# CREANDO OBJETOS
lista_cards = []
x = 50
for i in range(4):
    card = Label(x, 50, 80, 100, COLOR_CARD)
    card.set_text('Click!', 24)
    lista_cards.append(card)
    x += 110

while True:
    screen.fill(COLOR_FONDO)

    for card in lista_cards:
        card.draw(15, 30)
        card.set_border(COLOR_BORDER, 5)

    pygame.display.update()
    reloj.tick(FPS)

pygame.quit()
