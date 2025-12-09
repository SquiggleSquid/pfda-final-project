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

    def move(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
    
    def draw(self, screen):
        pygame.draw.circle(screen, self.color, self.rect.center, self.radius)

    def check_wall_collision(self):
        if self.rect.top <= 0:
            self.speed_y *= -1
        if self.rect.left <= 0 or self.rect.right >= self.screen_width:
            self.speed_x *= -1

    def check_death_plane(self):
        if self.rect.bottom > self.screen_height:
            self.speed_x = 0
            self.speed_y = 0
            return True
        return False

    def check_paddle_collision(self, paddle_rect):
            if self.rect.colliderect(paddle_rect):
                if self.speed_y > 0:
                    self.rect.bottom = paddle_rect.top
                else:
                    self.rect.top = paddle_rect.bottom

                self.speed_y *= -1


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
        dt = clock.tick(36)
pygame.quit()


if __name__ == "__main__":
    main()
