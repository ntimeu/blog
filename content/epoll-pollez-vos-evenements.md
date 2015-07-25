Title: epoll - pollez vos évènements
Date: 2015-02-21 12:58
Category: programmation
Tags: programmation, c, concurrence
Slug: epoll-pollez-vos-evenements
Author: ntimeu

epoll (man 2 epoll) est un mécanisme du noyau implémenté pour écouter plusieurs
descripteurs de fichiers sans devoir boucler dessus. L'avantage, c'est que vous
pouvez n'utiliser qu'un seul processus pour traiter plein d'évènements ! Un
petit exemple de code pour la route (lit la console, mais avec des capacités
"asynchrones") :

{% include_code epve/main.c lang:c :hidefilename: main.c %}
