import sys

sys.stdin = open("familytree.in", "r")
sys.stdout = open("familytree.out", "w")

n, cow1, cow2 = input().split()
n = int(n)

mother_of = {}

for _ in range(n):
    mother, child = input().split()
    mother_of[child] = mother


def find_distance_mom(c1, c2, mom_of) -> int:
    curr = c1
    target = c2
    distance = 0
    while curr in mom_of:
         curr = mom_of[curr]
         distance = distance + 1
         if curr == target:
             return distance
    return -1

def ancestor_word_mom(distance) -> str:
    if distance == 1:
        return "MOTHER"
    elif distance == 2:
        return "GRANDMOTHER"
    else:
        return "GREAT-" * (distance-2) + "GRANDMOTHER"

def find_distance_aunt(c1, c2, mom_of) -> int:
    curr = c1
    target = c2
    distance = 0
    while curr in mom_of:
         curr = mom_of[curr]
         distance += 1
         if curr in mom_of and target in mom_of and mom_of[curr] == mom_of[target]:
             return distance
    return -1

def ancestor_word_aunt(distance) -> str:
    if distance == 1:
        return "AUNT"
    else:
        return "GREAT-" * (distance-1) + "AUNT"

def ancestors(cow):
    ancestorSet = set()
    current = cow
    while current in mother_of:
        ancestorSet.add(current)
        current = mother_of[current]
    if current not in ancestorSet:
        ancestorSet.add(current)
    return ancestorSet


def is_cousin(c1, c2, mom_of) -> bool:
    ancestor1 = ancestors(c1)
    ancestor2 = ancestors(c2)
    return bool(ancestor1 & ancestor2)


if cow1 in mother_of and cow2 in mother_of and mother_of[cow1] == mother_of[cow2]:
    print("SIBLINGS")
else:
    d = find_distance_mom(cow1, cow2, mother_of)
    if d != -1:
        print(ancestor_word_mom(d))
    else:
        da = find_distance_aunt(cow1, cow2, mother_of)
        if da != -1:
            print(ancestor_word_aunt(da))
        else:
            if is_cousin(cow1, cow2, mother_of):
                print("COUSIN")
            else:
                print("UNKNOWN")







