Title: Rust, le nouveau C++ ?
Date: 2016-03-15 18:45
Categories: programmation
Tags: programmation, rust
Slug: rust-le-nouveau-cpp
Author: ntimeu

Après la sortie de [Rust 1.7](http://blog.rust-lang.org/2016/03/02/Rust-1.7.html),
on a appris que [Servo](https://servo.org/) (le nouveau moteur de de rendu web
de Mozilla, codé en Rust) allait bientôt sortir en version alpha sur nos
machines vers juin 2016. C'est développé via le projet
[Browserhtml](https://github.com/browserhtml/browserhtml), qui développe une
interface utilisateur pour les bureaux.

Ce qui est bien avec Servo, c'est sa conception : pas de bugs liés à la
mémoire (grâce à Rust), un rendu effectué en parallèle (grâce au modèle de
parallélisme de Rust) qui permet d'aller plus vite et surtout un système de
rendu remis au goût du jour, qui colle mieux aux architectures actuelles et
aux paradigmes de programmation modernes (et ça amène beaucoup de choses,
entre autre de la sécurité et de la modularité). Mais arrêtons de parler de
Servo, le sujet se place principalement sur Rust.

### Ce Rust, c'est bien ?

J'ai déjà rédigé un article sur le Rust
[par le passé]({filename}/rust-go-haskell-fpga-soc.md), qui effleurait
surtout les possibilités du Rust sans pour autant rentrer dans les détails.
Depuis quelques temps je suis à fond dans ce langage, et je pense être
capable de présenter ses avantages grâce à mon expérience.

Tout d'abord, qu'on l'aime ou que l'on ne l'aime pas, le système de type
est une véritable plus-value lors de la phase de conception d'un programme
quelconque, qui évite bien des erreurs dès la compilation et oblige le
développeur à réfléchir sur le fonctionnement final du logiciel.

Si on y ajoute les types structurés (comme les structures en C), les traits
et les implémentations, on obtient un système très proche de l'objet (où
les traits sont les interfaces du Java, les structures sont les attributs
des classes Java et les implémentations les méthodes implémentées pour
répondre à la spécification de l'interface). Voici la différence entre un
programme Java et Rust (même chose, à part que le programme Java n'a pas été
testé) :


{% include_code rlnc/equivalent.java lang:java %}


{% include_code rlnc/equivalent.rs lang:rust %}

En plus de celà, le modèle de retour du Rust permet de raisonner rapidement
sur le déroulement d'un programme, via deux types, Result (qui exprime si
tout s'est bien déroulé ou dans le cas contraire une explication de l'erreur)
et Option (très utile, par exemple si une queue est vide plutôt que de
renvoyer une erreur lors d'un pop() on peut renvoyer un résultat vide au
lieu de tester si la queue est vie à chaque fois). Un petit exemple pour la
route :


{% include_code rlnc/result.rs lang:rust %}

### Le pattern matching, meilleur ami du développeur

Le pattern matching, c'est le fait de tester quelque chose pour dire s'il
ressemble à un pattern (merci cap'tain Obvious). Sauf que contrairement à
un bloc if/else if/else, le pattern matching impose l'exhaustivité des
pattern, ce qui fait lever une erreur par le compilateur dans le cas
contraire. En plus d'être pratique, la syntaxe est élégante.

Si vous regardez l'exemple de code précédent, le bloc match permet de faire
du pattern matching sur le retour de la fonction pop_back(). Si jamais j'avais
oublié de tester le retour None, alors dans ce cas le compilateur aurait refusé
de compiler.

### Un gestionnaire de modules, c'est mieux

Une des grandes faiblesses des langages "à l'ancienne", c'est le manque
de ce gestionnaire de module, qui s'occupe de beaucoup de tâches très
importantes comme la gestion des dépendances, le cycle de vie du logiciel
et la mise en paquet. Entre JavaScript qui a un grand nombre de package
manager (officiel et non officiels) et le C/C++ qui n'en ont pas (ou
alors ça n'est pas très connu/utilisé), les développeurs de Rust ont
fait un choix plutôt judicieux : concevoir dès le départ un package manager
très efficace, à la fois simple et extensible. Du coup, on se retrouve
avec le système de Crates [crates.io](https://crates.io), qui permet de
trouver son bonheur parmi plus de 4.000 paquets. Ajoutez à ces deux
outils Git et vous obtenez un système stable, léger et fonctionnel.

### La macrogame

Ah, les macros, un sujet un peu "sensible", surtout quand on vient du
monde du C où les macros permettent de faire tout et son contraire.
Dans le cas du Rust, les macros sont très utiles, et sont basées sur
un concept assez logique : plutôt que de faire du remplacement de
texte (sed, préprocesseur), la macro décrit comment générer la partie
de l'AST qui correspond à la macro. C'est une sorte de système qui
génère du code, mais uniquement lors de la phase de génération de
l'AST, contrairement au C ou le préprocesseur fait du remplacement par
trouver/remplacer.


### En conclusion

Le Rust, c'est joli, ça fait ce qu'on lui demande, ça a plein de bibliothèques,
c'est bien conçu, ça nous embête quand on fait des trucs sales, mais c'est un
super langage qui mérite d'être reconnu (ainsi que ses créateurs).
