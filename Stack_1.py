class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)
        print(f"Pushed: {item}")

    def pop(self):
        if self.is_empty():
            print("Stack is empty. Cannot pop.")
            return None
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            print("Stack is empty. Nothing to peek.")
            return None
        return self.items[-1]

    def size(self):
        return len(self.items)

    def display(self):
        print("Stack (top to bottom):", self.items[::-1])


# Example usage:
if __name__ == "__main__":
    stack = Stack()

    stack.push(1)
    stack.push(2)
    stack.push(3)

    stack.display()

    print("Popped:", stack.pop())
    stack.display()

    print("Peek:", stack.peek())
    print("Size of stack:", stack.size())

    stack.pop()
    stack.pop()
    stack.pop()  # This will show an error message since the stack is empty
