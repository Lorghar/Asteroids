import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state, log_event
import player
from asteroid import Asteroid
from asteroidfield import AsteroidField
import sys
from shot import Shot

def main():
    pygame.init()
    Clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    player.Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)
    
    Player = player.Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    Field = AsteroidField()

    while 0 < 1:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        #player.Player.update(Player, dt)
        #player.Player.draw(Player, screen)
    
        updatable.update(dt)

        for asteroid in asteroids:
            if asteroid.collides_with(Player):
                log_event("player_hit")
                print("Game over!")
                sys.exit()

        for member in drawable:
            member.draw(screen)
        
        pygame.display.flip()
        Clock.tick(60)
        dt = Clock.tick(60) / 1000
        #print(dt)



    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")


if __name__ == "__main__":
    main()
