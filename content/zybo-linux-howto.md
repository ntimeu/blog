---
title: "Le projet sur la carte Zybo"
date: 2016-01-18T19:00:00+01:00
---

## Bon alors

Depuis cette année je travaille sur un projet orienté matériel suite à mon
entrée dans une filière orientée "embarqué" (à peu près tout ce qui tient à
l'informatique embarqué, du système d'exploitation aux logiciels qui se
lancent dessus en passant par la conception de matériel). Et pour ce projet
je dois réaliser un petit module matériel dont l'objectif est de capturer
des signaux externes, de les stocker en RAM et de pouvoir les manipuler (en
faire ce que vous voulez, vu qu'on stocke ça en RAM).

J'ai vraiment insisté pour mener ce projet car il allie hardware (partie
FPGA) et software (noyau/pilote), deux domaines que j'aime beaucoup et que
je n'avais jamais eu l'occasion de mettre ensemble. Du coup ce projet
réclame des compétences de plusieurs domaines, du design hardware (avec du
papier et du VHDL) et des compétences en programmation noyau
(majoritairement en C).

## Partie hardware

Pour la partie matérielle, la consigne est d'utiliser la plateforme
[Zybo](http://store.digilentinc.com/zybo-zynq-7000-arm-fpga-soc-trainer-board/),
une plateforme de développement axée autour de son processeur, le SoC
[Zynq 7010](https://en.wikipedia.org/wiki/Xilinx#Zynq) contenant un ARM
Cortex-A9 (double coeur), des modules annexes (Ethernet, etc) et un FPGA
à 28K cellules logiques (de quoi s'amuser, mais limite pour les design un
peu complexes). L'avantage, c'est d'avoir un accès direct au bus
[AXI](https://en.wikipedia.org/wiki/Advanced_Microcontroller_Bus_Architecture),
pour plus de performances (en effet sortir d'un SoC est très coûteux en
terme de temps). Donc si jusque-là tout va bien, c'est la suite qui se
complexifie.

## Partie software

Pour travailler l'objectif est de démarrer une distribution GNU/Linux grand
public sur les deux coeurs ARM et d'implémenter un pilote noyau qui
communique avec le module matériel développé plus haut pour lui donner des
ordres et effectuer les réservations de mémoire nécessaires à son bon
fonctionnement.

C'est à partir d'ici que les problèmes commencent :

* la documentation Digilent est assez "light" concernant la partie Linux sur
la Zybo
* le FPGA n'est pas reprogrammable "à la volée", c'est-à dire que pour reprogrammer le FPGA il est nécessaire de "hard-reset" (couper le courant,
appuyer sur le bouton de redémarrage ou encore redémarrer la carte)
* la programmation de la carte au démarrage s'effectue sur depuis un fichier
BOOT.bin, généré à la demande par les outils Xilinx, ce qui pose des
problèmes (notamment pour les personnes ne souhaitant pas installer les
outils nécessaires).
* 15 giga octets nécessaire pour installer les outils Xilinx et inscription
requise sur leur site pour pouvoir développer sur le Zynq

De même, compiler le noyau Linux pour la Zybo impose l'utilisation d'un
kernel modifié par Digilent, qui est assez ancien (on part sur du 3.18,
le noyau officiel 4.4 est déjà sorti) et ne semble pas vraiment maintenu.

Pour la partie utilisatrice, j'essaie toujours de compiler un espace
utilisateur pour la zybo mais il semblerait que ça ne marche pas beaucoup,
que ce soit avec [buildroot](https://busybox.net/) ou
[Yocto](https://www.yoctoproject.org/). J'ai réussi à lancer la partie
utilisateur en installant [un userspace
ArchARM](http://archlinuxarm.org/platforms/armv7/xilinx/zedboard)
normalement destiné à la [ZedBoard](http://zedboard.org/product/zedboard).
Ce n'est pas propre, mais ça marche sans poser de problèmes.
