class Node:
    def __init__(self, n, t, p):
        self.n, self.t, self.p = n, t, p
        self.l = self.r = None

class Log:
    def __init__(self): self.root = None

    def insert(self, n, t, p):
        def add(x, n, t, p):
            if not x: return Node(n, t, p)
            if n < x.n: x.l = add(x.l, n, t, p)
            elif n > x.n: x.r = add(x.r, n, t, p)
            return x
        self.root = add(self.root, n, t, p)

    def search(self, n):
        x = self.root
        while x:
            if n == x.n: return x
            x = x.l if n < x.n else x.r
        return None

    def delete(self, n):
        def min(x): return min(x, key=lambda y: y.n) if x else None
        def rem(x, n):
            if not x: return None
            if n < x.n: x.l = rem(x.l, n)
            elif n > x.n: x.r = rem(x.r, n)
            else:
                if not x.l: return x.r
                if not x.r: return x.l
                m = x.r
                while m.l: m = m.l
                x.n, x.t, x.p = m.n, m.t, m.p
                x.r = rem(x.r, m.n)
            return x
        self.root = rem(self.root, n)

    def inorder(self):
        def visit(x):
            if x:
                visit(x.l)
                print(f"{x.n} - {x.t} - {x.p}")
                visit(x.r)
        visit(self.root)

    def count(self):
        def total(x): return 0 if not x else 1 + total(x.l) + total(x.r)
        return total(self.root)

log = Log()
for n, t, p in [("Alice", "10:00", "Meeting"), ("Bob", "10:30", "Delivery"), ("Charlie", "11:00", "Interview")]:
    log.insert(n, t, p)

log.inorder()
print("Total:", log.count())
