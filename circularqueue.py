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


enqueue("it")
displayQueue()