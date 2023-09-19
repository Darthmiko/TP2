#créé par Mikolai Szychowski
#créé le 19 septembre 2023
#TP2
import random
chiffre_aléatoire = random.randint(0,1000)
print('Lordinateur a choisi un nombre entre 0 et 1000 essayez de le deviner.')
nb_essai=0
boucle_jeu=True
while boucle_jeu:
    essai=int(input('Entrez votre premier essai:'))
    if essai>chiffre_aléatoire:
        print('Le nombre est plus petit')
        nb_essai=nb_essai + 1
        boucle_jeu + True
    elif essai < chiffre_aléatoire:
        print('le nombre est plus grand')
        nb_essai=nb_essai + 1
        boucle_jeu = True
    elif essai == chiffre_aléatoire:
        print('Bravo! Vous avez trouvez!')
        boucle_jeu=False
    else:
        print('Erreur')
        boucle_jeu = True