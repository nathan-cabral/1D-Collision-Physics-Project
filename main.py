import pygame

pygame.init()

class bloco:    # criando tipo de objeto chamado bloco
    def __init__(self,mass,vel,x,y):  #inicializar o objeto
                # self=self representa o objeto na hora da criacao

        self.mass=mass 
        self.vel=vel
        self.x=x
        self.y=y
        
        # esse ultimo mass e vel é o valor que recebi por parametro      
        # na hora da criacao do objeto blocoX=bloco(m,v)
        
'''
    nesse momento do codigo, nenhum bloco foi criado, eu apenas defini o molde.
    seria tipo: quando o user quiser criar um objeto do tipo bloco siga esse molde.
'''


l=1000 
h=800

b1=bloco(10,2,700,h/2) 
b2=bloco(5,3,300,h/2)  # criacao dos objetos em si


window=pygame.display.set_mode((l,h)) # cria a janela de exibicao

start=True

while start:
    for event in pygame.event.get(): # fica verificando se tem algum evento acontecendo
        if event.type==pygame.QUIT: # verifica se o user clicou no X
            start=False # se ele clicou = loop encerra e janela fecha

pygame.draw.rect() #isso desenha a forma quadrada

pygame.quit() 