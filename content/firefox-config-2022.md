---
title: "Setup Firefox de 2022"
date: 2022-02-11T23:00:00+01:00
author: "noti"
---

Reprise du blog !

# Addons

* [µBlock Origin](https://addons.mozilla.org/en-US/firefox/addon/ublock-origin/),
  toujours aussi efficace. Pensez à passer en mode avancé et à bloquer tous les
  éléments de tierce-partie
* [Smart Referer](https://addons.mozilla.org/en-US/firefox/addon/smart-referer/),
  qui ne transmet pas le referer aux sites
* [Decentraleyes](https://addons.mozilla.org/en-US/firefox/addon/decentraleyes/),
  pour limiter les accès aux CDNs
* [ClearURLs](https://addons.mozilla.org/en-US/firefox/addon/clearurls/), pour
  nettoyer les URLs (pour retirer les infos de tracking des URLs)
* [Cookie AutoDelete](https://addons.mozilla.org/en-US/firefox/addon/cookie-autodelete/)
  supprime les cookies, et peu (par exemple) supprimer les cookies d'un domaine
  dès que le dernier onglet de ce domaine est fermé

Voilà pour les addons.

# Les options de config

Toutes ces options sont à manipuler dans la page about:config de Firefox :

* browser.cache.disk.enable à false (évite d'écrire le cache sur disque)
* browser.compactmode.show à true (restore la présence de l'option compacte
  pour l'interface)
* browser.contentblocking.category à strict (blocage intégré au navigateur;
  ne sert à rien par rapport à un µBlock Origin)
* extension.pocket.enabled à false (à moins que vous l'utilisiez, retirez-le)
* privacy.firstparty.isolate à true (pour isoler les cookies par domaines)
* privacy.resistFingerprinting à true (assez explicite)

C'est déjà un bon ensemble de modifications pour améliorer la vie privée sous
Firefox !
