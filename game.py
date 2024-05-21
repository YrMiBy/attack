import pygame
import random

# Инициализация Pygame
pygame.init()

# Определение констант
SCREEN_WIDTH = 800 # параметры окна
SCREEN_HEIGHT = 600
WHITE = (255, 255, 255) # несколько вариантов цветов
BLUE = (0, 0, 255)
BRICK_WIDTH = 80
BRICK_HEIGHT = 20

# Создание экрана
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Арканоид')

# Класс для платформы
class Platform:
    def __init__(self):
        self.width = 100
        self.height = 10
        self.x = (SCREEN_WIDTH - self.width) // 2
        self.y = SCREEN_HEIGHT - 20
        self.speed = 5

    def move_left(self):
        self.x -= self.speed
        if self.x < 0:
            self.x = 0

    def move_right(self):
        self.x += self.speed
        if self.x > SCREEN_WIDTH - self.width:
            self.x = SCREEN_WIDTH - self.width

    def draw(self):
        pygame.draw.rect(screen, WHITE, (self.x, self.y, self.width, self.height))

# Класс для мяча
class Ball:
    def __init__(self):
        self.size = 10
        self.x = SCREEN_WIDTH // 2
        self.y = SCREEN_HEIGHT // 2
        self.speed_x = random.choice([-2, 2])
        self.speed_y = -2

    def move(self):
        self.x += self.speed_x
        self.y += self.speed_y

        if self.x <= 0 or self.x >= SCREEN_WIDTH:
            self.speed_x *= -1
        if self.y <= 0:
            self.speed_y *= -1

    def draw(self):
        pygame.draw.circle(screen, WHITE, (self.x, self.y), self.size)

# Класс для кирпичей
class Brick:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        pygame.draw.rect(screen, BLUE, (self.x, self.y, BRICK_WIDTH, BRICK_HEIGHT))

# Создание платформы, мяча и кирпичей
platform = Platform()
ball = Ball()
bricks = []
for row in range(5):
    for col in range(10):
        brick = Brick(col * (BRICK_WIDTH + 5), row * (BRICK_HEIGHT + 5) + 50)
        bricks.append(brick)

# Основной игровой цикл
clock = pygame.time.Clock()
running = True
while running:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        platform.move_left()
    if keys[pygame.K_RIGHT]:
        platform.move_right()

    ball.move()

    # Проверка столкновения мяча с платформой
    if ball.y + ball.size >= platform.y and platform.x <= ball.x <= platform.x + platform.width:
        ball.speed_y *= -1

    # Проверка столкновения мяча с кирпичами
    for brick in bricks:
        if brick.x <= ball.x <= brick.x + BRICK_WIDTH and brick.y <= ball.y <= brick.y + BRICK_HEIGHT:
            bricks.remove(brick)
            ball.speed_y *= -1

    platform.draw()
    ball.draw()

    for brick in bricks:
        brick.draw()

    pygame.display.flip()
    clock.tick(60)

pygame.quit()