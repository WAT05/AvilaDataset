# Description
Machine learning project for Avila Dataset.

Datant du XIIe siècle, la bible d’Avila est une copie latine géante de la bible produite entre l’Italie et l’Espagne.

Le dataset associé, extrait à partir de 800 images de cette bible, contient des caractéristiques de « pattern » (style d’écriture manuscrite) pour chacune des lignes, et des colonnes et pages associées.

Le dataset, présenté sous forme de tableau nous fournit donc les caractéristiques suivantes :
F1 : intercolumnar distance (La distance entre les deux colonnes)
F2 : upper margin (La marge supérieure)
F3 : lower margin (La marge inférieure)
F4 : exploitation (La quantité d’encre sur la colonne)
F5 : row number (Le nombre de lignes de la colonne)
F6 : modular ratio (Le ratio entre la hauteur et la largeur des caractères)
F7 : interlinear spacing (L’espacement entre les lignes)
F8 : weight (La quantité d’encre sur la ligne)
F9 : peak number (Le nombre de pics verticaux)
F10 : modular ratio / interlinear spacing (Le ratio entre F6 et F7)
Les différentes « classes » sont des lettres distinguant les 12 auteurs (A, B, C, D, E, F, G, H, I, W, X, Y) et se trouvent à la fin de chaque échantillon.
Toutes ces données sont normalisées par une normalisation Z-score.

L’objectif final de ce projet est d’arriver à classifier chaque copiste en fonction de son style d’écriture (déterminée par les différentes caractéristiques) afin de pouvoir faire des prédictions à partir d’échantillons de valeurs de caractéristiques.

# Conclusion

Parmi tous les modèles testés, nous observons que les modèles de type "arbre" sont les plus performants, en particulier le XGBC avec lequel nous obtenons une précision de 99.8754% et une entropie croisée de seulement 0.0146. Pour arriver à de tels résultats, l'optimisation des hyperparamètres à l'aide de grilles de recherches a été une étape très importante.
