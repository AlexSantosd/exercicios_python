import pygame
pygame.init()
print('Tocando um mp3')
pygame.mixer.music.load('ex021.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()

