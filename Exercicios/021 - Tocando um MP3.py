#   Exercício Python 021 - Tocando um MP3
#   Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.

import pygame
pygame.init()
pygame.mixer.music.load('endereço')
pygame.mixer.music.play()
pygame.event.wait()
