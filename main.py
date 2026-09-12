import pygame

pygame.init()

start=True
window=pygame.display.set_mode((900,700))
while start:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            start=False