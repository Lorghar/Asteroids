import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state
import player

def main():
    pygame.init()
    Clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    Player = player.Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while 0 < 1:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        player.Player.update(Player, dt)
        player.Player.draw(Player, screen)
        pygame.display.flip()
        Clock.tick(60)
        dt = Clock.tick(60) / 1000
        #print(dt)



    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")


if __name__ == "__main__":
    main()
