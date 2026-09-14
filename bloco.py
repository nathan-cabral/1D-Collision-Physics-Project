class Bloco:    
    def __init__(self,mass,vel,x,y,cor):
                
        self.mass=mass
        self.vel=vel
        self.x=x
        self.y=y
        self.cor=cor
        self.size=mass*10
       
    def atualizar(self,l):
        self.x+=self.vel*0.5
        if self.x<=0:
            self.vel*=-1
        if self.x+self.size>=l: 
            self.vel*=-1
        