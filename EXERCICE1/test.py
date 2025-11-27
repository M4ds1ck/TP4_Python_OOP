from animaux import Chien, Chat, Vache, faire_parler

liste_animaux = [Chien(), Chat(), Vache(), Chien()]

for a in liste_animaux:
    faire_parler(a)