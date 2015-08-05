Title: Chroneek - Retour sur ArchLinux
Date: 2014-08-12 00:00
Category: OS
Tags: GNU/Linux, archlinux, chroneek
Slug: chroneek-retour-sur-archlinux
Author: ntimeu

Après plusieurs années passées sous OpenBSD et Debian, le grand retour sur
ArchLinux !

Pour ceux qui l'ignorent, [ArchLinux](https://www.archlinux.org/) est une
distribution GNU/Linux basée sur le principe de la
[Rolling Release](https://fr.wikipedia.org/wiki/Rolling_release). C'est tout
simplement le fait de mettre à jour en permanence les logiciels disponibles.

Evidemment, c'est une grosse fracture par rapport à
[Debian](https://www.debian.org/) qui tient à la stabilité de son système, et
ne prend en conséquence (généralement) que les paquets supportés à long terme
(par exemple, ils utilisent un noyau LTS, qui sera supporté pendant plusieurs
années et profitera des mises à jour de sécurité).


Archlinux travaille différemment, avec comme principale philosophie,
le principe [KISS](https://fr.wikipedia.org/wiki/KISS-principe) (Keep It Simple
Stupid) : rendre les choses simples, et ne pas les compliquer inutilement.


## Pendant l'installation, j'ai le bourdon ... ou pas !

Une chose importante à savoir sous Archlinux est que beaucoup de choses sont
faites à la main :

* sélectionner le schéma de partitionnement
* choisir le dépôt depuis lequel télécharger les paquets
* configurer le système
* installer l'interface graphique (et oui ! Qui a dit que c'était fait tout
seul ? )
* et encore beaucoup d'autres choses ...


Donc une fois la clef USB bootable insérée pas de "zolie" interface graphique
pour nous aider à installer notre système, mais à la place un magnifique shell
root sur un système live, et ce jusqu'à la fin de l'installation. Et la
première chose qui impressionne : 133 packages installés pour la distribution
de base (système minimal + compilateurs) ! C'est génial (no kidding)!


## L'interface graphique, elle est fantasteek !

Ensuite viens la phase ou ... on veut une interface graphique. Et ici, le choix
est assez large : Gnome, Enlightenment, KDE, OpenBox, ... (je vais pas faire la
liste, il y en a trop). Sauf que quand on les a tous essayés (ou presque,
permettez-moi d'exagérer un peu ^^), on aimerait bien avoir quelque chose de
nouveau : [i3](http://i3wm.org/) est un petit gestionnaire de bureau TRES
léger, contrôllable ... uniquement au clavier ! Donc on installe le serveur
X11, i3 et dmenu, et là tout de suite le système est super réactif ! On jongle
avec les environnements de travail rapidement, on lance des logiciels dans tous
les sens, la seule chose qui est compliquée, c'est de se souvenir des
raccourcis clavier ! Au pire, une petite fenêtre firefox branchée sur la doc et
celà passe très bien !


## Systemd : "Aie confiaaaannnnnce"

Là, c'est la chose qui fâche :
[systemd](http://freedesktop.org/wiki/Software/systemd/) est le système d'init
par défaut d'ArchLinux, et ce depuis longtemps (je crois qu'elle a d'ailleurs
été parmit les premières distributions Linux à utiliser systemd). Donc pas de
jolis scripts bash, mais à la place un système ...efficace, rapide et simple à
utiliser :

* un temps de boot de 2 secondes (interface graphique comprise) => ça change
BEAUCOUP de Debian
* ajouter un service ? Il suffit de demander à systemctl de l'ajouter
* les modules nécessaires sont lancés automatiquement (modules pour le matériel
uniquement)
* les logs sont simples à parcourir
* il s'occupe des connexions réseau à ta place

Donc systemd deviens assez impressionnant pour moi qui vient pourtant des
systèmes d'init classiques BSD, ce qui est assez cool.

## Du coup, la conclusion ?

(Oui, dernière fois que je lance des -eek et des blagues de ce niveau ^^)
En plus d'être en permanence à jour, ArchLinux offre un système rapide, clair,
léger et rapide, ce qui le rend assez différent des autres distributions
habituelles, et nous propose une capacité de contrôle assez incroyable sur ce
qui est présent au niveau système. A ceux qui souhaitent avoir une distribution
avancée, Archlinux est faite pour vous !
