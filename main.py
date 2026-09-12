import pygame
from bloco import Bloco #importando a classe Bloco

pygame.init()

l=1000 
h=800
cor1=(255,0,0)
cor2=(0,0,255)
b1=Bloco(10,2,(l/2)+200,h/2,cor1) 
b2=Bloco(5,3,(l/2)-200,h/2,cor2)  # criacao dos objetos em si

window=pygame.display.set_mode((l,h)) # cria a janela de exibicao

start=True

while start:
    for event in pygame.event.get(): # fica verificando se tem algum evento acontecendo
        if event.type==pygame.QUIT: # verifica se o user clicou no X
            start=False # se ele clicou = loop encerra e janela fecha

#pygame.draw.rect() isso desenha a forma quadrada

pygame.quit() 