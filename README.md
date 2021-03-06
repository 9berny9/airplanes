# Airplanes Algoritmus

## Úkol
Napište algoritmus v jazyce Python, který zajistí, aby počet pasažérů, kteří přistanou byl maximální. 
Preferované řešení je bez využití modulů (numpy, math a další).

## Popis problému
Máme řadu letadel s různým počtem pasažérů. Například 4 letadla s následujícími počty pasažérů [155, 54, 3, 10]. 
Pokud letadla přistávají bezprostředně po sobě, způsobuje to turbolence a celý proces přistávání se stává nebezpečným. 
Z tohoto důvodu je zakázáno, aby přistály za sebou následující letadla. 
Každé letadlo může přistát maximálně 1.

Využijeme-li naivní způsob přistávání, tj. přistává každé druhé letadlo, dopravíme 158 pasažérů (155 + 3). 
Ašak existuje lepší kombinace [155, 10], kde přistane o 7 pasažérů více.

[155, 55, 2, 96, 67, 203, 3] 
- naive -> 155 + 2 + 67 + 3 = 227
- best -> 155 + 96 + 203 = 454

## Data
- index 0: pole s pasazery
- index 1: spravny vysledek

test_cases = [  
    ( [155, 55, 2, 96, 67, 203, 3], 454 ),  
    ( [155, 54, 3, 10], 165 ),  
    ( [12, 43, 10, 8, 90, 123, 5, 3, 56], 230 ),  
    ( [1, 10, 200, 154, 160, 289, 454, 5, 10, 34], 849 ),  
    ( [347, 440, 342, 297, 104, 118, 119, 268, 218], 1130 ),  
    ( [463,  73, 282, 422, 271, 118, 112], 1128 )  
]