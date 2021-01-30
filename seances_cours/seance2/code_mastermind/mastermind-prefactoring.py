from random import randint


def lancer_jeu_mastermind():

    # On génère une combinaison secrête s aléatoirement.
    s = list()
    for i in range(5):
        s.append(randint(0, 9))
    print(s)

    # On construit une chaîne de caractère c contenant les chiffres de la liste s concaténés sans espace.
    c1 = str()
    for i in s:
        c1 += str(i)

    # On affiche une phrase de bienvenue
    print("Bienvenue au jeux Mastermind")

    # On boucle pour les 15 tentatives
    for i in range(15):

        # On demande à l'utilisateur de saisir 5 chiffres et on stocke ces entiers dans une liste p.
        print("Veuillez saisir une combinaison de 5 chiffres :")
        p = list()
        for j in range(5):
            p.append(int(input()))

        # On teste si le joueur a gagné et si c'est le cas on affiche un message de victoire et on termine.
        if p == s:
            print("Vous avez gagné")
            print("La combinaison était", c1)
            return

        # On construit une chaîne de caractère c2 contenant les chiffres de la liste p concaténés sans espace.
        c2 = str()
        for j in p:
            c2 += str(j)

        # On affiche la combinaison entrée par le joueur.
        print("Vous avez saisi", c2)

        # On calcule le nombre b de chiffre bien placés.
        b = 0

        # Pour chaque position dans p on teste si le chiffre est bien placé.
        for j in range(len(p)):
            # Si le chiffre à la position i est le même pour p et s alors il y a un chiffre bien placé de plus.
            if p[j] == s[j]:
                b += 1

        # On crée trois listes o_b, o_p et o_s de taille dix avec toutes les cases à 0.
        o_p = list()
        o_s = list()
        o_b = list()
        for j in range(10):
            o_p.append(0)
            o_s.append(0)
            o_b.append(0)

        # On va modifier la liste o_s de sorte à ce que o_s[c] contienne le nombre d'occurences de c dans la liste s.
        for j in range(len(s)):
            o_s[s[j]] += 1

        # On va modifier la liste o_s de sorte à ce que o_s[c] contienne le nombre d'occurences de c dans la liste p.
        for j in range(len(p)):
            o_p[p[j]] += 1

        # On va modifier la liste o_b de sorte à ce que o_b[c] contienne le nombre de fois ou le chiffre c est bien
        # placé, c'est-à-dire dans la même position dans s et p. Pour cela, on parcourt tous les chiffres c de 0 à 9.
        for c in range(10):

            # Pour chaque position dans la combinaison proposée.
            for j in range(len(p)):

                # Si la position corrrespond au chiffre c bien placé, on augmente la case correspondante de o_b.
                if p[j] == s[j] and p[j] == c:
                    o_b[c] += 1

        # On va maintenant compter le nombre de chiffres mal placés. Pour cela, on utilise le fait que pour une chiffre
        # c donné, si c apparaît x fois dans p et y fois dans la s, alors le nombre de fois où c est mal placé est égal
        # au minimum de x et de y moins le nombre de fois où c est bien placé.
        m = 0
        for c in range(10):
            m += min(o_p[c], o_s[c]) - o_b[c]

        # On va maintenant compter le nombre de chiffres bien placés. Pour cela il suffit de sommer les valeurs o_b[c]
        # pour tous les chiffres c.
        b = 0
        for c in range(10):
            b += o_b[c]

        # On affiche le nombre de chiffres bien placés et mal placés pour le joueur.
        print(b, "chiffre(s) bien placé(s) et", m, "chiffre(s) mal placé(s)")

    # Si le joueur n'a pas gagné après les 15 tentatives, on affiche un message de défaite.
    print("Vous avez perdu")
    print("La combinaison était", c1)


lancer_jeu_mastermind()
