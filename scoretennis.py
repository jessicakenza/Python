"""def gagnant_set(set_joueur1, set_joueur2):
    x = set_joueur1
    y = set_joueur2

    if x > y:
        return "Joueur 1 est le gagnant du set "
    elif y > x:
        return "Joueur 2 est le gagnant du set"
    else:
        return "Aucun gagnant"


set_joueur1 = 4
set_joueur2 = 2

resultat = gagnant_set(set_joueur1, set_joueur2)
print(resultat)
"""""
def gagnant_set(chaine):
    score_joueur1 = chaine.count('1')
    score_joueur2 = chaine.count('2')

    if score_joueur1 > score_joueur2:
        return '1'
    elif score_joueur2 > score_joueur1:
        return '2'
    else:
        return None

resultat_set = gagnant_set("111222")
if resultat_set:
    print(f"Le gagnant du set est le joueur {resultat_set}")
else:
    print("Match Nul.")
