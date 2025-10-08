class Node:
    def __init__(self, k): self.key, self.left, self.right, self.h = k, None, None, 1

def h(n): return n.h if n else 0
def bf(n): return h(n.left) - h(n.right)

def rotL(z):
    y = z.right; z.right = y.left; y.left = z
    z.h = max(h(z.left), h(z.right)) + 1
    y.h = max(h(y.left), h(y.right)) + 1
    return y

def rotR(z):
    y = z.left; z.left = y.right; y.right = z
    z.h = max(h(z.left), h(z.right)) + 1
    y.h = max(h(y.left), h(y.right)) + 1
    return y

def insert(n, k):
    if not n: return Node(k)
    if k < n.key: n.left = insert(n.left, k)
    elif k > n.key: n.right = insert(n.right, k)
    else: return n
    n.h = max(h(n.left), h(n.right)) + 1
    b = bf(n)
    if b > 1 and k < n.left.key: return rotR(n)
    if b < -1 and k > n.right.key: return rotL(n)
    if b > 1 and k > n.left.key: n.left = rotL(n.left); return rotR(n)
    if b < -1 and k < n.right.key: n.right = rotR(n.right); return rotL(n)
    return n

def pre(n):
    if n: print(n.key, end=' '); pre(n.left); pre(n.right)

root = None
for k in [10, 20, 30, 40, 50, 25]: root = insert(root, k)
pre(root)
 
