---
title: "Setup Firefox efficace de 2018"
date: 2018-06-28T18:30:00+01:00
---

Oui, je reste sous Firefox, je n'irais pas sous Chrome ou autres.


# Addons

* *µBlock Origin/µMatrix* : indispensables. Les deux sont configurés en mode
  "whitelist" uniquement (ils n'autorisent que les sites configurés
  explicitement). Mon préféré reste µMatrix de par sa configurabilité (ça se
  dit ?) et sa légèreté, mais µBlock reste le plus efficace (grace à ses
  filtres). Pas la peine d'installer les deux, un seul suffit.

Pour µBlock, le plus simple est de passer en mode avancé, puis de mettre dans
le rouge la colonne de gauche pour tous les third-parties. Dans cette même
colonne, mettez en gris les images, first-party script et les scripts inline.

Activez tous les filtres, mais pour les filtres régionnaux n'activez que ceux
de votre région, et n'utilisez pas les filtres expérimentaux (jamais eu
l'utilité).

* *HTTPs Everywhere* : indispensable. Le mettre en HTTPs only casse pas mal de
  sites encore aujourd'hui, mais on peut vivre avec (et le désactiver à la
  demande)

* *Multi-Account Containers* : (presque) indispensable. Permet d'isoler les
  cookies de navigation. Vous pouvez donc vous logguer sur deux gmails dans le
  même navigateur, ou utiliser gmail tout en étant non loggué sur le moteur de
  recherche ou sur gmaps

* *Smart Referer* : indispensable. Modifie le referer (le header http qui indique
  votre provenance à chaque requête HTTP) selon le domaine courant. A
  configurer en mode strict, et configurer la règle de réécriture pour ne rien
  envoyer

* *Grammalecte* : (in)dispensable. Je l'ai, mais je ne m'en sers que très rarement
  (ben oui, je ne bloggue pas souvent ^^). C'est un super outil pour corriger
  des textes (français uniquement).

C'est tout. Vu que ces extensions sont des WebExtensions, c'est léger, ça va
vite, ne nécessitent pas de redémarrage, sont simples et efficaces.


# Customisation de l'interface

* retour avant/arrière
* barre de navigation
* téléchargements (clic gauche sur l'icône > cacher automatiquement)
* les icônes des extensions


Sur i3 (mon gestionnaire de fenêtres), ma config est un peu particulière : pas
de bordures, pas de titres de fenêtres, donc si je retire (dans Firefox) la
bare de titre, ça déplace les onglets vers la droite, donc on peut laisser la
barre de titre (de toute façon elle est cachée par i3).

Mettez le thème dark (plus agréable, notamment le soir ou dans des endroits mal
éclairés), et passez en densité compacte (plus de place gagnée !!).


# Options

* on peut utiliser les polices Noto (évite le tofu)
* virer le spelling, passer la langue en anglais (pour éviter les sites mal
  traduits)
* ne pas lire les fichiers DRM-isés
* ne pas mettre à jour les moteurs de recherche
* changez votre moteur de recherche (genre par n'importe quoi de moins
  intrusif, Duckduckgo ou Qwant)
* bloquez toutes les permissions par défaut
* n'envoyez rien à Mozilla, et retirez SPECIFIQUEMENT les run studies (des
  expérimentations qui sont ajoutées de temps à autres), désolé
  Mozilla, mais vu comment vous gérez vos studies (oui, la pub dans le
  navigateur pour Mr Robot, par exemple), je m'en passe volontiers


# Certificats SSL

Si vous vous sentez suffisamment à l'aise, vous pouvez faire un tour dans les
certificats, et ôter la confiance à pas loin de 50% des certificats installés.
Evitez tout de même de virer les certificats de Let's Encrypt (je ne
suis pas fan du service, mais bon un paquet de sites l'utilise).
