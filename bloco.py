class Bloco:    # criando um tipo de objeto chamado bloco
    def __init__(self,mass,vel,x,y,cor):  #inicializar o objeto e pegando os parametros passados
                # self=self representa o objeto na hora da criacao
        #self. -> criando atributo
        self.mass=mass
        self.vel=vel
        self.x=x
        self.y=y
        self.cor=cor
        self.size=mass*10
        # apos o '=' -> parametros que peguei dentro do __inint__()
        # todos os valores dps do'=' precisam existir para serem acessados

    def atualizar(self,l):
        self.x+=self.vel*0.5
        if self.x<=0: #parede esquerda
            self.vel*=-1
        if self.x+self.size>=l: #parede direita
            self.vel*=-1
        