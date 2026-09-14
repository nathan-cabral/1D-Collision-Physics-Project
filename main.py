import pygame
from bloco import Bloco
from gets import get_mass,get_vel,welcome
from draw import Draw, draw_info 
from physics import colisao
pygame.init()

l=1000 
h=800 

cor1=(255,140,0)
cor2=(50,220,100)

welcome()

vel1=get_vel(1) 
vel2=get_vel(2)

mass1=get_mass(1)
mass2=get_mass(2)

b1=Bloco(mass1,vel1,(l/2)-200,h/2,cor1) 
b2=Bloco(mass2,vel2,(l/2)+200,h/2,cor2)

window=pygame.display.set_mode((l,h)) 

start=True

colidindo=False

while start:
    for event in pygame.event.get():
        if event.type==pygame.QUIT: 
            start=False 
    window.fill((0,0,0)) 

    b1.atualizar(l)
    b2.atualizar(l)
    
    if b1.x+b1.size>=b2.x and not colidindo:
        colisao(b1,b2)
        colidindo=True      
    if b1.x+b1.size<b2.x:
        colidindo=False

    draw_info(b1,window,"B1",750,100)
    draw_info(b2,window,"B2",100,100)

    Draw(b1,window)
    Draw(b2,window)
    pygame.display.update()


pygame.quit()