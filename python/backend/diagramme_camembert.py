import matplotlib.pyplot as plt

def afficher_diagramme(liste_valeurs):
    if len(liste_valeurs) == 2:  # Cas de deux valeurs
        labels = ['Nombre de conforme', 'Nombre de non conforme']

    else:  # Autre cas
        labels = ['Conformes n-1, non conformes n', 'Non conformes n-1, non conformes n', 'Non conformes n-1, conformes n']


    # Couleurs pour chaque partie


    # Création du diagramme en camembert
    plt.figure(figsize=(7, 7))
    plt.pie(liste_valeurs, labels=labels, autopct=lambda p: '{:.0f}'.format(p * sum(liste_valeurs) / 100), startangle=90)

    # Égalisation de l'axe pour que le camembert soit rond
    plt.axis('equal')

    # Ajout du titre
    if len(liste_valeurs) == 2: 
        plt.title('Répartition Conforme vs Non Conforme')
    else:
        plt.title('Comparaison n-1 n')

    # Affichage du diagramme
    plt.show()