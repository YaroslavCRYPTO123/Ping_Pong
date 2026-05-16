from pygame import *
from random import randint

init()
font.init()

WIN_WIDTH = 700
WIN_HEIGHT = 500

display.set_caption("Ping-Pong")
window = display.set_mode((WIN_WIDTH, WIN_HEIGHT))

font1 = font.SysFont('Arial', 40)
font2 = font.SysFont('Arial', 36)

img_raketka = "raketka.png"
img_fireball = "fireball.png"
img_background = "background.jpg"
img_raketka2 = "raketka2.png"

# Базовый класс для спрайтов
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

# Класс для левой ракетки (управление W/S)
class Player1(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < WIN_HEIGHT - self.rect.height - 5:
            self.rect.y += self.speed

# Класс для правой ракетки (управление Стрелками)
class Player2(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < WIN_HEIGHT - self.rect.height - 5:
            self.rect.y += self.speed

# Создание объектов
background = transform.scale(image.load(img_background), (WIN_WIDTH, WIN_HEIGHT))
paddle_left = Player1(img_raketka, 30, WIN_HEIGHT // 2 - 50, 30, 120, 5)
paddle_right = Player2(img_raketka2, WIN_WIDTH - 50, WIN_HEIGHT // 2 - 50, 30, 120, 5)
ball = GameSprite(img_fireball, WIN_WIDTH // 2 - 20, WIN_HEIGHT // 2 - 20, 60, 60, 4)

speed_x = ball.speed
speed_y = ball.speed

# Игровой цикл
clock = time.Clock()
FPS = 60
game = True
finish = False

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if not finish:
        window.blit(background, (0, 0))

        paddle_left.update()
        paddle_right.update()

        ball.rect.x += speed_x
        ball.rect.y += speed_y

        if ball.rect.y <= 0 or ball.rect.y >= WIN_HEIGHT - ball.rect.height:
            speed_y *= -1

        
        if sprite.collide_rect(paddle_left, ball):
            speed_x = abs(speed_x)
            ball.rect.x = paddle_left.rect.right

        if sprite.collide_rect(paddle_right, ball):
            speed_x = -abs(speed_x)
            ball.rect.x = paddle_right.rect.left - ball.rect.width

        
        paddle_left.reset()
        paddle_right.reset()
        ball.reset()

        if ball.rect.x < 0:
            finish = True
            lose_text = font1.render("Игрок 1 ПРОИГРАЛ!", True, (255, 0, 0))
            window.blit(lose_text, (WIN_WIDTH // 2 - 150, WIN_HEIGHT // 2))

        if ball.rect.x > WIN_WIDTH - ball.rect.width:
            finish = True
            lose_text = font1.render("Игрок 2 ПРОИГРАЛ!", True, (255, 0, 0))
            window.blit(lose_text, (WIN_WIDTH // 2 - 150, WIN_HEIGHT // 2))

    display.update()
    clock.tick(FPS)
