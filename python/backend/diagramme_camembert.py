import matplotlib.pyplot as plt

def afficher_diagramme(liste_valeurs):
    print(liste_valeurs)
    if len(liste_valeurs)==2: # longueur liste = 2 signifie on est dans le cas interface 3 car ya que deux valeurs
        labels = ['Nombre de conforme', 'Nombre de non conforme']
    else: # sinon on est dans l'interface 3
        labels = ['Conformes n-1, non conformes n', 'Non conformes n-1, non conformes n', 'Non conformes n-1, conformes n']

    # Valeurs à représenter dans le diagramme
    sizes = []
    for valeur in liste_valeurs:
        sizes.append(liste_valeurs)

    # Couleurs pour chaque partie
    colors = ['#ff9999','#66b3ff']

    # Création du diagramme en camembert
    plt.figure(figsize=(7, 7))
    plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)

    # Égalisation de l'axe pour que le camembert soit rond
    plt.axis('equal')

    # Ajout du titre
    plt.title('Répartition Conforme vs Non Conforme')

    # Affichage du diagramme
    plt.show()