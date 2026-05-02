from pygame import *
from random import randint

init()
font.init()

WIN_WIDTH = 700
WIN_HEIGHT = 500

display.set_caption("Ping-Pong")
window = display.set_mode((WIN_WIDTH, WIN_HEIGHT))

font1 = font.SysFont('Arial', 40)  # Основной шрифт (40 pt)
font2 = font.SysFont('Arial', 36)  # Второстепенный шрифт (36 pt)

img_raketka = "raketka.png"
img_fireball = "fireball.jpg"
img_background = "background.jpg"

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

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < WIN_WIDTH - 80:
            self.rect.x += self.speed
