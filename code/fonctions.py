def lancement(regles):
    while regles != "oui":
        regles=regles.lower()
        try:
            assert regles == "oui" or regles =="non"
        except AssertionError:
            regles=input("Vous n'avez pas saisi le bon terme; merci d'entrer oui ou non ").lower()
        if regles =="non":
            print("\n")
            print("L'ordinateur choisit un mot au hasard dans une liste, un mot de huit lettres maximum. Le joueur tente de trouver les lettres composant le mot. À chaque coup, il saisit une lettre. Si la lettre figure dans le mot, l'ordinateur affiche le mot avec les lettres déjà trouvées. Celles qui ne le sont pas encore sont remplacées par des étoiles (*). Le joueur a 8 chances. Au delà, il a perdu")
            break
    print("C'est parti!!")

def appel_dictionnaire():
    import os
    import ast
    try:
        with open('scores', 'r',encoding="utf8") as scores:
            base=scores.read()# Load configuration file values
    except FileNotFoundError:
        with open('scores','w',encoding="utf8") as scores: 
            scores.write("")
    with open('scores','r',encoding="utf8") as scores: 
        base=scores.read()
    if base != "":
        baseJoueurs=ast.literal_eval(base)
    else:
        baseJoueurs=base
    return baseJoueurs    
    
def identification(nom,baseJoueurs):
    baseJoueurs=dict(baseJoueurs)
    while nom not in baseJoueurs:
        validation=input("Nous ne vous avons pas trouvé, souhaitez vous créer un compte ? oui ou non : ")
        if validation.lower() == "oui":
            baseJoueurs[nom]=0
        else: 
            nom=input("Merci de re entrer votre nom : ")
    print("Ca marche")
    print(nom,"tu as actuellement",baseJoueurs[nom], "points")
    return baseJoueurs

def ajout_points(baseJoueurs):
    baseJoueurs=str(baseJoueurs)
    with open('scores','w',encoding="utf8") as scores: 
            scores.write(baseJoueurs)

def motAleatoire(listeMots,motsFaciles,motsMoyens,niveau):
    import random
    if niveau =="difficile":
        choixMot=random.choice(listeMots)
    elif niveau=="moyen": 
        choixMot=random.choice(motsMoyens)
    elif niveau=="facile": 
        choixMot=random.choice(motsFaciles)
    mot=choixMot.replace(" ","")
    return mot


def tentativeLettres(mot,nbreEssais,baseJoueurs,nom,x,niveau):
    #on lance une boucle tant qu'il reste des chances
    import unicodedata #Pour nettoyer les mots avec accents présents dans le dictionnaire
    #nettoyage des accents mais cela transforme en byte
    mot=unicodedata.normalize('NFKD', mot).encode('ASCII', 'ignore')
    #selection du mot nettoyé : on enleve le caractere b puis les ''autour du mot
    mot=str(mot)[2:].lower()
    mot=mot.replace("'","")
    motFloute=[]
    for i in range (len(mot)): 
        motFloute+="*"
    print(motFloute)
    print("Le mot à deviner fait", len(mot),"caracteres")
    while x <= nbreEssais:
        print("Il vous reste", nbreEssais," tentatives ")
        lettre=input("Entrez une lettre sans caracteres spéciaux ou le mot entier ")
        lettre=lettre.lower()
        #on lance une condition sur la taille des caracteres entrés : 1 lettre, 8 lettres(mot entier)ou le reste
        if len(lettre)==1 : 
            #on boucle sur le mot à trouver pr vérifier si la lettre est présente
            for i in range (len(mot)) :
                if lettre== mot[i]:
                    motFloute[i]=lettre
            if lettre in mot :
                print("Bravo vous avez trouvé une lettre, il vous reste",nbreEssais,"tentatives")
            else : 
                nbreEssais-=1
                print("Il vous reste ",nbreEssais,"tentatives")
            print(' '.join(motFloute))
        elif len(lettre)==len(mot):
            #on vérifie si l'entrée correspond au mot à trouver 
            if lettre.lower()==mot.lower():
                print("Vous avez trouvé!")
                score = nbreEssais
                print("Vous avez gagné {} points".format(score))
                #si oui, la boucle s'arrete 
                break
            else : 
                print("Retentez votre chance!!")
                nbreEssais-=1
                print("Il vous reste ",nbreEssais,"tentatives")
                print(' '.join(motFloute))
        #pour toutes les entrées ne faisant pas 1 ou taille du mot caracteres : 
        else : 
            print("Merci de n'entrer qu'une seule lettre ou le mot de ",len(mot)," lettres en entier ")
    score=nbreEssais
    print("La partie est finie, vous avez gagné",score,"points")
    print("Le mot à trouver était",mot)
    baseJoueurs[nom]+= score
    return baseJoueurs

