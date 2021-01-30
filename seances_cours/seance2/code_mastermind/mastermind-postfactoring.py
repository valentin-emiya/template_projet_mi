from random import randrange
from typing import List, Tuple

NOMBRE_CHIFFRES = 10

NOMBRE_TENTATIVES_MAX = 15

TAILLE_COMBINAISON = 5


def lancer_jeu_mastermind() -> None:
    combinaison_secrete = genere_combinaison_aleatoire()
    affiche_message_bienvenue()
    for nombre_tentatives in range(NOMBRE_TENTATIVES_MAX):
        combinaison_proposee = saisie_combinaison()
        if partie_est_gagnee(combinaison_secrete, combinaison_proposee):
            affiche_message_victoire(combinaison_secrete)
            return
        affiche_message_tour_de_jeu(combinaison_proposee, combinaison_secrete)
    affiche_message_defaite(combinaison_secrete)


def affiche_message_tour_de_jeu(combinaison_proposee: List[int], combinaison_secrete: List[int]) -> None:
    affiche_message_combinaison_proposee(combinaison_proposee)
    affiche_totals_chiffres_bien_et_mal_places(combinaison_proposee, combinaison_secrete)


def affiche_totals_chiffres_bien_et_mal_places(combinaison_proposee: List[int],
                                               combinaison_secrete: List[int]) -> None:
    occurence_chiffres_bien_places, occurence_chiffres_mal_places = totals_chiffres_bien_places_et_mal_places(
        combinaison_proposee, combinaison_secrete)
    print(occurence_chiffres_bien_places, "chiffres bien placé(s) et",
          occurence_chiffres_mal_places, "chiffres mal placé(s)")


def totals_chiffres_bien_places_et_mal_places(combinaison_proposee: List[int],
                                              combinaison_secrete: List[int]) -> Tuple[int, int]:
    occurences_chiffres_secrets = compte_chiffres(combinaison_secrete)
    occurences_chiffres_proposes = compte_chiffres(combinaison_proposee)
    occurences_chiffres_biens_places = compte_chiffres_bien_places(combinaison_proposee, combinaison_secrete)
    return total_chiffres_bien_places(occurences_chiffres_biens_places), \
           total_chiffres_mal_places(occurences_chiffres_biens_places,
                                     occurences_chiffres_proposes,
                                     occurences_chiffres_secrets)


def total_chiffres_bien_places(occurences_chiffres_biens_places: List[int]) -> int:
    assert len(occurences_chiffres_biens_places) == NOMBRE_CHIFFRES

    nombre_chiffres_bien_places = 0
    for chiffre in range(NOMBRE_CHIFFRES):
        nombre_chiffres_bien_places += occurences_chiffres_biens_places[chiffre]
    return nombre_chiffres_bien_places


def total_chiffres_mal_places(occurences_chiffres_biens_places: List[int],
                              occurences_chiffres_proposes: List[int],
                              occurences_chiffres_secrets: List[int]) -> int:
    assert len(occurences_chiffres_biens_places) == NOMBRE_CHIFFRES
    assert len(occurences_chiffres_proposes) == NOMBRE_CHIFFRES
    assert len(occurences_chiffres_secrets) == NOMBRE_CHIFFRES

    nombre_chiffres_mal_places = 0
    for chiffre in range(NOMBRE_CHIFFRES):
        nombre_chiffres_mal_places += min(occurences_chiffres_proposes[chiffre],
                                          occurences_chiffres_secrets[chiffre]) \
                                      - occurences_chiffres_biens_places[chiffre]
    return nombre_chiffres_mal_places


def affiche_message_defaite(combinaison_secrete: List[int]) -> None:
    print("Vous avez perdu")
    print("La combinaison était", combinaison_vers_chaine_caracteres(combinaison_secrete))


def compte_chiffres_bien_places(combinaison_proposee: List[int], combinaison_secrete: List[int]) -> List[int]:
    assert len(combinaison_secrete) == len(combinaison_proposee)

    occurences_chiffres_biens_places = nouvelle_liste_entiers(NOMBRE_CHIFFRES)
    for index in range(len(combinaison_secrete)):
        if combinaison_proposee[index] == combinaison_secrete[index]:
            chiffre_bien_place = combinaison_proposee[index]
            occurences_chiffres_biens_places[chiffre_bien_place] += 1
    return occurences_chiffres_biens_places


def compte_chiffres(combinaison: List[int]) -> List[int]:
    occurences_chiffres = nouvelle_liste_entiers(NOMBRE_CHIFFRES)
    for chiffre in combinaison:
        assert isinstance(chiffre, int)
        assert 0 <= chiffre <= NOMBRE_CHIFFRES
        occurences_chiffres[chiffre] += 1
    return occurences_chiffres


def affiche_message_victoire(combinaison_secrete: List[int]):
    print("Vous avez gagné")
    print("La combinaison était", combinaison_vers_chaine_caracteres(combinaison_secrete))


def affiche_message_combinaison_proposee(combinaison_proposee: List[int]):
    print("Vous avez saisi", combinaison_vers_chaine_caracteres(combinaison_proposee))


def saisie_combinaison() -> List[int]:
    print("Veuillez saisir une combinaison de", TAILLE_COMBINAISON, "chiffres :")
    combinaison_proposee = list()
    for index in range(TAILLE_COMBINAISON):
        combinaison_proposee.append(int(input()))
    return combinaison_proposee


def affiche_message_bienvenue() -> None:
    print("Bienvenue au jeux Mastermind")


def combinaison_vers_chaine_caracteres(combinaison_secrete: List[int]) -> str:
    chaine_caracteres = str()
    for chiffre in combinaison_secrete:
        chaine_caracteres += str(chiffre)
    return chaine_caracteres


def genere_combinaison_aleatoire() -> List[int]:
    combinaison = list()
    for i in range(TAILLE_COMBINAISON):
        combinaison.append(randrange(NOMBRE_CHIFFRES))
    return combinaison


def partie_est_gagnee(combinaison_secrete: List[int], combinaison_proposee: List[int]) -> bool:
    return combinaison_proposee == combinaison_secrete


def nouvelle_liste_entiers(taille: int) -> List[int]:
    resultat = list()
    for i in range(taille):
        resultat.append(0)
    return resultat


if __name__ == '__main__':
    lancer_jeu_mastermind()
