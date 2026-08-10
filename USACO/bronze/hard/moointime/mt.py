"""
input 2:

17 2
momoobaaaaaqqqcqq

output 2:

3
aqq
baa
cqq

input 3:

3 1
ooo

output 3:

25
aoo
boo
coo
doo
eoo
foo
goo
hoo
ioo
joo
koo
loo
moo
noo
poo
qoo
roo
soo
too
uoo
voo
woo
xoo
yoo
zoo
"""

import sys
sys.stdin = open("mt.in", "r")
sys.stdout = open("mt.out", "w")

from collections import defaultdict, Counter
from string import ascii_lowercase

n, f = map(int, input().split())
s = list(input().strip())

count = defaultdict(int)
answer = set()

def is_moo(text):
    return text[0] != text[1] and text[1] == text[2]

# Count moos in the original string
for start in range(n - 2):
    text = "".join(s[start:start + 3])

    if is_moo(text):
        count[text] += 1

for text in count:
    if count[text] >= f:
        answer.add(text)

# Try changing one character
for pos in range(n):
    starts = []

    for start in range(pos - 2, pos + 1):
        if 0 <= start and start + 2 < n:
            starts.append(start)

    old_count = Counter()

    for start in starts:
        text = "".join(s[start:start + 3])

        if is_moo(text):
            old_count[text] += 1

    original = s[pos]

    for letter in ascii_lowercase:
        if letter == original:
            continue

        new_count = Counter()

        for start in starts:
            chars = s[start:start + 3]
            chars[pos - start] = letter
            text = "".join(chars)

            if is_moo(text):
                new_count[text] += 1

        for text in new_count:
            total = count[text] - old_count[text] + new_count[text]

            if total >= f:
                answer.add(text)

answer = sorted(answer)

print(len(answer))

for text in answer:
    print(text)

