import pygame
from bloco import Bloco #importando a classe Bloco
from gets import get_mass,get_vel,welcome #importando os gets 
from draw import Draw, draw_info 
from physics import colisao
pygame.init()

l=1000 #largura da janela
h=800 #altura da janela

cor1=(255,140,0)
cor2=(50,220,100)

welcome()

vel1=get_vel(1) # chama o get velocidade
vel2=get_vel(2)

mass1=get_mass(1) # chama o get massa 
mass2=get_mass(2)

b1=Bloco(mass1,vel1,(l/2)-200,h/2,cor1) 
b2=Bloco(mass2,vel2,(l/2)+200,h/2,cor2)  # criacao dos objetos

window=pygame.display.set_mode((l,h)) # cria a janela de exibicao

start=True

colidindo=False

while start:
    for event in pygame.event.get():# fica verificando se tem algum evento acontecendo
        if event.type==pygame.QUIT: # verifica se o user clicou no X
            start=False # se ele clicou = loop encerra e janela fecha
    window.fill((0,0,0)) # limpa frame anterior

    b1.atualizar(l)
    b2.atualizar(l)
    
    if b1.x+b1.size>=b2.x and not colidindo:
        colisao(b1,b2)
        colidindo=True      
    if b1.x+b1.size<b2.x:
        colidindo=False

    draw_info(b1,window,"B1",750,100)
    draw_info(b2,window,"B2",100,100)

    Draw(b1,window) #cria os blocos na tela
    Draw(b2,window)
    pygame.display.update() # atualiza a cada frame


pygame.quit()