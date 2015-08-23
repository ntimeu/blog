Title: Saitek x52 pro - Problèmes et résolutions
Date: 2015-08-23 20:08
Category: jeux
Tags: jeux, games
Slug: x52-pro-problemes-et-resolutions
Author: ntimeu

Bon, pour petite info je me suis mis à
[Elite : Dangerous](https://www.elitedangerous.com/fr). C'est un peu comme Eve
Online mais plutôt que de contrôler un vaisseai de façon "omnisciente", on le
contrôle en tant que pilote. Donc c'est plus immersif.

## Le problème

Je me suis procuré une configuration [HOTAS](https://www.elitedangerous.com/fr)
de chez Saitek (un x52 pro pour être plus précis). Reçu assez rapidement, aucun
problème, il fonctionne très bien.

Le seul petit problème vient ... Des drivers sous Windows bien sur ! Impossible
de les installer correctement, même en suivant les instructions à la lettre.

### Note

Pour installer, il faudrait :

1. ne pas brancher le HOTAS (ne le faite SURTOUT PAS AVANT)
2. lancer l'installation des drivers DEPUIS le site de Saitek (et uniquement
depuis leur site, pour être sur de ne pas avoir de bugs)
3. lorsque l'installateur vous demande de brancher le HOTAS, faites-le et
avancez pour terminer l'installation.
4. à ce moment, c'est censé marcher

### Mais en fait

Chez moi, j'ai eu de nombreux bugs, notamment l'installation qui plante au bout
de dix minutes (oui, dix minutes !), le système qui freeze dès que je branche
le HOTAS, obligé de redémarrer directement via le bouton de la tour. C'est pas
bien pratique.

## Résolution

Evidemment, lorsque vous avez une carte mère récente et avec plein de trucs
"gamers" installés dessus vous avez souvent les versions les plus avancées des
technologies (pas forcément utiles, mais bon faut bien justifier le prix ...).

Dans mon cas, le problème venait de la présence de la fonctionnalité xHCI des
connecteurs USB (2 et 3). Déjà que les forums déconseillaient l'utilisation des
ports USB3 à cause de la compatibilité matérielle, en plus la norme xHCI qui
pose problème ! Donc direction BIOS (enfin UEFI, on est sur une carte gamer
tout de même !), on vire le xHCI, on reboot et là, l'installation se passe à
merveille, le HOTAS fonctionne et tout revient dans l'ordre !

## Moralité

1. virez le xHCI (si possible)
2. ne vous branchez QUE sur de l'USB2
