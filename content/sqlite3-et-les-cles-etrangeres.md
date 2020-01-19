---
title: "SQlite3 et les clés étrangères"
date: 2015-03-17T19:43:00+01:00
---

Aujourd'hui en expérimentant un design de base de données avec SQLite, je me
suis aperçu que les clés étrangères (FOREIGN KEY) n'étaient pas vérifiées lors
d'une insertion (on pouvait ajouter des tuples dont la valeur n'appartenait pas
à l'autre table). Donc si vous vous servez de SQLite3 sous ArchLinux, je vous
conseille fortement :

* d'exécuter la commande "PRAGMA foreign_keys = ON;" à chaque fois que vous
ouvrez votre BDD
* de TOUJOURS tester le logiciel qui utilise SQLite pour vérifier que les
contraintes soient validées


Juste pour info, le comportement par défaut de SQLite (sauf modification par
votre distribution ou vos soins) est de ne pas vérifier les contraintes FOREIGN
KEY. Donc prenez garde ^^

Plus d'informations :
[PAR ICI](https://sqlite.org/pragma.html#pragma_foreign_keys).
