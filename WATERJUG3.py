from collections import deque

def jug():
    visited = set()
    q = deque([(0, 0, 8)])

    while q:
        a, b, c = q.popleft()

        if (a, b, c) == (0, 4, 4):
            print(a, b, c)
            return

        if (a, b, c) in visited:
            continue
        visited.add((a, b, c))

        q.append((max(0, a-(5-b)), min(5, b+a), c))
        q.append((max(0, a-(8-c)), b, min(8, c+a)))
        q.append((min(3, a+b), max(0, b-(3-a)), c))
        q.append((a, max(0, b-(8-c)), min(8, c+b)))
        q.append((min(3, a+c), b, max(0, c-(3-a))))
        q.append((a, min(5, b+c), max(0, c-(5-b))))

jug()
