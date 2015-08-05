Title: Les jails - C'est tellement fun !
Date: 2013-12-07 15:15
Category: OS
Tags: FreeBSD, sécurité
Slug: les-jails-c-est-tellement-fun
Author: ntimeu

Pourquoi les jails ? Parce que c'est ma solution préférée : simple, longue à
déployer mais efficace par la suite. Et puis ça tourne sous mon FreeBSD !


Les jails, c'est un chroot disposant de capacités améliorées, comme la
modification de la racine du système de fichiers, mais aussi la séparation des
IDs de processus (un processus tournant dans un jail X ne verra QUE les
processus qui tourneront dans la même jail). Cela permet d'avoir une sécurité
renforcée et plus simple à maintenir qu'une sécurité basée sur des groupe
d'utilisateurs (attention : chaque jail est son propre système, il faut donc
gérer la sécurité dans chaque jail).


Un exemple de jails :

1. serveurs web + BDD
2. serveurs SMTP + IMAP/POP3
3. d'autres services


Essayez de placer dans le même jail les services qui sont inter dépendants,
cela permettra de bien gérer vos services !
