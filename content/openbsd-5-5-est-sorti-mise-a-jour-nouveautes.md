Title: OpenBSD 5.5 est sorti - Mise à jour, nouveautés
Date: 2014-05-03 18:55
Category: OS
Tags: BSD, OpenBSD, sécurité
Slug: openbsd-5-5-est-sorti-mise-a-jour-nouveaute
Author: ntimeu

Au menu, de nouveaux drivers (pilotes de périphériques) ont été ajoutés,
notamment au niveau de VMWare, VirtIO (pilotes dédiés aux entrées/sorties
virtuelles pour la virtualisation). De nouveaux pilotes réseau, et plus de
processeurs supportés par le système. (Rappelons qu'OpenBSD a un règle très
stricte concernant les pilotes : code source standard ou RIEN.
Pas de binaires précompilés).

[signify(1)](http://www.openbsd.org/cgi-bin/man.cgi?query=signify&sektion=1)
vérifie les packages à l'installation ! Plus de blagues sur les packages non
signés !


Les dates sont désormais sur 64 bits (8 octets). En gros, pas de problèmes lors
du passage de 2038 (on ne pourra pas dire qu'on n'était pas préparé). Pensez à
bien caster en long long int.


[pf(4)](http://www.openbsd.org/cgi-bin/man.cgi?query=pf&sektion=4) a reçu
plusieurs améliorations, surtout pour les files d'attentes (queues),
modification de la syntaxe et mise en place d'une décision de "TCP RST" en cas
de blocage.


[OpenSMTPD](https://www.opensmtpd.org/) est installé par défaut (OpenSMTPD est
un MTA/MDA dont l'objectif est de respecter la
[RFC 5321](https://tools.ietf.org/html/rfc5321), et est très léger, avec une
syntaxe de configuration proche de celle de Packet Filter). Je vous conseille
de regarder la syntaxe par défaut, qui est ... TRES simple, contrairement à
celle de Postfix.

En plus de cela, diverses améliorations ont été appliquées au logiciel
(utilisation mémoire/cpu moindre,
[TLS PFS](https://en.wikipedia.org/wiki/Perfect_forward_secrecy), amélioration
des backends, etc). Malheureusement, les différents backends (stockage des
utilisateurs/domaines virtuels) sont toujours instables, donc éviter de les
utiliser (même si je le fais ^^).


Plusieurs mécanismes de sécurité ont été ajoutés, la génération de nombres
pseudo-aléatoires se voit attribuer une "graine" (seed) par le bootloader,
ajoutant donc de l'entropie à la génération. La protection de la pile noyau
reçoit elle aussi de l'entropie par ce moyen.


Une grosse différence vient à l'intérieur de la libC, qui voit arriver la
fonction [explicit_bzero(3)](http://www.openbsd.org/cgi-bin/man.cgi?query=explicit_bzero&sektion=3).
Pourquoi cette fonction ? Car dans certains cas, le compilateur peut
"supprimer" l'appel à bzero(), pour optimiser (ce qui ne sert à rien, et peut
être la cause de bien des problèmes de sécurité).


Diverses améliorations au niveau des performances, du support du
multithreading, l'arrivée du système de fichiers
[tmpfs(8)](http://www.openbsd.org/cgi-bin/man.cgi?query=mount_tmpfs&sektion=8).
Je crois que je vais y passer pour mon /tmp.


[OpenSSH](http://www.openssh.com/) reçoit PLEIN de mises à jour, de nouveaux
algorithmes de chiffrement, et SUPPRESSION de la possibilité de se logger via
des clés RSA+MD5 (toutefois possible via une signature DSA). Attention, une
future version refusera tout simplement ces clés.


N'oubliez pas qu'[OpenBSD](http://www.openbsd.org/index.html) est développé
gratuitement par des bénévoles.

> Our efforts emphasize portability, standardization, correctness, proactive
> security and integrated cryptography.

Vous pouvez leur faire un don via la
[Fondation OpenBSD](http://www.openbsdfoundation.org/).
