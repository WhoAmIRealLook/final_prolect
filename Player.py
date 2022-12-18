import pygame

class PlayerObject(pygame.sprite.Sprite):
    # Создаем инициализатор(конструктор)
    def __init__(self):
        # Вызываем конструктор самого класса Sprite
        super().__init__()
        # Загружаем изображение
        self.image = pygame.image.load('космический корабль.jpg')
        # Настраиваем его. Не нужно здесь ничего менять, просто копируйте
        self.image = self.image.convert()
        #colorkey = self.image.get_at((0, 0))
        #self.image.set_colorkey(colorkey)
        # Задаем размер. Первая 100 - ширина, вторая 100 - высота
        self.image = pygame.transform.scale(self.image, (100, 100))
        # Задаем границы
        self.rect = self.image.get_rect()

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.rect.top -= 5
        if keys[pygame.K_DOWN]:
            self.rect.top += 5
        if keys[pygame.K_LEFT]:
            self.rect.left -= 5
        if keys[pygame.K_RIGHT]:
            self.rect.left += 5