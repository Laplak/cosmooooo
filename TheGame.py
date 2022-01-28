import pygame
import os
import sys
import random


class Border(pygame.sprite.Sprite):
    def __init__(self, location):
        super().__init__(game_sprites)

        if location == 1:
            self.image = load_image('upper_borderline.png', -1)
        elif location == 2:
            self.image = load_image('downer_borderline.png', -1)

        self.rect = self.image.get_rect()

        if location == 1:
            self.rect.y = 5
        elif location == 2:
            self.rect.y = -10

    def update(self, *args):
        pass


class RedUFO(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__(game_sprites)
        self.image = load_image('red_UFO.png', -1)
        self.rect = self.image.get_rect()

        self.rect.x = -194
        self.rect.y = 165

        self.vy = 5

    def update(self):
        if event.type == pygame.KEYDOWN and pygame.KEYDOWN.__mod__():
            



class BlueUFO(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__(game_sprites)
        self.image = load_image('blue_UFO.png', -1)
        self.rect = self.image.get_rect()

        self.rect.x = 504
        self.rect.y = -35

        self.vy = 5

    def update(self):
        pass


class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__(game_sprites)
        self.image = load_image('circle.png', -1)
        self.rect = self.image.get_rect()

        self.rect.x = 475
        self.rect.y = 274

        self.vx = 5
        self.vy = 5

    def update(self):
        pass


# functions
def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)

    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()

    image = pygame.image.load(fullname)

    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()

    return image


if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Cosmo Ball')
    size = width, height = 1000, 600
    screen = pygame.display.set_mode(size)

    # sprite groups
    starting_screens_sprites = pygame.sprite.Group()
    horizontal_borders = pygame.sprite.Group()
    game_sprites = pygame.sprite.Group()

    # images
    background = load_image('background.png')

    upper_border = Border(1)
    downer_border = Border(2)
    red_ufo = RedUFO()
    blue_ufo = BlueUFO()
    ball = Ball()

    # sprites
    start_screen_sprite = pygame.sprite.Sprite()
    start_screen_sprite.image = load_image("start_screen.png")
    start_screen_sprite.rect = start_screen_sprite.image.get_rect()
    start_screen_sprite.rect.x = 0
    start_screen_sprite.rect.y = 0

    level_screen_sprite = pygame.sprite.Sprite()
    level_screen_sprite.image = load_image("level.png")
    level_screen_sprite.rect = level_screen_sprite.image.get_rect()
    level_screen_sprite.rect.x = 0
    level_screen_sprite.rect.y = 0

    starting_screens_sprites.add(level_screen_sprite)
    starting_screens_sprites.add(start_screen_sprite)

    running = True
    # variables
    fps = 30
    v = 20
    start_screen_moving = 0
    level_screen_moving = 0
    mode = 'start screen'
    untouchable = False
    clock = pygame.time.Clock()

    while running:

        game_sprites.draw(screen)

        # events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif (event.type == pygame.MOUSEBUTTONDOWN) and (mode == 'start screen') and not untouchable:
                if pygame.mouse.get_pos()[0] <= 500:
                    start_screen_moving = -20
                else:
                    start_screen_moving = 20
                untouchable = True

            elif (event.type == pygame.MOUSEBUTTONDOWN) and (mode == 'level screen') and not untouchable:
                if pygame.mouse.get_pos()[0] <= 500:
                    level_screen_moving = -20
                else:
                    level_screen_moving = 20
                untouchable = True

        # update
        if (start_screen_sprite.rect.x == 1000 or start_screen_sprite.rect.x == -1000) and (mode == 'start screen'):
            start_screen_moving = 0
            untouchable = False
            mode = 'level screen'

        if (level_screen_sprite.rect.x == 1000 or level_screen_sprite.rect.x == -1000) and (mode == 'level screen'):
            level_screen_moving = 0
            untouchable = False
            mode = 'the game screen'

        # THE GAME
        if mode == 'the game screen':
            game_sprites.draw(screen)

        if mode != 'the game screen':
            screen.blit(background, (0, 0))
        start_screen_sprite.rect.x += start_screen_moving
        level_screen_sprite.rect.x += level_screen_moving

        starting_screens_sprites.draw(screen)

        # какая-то
        clock.tick(fps)
        pygame.display.flip()
    pygame.quit()
