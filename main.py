import pygame
from bloco import Bloco #importando a classe Bloco

pygame.init()

l=1000 
h=800
cor1=(255,0,0)
cor2=(0,0,255)

# Pegar os dados do objeto e só dps abrir a janela de simulacao

print("Welcome to 1D collison simulator made by Nathan")

print("Please, enter values for velocity")
print("Velocities permitted: -10 (m/s) to 10 (m/s)")
vel1=int(input("Insert inicial velocity for object 1 (m/s): "))

if vel1 >10:
    print("Velocities permitted: -10 (m/s) to 10 (m/s)")
    choice=int(input(""))
vel2=int(input("Insert inicial velocity for object 2 (m/s): "))
print("Please, enter positives massses for the objects")
mass1=int(input("Insert mass for object 1 (kg): "))
mass2=int(input("Insert mass for object 2 (kg): "))


b1=Bloco(mass1,vel1,(l/2)+200,h/2,cor1) 
b2=Bloco(mass2,vel2,(l/2)-200,h/2,cor2)  # criacao dos objetos

window=pygame.display.set_mode((l,h)) # cria a janela de exibicao

start=True

while start:
    for event in pygame.event.get(): # fica verificando se tem algum evento acontecendo
        if event.type==pygame.QUIT: # verifica se o user clicou no X
            start=False # se ele clicou = loop encerra e janela fecha

#pygame.draw.rect() isso desenha a forma quadrada

pygame.quit() 