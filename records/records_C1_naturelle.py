Records avec C1

Conjecture "Spivey" : pas de cycle pour 2^n et 3*(2^n) donc 2,3,4,8,12,16,24,32,48


N=2 - complete (1 distribs)
Joueur 1 : [1]
Joueur 2 : [2]
Duree pour cette partie : 1


N=3 - Taille des mains non symétrique - complete (3 distribs)
Joueur 1 : [2]
Joueur 2 : [1, 3]
Duree pour cette partie : 3


N=4 - complete (12 distribs)
Joueur 1 : [1, 3]
Joueur 2 : [4, 2]
Duree pour cette partie : 6


N=5 - Taille des mains non symétrique - complete (60 distribs)
Joueur 1 : [1, 4]
Joueur 2 : [2, 3, 5]
Duree pour cette partie : 8
2 cycles différents tous de taille 6
Nouveau Cycle de taille 6 False : (((4, 2), (3, 5, 1)), ((2, 4, 3), (5, 1)), ((4, 3), (1, 5, 2)), ((3, 4, 1), (5, 2)), ((4, 1), (2, 5, 3)), ((1, 4, 2), (5, 3)))
Nouveau Cycle de taille 6 False : (((4, 3), (2, 5, 1)), ((3, 4, 2), (5, 1)), ((4, 2), (1, 5, 3)), ((2, 4, 1), (5, 3)), ((4, 1), (3, 5, 2)), ((1, 4, 3), (5, 2)))


N=6 - complete (360 distribs)
Joueur 1 : [1, 3, 5]
Joueur 2 : [4, 6, 2]
Duree pour cette partie : 15


N=7 - Taille des mains non symétrique - complete (2520 distribs)
Joueur 1 : [3, 6, 2]
Joueur 2 : [4, 5, 1, 7]
Duree pour cette partie : 15
52 cycles différents tous de taille 8
Nouveau Cycle de taille 8 False : (((2, 7, 3), (4, 1, 6, 5)), ((7, 3), (1, 6, 5, 4, 2)), ((3, 7, 1), (6, 5, 4, 2)), ((7, 1), (5, 4, 2, 6, 3)), ((1, 7, 5), (4, 2, 6, 3)), ((7, 5), (2, 6, 3, 4, 1)), ((5, 7, 2), (6, 3, 4, 1)), ((7, 2), (3, 4, 1, 6, 5)))


N=8 - complete (20160 distribs)
Joueur 1 : [1, 4, 6, 8]
Joueur 2 : [7, 2, 5, 3]
Duree pour cette partie : 26


N=9 - Taille des mains non symétrique - complete (181440 distribs)
Joueur 1 : [1, 2, 3, 8]
Joueur 2 : [6, 5, 4, 7, 9]
Duree pour cette partie : 28
Nouveau Cycle de taille 20 False : (((9, 4, 6, 5), (3, 8, 2, 7, 1)), ((4, 6, 5, 9, 3), (8, 2, 7, 1)), ((6, 5, 9, 3), (2, 7, 1, 8, 4)), ((5, 9, 3, 6, 2), (7, 1, 8, 4)), ((9, 3, 6, 2), (1, 8, 4, 7, 5)), ((3, 6, 2, 9, 1), (8, 4, 7, 5)), ((6, 2, 9, 1), (4, 7, 5, 8, 3)), ((2, 9, 1, 6, 4), (7, 5, 8, 3)), ((9, 1, 6, 4), (5, 8, 3, 7, 2)), ((1, 6, 4, 9, 5), (8, 3, 7, 2)), ((6, 4, 9, 5), (3, 7, 2, 8, 1)), ((4, 9, 5, 6, 3), (7, 2, 8, 1)), ((9, 5, 6, 3), (2, 8, 1, 7, 4)), ((5, 6, 3, 9, 2), (8, 1, 7, 4)), ((6, 3, 9, 2), (1, 7, 4, 8, 5)), ((3, 9, 2, 6, 1), (7, 4, 8, 5)), ((9, 2, 6, 1), (4, 8, 5, 7, 3)), ((2, 6, 1, 9, 4), (8, 5, 7, 3)), ((6, 1, 9, 4), (5, 7, 3, 8, 2)), ((1, 9, 4, 6, 5), (7, 3, 8, 2)))
336 Cycles de tailles 20 et 30


N=12 - 10^7 (9mn)
Nouveau record : [3, 1, 4, 9, 12, 10] [7, 6, 11, 5, 2, 8]        Duree = 74

N=16 - 10^7 (52mn ;  10^6 en 1mn48)
Nouveau record : [3, 8, 10, 7, 16, 9, 11, 2] [4, 12, 13, 5, 6, 1, 14, 15]        Duree = 198

N=24 - 10^7 (55mn ; 10^6 en 5mn)
Nouveau record : [11, 9, 8, 23, 20, 21, 5, 1, 15, 6, 4, 13] [17, 19, 7, 12, 14, 10, 24, 16, 22, 2, 18, 3]        Duree = 576

N=32 - 10^7 (124mn ; 10^6 en 12mn)
Nouveau record : [9, 27, 24, 29, 3, 21, 6, 8, 31, 19, 7, 5, 28, 13, 22, 26] [14, 10, 1, 11, 32, 30, 20, 25, 15, 16, 12, 18, 17, 23, 4, 2]     Duree = 1302


N=48 - 10^6 (45mn)
Nouveau record : [20, 9, 45, 14, 30, 15, 36, 29, 40, 5, 39, 16, 13, 41, 27, 8, 1, 19, 48, 17, 18, 10, 3, 33] [28, 26, 24, 6, 42, 12, 43, 21, 37, 11, 22, 4, 47, 44, 7, 34, 31, 32, 25, 46, 23, 2, 35, 38]     Duree = 2790


N=64 - 10^6 (11h)
Nouveau record : [30, 31, 11, 5, 20, 61, 1, 17, 62, 28, 36, 59, 55, 23, 42, 9, 63, 58, 47, 54, 56, 38, 15, 10, 8, 3, 41, 2, 40, 51, 27, 6] [57, 50, 24, 37, 12, 48, 32, 46, 26, 29, 19, 35, 16, 22, 60, 52, 14, 53, 18, 64, 25, 45, 13, 43, 21, 34, 7, 49, 4, 33, 44, 39]          Duree = 4696


