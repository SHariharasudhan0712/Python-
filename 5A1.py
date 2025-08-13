class Node:
    def __init__(self,coeff,pow):
        self.coeff =coeff
        self.pow = pow
        self.next = None
class polynomial:
    def __init__(self):
        self.head =None
    def append(self,coeff,pow):
        new_node(coeff.pow)
        if self.head is None:
           self.head=new_Node
        else:
            temp=self.head
            result=[]
            while temp:
             result.append (f,"((temp coeff)X^{temp pow}")
             temp=temp.next
             print("^",join(result))
    def addpolynomial(self,p1,p2):
        a=p1
        b=p2
        newhead=node(0,0)
        c=new.head
        while a is not None or b is not None:
            if a is None:
                c.next = b
                break
            elif a.pow == b.pow:
                 c.next =node(a.coeff+b.coeff,a.pow)
                 a=a.next
                 b=b.next
            elif a.pow>b.pow:
                 c.next.node(a,coeff,a.pow)
                 a=a.next
            else:
                c.next=node (b.coeff,b.pow)
                c=c.next
                return new.head.next
            
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
