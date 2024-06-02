# s24004
#おみくじプログラム

import random

kuji = ["大吉","中吉","小吉","凶"]

print(random.choice(kuji))


def getKuji():
    luck = random.choice(kuji)
    print(luck)
    return luck
