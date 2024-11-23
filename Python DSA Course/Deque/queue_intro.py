from collections import deque
import threading
import time
# Implementation of queue using list

l1=[]
l1.insert(0,"Hello")
l1.insert(0,"Hello 2")
l1.insert(0,"12321")
print(l1)
l1.pop()
print(l1)

# Implementation of queue using deque

d1 = deque()
d1.appendleft(23)
d1.appendleft(432)
d1.appendleft(32)
print(d1)
d1.pop()
print(d1)


class Queue():
    def __init__(self):
        self.container = deque()
    def enqueue(self, val):
        self.container.appendleft(val)
    def is_empty(self):
        return len(self.container)==0
    def dequeue(self):
        self.container.pop()
    def size(self):
        return len(self.container)
    def printf(self):
        return self.container

def place_order(order):
    que = Queue()
    for i in order:
        print(f"Taking order: {i}")
        que.enqueue(i)
        time.sleep(0.5)
def serve_order(order):
    que = Queue()
    for i in order:
        que.enqueue(i)
        time.sleep(2)
        print(f"Your order {i} is ready")
        
        
# pq = Queue()

# pq.enqueue({
#     'company': 'WalMart',
#     'timestamp': '15 apr, 11.01 AM',
#     'price': 131.10
# })
# pq.enqueue({
#     'company': 'Target',
#     'timestamp': '15 apr, 11.02 AM',
#     'price': 132
# })
# pq.enqueue({
#     'company': 'Costco',
#     'timestamp': '15 apr, 11.03 AM',
#     'price': 135
# })
# print(pq.printf())
# pq.dequeue()
# print(pq.printf())
orders = ['pizza','samosa','pasta','biryani','burger']
thread1 = threading.Thread(target = place_order(order = orders))
thread2 = threading.Thread(target = serve_order(order = orders))

# Start the threads
thread1.start()
time.sleep(1)
thread2.start()

# Wait for both threads to complete
thread1.join()
thread2.join()