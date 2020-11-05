import pygame,sys

pygame.init()
vInfo = pygame.display.Info()
size = width,height = 600,400

#screen = pygame.display.set_mode(size)
screen = pygame.display.set_mode(size,pygame.RESIZABLE)
#screen = pygame.display.set_mode(size,pygame.NOFRAME)
#screen = pygame.display.set_mode(size,pygame.FULLSCREEN)
pygame.display.set_caption("Pygame事件处理")

while True:
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            sys.exit()
        elif event.type ==pygame.KEYDOWN:
            if event.unicode =="":
                print("[KEYDOWN}:","#",event.key,event.mod)
            else:
                print("[KEYDOWN}:","#",event.unicode,event.key,event.mod)
        elif event.type == pygame.MOUSEMOTION:
            print("[MOUSEMOTION]:",event.pos,event.rel,event.buttons)
        elif event.type == pygame.MOUSEBUTTONUP:
            print("[MOUSEBUTTONUP]:",event.pos,event.button)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print("[MOUSEBUTTONDOWN]:",event.pos,event.button)

    pygame.display.update()

