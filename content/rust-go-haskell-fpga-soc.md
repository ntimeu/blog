Title: Rust, Go, Haskell, FPGA et SoC - Le bazar de cette fin d'année
Date: 2015-12-14 17:00
Category: programmation
Tags: programmation, hardware
Slug: rust-go-haskell-fpga-soc
Author: ntimeu

Bon, voila un paquet de temps que je n'ai pas posté d'articles sur le blog,
à la fois par manque de temps et surtout par manque d'envie. Vu la quantité
de travail à réaliser, je n'ai pas trop eu le temps de m'y consacrer. Mais
cet article est là pour relancer le blog, j'espère pouvoir écrire un peu
plus l'année prochaine (oui parce qu'en trois semaines je n'aurai pas le
temps ^^).


### Rust, Go et Haskell

On commence par un gros morceau (plusieurs même) avec les langages de
programmation. Grâce à mes études j'ai l'opportunité de concevoir un système
qui nécessite d'effectuer du passage de messages, de l'asynchrone avec des
files d'attente et des verrous partagés. Du coup pour réaliser ce programme
j'ai pas vraiment envie d'utiliser les langages que j'utilise habituellement
(Python et C) pour plusieurs raisons, on va donc commencer avec le C :

* nécessite de tout faire soi-même
* bon parallélisme
* risque d'erreurs de pointeurs très ouvent
* synchro très présente

Et pour le Python :

* assez simple
* module asyncio, donc pas de parallélisme mais de l'asynchrone à fond
* le GIL (Global Interpreter Lock) risque de poser problème (si on part sur
du multiprocessing)

Du coup pour éviter d'utiliser ces langages (souvent sujets aux erreurs de
codage, et surtout de types pour le python), j'ai décidé d'aller voir du
côté des nouveaux langages de programmation qui offrent (entre autres) des
méthodes intégrées aux compilateurs pour éviter les problèmes de
concurrence. J'ai pensé au Go et au Rust, tous deux lancés vers la même
époque (2009-2010) et qui poursuivent les mêmes objectifs, c'est-à dire
proposer aux développeurs un moyen de coder simplement tout en ayant des
garanties sur l'utilisation de la mémoire et la synchronisation des
ressources.


#### On commence par le Go

Le Go est un langage développé au sein de Google par des personnes assez
compétentes dans le domaine (comme
[Ken Thompson](https://en.wikipedia.org/wiki/Ken_Thompson),
[Rob Pike](https://en.wikipedia.org/wiki/Rob_Pike) ou encore
[Robert Griesemer](https://en.wikipedia.org/wiki/Robert_Griesemer)). C'est
un langage typé statiquement, compilé, impératif et concurrent. Typé parce
que les types c'est le bien, compilé parce qu'on n'a pas forcément envie
d'installer un logiciel complet pour faire tourner une petite appli, et
enfin concurrent parce qu'il propose un mode de parallélisme très simple à
utiliser et accessibles aux débutants.

En plus de tout celà, le langage a une fonctionnalité inédite (pour moi
pauvre mortel) : les bibliothèques sont toutes compilées statiquement dans
l'exécutable de destination ! Finit les dépendances sur la lib**, ici tout
est intégré, ce qui est très pratique à première vue. Néanmoins cette façon
de compiler a des limitations : en cas d'erreur dans une bibliothèque (par
exemple une bibliothèque de chiffrement mal implémentée), c'est à la
personne qui crée le programme de faire attention ! Et à ce moment on
commence à comprendre l'intérêt des librairies dynamiques, plus simples à
mettre à jour. De plus, le manque de gestion des versions des dépendances
oblige le développeur à suivre la dernière version des outils qu'il utilise,
ce qui n'est pas forcément fait par tous et peut amener sur des collisions
de versions ou des API incompatibles.

En tout cas, je garde une très bonne image de ce langage, malgré ses
quelques défauts (ah oui, j'ai oublié de parler des deux façon de faire des
déclarations/initialisations de variables ^^). BTW merci à
[Racam](https://www.racam.fr/) pourles conseils sur le Go.


#### Et puis le Rust

Après avoir bricolé quelques utilitaires en Go, je me suis dirigé vers le
[Rust](https://www.rust-lang.org/) qui est un langage conçu par les gars de
Mozilla (oui vous savez, ceux qui font votre meilleur ami le
[Panda Roux](https://www.mozilla.org/en-US/)) et qui a pour objectif de
fournir un langage avec de fortes contraintes en matière de programmation.

Ici aussi il s'agit d'un langage typé statiquement et compilé, mais qui
ajoute des idées de "prêt", de "durée de vie" des variables et de "contexte"
qui empêchent de nombreuses erreurs dès la compilation. Avec ces concepts,
le programmeur a des outils simples et efficaces pour créer des programmes
sans fautes (bon après les calculs peuvent être mauvais, mais ça c'est la
faute au codeur).

C'est un très bon langage, qui dispose d'une syntaxe claire (comparable au
C) avec des ajouts qui proviennent probablement de différents langages (oui
Haskell, tu es visé !). L'outil Cargo (qui permet de gérer un projet et ses
dépendances) est très complet, mais devrait (à mon sens) être intégré au
code de Rust pour que le code soit réalisé de façon assez propre dès le
début d'un projet.
