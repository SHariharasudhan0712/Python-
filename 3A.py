MAXSIZE = 5
stack = []
top = -1

def push(book_title):
    global top
    if top >= MAXSIZE - 1:
        print("Stack overflow: cannot push more books.")
    else:
        top += 1
        stack.append(book_title)
        print(f"Book '{book_title}' pushed onto the stack.")

def pop():
    global top
    if top == -1:
        print("Stack underflow: no books to pop.")
    else:
        removed_book = stack.pop()
        print(f"Book '{removed_book}' popped from the stack.")
        top -= 1

def peek():
    if top == -1:
        print("Stack is empty.")
    else:
        print(f"Top book on the stack: '{stack[top]}'")

def display():
    if top == -1:
        print("Stack is empty.")
    else:
        print("Books in stack (top to bottom):")
        for i in range(top, -1, -1):
            print(f"{i + 1}. {stack[i]}")

# Test the stack
push("History of India")
push("History of Japan")
push("History of China")
push("History of Veerandra Pandi")
push("History of Marvel")
push("History of DC")  # This one will cause stack overflow

display()
peek()
pop()
pop()
display()
peek()

        
