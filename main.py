import random
from random import randrange, randint, random

import pygame
from pygame.sprite import Group, Sprite, spritecollideany

from settings import size, width, height


class Ball(Sprite):
    def __init__(self, radius, x, y):
        super().__init__(all_sprites)
        self.radius = radius
        self.image = pygame.Surface((2 * radius, 2 * radius),
                                    pygame.SRCALPHA, 32)
        pygame.draw.circle(self.image, pygame.Color("red"),
                           (radius, radius), radius)
        self.rect = pygame.Rect(x, y, 2 * radius, 2 * radius)
        self.vx = random() * randint(-5, 5) + 1
        self.vy = random() * randint(-5, 5) + 1

    def update(self):
        self.rect = self.rect.move(self.vx, self.vy)
        if spritecollideany(self, horizontal_borders):
            self.vy = -self.vy
        if spritecollideany(self, vertical_borders):
            self.vx = -self.vx


class Border(Sprite):
    def __init__(self, x1, y1, x2, y2):
        super().__init__(all_sprites)
        if x1 != x2:
            self.add(horizontal_borders)
            self.image = pygame.Surface([x2 - x1, 1])
            self.rect = pygame.Rect(x1, y1, x2 - x1, 1)
        else:
            self.add(vertical_borders)
            self.image = pygame.Surface([1, y2 - y1])
            self.rect = pygame.Rect(x1, y1, 1, y2 - y1)


pygame.init()
screen = pygame.display.set_mode(size)

all_sprites = Group()
horizontal_borders = Group()
vertical_borders = Group()

Border(5, 5, width - 5, 5)
Border(5, height - 5, width - 5, height - 5)
Border(5, 5, 5, height - 5)
Border(width - 5, 5, width - 5, height - 5)

for i in range(100):
    Ball(20, width // 2, height // 2)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            all_sprites.update(event)
    screen.fill('aqua')
    all_sprites.draw(screen)
    all_sprites.update()
    pygame.display.flip()

pygame.quit()
