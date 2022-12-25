import pygame
import Player
import Enemy

pygame.init()

width = 500
height = 500

win = pygame.display.set_mode((width, height))

all_sprites = pygame.sprite.Group()

player = Player.PlayerObject()

player.rect.left = width - 290
player.rect.top = height - 100

enemy = Enemy.Enemy()
enemy.rect.left = 200

enemy1 = Enemy.Enemy()
enemy1.rect.left = 100

enemy2 = Enemy.Enemy()
enemy2.rect.left = 300

all_sprites.add(player)

enemy_sprites = pygame.sprite.Group()

enemy_sprites.add(enemy)
enemy_sprites.add(enemy1)
enemy_sprites.add(enemy2)
FPS = 60
clock = pygame.time.Clock()

# Загружаем изображение
background_image = pygame.image.load('cosmos-NASA.png')
# Настраиваем его. Не нужно здесь ничего менять, просто копируйте
background_image = background_image.convert()
colorkey = background_image.get_at((0, 0))
background_image.set_colorkey(colorkey)
# Задаем размер. Первая 100 - ширина, вторая 100 - высота
background_image = pygame.transform.scale(background_image, (width, height))

x = player.rect.left
y = player.rect.top
pressed = pygame.mouse.get_pressed()
if pressed[0]:
    pygame.draw.rect(win, [255, 0, 0], (x, y, width, height))



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    hits = pygame.sprite.spritecollide(player, enemy_sprites, True)
    win.fill((255, 255, 255))
    win.blit(background_image, (0, 0))
    all_sprites.draw(win)
    enemy_sprites.draw(win)
    all_sprites.update()
    enemy_sprites.update()
    pygame.display.update()
    clock.tick(FPS)
