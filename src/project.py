import random
import pygame

class Ball():

    def __init__(self, x, y, radius, color, screen_width, screen_height):
        self.x = x
        self.y = y
        self.radius = radius #7.5
        #self.color = self.get_random_color()
        self.color = color #pygame.Color((0,255,0))
        color = self.get_random_color()

        self.screen_width = screen_width
        self.screen_height = screen_height

        self.speed_x = random.choice([-1, 1]) * random.randint(5, 8)
        self.speed_y = random.choice([-1, 1]) * random.randint(5, 8)

        self.rect = pygame.Rect(screen_width//2-self.radius, 
            screen_height//2-self.radius, self.radius*2, self.radius*2)

    def get_random_color(self):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        return (r, g, b)

    #def update(self, dt):
        #self.age += dt

    def move(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
    
    def draw(self, screen):
        pygame.draw.circle(screen, self.color, self.rect.center, self.radius)

    def check_wall_collision(self):
        # Bounce off horizontal walls
        if self.rect.x - self.radius < 0 or self.rect.x + self.radius > self.screen_width:
            self.speed_x *= -1
        # Bounce off vertical walls
        if self.rect.y - self.radius < 0:
            self.speed_y *= -1

    def check_death_plane(self):
        # Death plane
        if self.rect.y + self.radius > self.screen_height:
            self.speed_x = 0
            self.speed_y = 0
            return True
        return False

    def check_paddle_collision(self, paddle):
        if self.rect.colliderect(paddle):
            if self.speed_y > 0:
                self.rect.right = paddle.left
            elif self.speed_y < 0:
                self.rect.left = paddle.right
        
            self.speed_y *= -1
"""
class BallTrail():
    def __init__(self, pos, size, life):
        self.pos = pos
        self.size = size
        self.life = life
        self.ball_trail = [ ] 

    def update(self, dt):
        ball = Ball(self.pos, size=self.size, life=self.life)
        self.ball_trail.insert(0, ball)
        self._update_ball(dt)
        self._update_pos()

    def _update_ball(self, dt):
        for idx, ball in enumerate(self.ball_trail):
            ball.update(dt)
            if ball.dead:
                del self.ball_trail[idx]

    def _update_pos(self):
        x, y, = self.pos
        y += self.size
        self.pos (x,y)

    def draw(self, screen):
        for ball in self.ball_trail:
            ball.draw(screen)
"""


def create_paddle(x, y, width, height):
    return pygame.Rect(x, y, width, height)

def main():
    pygame.init()
    pygame.display.set_caption("8-Ball Juggle")
    clock = pygame.time.Clock()
    dt = 0

    screenWidth=400
    screenHeight=600
    screen = pygame.display.set_mode((screenWidth, screenHeight))

    ball_color = Ball.get_random_color(screen)
    ball = Ball(screenWidth//2, screenHeight//2, 7.5, 
                ball_color, screenWidth, screenHeight)


    running = True
    while running:
        # Event Loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            mouse_position = pygame.mouse.get_pos()
            paddle = create_paddle(mouse_position[0]-50,screenHeight-50, 100, 25)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            running=False

        # Game logic
        current_paddle = create_paddle(mouse_position[0]-50,screenHeight-50, 100, 25)

        # Render & Display
        black = pygame.Color (0,0,0)
        screen.fill(black)

        ball.move()
        ball.draw(screen) 
        current_paddle = pygame.draw.rect(screen, (pygame.Color("#431736")), paddle)
        ball.check_wall_collision()

        if ball.check_death_plane() == True:
            print("Game Over!")
            running = False

        ball.check_paddle_collision(current_paddle)

        pygame.display.flip()
        dt = clock.tick(12)
pygame.quit()


if __name__ == "__main__":
    main()
