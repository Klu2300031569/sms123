import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH = 800
HEIGHT = 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dino Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

# Load images
dino_image = pygame.Surface((40, 40))
dino_image.fill(GREEN)
obstacle_image = pygame.Surface((20, 40))
obstacle_image.fill(BLACK)

# Dino properties
dino_x = 50
dino_y = HEIGHT - 60
dino_jump = False
jump_count = 10

# Obstacle properties
obstacles = []
obstacle_timer = 0

# Game variables
clock = pygame.time.Clock()
score = 0
font = pygame.font.Font(None, 36)

# Main game loop
running = True
while running:
    clock.tick(30)
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Handle jumping
    keys = pygame.key.get_pressed()
    if not dino_jump:
        if keys[pygame.K_SPACE]:
            dino_jump = True
    else:
        if jump_count >= -10:
            neg = 1
            if jump_count < 0:
                neg = -1
            dino_y -= (jump_count ** 2) * 0.3 * neg  # Adjusted jump force
            jump_count -= 1
        else:
            dino_jump = False
            jump_count = 10

    # Create obstacles
    obstacle_timer += 1
    if obstacle_timer > 30:  # Increased time between obstacles
        obstacle_x = WIDTH
        obstacles.append([obstacle_x, HEIGHT - 60])
        obstacle_timer = 0

    # Move obstacles
    for obstacle in obstacles:
        obstacle[0] -= 3  # Slower speed

    # Remove off-screen obstacles
    obstacles = [obstacle for obstacle in obstacles if obstacle[0] > 0]

    # Collision detection
    for obstacle in obstacles:
        if (dino_x + 40 > obstacle[0] and dino_x < obstacle[0] + 20 and
                dino_y + 40 > obstacle[1]):
            running = False  # End game on collision

    # Draw dino
    screen.blit(dino_image, (dino_x, dino_y))

    # Draw obstacles
    for obstacle in obstacles:
        screen.blit(obstacle_image, (obstacle[0], obstacle[1]))

    # Update score
    score += 1
    score_text = font.render(f'Score: {score}', True, BLACK)
    screen.blit(score_text, (10, 10))

    pygame.display.flip()

pygame.quit()
