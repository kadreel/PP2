import pygame
import os

pygame.init()
pygame.mixer.init()

W = H = 600
screen = pygame.display.set_mode((W, H))
pygame.display.set_caption("hewwo.")
font = pygame.font.Font(None, 36)

songs = ["lab 7/cassetteer/Counter Punch.ogg", "lab 7/cassetteer/Flow State.ogg", "lab 7/cassetteer/Kinetic Move.ogg", "lab 7/cassetteer/Stealth Approach.ogg"]
song_lengths = {
    "Counter Punch": 255,
    "Flow State": 241,
    "Kinetic Move": 293,
    "Stealth Approach": 281,
}
current_song = 0

pygame.mixer.music.load(songs[current_song])
pygame.mixer.music.play()
pygame.mixer.music.pause()

def play_pause():
    if pygame.mixer.music.get_busy():
        pygame.mixer.music.pause()
    else:
        pygame.mixer.music.unpause()

def next_song():
    global current_song
    current_song = (current_song + 1) % len(songs)
    pygame.mixer.music.load(songs[current_song])
    pygame.mixer.music.play()
    pygame.mixer.music.set_pos(0)

def previous_song():
    global current_song
    current_song = (current_song - 1) % len(songs)
    pygame.mixer.music.load(songs[current_song])
    pygame.mixer.music.play()
    pygame.mixer.music.set_pos(0)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:  # Handle key presses
            if event.key == pygame.K_SPACE:
                play_pause()
            elif event.key == pygame.K_RIGHT:
                next_song()
            elif event.key == pygame.K_LEFT:
                previous_song()
            elif event.key == pygame.K_ESCAPE:
                running = False

    screen.fill((0, 0, 0))
    song_path = songs[current_song]
    
    song_name = os.path.splitext(os.path.basename(song_path))[0]
    song_name = song_name.title()

    song_time_Seconds = song_lengths.get(song_name, 0)
    song_time_TrueSEC = song_time_Seconds % 60
    song_time_TrueMIN = song_time_Seconds // 60

    song_time_CurSeconds = int(pygame.mixer.music.get_pos() / 1000)
    song_time_CurSEC = song_time_CurSeconds % 60
    song_time_CurMIN = song_time_CurSeconds // 60

    if pygame.mixer.music.get_busy():
        name = font.render(f"Now Playing: {song_name}", True, (255, 255, 255))
    else:
        name = font.render(f"Paused: {song_name}", True, (255, 255, 255))
    timeProg = font.render(f"{song_time_CurMIN}:{song_time_CurSEC:02} / {song_time_TrueMIN}:{song_time_TrueSEC:02}", True, (255, 255, 255))
    exit_text = font.render("Space = un/pause, arrows = switch, ESC = exit", True, (255, 255, 255))
    
    screen.blit(timeProg, (W/2 - timeProg.get_width()/2, H/2 - timeProg.get_height()/2 + 50))
    screen.blit(name, (W/2 - name.get_width()/2, H/2 - name.get_height()/2))
    screen.blit(exit_text, (W/2 - exit_text.get_width()/2, H/2 - exit_text.get_height()/2 + 100))
    pygame.display.flip()

pygame.quit()
