import pygame


pygame.init()
x = 400
y = 300
velocidade = 15
fundo = pygame.image.load('img/rua.png')
carro = pygame.image.load('img/carro.png')

## tamanho da janela do jogo em pixels
janela = pygame.display.set_mode((800, 600))
## nome que fica em cima da janela
pygame.display.set_caption('Nerd World of Python')

janela_aberta = True

## para manter a jenale aberta e fecha só caso aperte no X
while janela_aberta:
    ## delay pra atualização da tela não fica muito rápida
    pygame.time.delay(50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            janela_aberta = False

    comandos = pygame.key.get_pressed()
    if comandos[pygame.K_UP]:
        y -= velocidade
    elif comandos[pygame.K_DOWN]:
        y += velocidade
    elif comandos[pygame.K_RIGHT]:
        x += velocidade
    elif comandos[pygame.K_LEFT]:
        x -= velocidade

    janela.blit(fundo, (0, 0))
    janela.blit(carro, (x, y))

    ## atualiza a tela
    pygame.display.update()

pygame.quit()
