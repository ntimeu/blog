---
title: "Alpine Linux"
date: 2016-04-10T22:07:00+01:00
---

Retour d'un article, après quelques temps (oui mon dernier article date de mars
mais bon, pas vraiment le temps et l'envie).

Aujourd'hui on va parler d'une petite distribution Linux que j'ai découvert
récemment en trainant sur les Interwebs. Elle s'appelle
[Alpine Linux](http://alpinelinux.org/), et a pour objectifs la securité à tout
prix, tout en étant légère et rapide. Pour atteindre ses objectifs, elle repose
sur plusieurs mécanismes :

* [Busybox](http://www.busybox.net/) qui est un outil permettant de créer un
espace utilisateur très simple et ne contenant qu'un seul exécutable (les
autres exécutables étant des liens symboliques vers ce dernier)
* [musl libc](http://www.musl-libc.org/), une implémentation de la bibliothèque
standard qui se veut simple, rapide, légère et surtout correcte (qui respecte
les standards en place)
* [OpenRC](https://wiki.gentoo.org/wiki/Project:OpenRC), un système d'init
simple (concurrent de systemd, mais plus simple) créé par les développeurs de
la distribution [Gentoo](https://gentoo.org/)
* [grsecurity](https://grsecurity.net/), un patch pour le noyau Linux qui
ajoute énormément de mécanismes de sécurité, comme l'ASLR et des vérifications
supplémentaires

La première chose que l'on remarque, c'est l'utilisation d'outils généralement
employés dans l'embarqué, **musl** et **Busybox**. Ils sont très légers, et
Busybox a l'avantage d'être automatisable très rapidement grâce à son système
de construction (basé sur les Makefile).

Cette distribution est plutôt intéressante, notamment car elle a son usage dans
les serveurs et les containeurs (l'un pour la sécurité, l'autre pour ses 130 MB
quand installés). Donc si par hasard vous avez besoin d'une distribution légère
et utilisable un peu partout, n'hésitez pas à y jeter un oeuil !
