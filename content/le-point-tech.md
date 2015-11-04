Title: Le point tech
Date: 2015-11-04 16:00
Categories: programmation
Tags: Linux, programmation
Slug: le-point-tech
Author: ntimeu

Bon après quelques temps passés sans activité sur le blog, retour sur les
petites améliorations technologiques qui sont apparues récemment.

### OpenBSD 5.8

OpenBSD 5.8 est sorti le 18 octobre 2015 (en lieu et place du combo 1^er mai
- 1^er octobre) pour fêter le 20^ème anniversaire du code source du noyau.
Au menu, plus de hardware supporté (support des instructions AVX sur les
processeurs x86, support de plusieurs nouveaux trackpads dans le driver
[wscons(4)](http://www.openbsd.org/cgi-bin/man.cgi?query=wscons&sec=4)), des
améliorations dans le système d'installation (et dans les paramètre par
défaut), des grosses améliorations dans les démons réseau comme
[bgp(8)](http://www.openbsd.org/cgi-bin/man.cgi?query=bgpd&sektion=8) ou
[ospf(8)](http://www.openbsd.org/cgi-bin/man.cgi?query=ospfd&sektion=8),
l'appel système [tame(2)](http://www.openbsd.org/cgi-bin/man.cgi?query=tame&sektion=2&manpath=OpenBSD-5.8)
est désormais supporté par OpenBSD, et également des améliorations un peu
partout, comme sur [OpenSMTPD](https://www.opensmtpd.org/),
[httpd(8)](http://www.openbsd.org/cgi-bin/man.cgi?query=httpd&sektion=8) et
OpenSSH.


### Fedora 23

Je me suis mis à utiliser Fedora 22 dans le cadre des projets à réaliser à
l'école, notamment pour installer des outils de développement pour FPGA.
C'est un système très stable, qui dispose de nombreux outils et paquets un
peu plus à jour que le Debian de base.

La sécurité n'est pas en reste, avec notamment l'intégration de SELinux en
mode "enforcing" (pour rappel, le mode enforcing bloque les accès non
autorisés et en plus ajoute une entrée aux logs, tandis que le mode
"permissive" (très souvent activé car la configuration de SELinux est assez
compliquée). C'est une très bonne pratique, et je vous encourage à lire le
site [Stop Disabling SELinux](http://stopdisablingselinux.com/) (en passant
merci à [Sebsauvage](http://sebsauvage.net/links/?jZVyyQ) pour le lien).


### Debian 8 (aka jessie)

Il marche toujours très bien, le gestionnaire de réseau ne me pose pas de
problèmes cette fois-ci (je me demande comment ont-ils fait pour avoir un
gestionnaire de connexions aussi bien intégré que le leur), par contre j'ai
finit par compiler GHC (le compilateur Haskell) dans sa dernière version à
la main, sinon la version était trop ancienne pour certains projets (on
parlera notamment de hakyll qui avait un problème de dépendances au moment
de la compilation).


### Programmation et travail

J'utilise de plus en plus git, que ce soit pour ce blog, pour les projets
ou encore pour les documents que je rédige pratiquement uniquement en LaTeX
depuis septembre (que ce soient les rapports, articles ou encore
présentations). J'aime beaucoup plus travailler sur mes documents en LaTeX
car on ne se préoccupe pas de la présentation au départ et le texte est
généré de façon claire. Et puis rédiger un document sous Vim, pouvoir le
versionner sous Git, que c'est reposant !

Concernant Git je ne peux plus m'en passer, des fichiers de configuration
aux fichiers de code en passant par les documents LaTeX, tout est versionné
ce qui est très pratique et m'a sauvé la vie un bon paquet de fois (modifier
un code puis revenir en arrière en cas de bêtises).

### Shaarli

L'appli [shaarli](http://links.ntimeu.fr/) fonctionne assez bien, avec plus
de 100 liens postés sur l'appli. Ca tiens bien, ça ne plante pas et le code
semble assez stable (malgré le fait qu'il soit en pré-release depuis
lontemps).
