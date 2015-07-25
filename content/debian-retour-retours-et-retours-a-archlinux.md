Title: Debian - Retour, retours et retour à ArchLinux
Date: 2015-06-01 22:41
Category: archlinux
Tags: archlinux, debian
Slug: debian-retour-retours-et-retours-a-archlinux
Author: ntimeu

Dans mon article précédent, j'expliquais pourquoi (de façon évasive) j'avais
pris la décision d'aller sous Debian.

Le seul problème (et si ce n'était que celui-là), c'est que la philosophie de
Debian, c'est d'avoir tout en packages dans les dépôts, et en version stable.
Donc, quand je veux installer un package Haskell (par exemple
[Wreq](http://hackage.haskell.org/package/wreq)), j'utilise cabal pour
installer le paquet. Sauf qu'à ce moment-là, tout s'écroule ! Nombreuses
erreurs, paquets installés non présents (à cause des versions multiples). Donc
suite à un petit raz-le-bol de ce genre de problème, j'ai décidé de retourner à
ArchLinux.

Mais pas n'importe comment. Donc l'installation tournera autour de :

* Enlightenment (gestionnaire de fenêtres)
* Connman (gestionnaire de connexions réseau, très bien intégré avec Enlightenment)

En effet, Connman semble fonctionner très bien (aucun problème depuis la
réinstallation). Très peu de configuration à effectuer (BEAUCOUP plus que
Debian, mais au moins on fait ce qu'on veut à l'installation), le tout marche
directement (materiel Intel majoritairement, wifi + carte HD5200).

NB: quel bonheur de retourner sous une
[rolling-release](https://en.wikipedia.org/wiki/Rolling_release), paquets en
dernière version. Et puis, GCC 5.1 !
