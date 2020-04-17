
		###Régles du jeu###
"""l'ordinateur choisit un mot au hasard dans une liste, un mot de huit lettres maximum. 
Le joueur tente de trouver les lettres composant le mot. À chaque coup, il saisit une lettre. 
Si la lettre figure dans le mot, l'ordinateur affiche le mot avec les lettres déjà trouvées. 
Celles qui ne le sont pas encore sont remplacées par des étoiles (*). Le joueur a 8 chances. Au delà, il a perdu"""
from donnees import * 
from fonctions import *
import os
print("Bienvenu au jeu du pendu")
regles=input("Connaissez-vous les régles? merci de répondre par oui ou non :")
###affichage des régles 
lancement(regles)
### vérification du nom du joueurs et récupération de ses points 
nom=input("merci de saisir votre nom: ")
##récupération du fichier contenant les identifiants:
baseJoueurs=appel_dictionnaire()  
##récupération/ ou création de l'identifiant joueur et des ses points 
baseJoueurs=identification(nom,baseJoueurs)
#boucle pour relancer la partie si le joueur souhaite : 
#initialisation de la variable
nouvellePartie ="oui"
while nouvellePartie != "non" : 
    #generation mot aléatoire
    niveau= input("merci de sélectionner votre niveau : facile, moyen ou difficile ")
    mot= motAleatoire(listeMots, motsFaciles,motsMoyens,niveau)
    print("il vous reste 8 essais pour trouver le mot")
    #saisie de la lettre ou du mot et jeu 
    tentativeLettres(mot,nbreEssais,baseJoueurs,nom,x,niveau)
    #ajouts points à l'alias
    ajout_points(baseJoueurs)
    #demander si autre partie 
    nouvellePartie=input("voulez vous rejouer:oui ou non ? ").lower()
    if nouvellePartie =="non":
    	print("Merci d'avoir joué au Pendu! Revenez quand vous voulez !!!")
    	break
    else: 
        while nouvellePartie !="oui":
            try :
                assert nouvellePartie == "oui" or nouvellePartie =="non"
            except AssertionError:
                nouvellePartie=input("Merci de répondre par oui ou par non. Souhaitez vous rejouer ? oui/non ").lower()
                if nouvellePartie =="non":
                    print("")
                    print("Merci d'avoir joué au Pendu! Revenez quand vous voulez !!!")
os.system("pause")







