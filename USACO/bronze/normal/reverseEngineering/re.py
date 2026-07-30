import sys
sys.stdin = open("re.in", "r")
sys.stdout = open("re.out", "w")
data = sys.stdin.read().split()
idx = 0

t = int(data[idx])
idx += 1

for _ in range(t):
    n = int(data[idx])
    m = int(data[idx + 1])
    idx += 2

    examples = []

    for _ in range(m):
        s = data[idx]
        result = data[idx + 1]
        idx += 2
        examples.append([s, result])

    changed = True

    while changed:
        changed = False

        for bit in range(n):
            for value in ["0", "1"]:
                outputs_seen = set()

                for s, result in examples:
                    if s[bit] == value:
                        outputs_seen.add(result)

                if len(outputs_seen) == 1:
                    new_examples = []

                    for s, result in examples:
                        if s[bit] != value:
                            new_examples.append([s, result])

                    examples = new_examples
                    changed = True

    if len(examples) == 0:
        print("OK")
    else:
        print("LIE")