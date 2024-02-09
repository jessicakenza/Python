def calculer_salaire_horaire(salaire_mensuel, heures_travaillees_par_semaine):
    heures_par_mois = heures_travaillees_par_semaine * 4
    salaire_horaire = salaire_mensuel / heures_par_mois
    return salaire_horaire

def main():
    # Demander à l'utilisateur d'entrer le salaire mensuel et le nombre d'heures travaillées par semaine
    salaire_mensuel = float(input("Entrez le salaire mensuel de l'employé : "))
    heures_travaillees_par_semaine = float(input("Entrez le nombre d'heures travaillées par semaine : "))
    salaire_horaire = calculer_salaire_horaire(salaire_mensuel, heures_travaillees_par_semaine)
    print(f"Le salaire horaire de l'employé est : {salaire_horaire} euros par heure.")

if __name__ == "__main__":
    main()
