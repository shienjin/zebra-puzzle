import itertools
import time

"""
1.  There are five houses.
2.  The Englishman lives in the red house.
3.  The Spaniard owns the dog.
4.  Coffee is drunk in the green house.
5.  The Ukrainian drinks tea.
6.  The green house is immediately to the right of the ivory house.
7.  The Old Gold smoker owns snails.
8.  Kools are smoked in the yellow house.
9.  Milk is drunk in the middle house.
10. The Norwegian lives in the first house.
11. The man who smokes Chesterfields lives in the house next to the man with the fox.
12. Kools are smoked in the house next to the house where the horse is kept.
13. The Lucky Strike smoker drinks orange juice.
14. The Japanese smokes Parliaments.
15. The Norwegian lives next to the blue house.

Now, who drinks water? Who owns the zebra?
"""


def immediate_right(h1, h2):
    return h1-h2 == 1


def next_to(h1, h2):
    return abs(h1-h2) == 1

houses = [first, _, middle, _, _] = [1, 2, 3, 4, 5]  # 1

orderings = list(itertools.permutations(houses, 5))

# Englishman, Spaniard, Ukrainian, Norwegian, Japanese
# red, green, ivory, yellow, blue
# Coffee, tea, Milk, oj, water
# dog, snails, fox, horse, zebra
# OldGold, Kools, Chesterfields, LuckyStrike, Parliaments
g = ((red, green, ivory, yellow, blue,
      Englishman, Spaniard, Ukrainian, Norwegian, Japanese,
      Coffee, tea, Milk, oj, water,
      dog, snails, fox, horse, zebra,
      OldGold, Kools, Chesterfields, LuckyStrike, Parliaments
      )
     for (red, green, ivory, yellow, blue) in orderings
     if immediate_right(green, ivory)  # 6
     for (Englishman, Spaniard, Ukrainian, Norwegian, Japanese) in orderings
     if Englishman == red  # 2
     if next_to(Norwegian, blue)  # 15
     if Norwegian == first  # 10
     for (Coffee, tea, Milk, oj, water) in orderings
     if Coffee == green  # 4
     if Ukrainian == tea  # 5
     if Milk == middle  # 9
     for (dog, snails, fox, horse, zebra) in orderings
     if Spaniard == dog  # 3
     for (OldGold, Kools, Chesterfields, LuckyStrike, Parliaments) in orderings
     if OldGold == snails  # 7
     if Kools == yellow  # 8
     if next_to(Chesterfields, fox)  # 11
     if next_to(Kools, horse)  # 12
     if LuckyStrike == oj  # 13
     if Japanese == Parliaments  # 14
     )

# start = time.time()
# print next(g)
# end = time.time()
# print 'Time:', end - start

(red, green, ivory, yellow, blue,
 Englishman, Spaniard, Ukrainian, Norwegian, Japanese,
 Coffee, tea, Milk, oj, water,
 dog, snails, fox, horse, zebra,
 OldGold, Kools, Chesterfields, LuckyStrike, Parliaments
 ) = next(g)

colors = dict(zip(['red', 'green', 'ivory', 'yellow', 'blue'],
                  [red, green, ivory, yellow, blue]))
nationalities = dict(zip(['Englishman', 'Spaniard', 'Ukrainian', 'Norwegian', 'Japanese'],
                         [Englishman, Spaniard, Ukrainian, Norwegian, Japanese, ]))
drinks = dict(zip(['Coffee', 'tea', 'Milk', 'oj', 'water'],
                  [Coffee, tea, Milk, oj, water]))
animals = dict(zip(['dog', 'snails', 'fox', 'horse', 'zebra'],
                   [dog, snails, fox, horse, zebra]))
smokes = dict(zip(['OldGold', 'Kools', 'Chesterfields', 'LuckyStrike', 'Parliaments'],
                  [OldGold, Kools, Chesterfields, LuckyStrike, Parliaments]))

for property_group in [colors, nationalities, drinks, animals, smokes]:
    print sorted(property_group.items(), key=lambda (p, h): h)
