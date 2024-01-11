
def gagnant_set(set_joueur1, set_joueur2):
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

def gagnant_match(joueur1,joueur2):
    if