class Bloco:    # criando um tipo de objeto chamado bloco
    def __init__(self,mass,vel,x,y,cor):  #inicializar o objeto e pegando os parametros passados
                # self=self representa o objeto na hora da criacao

        self.mass=mass
        self.vel=vel
        self.x=x
        self.y=y
        self.cor=cor
        self.size=mass*10
        
        # self. -> significa que o obj esta sendo criado
        # apos o '=' -> parametros que peguei dentro do __inint__()
        # todos os valores dps do'=' precisam existir para serem acessados
        
'''
    nesse momento do codigo, nenhum bloco foi criado, eu apenas defini o molde.
    seria tipo: quando o user quiser criar um objeto do tipo bloco siga esse molde.
'''