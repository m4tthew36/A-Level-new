import os 

maxSize = 10
queue = ["-" for _ in range(10)]

front = -1 
rear = -1

def displayQueue():
    print("front: ", front)
    print("rear: ", rear)
    print("------------")
    for i,v in enumerate(queue):
        print(i, ":", v)


def enqueue(item):
    global front, rear 
    if not (rear + 1) % maxSize == front: 
        if front == -1: 
            front = 0 
        rear = (rear + 1) % maxSize 
        queue[rear] = item 
    else: 
        print("Queue Full")

def dequeue():
    global rear 
    global front 

    if front == -1: 
        return -1 
    else: 
        item = queue[front]
        if front == rear: 
            front = -1 
            rear = -1 
        else: 
            front = (front + 1 ) % maxSize 
        return item 

    
while True: 

    method = input("E or D: ").lower()
    os.system("clear")
    if method == "e": 
        data = input("Enter item to put into queue ")
        enqueue(data)
    elif method == "d": 
        data = dequeue()
        print(data)

    displayQueue()


