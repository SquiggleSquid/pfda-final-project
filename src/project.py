import random
import pygame

class Ball():

    def __init__(self, pos, size, color, radius):
        self.pos = pos
        self.size = size
        self.color = random.choice(color)
        self.radius = radius

        self.surface = self.update_surface()

    def update_surface(self):
        x, y, = self.pos
        y += self.size
        self.pos = (x,y)

        surf = pygame.Surface((self.radius * 1.2, self.radius * 2), pygame.SRCALPHA)
        pygame.draw.circle(surf, self.color, (x, y), self.size*0.8)
        return surf
    
    def draw(self, surface):
        self.surface = surface
        surface.blit(self.surface, self.pos)

class Racket():

    def __init__(self, pos, size, color):
        self.pos = pos
        self.size = size
        self.color = random.choice(color)

        self.surface = self.update_surface()

    def update_surface(self):
        x = self.pos[0]
        y = self.pos[1]
        x += 1
        y += 1 
        if x > 0:
            x = 0
            y = 0

        surf = pygame.Surface((self.size*20, self.size*5))
        surf.fill(self.color)
        return surf
    
    def draw(self, surface):
        self.surface = surface
        surface.blit(self.surface, self.pos)


def main():
    pygame.init()
    pygame.display.set_caption("Digital Rain")
    clock = pygame.time.Clock()
    dt = 0
    resolution = (800, 600)
    screen = pygame.display.set_mode(resolution)

    ball = Ball(resolution)
    racket = Racket(resolution)

    running = True
    while running:
        # Event Loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # Mouse/keyboard controls for platform (racket)
            #elif event.type == pygame.KEYDOWN:
                #if event.key == pygame.K_1:
                    #new_color = palette1
                    #Particle((0,0), 15, 1000, palette1, 7.5)
                    #Racket()


        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            running=False

        # Game logic
        ball.update(dt)
        racket.update(dt)
        # Render & Display
        black = pygame.Color (0,0,0)
        screen.fill(black)
        ball.draw(screen)
        racket.draw(screen)
        pygame.display.flip()
        dt = clock.tick(12)
pygame.quit()


if __name__ == "__main__":
    main()
