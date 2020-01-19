---
title: "Le setup de dev ultime (pour ceux qui aiment comprendre)"
date: 2018-06-28T18:00:00+01:00
---

Si vous voulez tester des trucs sous ArchLinux tout en les isolant bien du
reste de votre environnement, vous avez plusieurs solutions :

* LXC, très pratique mais avec un peu de config
* Docker, si vous aimez utiliser l'espace disque et utiliser des containers non
  vérifiés (vous sentez le sarcasme au moins ?)
* systemd-nspawn, qui fait un peu tout

L'exemple typique, c'est avec PHP : on a besoin de PHP, d'un serveur web, d'un
serveur de BDD et parfois d'autres trucs. Si on installe tout ça sur notre
environnement courant, ça va nécessiter de garder la trace de ce qui a été
installé, de ce qui a été ajouté manuellement, quelle configuration, etc. Et
une machine virtuelle, c'est lourd, ça nécessite de pré-allouer une certaine
quantité de mémoire au démarrage, ça nécessite un disque virtuel, etc. Donc non
merci pour ces deux solutions.

J'ai déjà fait du LXC, mais s'il faut le reconfigure à chaque changement de
machine, c'est la galère. Côté Docker, je n'ai pas tellement envie de
l'utiliser, vu que les containers que l'on peut installer sont fait par
n'importe qui et ne sont pas vérifiés (genre les mineurs de cryptomonnaies
installés discrètement).

Du coup pour tester différents trucs (notamment des framework pour le web)
sans impacter ma config actuelle (et surtout pour ne pas avoir à ajouter de
services au démarrage, etc), j'ai commencé à utiliser systemd-nspawn.


## Debootstrap + nspawn

Premièrement, on va utiliser debootstrap, qui permet d'installer la base
minimale de Debian (sans kernel, juste les utilitaires). Sous ArchLinux, vous
devez installer les paquets *debootstrap* et *debian-archive-keyring* (si vous
n'installez pas le trousseau de clés, la vérification des paquets ne marchera
pas et debootstrap n'installera rien).

{{< highlight bash >}}
sudo pacman -S debootstrap debian-archive-keyring
{{< / highlight >}}


Une fois l'installation des deux paquets terminée, vous pouvez créer un nouveau
container :

{{< highlight bash >}}
sudo debootstrap stable myContainer http://ftp.fr.debian.org/debian/
{{< / highlight >}}


Laissez debootstrap faire son boulot, et à la fin, faites :

{{< highlight bash >}}
sudo systemd-nspawn -UD myContainer
{{< / highlight >}}


* l'option -U permet de lancer un conteneur non privilégié (pour plus de sécu),
  c'est-à dire qu'un utilisateur différent de root sera utilisé pour
  représenter les utilisateurs à l'intérieur du conteneur
* l'option -D permet de spécifier le répertoire à utiliser


Une fois à l'intérieur du conteneur, donnez un mot de passe au compte root :

{{< highlight bash >}}
passwd
{{< / highlight >}}


Sortez du conteneur (Ctrl-d ou *exit*). A partir de ce moment, vous pourrez
démarrer votre conteneur de cette façon :

{{< highlight bash >}}
sudo systemd-nspawn -bUD myContainer
{{< / highlight >}}


La console va vous montrer des traces de boot (mais comme il n'y a pas de
noyau, c'est instantanné), et vous placera dans un vrai shell, sur lequel vous
pourrez vous logguer avec l'utilisateur de votre choix. Evidemment, vous pouvez
utiliser *machinectl* pour démarrer automatiquement vos conteneurs, vous y
connecter, etc.

Si vous voulez utiliser sudo à l'intérieur du conteneur, vous aurez une erreur,
donc pensez à modifier votre /etc/hosts en ajoutant le nom de votre machine
(vu que le conteneur partage le réseau avec l'hôte, ça cause quelques soucis) :

{{< highlight text >}}
127.0.0.1 localhost <votre hostname>
{{< / highlight >}}


Et c'est bon, votre conteneur est terminé ! Plus qu'à tout casser à l'intérieur
! Un simple rm suffira pour nettoyer le conteneur sans rien toucher d'autre.
