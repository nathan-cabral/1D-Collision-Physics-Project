import pygame

def Draw(bloco,window):

    #pygame.Rect(bloco.x,bloco.y,
                #bloco.size,bloco.size)

    #pygame.Rect-> forma do quadrado
    # (x,y,largura,altura)

    pygame.draw.rect(window,bloco.cor,
                     pygame.Rect(bloco.x,bloco.y,
                                 bloco.size,bloco.size
                                 )
                    ) 
    


    
    
    
