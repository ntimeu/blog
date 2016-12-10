Back to the Arch
################

:date: 2016-12-11 01:00:00
:tags: misc, programmation
:category: OS
:slug: back-to-the-arch
:author: ntimeu
:summary: Retour sur ArchLinux

Petit retour sur le blog, après plusieurs (longs) mois de travail et de
changements.

=======
Firefox
=======

Toujours chez le panda roux, même si la configuration a quelque peu changé :

* on conserve `µBlock Origin`_, qui passe en mode expert et on lui fait bloquer
  tous les domaines externes (3rd party)
* on supprime Privacy Badger, qui fait double emploi avec µBlock
* `HTTPs Everywhere`_ reste en place sans rien toucher
* entrée très remarquée de VimFX_, qui devient mon outil de prédilection pour
  utiliser Firefox (raccourcis Vim dans Firefox)

.. _`µBlock Origin`: https://github.com/gorhill/uBlock
.. _`HTTPs Everywhere`: https://www.eff.org/https-everywhere
.. _VimFX: https://github.com/akhodakivskiy/VimFx


=================
ArchLinux is back
=================

Bon, retour sur ArchLinux_ qui reste ainsi ma distribution préférée. On retrouve
notamment :

* ConnMan_ pour la gestion de la partie réseau. Effectivement, j'aurais pu
  install NetworkManager, mais bon pour l'usage que j'en ait ... En plus ça
  marche très bien
* i3_ reste l'environnement graphique
* Vim_ l'éditeur préféré. Passage par Vundle_ pour la gestion des plugins. Et en
  passant, la configuration est beaucoup plus simple, et est dispo sur github_

.. _ConnMan: https://wiki.archlinux.org/index.php/Connman
.. _ArchLinux: https://www.archlinux.org/
.. _ConnMan: https://wiki.archlinux.org/index.php/Connman
.. _i3: https://wiki.archlinux.org/index.php/I3
.. _Vim: https://wiki.archlinux.org/index.php/Vim
.. _Vundle: https://github.com/VundleVim/Vundle.vim
.. _github: https://github.com/ntimeu/vimconf


========
Langages
========

Haskell => poubelle, je reste pour l'instant sur C++ et Rust. Ca marche, c'est
efficace (le C++ moderne est une tuerie, mais reste malgré tout en deça des
capacités du Rust), les performances sont bonnes, les langages sont élégants.

Je me suis formé sur cmake_, maintenant quand C++ il y a besoin, CMake est
utilisé. Même pour les petits codes. Sinon un autre bon outil est tup_, qui est
un système de construction plus basique que cmake mais est plus performant que
les autres (par contre bonjour la dépendance à fuse).

Pareil, je travaille en ce moment sur OpenCL pour effectuer du traitement
d'images. C'est plutôt pas mal, l'API est très bien documentée et claire, et le
wrapper C++ est très bien écrit. Sans compter qu'il existe un project libre pour
fournir une implémentation libre d'OpenCL sur les GPU Intel, Beignet_. Du coup
on peut faire de l'OpenCL sans avoir à recompiler de noyau ou d'appliquer des
patches à un noyau ancien.

.. _cmake: https://cmake.org/
.. _tup: http://gittup.org/tup/
.. _Beignet: https://www.freedesktop.org/wiki/Software/Beignet/


======
Outils
======

Grosse formation à Buildroot_ et Yocto_. Enfin par Yocto je parle surtout
d'OpenEmbedded_, Yocto étant seulement un utilisateur de la distribution de
base. Je reste tout de même fidèle à Buildroot_, qui est plus simple à prendre
en main et plus léger à l'utilisation.

.. _Buildroot: https://buildroot.org/
.. _Yocto: https://www.yoctoproject.org/
.. _OpenEmbedded: http://www.openembedded.org/wiki/Main_Page
