Title: Nginx - Après un an d'utilisation
Date: 2014-09-04 15:53
Category: GNU/Linux
Tags: bsd, gnu-linux, concurrence
Slug: nginx-apres-un-an-d-utilisation
Author: ntimeu

Nginx, je l'avais déjà évoqué lors de mon billet sur les Kernel Queues. C'est
un serveur haute performance capable de faire office de serveur web, de reverse
proxy, etc ...


L'avantage de ce serveur réside dans sa conception : ici pas de système de fork
(ou thread) par client, ni d'interpréteur PHP.


Du coup, on voit la différence : tout au long de l'année, ce serveur ne
consomme que quelques Mo de RAM, et me permet donc d'accepter un bon gros
paquet de clients sans avoir trop de problèmes. L'inconvénient, c'est que
l'interpréteur PHP présent dans apache n'existe pas. Donc on est obligé
d'installer un php-fpm pour servir les pages en php, ce qui est plutôt
pratique pour effectuer les mises à jour séparées du serveur et de
l'interpréteur.


Une autre raison, pour laquelle je n'installerai plus Apache, c'est la
configuration. Ici on a droit à une syntaxe claire, très peu de lignes, on crée
son serveur depuis zéro, et simplement. Créer un template est simple, et peut
se faire en quelques lignes et pour plein de langages différents. La séparation
des hôtes virtuels est simple et claire.


Donc en conclusion : utilisez Nginx, c'est bon pour la santé !
