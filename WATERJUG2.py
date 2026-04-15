from collections import deque

def jug():
    visited = set()
    q = deque([(12, 0, 0)])

    while q:
        a, b, c = q.popleft()

        if (a, b, c) == (6, 6, 0):
            print(a, b, c)
            return

        if (a, b, c) in visited:
            continue
        visited.add((a, b, c))

        q.append((max(0, a-(8-b)), min(8, b+a), c))
        q.append((max(0, a-(5-c)), b, min(5, c+a)))
        q.append((min(12, a+b), max(0, b-(12-a)), c))
        q.append((a, max(0, b-(5-c)), min(5, c+b)))
        q.append((min(12, a+c), b, max(0, c-(12-a))))
        q.append((a, min(8, b+c), max(0, c-(8-b))))

jug()
