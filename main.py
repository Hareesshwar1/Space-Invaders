#Get Into The Game
import pygame
import random
import math

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
FPS = 60
PLAYER_SPEED = 5
ALIEN_SPEED = 3
BULLET_SPEED = 10
ALIEN_DROP = 30
ALIEN_HIT_POINTS = 3

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Invaders")

# Load images
player_img = pygame.Surface((50, 30))
player_img.fill(GREEN)
alien_img = pygame.Surface((40, 30))
alien_img.fill(RED)
bullet_img = pygame.Surface((10, 20))
bullet_img.fill(WHITE)

# Define classes
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = player_img
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH // 2
        self.rect.bottom = HEIGHT - 10
        self.speed = PLAYER_SPEED

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.right < WIDTH:
            self.rect.x += self.speed

class Alien(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = alien_img
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, WIDTH - self.rect.width)
        self.rect.y = random.randint(-100, -40)
        self.speed = ALIEN_SPEED
        self.hit_points = ALIEN_HIT_POINTS

    def update(self):
        self.rect.y += self.speed
        if self.rect.top > HEIGHT:
            self.rect.x = random.randint(0, WIDTH - self.rect.width)
            self.rect.y = random.randint(-100, -40)

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = bullet_img
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y
        self.speed = BULLET_SPEED

    def update(self):
        self.rect.y -= self.speed
        if self.rect.bottom < 0:
            self.kill()

# Initialize sprite groups
all_sprites = pygame.sprite.Group()
aliens = pygame.sprite.Group()
bullets = pygame.sprite.Group()

player = Player()
all_sprites.add(player)

for _ in range(10):
    alien = Alien()
    all_sprites.add(alien)
    aliens.add(alien)

# Main game loop
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullet = Bullet(player.rect.centerx, player.rect.top)
                all_sprites.add(bullet)
                bullets.add(bullet)

    # Update
    all_sprites.update()

    # Check for collisions
    for bullet in bullets:
        hits = pygame.sprite.spritecollide(bullet, aliens, False)
        for hit in hits:
            hit.hit_points -= 1
            if hit.hit_points <= 0:
                hit.kill()
            bullet.kill()

    # Draw
    screen.fill(BLACK)
    all_sprites.draw(screen)
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(FPS)

pygame.quit()
#Hareesshwar Ponnambalam.
