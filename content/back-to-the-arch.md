---
title: "Back to the Arch"
date: 2016-12-11T01:00:00+01:00
---

Petit retour sur le blog, après plusieurs (longs) mois de travail et de
changements.

# Firefox

Toujours chez le panda roux, même si la configuration a quelque peu changé :

* on conserve [µBlock Origin](https://github.com/gorhill/uBlock), qui passe en
  mode expert et on lui fait bloquer
  tous les domaines externes (3rd party)
* on supprime Privacy Badger, qui fait double emploi avec µBlock
* [HTTPs Everywhere](https://www.eff.org/https-everywhere) reste en place sans
  rien toucher
* entrée très remarquée de [VimFX](https://github.com/akhodakivskiy/VimFx), qui
  devient mon outil de prédilection pour utiliser Firefox (raccourcis Vim dans
  Firefox)


# ArchLinux is back

Bon, retour sur [ArchLinux](https://www.archlinux.org/) qui reste ainsi ma
distribution préférée. On retrouve notamment :

* [ConnMan](https://wiki.archlinux.org/index.php/Connman) pour la gestion de la
  partie réseau. Effectivement, j'aurais pu installer NetworkManager, mais bon
  pour l'usage que j'en ait ... En plus ça marche très bien
* [i3](https://wiki.archlinux.org/index.php/I3) reste l'environnement graphique
* [Vim](https://wiki.archlinux.org/index.php/Vim) l'éditeur préféré. Passage par
  [Vundle](https://github.com/VundleVim/Vundle.vim) pour la gestion des plugins.
  Et en passant, la configuration est beaucoup plus simple, et est dispo sur
  [github](https://github.com/ntimeu/vimconf)


# Langages

Haskell => poubelle, je reste pour l'instant sur C++ et Rust. Ca marche, c'est
efficace (le C++ moderne est une tuerie, mais reste malgré tout en deçà des
capacités du Rust), les performances sont bonnes, les langages sont élégants.

Je me suis formé sur [cmake](https://cmake.org/), maintenant quand C++ il y a
besoin, CMake est utilisé. Même pour les petits codes. Sinon un autre bon outil
est [tup](http://gittup.org/tup/), qui est un système de construction plus
basique que cmake mais est plus performant que les autres (par contre bonjour
la dépendance à fuse).

Pareil, je travaille en ce moment sur OpenCL pour effectuer du traitement
d'images. C'est plutôt pas mal, l'API est très bien documentée et claire, et le
wrapper C++ est très bien écrit. Sans compter qu'il existe un project libre pour
fournir une implémentation libre d'OpenCL sur les GPU Intel,
[Beignet](https://www.freedesktop.org/wiki/Software/Beignet/). Du coup
on peut faire de l'OpenCL sans avoir à recompiler de noyau ou d'appliquer des
patches à un noyau ancien.


# Outils

Grosse formation à [Buildroot](https://buildroot.org/) et
[Yocto](https://www.yoctoproject.org/). Enfin par Yocto je parle surtout
d'[OpenEmbedded](http://www.openembedded.org/wiki/Main_Page), qui est utilisé
par Yocto pour produire une distribution de base. Je reste tout de même fidèle à
Buildroot, qui est plus simple à prendre en main et plus léger à l'utilisation.
