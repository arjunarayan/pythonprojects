import sys
sys.stdin = open("backforth.in", "r")
sys.stdout = open("backforth.out", "w")

barn1 = list(map(int, input().split()))
barn2 = list(map(int, input().split()))
possible = set()

for tue in barn1:
    b1_after_tue = barn1.copy()
    b2_after_tue = barn2.copy()

    b1_after_tue.remove(tue)
    b2_after_tue.append(tue)

    for wed in b2_after_tue:
        b1_after_wed = b1_after_tue.copy()
        b2_after_wed = b2_after_tue.copy()

        b2_after_wed.remove(wed)
        b1_after_wed.append(wed)

        for thu in b1_after_wed:
            b1_after_thu = b1_after_wed.copy()
            b2_after_thu = b2_after_wed.copy()

            b1_after_thu.remove(thu)
            b2_after_thu.append(thu)

            for fri in b2_after_thu:
                final_barn1_amount = 1000 - tue + wed - thu + fri
                possible.add(final_barn1_amount)

print(len(possible))