maxSize = 10
array = ["-" for _ in range(10)]

front = -1 
rear = -1

def displayQueue():
    print("front: ", front)
    print("rear: ", rear)
    print("------------")
    for i,v in enumerate(stack):
        print(i, ":", v)