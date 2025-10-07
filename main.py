import pygame
from pygame.locals import *


# Initialisation
pygame.init()

# Création d'une petite fenêtre (400x300 par exemple)
fenetre = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Ma première fenêtre Pygame")

# Boucle principale
en_cours = True
while en_cours:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            en_cours = False

# Quitter proprement
pygame.quit()