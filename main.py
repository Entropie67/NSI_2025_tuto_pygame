import pygame
from pygame.locals import *


# Initialisation
pygame.init()

# Dimensions de la fenêtre
LARGEUR, HAUTEUR = 600, 600
# Couleurs (R, G, B)
NOIR = (0, 0, 0)
ROUGE = (255, 0, 0)
BLEU = (0, 0, 255)



# Création d'une petite fenêtre (400x300 par exemple)
fenetre = pygame.display.set_mode((LARGEUR, HAUTEUR))
pygame.display.set_caption("Ma première fenêtre Pygame")

# Boucle principale
en_cours = True
while en_cours:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            en_cours = False

    # Remplir la fenêtre en noir
    fenetre.fill(BLEU)

    # Dessiner un rectangle rouge : (surface, couleur, (x, y, largeur, hauteur))
    pygame.draw.rect(fenetre, ROUGE, (50, 50, 100, 60))

    # Mise à jour de l’affichage
    pygame.display.flip()







# Quitter proprement
pygame.quit()