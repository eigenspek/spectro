Ce programme est fait pour jouer avec des données de spectro

tous les programmes utilisent le module spectroD

Avant tout, il est nécessaire de créer un dossier 'images-sources' puis 3 sous-dossiers '_background','_lightsource','_sample'.


ABSORPTION.PY :

----> pour obtenir un spectre d'absorption d'un échantillon : 

 il faut : 

* prendre plusieurs séries de photos pour les spectres :
	- une série dans le noir avant d'aller la lumière source, pour le background ###( REVOIR L'UTILITE DE CETTE ETAPE )###
	- une série sans échantillon, juste de la lumière source
	- une série avec échantillon

* placer les photos du background dans le dossier : /images-source/_background
* placer les photos de la lumière source dans le dossier : /images-source/_lightsource
* placer les photos des spectres avec échantillon dans : /images-source/_sample
* lancer le programme absorption.py
-> celui-ci renverra le spectre d'absorption
# il est possible d'obtenir les spectres moyens du background, de la source lumineuse et du spectre avec échantillon, en décommentant dans le fichier absorption.py

AVERAGESPEC.PY : 

 Ce programme permet d'obtenir un spectre moyenné sur plusieurs images. Il faut juste pour cela mettre toutes les images dans un même dossier.
Le nom du dossier est à choisir, il faut simplement mettre ce dossier dans le dossier /images-source .
Lorsque le programme demande le nom du dossier, bien penser à mettre le nom entre guillemets, comme 'mondossier'. 

 * lancer le programme averagespec.py
-> penser à enregistrer le spectre obtenu

RAMAN.PY : 

	Ce programme est un algorithme naif qui sur un spectre, trouve les coordonnées du pic le plus intense et l'utilise comme réference.
Sur ce même spectre, chaque pic précedent le pic le plus intense est un pic d'energie plus faible, indiquant qu'une particule ou plus a été crée dans le milieu, il peut s'agir de niveaux vibrationnels ou rotationnels, et on peut adopter la vision particulaire pour parler de phonons dans les solides. Ainsi, on utilise le pic le plus intense ( supposé être la ligne de réference ) comme zéro et on refere chaque pic arrivant avant, à celui-ci. De cette manière on obtient un spectre avec les energies des particules créees dans le milieu. 
