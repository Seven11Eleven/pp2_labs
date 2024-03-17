import pygame

pygame.mixer.init()
pygame.init()
screen = pygame.display.set_mode((1280, 600))
pygame.display.set_caption("Музыкальный проигрыватель")
clock = pygame.time.Clock()
done = False
songs = ['music/Dos-Masan_Taskhan_Narbaeva_-_Akhau_bikem_73103040.mp3',
         'music/Dos-Masan_Murat_Kusainov_-_16_kyz_73103044.mp3',
         'music/Korol_i_SHut_-_Durak_i_molniya_48182429.mp3',
         'music/YUrijj_SHatunov_-_Sedaya_noch_50310007.mp3',
         'music/simpatichnyie-kotyata-zvukovoy-effekt-42841.mp3']
pygame.mixer.music.load(songs[0])
pygame.mixer.music.play()
current_song_index = 0
paused = False

font = pygame.font.Font( None, 36)  # Шрифт

# Текст с объяснением функционала
instruction_text = [
    "Используйте стрелки '<' и '>' для переключения между песнями.",
    "Нажмите пробел для паузы/продолжения проигрывания.",
    "Программа автоматически переключает на следующую песню после окончания текущей."
]

while not done:
    screen.fill((255, 255, 255))
    pygame.draw.rect(screen, (200, 200, 200), pygame.Rect(50, 50, 400, 50))  # Поле для отображения текущей песни

    # Название тек песни
    current_song_text = font.render("Текущая песня: " + songs[current_song_index], True, (0, 0, 0))
    screen.blit(current_song_text, (60, 60))

    # текст с функционалом
    for idx, line in enumerate(instruction_text):
        instruction = font.render(line, True, (128, 5, 5))
        screen.blit(instruction, (60, 150 + idx * 40))


    # логика переключения между песнями и паузы
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                current_song_index = (current_song_index + 1)
                pygame.mixer.music.load(songs[current_song_index])
                pygame.mixer.music.play()
                paused = False
            elif event.key == pygame.K_LEFT:
                current_song_index = (current_song_index - 1)
                pygame.mixer.music.load(songs[current_song_index])
                pygame.mixer.music.play()
                paused = False
            elif event.key == pygame.K_SPACE:
                if paused:
                    pygame.mixer.music.unpause()
                    paused = False
                else:
                    pygame.mixer.music.pause()
                    paused = True

    # логика переключения на другую песню после конца текущей
    if not pygame.mixer.music.get_busy() and not paused:
        current_song_index = (current_song_index + 1) % len(songs)
        pygame.mixer.music.load(songs[current_song_index] )
        pygame.mixer.music.play()

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
