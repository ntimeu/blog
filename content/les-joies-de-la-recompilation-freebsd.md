Title: Les joies de la recompilation - FreeBSD
Date: 2013-12-03 18:35
Category: OS
Tags: FreeBSD
Slug: les-joies-de-la-recompilation-freebsd
Author: ntimeu

# Ah ... Recompiler son noyau FreeBSD, les joies du redémarrage impossible ...

Et oui, recompiler un noyau, c'est jamais facile, surtout pour les personnes
qui n'y connaissent rien mais qui veulent apprendre.

L'une des choses que j'apprécie beaucoup, c'est d'avoir une doc complète pour
expliquer le processus de compilation du noyau. Et les BSD ont énormément de
doc là-dessus.

## Un BSD, c'est bien, 2 BSDs, c'est mieux, 3 BSDs, c'est ...

Pour compiler FreeBSD, il vous faut :

* Un FreeBSD ^^
* Beaucoup de patience (deux heures chez moi)


Pour compiler, il vous suffit de suivre la page
[dédiée](http://www.freebsd.org/doc/en/books/handbook/makeworld.html) à cet
univers. Pour les sources, il vous suffit de chercher dans la
[doc](http://www.freebsd.org/doc/en_US.ISO8859-1/books/handbook/updating-upgrading.html).

## Une fois compilé, ça nous change quoi ?

Un noyau compilé, si vous avez modifié ses options, peut aider à :

* Avoir un noyau plus rapide
* Avoir un noyau qui consomme moins de mémoire
* Ajouter des fonctionnalités intéressantes à votre système.


Et justement, ce sont ces nouvelles fonctionnalités qui m'intéressent.
