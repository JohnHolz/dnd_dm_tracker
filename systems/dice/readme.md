## Dice System

From the dice system we will need a Roll dice function working. Like
    
    roll('1d6+2') # -> random int between 1-6 plus 2

We need too:  
1. default random mean rolls:

        10*d10+10 -> 60
        10*d6 +10 -> 45
        10*d4 +10 -> 35

2. random default value rolls:

        start_gold: 20*d8 + 20 -> 110
        human+hp: lvl*d6 + 10 -> lvl*3.5+10