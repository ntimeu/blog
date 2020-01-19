---
title: "Joystick Saitek, quand ça veut pas ..."
date: 2017-03-05T22:00:00+01:00
---

1. désactiver l'xHCI dans l'UEFI de la carte mère
2. installer les drivers pour le HOTAS
3. brancher le HOTAS
4. lancer l'éditeur de profil

    * aller dans l'onglet programmation
    * passer en vue grille
    * spprimer toutes les colonnes (sauf la première)
    * déprogrammer tous les boutons

5. Lancez le gestionnaire de profils (qui devrait se lancer dans la barre
    des tâches)

    * clic droit sur l'icône -> configuration
    * onglet MFD
    * décocher la case "enable Clutch mode"
