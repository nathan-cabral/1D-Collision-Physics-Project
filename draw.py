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

def draw_info(bloco,window,nome,x,y): # cria os textos na tela
    font = pygame.font.Font(None,30) 
    text1 = font.render(f"Mass: {bloco.mass} kg", True, bloco.cor)
    text2 = font.render(f"Velocity: {bloco.vel:.4f} m/s", True, bloco.cor)

    window.blit(text1, (x, y))
    window.blit(text2, (x, y+25))


    
    
    
