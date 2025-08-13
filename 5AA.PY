class Node:
    def __init__(self, coeff, pow):
        self.coeff = coeff
        self.pow = pow
        self.next = None

class Polynomial:
    def __init__(self):
        self.head = None

    def append(self, coeff, pow):
        new_node = Node(coeff, pow)
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node

    def print_polynomial(self):
        temp = self.head
        result = []
        while temp:
            result.append(f"{temp.coeff}x^{temp.pow}")
            temp = temp.next
        print(" + ".join(result))

    def add_polynomial(self, p1, p2):
        a = p1.head
        b = p2.head
        new_poly = Polynomial()
        c = None

        while a is not None or b is not None:
            if a is None:
                new_poly.append(b.coeff, b.pow)
                b = b.next
            elif b is None:
                new_poly.append(a.coeff, a.pow)
                a = a.next
            elif a.pow == b.pow:
                new_poly.append(a.coeff + b.coeff, a.pow)
                a = a.next
                b = b.next
            elif a.pow > b.pow:
                new_poly.append(a.coeff, a.pow)
                a = a.next
            else:
                new_poly.append(b.coeff, b.pow)
                b = b.next

        return new_poly


poly1 = Polynomial()
poly1.append(5, 3)
poly1.append(4, 2)
poly1.append(2, 1)

poly2 = Polynomial()
poly2.append(3, 1)
poly2.append(5, 0)

print("First polynomial:")
poly1.print_polynomial()

print("Second polynomial:")
poly2.print_polynomial()

result = poly1.add_polynomial(poly1, poly2)
print("Result polynomial:")
result.print_polynomial()
