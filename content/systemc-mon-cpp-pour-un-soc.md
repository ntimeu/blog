---
title: "SystemC - mon C++ pour un SoC !"
date: 2015-04-15T16:30:00+01:00
---

Depuis quelques temps, je m'intéresse de plus en plus à la conception de
matériel et je m'attarde principalement sur le fonctionnement des CPUs et
cartes réseaux pour plusieurs raisons :

* les CPUs sont le coeur même de notre ordinateur; appréhender leur
fonctionnement permet de mieux optimiser certains codes
* sans réseau ni interconnexion, l'ordinateur n'a que peux d'intérêts (sauf
certains cas)


J'ai donc visité plein de sites, plein de cours en ligne, mais malheureusement
peu traitent de la conception de hardware pour des raisons simples :

* concevoir du hardware, c'est très peu répandu et très compliqué (matériel
cher, besoin de tout spécifier, ...)
* peu de ressources libres sur la conception de hardware (GHDL est libre, mais
trop compliqué/long à installer), peu d'outils (les environnements
constructeurs semblent être les seuls à être réellement fonctionnels)
* la plupart des pièces hardware sont des "boîtes noires", on sait quelles
fonctions sont réalisées, mais pas comment


Donc pour faire de la conception de hardware, ça semble râpé. Mais je suis
tombé sur une sorte de "méta langage", le
[SystemC](https://en.wikipedia.org/wiki/SystemC). C'est un ensemble de macros,
de classes et d'outils pour concevoir des modules (peut à la fois servir à
créer des logiciels ou du hardware) à interconnecter pour donner naissance à un
objet complet.


### Mais du coup, pourquoi en parler ?

Mon objectif pour les prochaines semaines (voir mois) c'est de présenter le
fonctionnement de SystemC, d'expliquer comment s'en servir et comment faire une
sorte de simulation de matériel. L'objectif final serait de réaliser un petit
processeur, et pour le fun il serait basé sur un
[processeur à pile](https://en.wikipedia.org/wiki/Stack_machine), où il n'y a
pas de registres mais où les opérations sont réalisées sur le haut de la pile
(par exemple, l'instruction "+" effectue l'addition des deux derniers entiers
présents sur le haut de la pile).

Donc l'objectif c'est de trouver la motivation et écrire, pour pouvoir à la fin
obtenir un "cahier" présentant les fonctionnalités que j'aurais utilisées dans
le cadre de SystemC.
