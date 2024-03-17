import pygame
from datetime import datetime

pygame.init()

# Размеры окна
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 900
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# Загрузка изображений
BG_IMAGE_PATH = 'images/mainclock.png'
LEFT_HAND_IMAGE_PATH = 'images/rightarm.png'
RIGHT_HAND_IMAGE_PATH = 'images/leftarm.png'

bg_image = pygame.image.load(BG_IMAGE_PATH)
left_hand_image = pygame.image.load(LEFT_HAND_IMAGE_PATH)
right_hand_image = pygame.image.load(RIGHT_HAND_IMAGE_PATH)
rect = bg_image.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2))

running = True
clock = pygame.time.Clock()

while running:
    screen.blit(bg_image, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    current_time = datetime.now().time()
    seconds = current_time.second

    # логика вращения стрелок
    left_hand_angle = -(seconds * 6)
    left_hand_rotate = pygame.transform.rotate(left_hand_image, left_hand_angle)
    left_rect = left_hand_rotate.get_rect(center=rect.center)
    screen.blit(left_hand_rotate, left_rect.topleft)

    right_hand_angle = -(seconds * 6)
    right_hand_rotate = pygame.transform.rotate(right_hand_image, right_hand_angle)
    right_rect = right_hand_rotate.get_rect(center=rect.center)
    screen.blit(right_hand_rotate, right_rect.topleft)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
