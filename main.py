import pygame
import Player
import Enemy

pygame.init()

width = 500
height = 500

win = pygame.display.set_mode((width, height))

all_sprites = pygame.sprite.Group()

player = Player.PlayerObject()

enemy = Enemy.Enemy()
enemy.rect.left = 200

all_sprites.add(player)

enemy_sprites = pygame.sprite.Group()

enemy_sprites.add(enemy)

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