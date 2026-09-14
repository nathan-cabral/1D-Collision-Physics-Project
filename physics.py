def colisao(b1,b2): 
    v1i=b1.vel
    v2i=b2.vel
    v1f=(b1.mass-b2.mass)/(b1.mass+b2.mass)*v1i + 2*(b2.mass)/(b1.mass+b2.mass)*v2i
    v2f=(2*b1.mass)/(b1.mass+b2.mass)*v1i + (b2.mass-b1.mass)/(b1.mass+b2.mass)*v2i
    b1.vel=v1f
    b2.vel=v2f