import pygame
pygame.init()
pygame.mixer.music.load("mega.mp3")
pygame.mixer.music.play()

while pygame.mixer.music.get_busy():
    pygame.time.clock().tick(10)