import pygame

COR_FUNDO = (18, 18, 32)
COR_CHAO = (70, 70, 95)
COR_PAINEL = (30, 30, 46)
COR_TITULO = (230, 230, 240)
COR_TEXTO = (215, 215, 220)


def draw_background(window, largura, floor_y):
    window.fill(COR_FUNDO)
    pygame.draw.line(window, COR_CHAO, (0, floor_y), (largura, floor_y), 3)


def draw_title(window, largura, titulo="1D Collision Simulator"):
    font = pygame.font.Font(None, 42)
    texto = font.render(titulo, True, COR_TITULO)
    rect = texto.get_rect(center=(largura // 2, 40))
    window.blit(texto, rect)


def Draw(bloco, window):
    rect = pygame.Rect(bloco.x, bloco.y, bloco.size, bloco.size)

    sombra = rect.copy()
    sombra.y += 6
    sombra_surf = pygame.Surface((sombra.width, sombra.height), pygame.SRCALPHA)
    pygame.draw.rect(sombra_surf, (0, 0, 0, 90), sombra_surf.get_rect(), border_radius=10)
    window.blit(sombra_surf, sombra.topleft)

    pygame.draw.rect(window, bloco.cor, rect, border_radius=10)
    pygame.draw.rect(window, (255, 255, 255), rect, width=2, border_radius=10)


def draw_info(bloco, window, nome, largura_janela):
    
    font_nome = pygame.font.Font(None, 28)
    font_dados = pygame.font.Font(None, 24)

    linhas = [
        (nome, font_nome, bloco.cor),
        (f"Mass: {bloco.mass:.1f} kg", font_dados, COR_TEXTO),
        (f"Velocity: {bloco.vel:.3f} m/s", font_dados, COR_TEXTO),
    ]

    textos = [fonte.render(txt, True, cor) for txt, fonte, cor in linhas]
    largura_painel = max(t.get_width() for t in textos) + 24
    altura_painel = sum(t.get_height() for t in textos) + 20

    centro_x = bloco.x + bloco.size / 2
    painel_x = centro_x - largura_painel / 2
    painel_x = max(5, min(painel_x, largura_janela - largura_painel - 5))
    painel_y = bloco.y - altura_painel - 15

    painel_rect = pygame.Rect(painel_x, painel_y, largura_painel, altura_painel)
    pygame.draw.rect(window, COR_PAINEL, painel_rect, border_radius=8)
    pygame.draw.rect(window, bloco.cor, painel_rect, width=2, border_radius=8)

    y_atual = painel_y + 10
    for texto in textos:
        x_atual = painel_x + (largura_painel - texto.get_width()) / 2
        window.blit(texto, (x_atual, y_atual))
        y_atual += texto.get_height() + 2