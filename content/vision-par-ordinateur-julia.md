---
title: "Vision, apprentissage machine via Julia & Flux"
date: 2022-02-12T18:30:00+01:00
author: "noti"
---

Aujourd'hui, on va faire un petit peu d'apprentissage machine, tout en
découvrant un nouveau langage : [Julia](https://julialang.org/).
C'est un langage qui se veut aussi simple que python, tout en étant compilé à
la demande (compilation en Juste à Temps ou JIT pour les anglophones). On va
également découvrir [Flux.jl](https://fluxml.ai/), l'une des bibliothèques que
j'ai découvertes et qui me semble extrêmement bien conçue.


# Julia

[Julia](https://julialang.org/), c'est un langage "scientifique" (en tout cas
quand on regarde son site officiel, c'est ce qui saute aux yeux).
C'est en quelque sorte un python, mais en mieux :

* compilé à la volée (JIT) via LLVM
* système de types déduis ou forcés par le développeur
* code natif
* utilisable en ligne de commande (REPL) ou comme un programme complet
* gestionnaire de paquets intégré, un peu comme le module venv de python

À l'utilisation, le langage est vraiment intéressant, même si la documentation
est quelque peu lourde et pas si simple à comprendre.


# Flux

Flux est l'une des bibliothèques d'apprentissage machine disponible pour Julia.
Son fonctionnement est assez intéressant :

* plutôt que de définir des types de données customisés, on va exploiter
  directement les capacités de Julia (par exemple, on utilise des matrices
  Julia, pas de types de données optimisés pour certains usages)
* une API simple d'accès (si vous avez déjà fait un peu de ML et déjà utilisé
  un autre outil, comme PyTorch)

Ayant utilisé de façon assez extensive PyTorch (à l'occasion j'essaierais de
trouver du temps pour écrire un article), j'ai découvert par hasard Julia
et Flux, qui proposent une API assez similaire à PyTorch tout en ayant une
écriture aussi simple et utilisable que du python.


# Vision par ordinateur, machine learning

Je n'ai pas la prétention d'être une référence dans le domaine du machine
learning, et n'ayant pas le temps/l'envie, je ne vais pas expliquer comment ça
marche, ni pourquoi ça marche.

Si le machine learning vous intéresse, les vidéos de
[DeepLearning.AI](https://www.deeplearning.ai/) sont disponibles sur YouTube
(je vous laisse regarder).

# C'est parti !

On commence simplement. On a besoin de trois choses :

1. julia (ben oui), installé simplement (soit via le site officiel, soit via
   votre package manager; attention sous ArchLinux il faut julia-bin, sinon il
   y aura des problèmes de compilation)
2. un ensemble de données. Pour cet exercice, on va utiliser
   [FashionMNIST](https://github.com/zalandoresearch/fashion-mnist), via le
   paquet [MLDatasets.jl](https://github.com/JuliaML/MLDatasets.jl).
3. du temps et de la patience

Les images de FashionMNIST permettent d'entraîner un réseau capable de classer
des images de vêtements en 10 classes différentes :

* t-shirt
* pantalon
* pull over
* robe
* manteau
* sandale
* chemise
* basket
* sac
* bottine

## On commence simplement

Tout va se passer dans un fichier, que je vais appeler simple.jl.

{{< highlight julia >}}
import Pkg

Pkg.add([
	Pkg.PackageSpec(name="Flux", version="0.12.9"),
	Pkg.PackageSpec(name="MLDatasets", version="0.5.15")
])

import Flux
import MLDatasets: FashionMNIST
{{< /highlight >}}

Ici, on commence par vérifier que Flux.jl et MLDatasets.jl aient été bien
installés par le gestionnaire de paquet.

## Création du modèle

{{< highlight julia >}}

model = Flux.Chain(
	Flux.DepthwiseConv((3, 3), 1 => 64, Flux.leakyrelu; pad=1),
	Flux.MaxPool((2, 2)),
	Flux.flatten,
	Flux.Dense(14^2 * 64, 512, Flux.leakyrelu),
	Flux.Dropout(5e-1),
	Flux.Dense(512, 512, Flux.leakyrelu),
	Flux.Dropout(5e-1),
	Flux.Dense(512, 10)
)

{{< /highlight >}}

Ce modèle est assez simple :


0. en entrée, on attend une matrice de 28x28x1
1. un niveau de convolution (même s'il s'appelle DepthwiseConv, c'est une
   convolution) de 3x3, qui sort une matrice de 28x28x64 (grâce au "padding" de
   un pixel ajouté tout autour de l'entrée)
2. un "moyenneur", qui travaille sur des blocs de 2x2 pixels. Ce qui divise la
   taille de la matrice par deux (uniquement sur les deux premières dimensions)
3. on "aplatit" la matrice, passant de 14x14x64 à un vecteur de 12544x1
4. on passe ensuite de 12544 à 512 via un niveau de neurones
5. un niveau de "dropout" (qui va mettre les valeurs à zéro selon une
   probabilité)
6. un niveau de neurones, sortant toujours 512 valeurs
7. encore un niveau de "dropout"
8. le dernier niveau de neurones, qui sort 10 valeurs (correspondant aux
   labels de notre image)


## Chargement des images

Pour simplifier l'entraînement, on va regrouper les images en groupes de 64 (ou
par 10, 20, 30, voir pas du tout). L'avantage étant qu'en s'entraînant sur un
ensemble d'images, on va aller moins vite, mais beaucoup plus vite qu'en
s'entraînant image par image (l'idée étant d'utiliser l'erreur moyenne plutôt
que l'erreur sur chaque calcul).

{{< highlight julia >}}

x_train = Flux.unsqueeze(FashionMNIST.traintensor(Float32, 1:60000), 3)
y_train = Flux.onehotbatch(FashionMNIST.trainlabels(1:60000), 0:9)
train_loader = Flux.DataLoader(
	(x_train, y_train);
	batchsize=64,
	shuffle=true,
	partial=true
)

{{< /highlight >}}

La variable x_train va contenir les images dans une matrice de 28x28x1x60000,
y_train une matrice de 10x60000 (y_train contient les valeurs attendues en
sortie de réseau).

Je mélange (shuffle) les ensembles de 64 images histoire de
ne jamais avoir les mêmes suites de données, et j'autorise les ensembles
partiels (si à la fin on a moins de 64 images dans un ensemble, on autorise le
calcul sur moins d'images).

On pourrait d'ailleurs aller plus loin, en modifiant les images chargées pour
leur ajouter du bruit (par exemple une petite rotation, un renversement, etc)
pour augmenter la difficulté d'apprentissage, mais également permettre au
réseau de mieux apprendre les concepts derrière les images.


## Fonction de perte (loss), optimiseur

La fonction de perte (loss) va permettre de calculer la différence entre
l'attendu et le calculé. C'est cette fonction qui va nous dire à quel point le
réseau apprend bien ou non.

Ici, on est sur un réseau calculant la classe d'une entrée, donc il va falloir
utiliser la fonction logitcrossentropy de Flux (il existe plein de méthodes de
calcul de pertes, pour classer des entrées celle-ci est conseillée).

L'optimiseur va servir à moduler la perte pour ajuster le réseau. Dans mon cas,
je vais utiliser l'algorithme ADAM, qui semble avoir un bon niveau de
performances par rapport aux autres (par exemple le gradient).

{{< highlight julia >}}

loss(ŷ, y) = Flux.Losses.logitcrossentropy(ŷ, y)
opt = Flux.Optimise.ADAM(1e-3)

{{< /highlight >}}


## Entraînement


{{< highlight julia >}}

parameters = Flux.params(model)

for (X, y) in train_loader
	grads = Flux.gradient(parameters) do
		loss(model(X), y)
	end

	Flux.Optimise.update!(optimizer, parameters, grads)
end

{{< /highlight >}}

On commence par extraire les paramètres du réseau, puis on itère sur les
différents batchs d'images, qu'on fait passer dans le réseau. Puis on calcule la
perte entre le calculé et l'attendu, et on met à jours les paramètres du réseau
grâce à la perte et à l'optimiseur.

Honnêtement le fonctionnement de cette étape est assez complexe (et je ne
prétends pas le comprendre complètement moi-même), donc je passe aujourd'hui.


## Vérification des résultats

Dernière étape : on vérifie que le réseau apprenne bien ! On charge un autre
ensemble d'images (ne **JAMAIS** tester le réseau sur un ensemble d'images
qu'il a déjà rencontré, il risque de passer pour meilleur qu'il ne l'est).

{{< highlight julia >}}

total_loss = 0.0
correct_guesses = 0

for (X, y) in test_loader
	ŷ = model(X)

	total_loss += loss(ŷ, y)
	correct_guesses += reduce(+, Flux.onecold(ŷ) .== Flux.onecold(y))
end

num_images = size(test_loader.data[1], 3)
num_batches = ceil(UInt64, num_images / test_loader.batchsize)

println("loss: ", loss / num_batches,
		", accuracy: ", correct_guesses, "/", num_images)

{{< /highlight >}}


## On recommence ?

Le réseau a atteint un certain niveau (perte moyenne et précision). Pourquoi ne
pas recommencer à nouveau ?

{{< highlight julia >}}

for epoch in 1:10
	<insérer ici le code des deux étapes précédentes>
end

{{< /highlight >}}


# Conclusion

Le code est disponible sur github :
[SimpleCNN.jl](https://github.com/ntimeu/SimpleCNN.jl) !

Aujourd'hui, le code est un peu plus complexe et mieux organisé, notamment
grâce à une séparation claire en fonctions, une petite barre de
progression pour rajouter de l'interactivité (car sur CPU l'entraînement peut
être assez long).

Il est également possible, si vous avez un GPU NVidia, de déplacer les calculs
sur votre carte graphique. Cela nécessite quelques modifications, mais le code
reste relativement équivalent à ce qu'on a vu.

Par contre, ayant testé PyTorch, je suis assez déçu niveau performances : je
m'attendais à ce que le code soit plus performant, mais au final PyTorch est
bien plus rapide (avec le même réseau, même convolution, etc). La bibliothèque
Torch (avec laquelle PyTorch interagit) est bien plus optimisée. En même temps,
on parle d'une bibliothèque conçue et développée par Facebook.
