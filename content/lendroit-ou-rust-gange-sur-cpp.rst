L'endroit où Rust gagne sur le C++
##################################

:date: 2017-02-06 19:00
:category: programmation
:tags: programmation, Rust, C++
:slug: lendroit-ou-rust-gagne-cpp
:author: ntimeu


Const-correctness
-----------------

En C++, la déclaration d'une variable est par défaut non constante, c'est-à
dire qu'elle est modifiable par défaut.

.. code-block:: c++

    int i = 0;
    i++; /** It works */

Très souvent, il est possible de déclarer la variable en tant que constante :

.. code-block:: c++

    const int i = retour_dune_fonction(...);
    if (i != ...)
        ...

Si la variable n'a pas à être modifiée, il faut utiliser ce const. Sauf que
bien généralement, personne ne l'utilise. Pire encore, il arrive des endroits
où l'on utilise des pointeurs constants ! Exemple :

.. code-block:: c++

    const unsigned long long int* p = &variable_contenant_un_entier;

Faites l'exercice : qu'est-ce qui est constant ici ? Le pointeur ou la valeur
pointée par le pointeur ? Si vous ne le savez pas (ou que vous essayez de vous
souvenir de comment vous faisiez à l'époque), un indice : lisez de droite à
gauche à partir du nom du pointeur

Dans la plupart des cas, les variables n'ont pas besoin d'être changées. Et il
arrive parfois de se tromper de touche, et d'affecter la variable au lieu de la
comparer à une autre. Là, deux écoles : soit vous avez les bons flags de
compilation, soit vous ne les avez pas (et généralement, on ne les a pas).

Rust fait l'inverse : plutôt que d'obliger le développeur à réfléchir à la
const-corectness au moment de déclarer la variable, il considère que toute
variable déclarée est constante. Avantage ?

* une variable ne devant pas être modifiée lèvera une erreur de compilation si
  on tente de la modifier par erreur (typo ou autre)
* seules les variables non-constantes devront être déclarées non constantes, et
  ça en fait généralement moins
* les compilateurs sont capables d'optimiser certaines variables lorsqu'elles
  sont constantes, donc c'est tout bénef

Résultat ? Votre code est plus sûr par défaut. Ah, et lorque la variable
déclarée n'est pas utiliseé mais tout de même déclarée en constante, rust vous
le dit en warning.


Les chaînes de caractères
-------------------------

En C++, une chaîne de caractère (la classe std::string hein, pas char[]) est un
tableau de char. En C/C++, un char est un octet. Un octet, c'est l'alphabet
ascii. En Rust, une chaîne de caractère (String) est un tableau de char. En
Rust, un char est un caractère UTF-8 (donc multi-octets).

Si vous arrivez à faire de l'UTF-8 de façon transparente en C++ simplement,
sans se prendre la tête et sans bibliothèque externe, appelez-moi. Ah et il est
possible de manipuler de façon très efficace ces tableaux de char, via le type
&str (qui est constant en plus).


Les types
---------

Plutôt que d'avoir des types dont on ne connait jamais la taille (unsigned lont
int, quand tu nous tiens ...) à moins de connaître l'architecture de
destination et la spécification du C, en Rust les types entiers ont leur nombre
de bits dans leur nom :

* i8, i16, i32, i64 pour les entiers signés sur 1, 2, 4 ou 8 octets
* u8, u16, u32, u64 pour les entiers non signés sur 1, 2, 4 ou 8 octets
* f32 et f64 pour les flottants selon la précision possible

Si besoin il y a usize et isize pour des types dépendants de l'architecture. Et
en mode débug les entiers émettent une erreur en cas de dépassement
de leur capacité (genre stocker 255+1 dans un u8).


La durée de vie
---------------

En Rust chaque variable a une durée de vie : si vous déclarez une variable
locale, que vous passez un pointeur de cette variable à une autre fonction qui
tourne dans un thread à côté, et bien si vous sortez de la fonction où la
variable est déclarée, vous allez probablement avoir un accès à de la mémoire
qui n'existe plus. Pareil, si la variable est partagée sans protection entre 10
fonctions il va y avoir du grabuge.

Et ça, le Rust ne le permet pas. Alors certes, c'est fatigant au début de se
battre avec le Borrow Checker (qui vérifie la durée de vie), mais une fois que
c'est fait, on s'en sort sans problème, et surtout on a la garantie de ne
jamais accéder à ce qui n'existe plus.

En C++ c'est possible à coup de unique_ptr et de shared_ptr, mais jusqu'à
aujourd'hui la plupart des cours d'introduction au C++ ne présentent pas ce
point. Donc on se retrouve avec beaucoup de nouveaux développeurs C++ qui font
du "C with classes". Et donc avec beaucoup de bugs.


La bibliothèque standard
------------------------

Depuis le standard C++11, on commence à voir arriver des jolies choses comme
une bibliothèque de thread mieux conçue, des containeurs très pratiques dans la
STL, des fonctions mathématiques poussées et une bibliothèque pour manipuler le
système de fichiers (notez que pour les deux derniers points on les attend lors
du C++17, qui devrait sortir l'année de publication de cet article). C'est
cool.

En Rust, `la bibliothèque standard <https://doc.rust-lang.org/stable/std/>`_
est déjà bien fournie, avec la plupart des APIs déjà standardisées. Oh et en
plus de la bilbiothèque de manipulation des fichiers déjà prête, on peut
manipuler le réseau en standard (indépendamment de l'architecture) et avec la
couche de sécurité du langage (durée de vie des variables, etc).


Les outils fournis par défaut
-----------------------------

`Cargo <http://doc.crates.io/>`_ est le gestionnaire de projets de Rust. Il
gère les dépendances, la compilation, le lancement des tests et la génération
de la doc. Tout est standardisé et clairement exprimé. Et c'est super léger.

En C++ ? Bah vous avez le choix. En système de construction ?

* CMake
* autotools
* b|2 (Build2)
* Ninja
* tup
* Maven ?

En tests ?

* GoogleTest
* libunittest
* Boost Test
* Qt Test

En doc ?

* Doxygen
* (je n'en connais pas d'autre donc je vais faire comme si de rien n'était)

C'est cool d'avoir le choix. Mais quand ils ont tous leurs méthodes pour
construire/tester/documenter un projet, s'adapter à un projet peu vite devenir
très compliqué.
