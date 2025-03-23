import random
import pygame
import pygame.freetype

pygame.init()
clock = pygame.time.Clock()

screen = pygame.display.set_mode((1000, 600))
pygame.display.set_caption('Flappy Bird')

bird_image = pygame.image.load('bird.png')
wall_image = pygame.image.load('wall.png')
bird_image = pygame.transform.scale(bird_image, (80, 60))
wall_image = pygame.transform.scale(wall_image, (100, 500))
bird_rect = bird_image.get_rect()
bird_rect.center = (300, 300)
font = pygame.freetype.Font(None, 30)

bird_speed = 0
gravity = 0.5
jump = 1

wall_group = pygame.sprite.Group()
spawn_wall_event = pygame.USEREVENT
pygame.time.set_timer(spawn_wall_event, 1000)

game_status = 'game'

class Wall(pygame.sprite.Sprite):
    def __init__(self, pos, image):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = pos

    def update(self):
        global game_status
        self.rect.x -= 10
        if self.rect.colliderect(bird_rect):
            game_status = 'menu'

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == spawn_wall_event:
            wall = Wall((1050, random.choice([-50, -100, -150])), wall_image)
            wall_group.add(wall)
            wall = Wall((1050, random.choice([-650, 700, 750])), wall_image)
            wall_group.add(wall)

    if game_status == 'game':
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            bird_speed -= jump
        bird_speed += gravity
        bird_rect.centery += int(bird_speed)

        screen.fill((100, 100, 100))
        screen.blit(bird_image, bird_rect)

        wall_group.update()
        wall_group.draw(screen)
    else:
        font.render(screen, (300, 300), 'Game over', (255, 255, 255))

    pygame.display.flip()
    clock.tick(60)
