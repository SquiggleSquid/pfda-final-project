import random
import pygame

class Ball():

    def __init__(self, x, y, radius, color, screen_width, screen_height):
        self.x = x
        self.y = y
        self.radius = radius #7.5
        #self.color = self.get_random_color()
        self.color = color #pygame.Color((0,255,0))

        self.screen_width = screen_width
        self.screen_height = screen_height

        self.speed_x = random.choice([-1, 1]) * random.randint(3, 8)
        self.speed_y = random.choice([-1, 1]) * random.randint(3, 8)

    def get_random_color(self):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        return (r, g, b)

    def move(self):
        self.x += self.speed_x
        self.y += self.speed_y

    def check_wall_collision(self):
        # Bounce off horizontal walls
        if self.x - self.radius < 0 or self.x + self.radius > self.screen_width:
            self.speed_x *= -1
        # Bounce off vertical walls
        if self.y - self.radius < 0:
            self.speed_y *= -1

        # Death plane
        if self.y + self.radius > self.screen_height:
            self.speed_x = 0
            self.speed_y = 0

    #def update_surface(self):
        #surf = pygame.Surface((self.radius * 1.2, self.radius * 2), pygame.SRCALPHA)
        #pygame.draw.circle(surf, self.color, (x, y), self.size*0.8)
        #return surf
    
    def draw(self, surface):
        self.surface = surface
        #surface.blit(self.surface, self.pos)


def create_paddle(x, y, width, height):
    return pygame.Rect(x, y, width, height)

def main():
    pygame.init()
    pygame.display.set_caption("8-Ball Juggle")
    clock = pygame.time.Clock()
    dt = 0

    screenWidth=400
    screenHeight=600
    resolution = (screenWidth, screenHeight)

    screen = pygame.display.set_mode((screenWidth, screenHeight))

    ball = Ball(resolution, 15, pygame.Color((0,255,0)), 7.5, screenWidth, screenHeight)

    running = True
    while running:
        # Event Loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            mouse_position = pygame.mouse.get_pos()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            running=False

        # Game logic
            #ball.update(dt)
        current_paddle = create_paddle(mouse_position[0]-50,screenHeight-50, 100, 25)

        # Render & Display
        black = pygame.Color (0,0,0)
        screen.fill(black)
        ball.draw(screen)
        pygame.draw.rect(screen, (pygame.Color("#431736")), current_paddle)

        pygame.display.flip()
        dt = clock.tick(12)
pygame.quit()


if __name__ == "__main__":
    main()
