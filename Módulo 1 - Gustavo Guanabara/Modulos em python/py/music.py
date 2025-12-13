import pygame
import time
pygame.init()
pygame.mixer.music.load('i-wanna.mp3')
pygame.mixer.music.play()
time.sleep(60)
pygame.mixer.music.stop()
pygame.quit