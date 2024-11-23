# Same functionality as Ctrl+Z or the abck button apps and websites
# push/pop -> O(1)
# we use deque to implement stack and queues in python as list are not that efficient to implement them

from collections import deque

d1 = deque()
print(dir(d1))
d1.append("Hello I'm")
d1.append("Dexter")
d1.append("Morgan")
print(d1)
print(len(d1))
for i in range(len(d1)):
    print(d1[i])
d1.pop()
print(d1) # works for directly but when creating a class, create a printf function otherwise it will simpy return addresss of stack

# Implementation using array

class Stack:
    def __init__(self):
        self.container = deque()
    def push(self, val):
        self.container.append(val)
    def pop(self):
        self.container.pop()
    def peek(self):
        return self.container[-1]
    def printf(self):
        return self.container
    def is_empty(self):
        return len(self.container)==0
    def size(self):
        return len(self.container)
    def reverse(self, str1):
        stack = Stack()
        res = ''
        for s in str1:
            stack.push(s)
        for i in range(len(str1)):
            res+=stack.peek()
            stack.pop()
        return res
    
    # is_balanced("({a+b})")     --> True
    # is_balanced("))((a+b}{")   --> False
    # is_balanced("((a+b))")     --> True
    # is_balanced("))")          --> False
    # is_balanced("[a+b]*(x+2y)*{gg+kk}") --> True
    
    
    def is_balance(self, brackets):
        stack = Stack()
        brak = {'{':'}', '(':')', '[':']'}
        if brackets[0] not in brak:
            return False
        for s in brackets:
            if s in brak:
                stack.push(s)
            elif s in brak.values():
                if stack.is_empty:
                    return False
                if s == brak[stack.peek()]:
                    stack.pop()
        return stack.is_empty()

stak = Stack()
stak.push(54)
stak.push(43)
stak.push(12)
stak.push(67)
print(stak.printf())
stak.pop()
print(stak.printf())
print(stak.peek())
print(stak.size())
print(stak.is_empty())
print(stak.reverse("We will conquere COVID-19"))
print(stak.is_balance("())((a+b}{"))