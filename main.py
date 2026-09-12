import pygame

pygame.init()

class bloco:    # criando tipo de objeto chamado bloco
    def __init__(self,mass,vel):  #inicializar o objeto
                # self=self representa o objeto na hora da criacao

        self.mass=mass 
        self.vel=vel
        # esse ultimo mass e vel é o valor que recebi por parametro      
        # na hora da criacao do objeto blocoX=bloco(m,v)
        
'''
    nesse momento do codigo, nenhum bloco foi criado, eu apenas defini o molde.
    seria tipo: quando o user quiser criar um objeto do tipo bloco siga esse molde.
'''


bloc1=bloco(10,2) 
bloc2=bloco(5,3)  # criacao dos objetos em si

l=1000 
h=800

window=pygame.display.set_mode((l,h)) # cria a janela de exibicao

start=True

while start:
    for event in pygame.event.get(): # fica verificando se tem algum evento acontecendo
        if event.type==pygame.QUIT: # verifica se o user clicou no X
            start=False # se ele clicou = loop encerra e janela fecha

pygame.draw.rect() #isso desenha a forma quadrada

pygame.quit() 