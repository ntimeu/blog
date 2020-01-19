---
title: "C++ - do not use using into your header configuration"
date: 2015-04-20T22:16:00+01:00
---

On utilise souvent la directive "using namespace" en C++ pour éviter d'ajouter
le nom de l'espace de nom pour accéder à ce qu'il contient (classe, fonction,
variable, constante), parce que :

* ça permet d'écrire moins de code
* ça rend le code plus lisible


Le seul problème, c'est quand vous souhaitez écrire une bibliothèque : et
notamment lorsqu'on crée une classe avec des attributs ayant un type
appartenant à une autre bibliothèque (SystemC par exemple). Du coup, on est
tenté d'utiliser la directive using pour ne pas retaper l'espace de nom avant
de taper le type. Le seul problème, c'est que le faire dans un header, c'est
une TRES mauvaise idée : je m'explique.

{{< highlight cpp >}}
#include <iostream>

using namespace std;

int main()
{
    cout << "Salut" << endl;
    return 0;
}
{{< / highlight >}}

Le code est lisible, simple et léger. Sauf que si vous avez dans un espace de
nom (que vous aurez évidemment nommé monnamespaceinutile pour coller à
l'exemple) autre que celui d'iostream et qui contient cout et endl, alors plus
rien ne va ! Explications :


{{< highlight cpp >}}
#ifndef CLASSE_INUTILE
#define CLASSE_INUTILE

#include "monnamespaceinutile.h"

using namespace monnamespaceinutile;

class ClasseInutile
{
    ...
};

#endif
{{< / highlight >}}


Sauf que si vous incluez ce header dans un autre fichier, et que vous essayez
d'accéder à cout ou endl, il risque d'y avoir collision et le compilateur
refusera de compiler ! Et si ce header est accessible par un autre développeur,
il sera lui aussi coincé. Donc moralité, n'utilisez JAMAIS "using namespace"
dans un header qui peut être inclus !

En plus, préciser le nom de l'espace de nom permet de comprendre directement à
quelle bibliothèque appartient la fonction/classe.

## Concernant SystemC

SystemC a une petite capacité intéressante et fatigante à la fois : il y a deux
headers, systemc.h et systemc ! Et le problème, c'est que systemc.h pose le
problème soulevé dans cet article, c'est-à dire les using namespace dans le
fichier d'en-tête. C'est pratique (évite de retaper sc_core::) dans chaque
fichier, mais en cas de conflit, bonne chance pour débugger !
