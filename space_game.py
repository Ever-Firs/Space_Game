import pygame, control
from gun import Gun


def run():
    pygame.init()
    screen = pygame.display.set_mode((700, 800))
    pygame.display.set_caption('Space')
    bg_color = (0, 0, 0)
    gun = Gun(screen)

    while True:
        control.events(gun)
        gun.update_gun()
        screen.fill(bg_color)
        gun.output()
        pygame.display.flip()


run()
