---
title: "Chroneek Firefox - gros nettoyage de printemps"
date: 2016-04-11T18:30:00+01:00
---

Petit article sur la configuration de mon Firefox préféré. En trois mots :
sécurité, vie privée et simplicité !

* [HTTPS-Everywhere](https://www.eff.org/https-everywhere), développé par
l'[EFF](https://www.eff.org/), qui passe automatiquement les sites connus
vers sa version sécurisée (HTTPS). C'est léger et j'oublie presque qu'il
est en tâche de fond
* [Privacy Badger](https://www.eff.org/privacybadger), là aussi un outil de
l'EFF qui permet (par domaine) de bloquer la connexion ou d'autoriser la
connexion (en bloquant ou non les cookies). C'est très efficace, mais
nécessite un peu de travail au début pour configurer les listes de blocage
* [uBlock Origin](https://github.com/gorhill/uBlock), conçu par le
développeur [Raymond
Hill](https://addons.mozilla.org/fr/firefox/user/gorhill/). Excellent sur
tous les points, j'utilise la plupart des filtres généraux ainsi que les
filtres par région EU et FRA
* et c'est tout

L'avantage de cette configuration, c'est qu'elle est très légère, sans
fioritures et impacte très peu le CPU. De plus, les petites choses
douteuses qui passent au travers de Privacy Badger sont immédiatement
bloquées par uBlock, ce qui offre une bonne petite protection.


### Et les plugins ?

Et non, ça fait longtemps que les plugins Flash/Java/autres sont supprimés.
Je ne les utilise plus (beaucoup de sites sont en HTML5 maintenant), ils
sont trop responsables de brèches de sécurité et sont trop lourds (en plus
d'être bourrés de DRM). Donc poubelle pour ces plugins (cette règle est
"system-wide" => donc pas installés du tout sur mes machines).


### Et pour le streaming ?

Pour ceux qui (comme moi) aiment regarder d'autres personnes jouer en
direct, c'est assez compliqué. La plateforme de référence (ou plutôt celle
avec le plus grand nombre de "streams"), [Twitch](https://www.twitch.tv/),
utilise encore un lecteur écrit en Flash. Donc impossible de regarder un
direct dans Firefox ! Résultat, soit on change de plateforme (regardez du
côté de [Hitbox](http://www.hitbox.tv/), ils sont 100% HTML5), soit on
utilise des outils externes au navigateur, avec notre meilleur ami VLC et
l'outil python [Livestramer](http://docs.livestreamer.io/) (qui envoie le
flux vidéo directement dans VLC). Donc légèreté et fluidité (et le décodage
matériel de VLC en prime !).


### Et niveau distribution ?

Pour ne pas changer, je suis repassé sous ArchLinux pour avoir les derniers
paquets à jour. En plus, cette fois j'ai correctement configuré mon
environnement de travail (j'utilise notamment un combo i3 +
NetworkManager + [Redshift](http://jonls.dk/redshift/)). NM gère le réseau
tout seul (mieux que mon ancienne configuration Netctl), avec le switch
automatique; i3 pour la partie bureau, contrôlable au clavier uniquement;
et enfin redshift pour moduler l'affichage de la lumière bleue en fonction
de l'heure.


### En parlant de Redshift

Vous devriez jeter un oeuil à cet outil, qui réduit la lumière bleue (qui
vous "empêche" de vous endormir car le cerveau pense être en plein jour et
fait en sorte de rester éveillé). C'est libre et gratuit, et c'est toujours
mieux que sa version propriétaire, f.lux.

Pour Android, il semblerait que [Red
Moon](https://github.com/raatmarien/red-moon) soit un équivalent à
Redshift, mais avec une interface simplifiée et surtout sous licence libre
(MIT). Je viens de l'installer donc je n'ai pas vraiment de retours, si ce
n'est que l'application est très pratique.
