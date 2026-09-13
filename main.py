import pygame
from bloco import Bloco #importando a classe Bloco
from gets import get_mass,get_vel,welcome #importando os gets 
from draw import Draw 
pygame.init()

l=1000 #largura da janela
h=800 #altura da janela

cor1=(255,0,0)
cor2=(0,0,255)

welcome()

vel1=get_vel(1) # chama o get velocidade
vel2=get_vel(2)

mass1=get_mass(1) # chama o get massa 
mass2=get_mass(2)

b1=Bloco(mass1,vel1,(l/2)+200,h/2,cor1) 
b2=Bloco(mass2,vel2,(l/2)-200,h/2,cor2)  # criacao dos objetos

window=pygame.display.set_mode((l,h)) # cria a janela de exibicao

start=True

while start:
    for event in pygame.event.get():# fica verificando se tem algum evento acontecendo
        if event.type==pygame.QUIT: # verifica se o user clicou no X
            start=False # se ele clicou = loop encerra e janela fecha
    window.fill((0,0,0)) # limpa frame anterior 
    Draw(b1,window) #cria os blocos na tela
    Draw(b2,window)
    pygame.display.update() # atualiza a cada frame
    

#pygame.draw.rect() isso desenha a forma quadrada

pygame.quit() 