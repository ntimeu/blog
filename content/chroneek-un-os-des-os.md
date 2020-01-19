---
title: "Chroneek - un os, des os"
date: 2014-10-20T22:01:00+01:00
---

Alors pour aujourd'hui, une petite explication sur comment fonctionne un
système d'exploitation, et tout celà grace à une image : "Programmer un OS,
c'est jouer avec un espace de mémoire plus ou moins grand".


Lorsque vous programmez, tout se passe en mémoire : le programme est stocké,
chargé en mémoire par le noyau et exécuté. Il s'agit donc de gérer le placement
en mémoire de plusieurs programmes, lancés ou pas.


[D'après Candy](http://forum.osdev.org/viewtopic.php?t=10099) :

> When you OSdev you do not have anything but a big space called "address
> space", filled with wastelands, potholes and quicksand (equivalent to free
> memory, nonexistant memory and device memory). You do not get ANYTHING for
> free. There are a few things you can pretty much assume nowadays (and I know
> I'm going to be attacked on this later on), there is something called IO
> space in which some devices are present, there is a PS/2 keyboard (lying
> already... I don't have a PS2 keyboard), you can use a mouse (of sorts),
> there is textual video memory from 0xB8000 and on, and your own code (512
> bytes) is present at 0x7C00.
