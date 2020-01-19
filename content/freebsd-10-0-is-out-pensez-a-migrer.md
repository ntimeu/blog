---
title: "FreeBSD 10.0 is out - Pensez à migrer !"
date: 2014-01-22T21:33:00+01:00
---

Au menu de cette nouvelle version :

* suppression de gcc dans la base, arrivée de LLVM/Clang (nouveau compilateur,
qui semble plus rapide après quelques compilations)
* disparition du DNS Bind, pour le remplacer par UNBOUND (après plusieurs
recherches, il semble que Unbound soit plus performant et modulaire que Bind,
à voir)
* BHyve on the road ! (pour ceux qui se posent des questions, BHyve est un
hyperviseur, comme qemu-kvm, qui fait de la virtualisation, mais intégré aux
systèmes BSD). Plus besoin de VirtualBox !


Pour en savoir plus, allez voir
[FreeBSD WhatsNew](https://wiki.freebsd.org/WhatsNew/FreeBSD10).
