# War Card Game - Le jeu de La Bataille

Cette page contient le code correspondant à l'article *Les défis du jeu de la bataille* de la revue [Pour La Science](https://www.pourlascience.fr/) (PLS 569 - janv 2025) et reprend les résultats de l'ancien article (*La bataille enfin analysée* [PLS215, sept 1995](https://www.cristal.univ-lille.fr/~jdelahay/pls/1995/030.pdf)).
L'ensemble de ce travail a été réalisé par les Pr Philippe Mathieu et Jean-paul Delahaye ([CRISTAL](http://www.cristal.univ-lille.fr), [SMAC team](https://www.cristal.univ-lille.fr/?rubrique27&eid=17), [Lille University](http://www.univ-lille.fr)).
<p></p>
Le jeu de la bataille, joué dans le monde entier est sans doute le plus simple des jeux de cartes. Il regorge néanmoins de nombreux mystères notamment sur les records de longueur de parties ou l'existence de cycles.
Le code ci-dessous est le code qui a permis d'établir les records cités dans l'article. Les résultats représentés sont entièrement reproductibles.
<p></p>
Existe-t-il des parties infinies à la bataille française (sans carte à l'envers) ? Nous avons trouvé en 1995 une solution positive pour 32 cartes avec rangement naturel, mais pas pour les 3 autres (32 cartes rangement optimisé, 52 cartes rangements naturel et optimisé).
C'est un vrai défi ! 

<img src="img/histo_naturelle_32cartes_10000parties.png" alt= "histo durees 32 cartes" width="46%"/> <img src="img/histo_naturelle_52cartes_10000parties.png" alt= "histo durees 52 cartes" width="46%"/>

# Principe
Le principe du jeu de Bataille : 2 joueurs jouent simultanément, chacun avec sa pile de cartes. Chacun pose une carte visible sur le tapis. La plus forte valeur l'emporte. En cas d'égalité, on recommence à jouer en empilant les cartes sur le tapis tant qu'il y a égalité. Quand l'un des deux pose une carte supérieure, il remporte l'ensemble du tas. Le jeu s'arrête quand l'un des joueurs n'a plus de carte.
<p></p>
Idéalement, en OOP, on coderait une classe `Carte(valeur, couleur)` et une classe `Joueur(main)`, mais à la bataille, la couleur ne sert qu'à indiquer combien de fois une valeur apparait. On supprime donc la classe `Carte`, et finalement aussi la classe `Joueur` puisqu'il n'y en n'a que 2. Un jeu de cartes n'est alors plus qu'un tableau d'entiers de 1 à n valeurs V, chaque entier apparaissant C couleurs fois. Par exemple avec C=4 et V=3 , les C*V cartes pourraient être [1,2,2,1,2,3,1,2,3,1,3,3]. Une partie est donc définie par 2 "mains" qui sont des tableaux d'entiers.
Le fait de ne pas avoir d'objet, non seulement simplifie le code, mais l'accélère, puisqu'il n'y a  plus d'allocations/desallocations d'objets.
<p></p>
Le programme est paramétrique : le nombre de couleurs, le nombre de valeurs, et la manière de ranger les cartes sous le paquet pour chacun des joueurs sont réglables et fournissent pour chaque valeur un nouveau problème à étudier.

# Records actuels
- [4 couleurs, rangement naturel](records_C4_naturelle.py)
- [4 couleurs, rangement optimisé](records_C4_optimisee.py)
- [1 couleur, rangement naturel](records_C1_naturelle.py)

# Biblio
- [JP Delahaye - P Mathieu. Pour la Science 215, sept 1995](https://www.cristal.univ-lille.fr/~jdelahay/pls/1995/030.pdf)
- [M Mayer - Github "Beggar my Neighbour"](https://github.com/matthewmayer/beggarmypython)
- [M Paulhus - Beggar My Neighbour. The American Mathematical Monthly, 106(2), pp162–165](https://www.tandfonline.com/doi/abs/10.1080/00029890.1999.12005024)
- [M Spivey - Cycles in war, INTEGERS 10, pp 747-764, 2010](https://www.emis.de/journals/INTEGERS/papers/kg2/kg2.pdf)
- [E Lakshtanov and V Roshchina - On Finiteness in the Card Game of War](https://arxiv.org/pdf/1007.1371)
- [Wikipedia EN](https://en.wikipedia.org/wiki/War_(card_game))
- [Wikipedia FR](https://fr.wikipedia.org/wiki/Bataille_(jeu))

# License

This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this program.
If not, see http://www.gnu.org/licenses/.
