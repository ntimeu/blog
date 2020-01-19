---
title: "Yocto et Buildroot - Les distributions de l'embarqué !"
date: 2016-05-21T15:45:00+01:00
---

Dans le monde de l'embarqué, il est assez complexe de construire un système
complet (bootloader + noyau + espace utilisateur). De plus le maintenir est
compliqué, car les versions des logiciels installés peuvent changer, les
dépendances bouger et des failles de sécurité peuvent être corrigées. Il faut
également faire en sorte que la compilation de tout ce système soit au maximum
automatique afin de limiter le temps perdu par les concepteurs.

Pour pallier à ces problèmes, des développeurs ont conçu deux façons de faire :
[Buildroot](https://buildroot.org/) et [Yocto](https://yoctoproject.org/). Ces
deux projets sont très différents dans leur façon de générer le système
embarqué :

* Yocto permet de générer une distribution complète, avec des paquets (comme
Debian, Ubuntu, etc), ce qui simplifie la maintenance d'un système embarqué.
* Buildroot a surtout pour but de fournir un système all-in-one, c'est à dire
que le système final ressemblera à un firmware, avec peu de fichiers et le tout
sera self-contained.

Ces deux outils sont très pratiques, car ils sont capables de prendre en compte
d'eux-mêmes une étape assez longue et compliquée de la génération d'un système
embarqué : la construction du(des) compilateur(s) croisé(s). En effet, il est
assez rare de compiler un système embarqué sur la plateforme cible, qui ne sont
pas forcément des foudres de guerre (essayez de compiler un système basé sur
Buildroot avec les bibliothèques graphiques sur un Raspberry pi 1 :). Du coup,
Buildroot et Yocto génèrent directement sur le PC de construction les
compilateurs et l'utilisent pour construire le système embarqué après coup.


## Utilisabilité

Niveau utilisabilité, j'apprécie particulièrement Buildroot pour plusieurs
raisons :

* il est simple car basé sur des Makefile et dispose d'une interface KConfig
(qui utilise des interfaces graphiques en console ou GTK/Qt)
* s'intégrer dans le système de construction est très simple
* une simple commande "make" est nécessaire pour lancer la compilation


## Développement

De la même façon, Buildroot est bien plus simple d'accès pour ceux souhaitant
ajouter un paquet ou ajouter le support d'une carte. Généralement un simple
fichier est à créer ou modifier afin d'étendre la plateforme.

Yocto est quant à lui extrêmement modulaire, mais provoque parfois des retards
par rapport à sa version de base. De plus, l'architecture du projet est
assez complexe à comprendre, et développer un support pour une carte spéciale
(donc un BSP) est assez long et difficile (mais pas infaisable).


## Lequel utiliser ?

Selon moi, tout dépend de l'objectif : si le système doit être connecté de façon
permanente à Internet, alors Yocto est un bon choix car il permet de mettre à
jour simplement les différents composants de la distribution générée.

Si le système cible n'est pas ou peu connecté à Internet, et ne nécessite pas de
mises à jour en permanence, alors Buildroot et son approche "firmware" du
système est plus indiquée.
