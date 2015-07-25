Title: Unbound - libérez votre DNS !
Date: 2015-04-07 20:28
Tags: sécurité, projets, bricolage, chroneek
Slug: unbound-liberez-votre-dns
Author: ntimeu


[Unbound](https://unbound.net/) est un DNS résolveur qui permet d'interroger la
base de données des noms de domaines (et oui, car le DNS est en fait une
gigantesque base de données clé-valeur, à l'échelle d'Internet). Son objectif
est de répondre aux requêtes de clients (votre PC, Firefox, ...), tout en
mettant en cache pour accélérer les réponses aux autres clients.


Donc si vous souhaitez mettre en place (pour vous) Unbound, c'est très simple !
Un exemple pour ArchLinux :

{% include_code ulvd/install-archlinux.sh lang:sh %}

Dans le fichier /etc/unbound/unbound.conf, il vous suffit d'ajouter (ou de
modifier) la ligne suivante (limite les connexions à la boucle locale pour plus
de sécurité) :

{% include_code ulvd/unbound.conf lang:conf :hidefilename: unbound.conf %}

Ces réglages ne suffisent pas si vous utiliser DHCPCD. Vous devez indiquer à
dhcpcd de ne pas changer le fichier /et/resolv.conf, et donc il suffit d'éditer
/etc/dhcpcd.conf et d'ajouter à la fin :

{% include_code ulvd/dhcpcd.conf lang:conf :hidefilename: dhcpcd.conf %}

Pour finir, il suffit de ne laisser dans /etc/resolv.conf que :

{% include_code ulvd/resolv.conf lang:conf :hidefilename: resolv.conf %}

Un petit redémarrage et tout fonctionne !

### Et tout ça pour quoi ?
Changer de DNS ne sers pas fondamentalement, mais permet (parfois) d'améliorer :

* le temps de réponse (visuel) de l'application
* la latence de vos logiciels
* parfois, les FAI ne mettent pas en place un serveur très performant pour
répondre à de nombreuses requêtes. Les changer peut grandement améliorer votre
temps de réponse


Malheureusement, si chacun utilisait ce type de montage, les DNS racine ne
tiendraient pas la charge (il s'agit des DNS de premier niveau, je vous
conseille de regarder wikipédia pour avoir plus d'informations). Donc il existe
plusieurs DNS résolveurs qui sont fournis par des entreprises/associations et
qui mutualisent les requêtes. Plusieurs résolveurs sont fournis publiquements,
comme OpenNIC (46.105.212.15) ou encore OpenDNS (208.67.222.222 et
208.67.220.220).

### Et comme toujours ...

Lisez la page manuel d'Unbound (man
[unbound.conf(5)](https://unbound.net/documentation/unbound.conf.html)) pour
bien comprendre et configurer le logiciel !
