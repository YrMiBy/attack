import pygame
import random

pygame.init()

# Определение размеров окна
WIDTH, HEIGHT = 800, 600
CELL_SIZE = 20 # размер клетки


BLACK = (0, 0, 0) # цвет окна
GREEN = (0, 255, 0) # цвет змейки
RED = (255, 0, 0) # цвет мишени

class Snake: # класс змея
    def __init__(self):
        self.body = [(WIDTH / 2, HEIGHT / 2)] # центр окна
        self.direction = (1, 0) #  движение

    def move(self): # функция движения
        head = self.body[0] # голова
        new_head = (head[0] + self.direction[0] * CELL_SIZE, head[1] + self.direction[1] * CELL_SIZE)
        self.body.insert(0, new_head)
        self.body.pop()

    def change_direction(self, direction): # функция изменения направления клавишами
        if direction == 'UP' and self.direction != (0, 1):
            self.direction = (0, -1)
        elif direction == 'DOWN' and self.direction != (0, -1):
            self.direction = (0, 1)
        elif direction == 'LEFT' and self.direction != (1, 0):
            self.direction = (-1, 0)
        elif direction == 'RIGHT' and self.direction != (-1, 0):
            self.direction = (1, 0)

    def grow(self): # функция вырастания при поглощении мишени
        tail = self.body[-1] # хвост
        self.body.append((tail[0] - self.direction[0] * CELL_SIZE, tail[1] - self.direction[1] * CELL_SIZE))

    def check_collision(self): # функция проверки столкновения
        head = self.body[0]
        if head[0] < 0 or head[0] >= WIDTH or head[1] < 0 or head[1] >= HEIGHT:
            return True
        if head in self.body[1:]:
            return True
        return False

    def draw(self, screen): # отрисовка
        for segment in self.body:
            pygame.draw.rect(screen, GREEN, (segment[0], segment[1], CELL_SIZE, CELL_SIZE))

class Apple: # функция перемещения мишени
    def __init__(self):
        self.position = (random.randint(0, WIDTH // CELL_SIZE - 1) * CELL_SIZE, random.randint(0, HEIGHT // CELL_SIZE - 1) * CELL_SIZE)

    def draw(self, screen):
        pygame.draw.rect(screen, RED, (self.position[0], self.position[1], CELL_SIZE, CELL_SIZE))

def main():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Snake')

    clock = pygame.time.Clock() # отслеживание времени
    snake = Snake()
    apple = Apple()

    while True: # игровой цикл
        screen.fill(BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT: # выход
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN: # перемещение
                if event.key == pygame.K_UP:
                    snake.change_direction('UP')
                elif event.key == pygame.K_DOWN:
                    snake.change_direction('DOWN')
                elif event.key == pygame.K_LEFT:
                    snake.change_direction('LEFT')
                elif event.key == pygame.K_RIGHT:
                    snake.change_direction('RIGHT')

        snake.move()

        if snake.body[0] == apple.position:
            snake.grow()
            apple = Apple()

        if snake.check_collision(): # проверка столкновения
            pygame.quit()
            quit()

        snake.draw(screen)
        apple.draw(screen)

        pygame.display.update()
        clock.tick(10)

if __name__ == '__main__': # вызов функции main
    main()