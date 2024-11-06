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
    global rear 

    if not rear == maxSize -1 :
        rear +=1
        queue[rear] = item 
    else: 
        print("queue full")

def dequeue():
    global rear 
    global front 


    if not front == rear:
        front += 1

    return queue[front]



displayQueue()
enqueue("yes")
enqueue("item")
displayQueue()

print(dequeue())
displayQueue()