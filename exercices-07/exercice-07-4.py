# exo 7.4
# en utilisant une boucle for, on tire 100 fois un nombre entier `r` au hasard entre 1 et 10 inclus
# affichez `r` s'il est plus petit ou égal à 5

import random

# réponse 7.4

for r in range(101):
    r = random.randint(0,10)
    if r <= 5:
        print(r)
