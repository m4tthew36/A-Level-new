class Queue: 
    def __init__(self):
        self.queue = ["-" for _ in range(10)]
        self.length = 10
        self.front = -1 
        self.rear = -1 
    
    def enqueue(self, item): 
        if not (self.rear + 1) % self.length == self.front: 
            if self.front == -1: 
                self.front = 0 
            self.rear = (self.rear + 1) % self.length 
            self.queue[self.rear] = item 
        else:
            print("Queue Full!")
    
    def dequeue(self): 
        if self.front == -1: 
            return -1 
        else: 
            item = self.queue[self.front]
            if self.front == self.rear: 
                self.front = -1 
                self.rear = -1 
            else: 
                self.front = (self.front + 1) % self.length
            return item 
        
    def displayQueue(self):
        print("front: ", self.front)
        print("rear: ", self.rear)
        print("------------")
        for i,v in enumerate(self.queue):
            print(i, ":", v)

    def isFull(self):
        if (self.rear + 1) % self.length == self.front:
            return True 
        else: 
            return False 

def rebuildQueue(temp, queue, start):
    temp = [queue.dequeue() for _ in range((queue.rear-queue.front) + 1)]
    queue.enqueue(start)
    for d in temp: 
        queue.enqueue(d)


rankings = { 
    "High": ["Broken Back", "Brain Bleeding", "Heart Attack", "a"],
    "Medium": ["Cracked Skull", "Broken Leg", "Eyeball Fell Out", "b"],
    "Low": ["Broken Finger", "Cut", "c"]
}

priorityQueue = [ 
    Queue(), 
    Queue(),
    Queue()
]

tempQueue = [] 

while True: 
    option = input("(A)dd or (N)ext Patitent: ").lower()
    if option == "a": 
        injury = input("What injury does the paitent have: ").lower()
        level = ""
        for k,v in rankings.items():
            if injury in v: 
                level =  k

        if not level == "": 
            if level == "High":
                if not priorityQueue[0].isFull():
                    priorityQueue[0].enqueue(injury)
                else: 
                    rebuildQueue(tempQueue,priorityQueue[1], injury)

            elif level == "Medium":
                if not priorityQueue[1].isFull():
                    priorityQueue[1].enqueue(injury)
                else: 
                    rebuildQueue(tempQueue,priorityQueue[2], injury)

            elif level=="Low": 
                if not priorityQueue[2].isFull():
                    priorityQueue[2].enqueue(injury)
                else: 
                    rebuildQueue(tempQueue,priorityQueue[1], priorityQueue[2].dequeue())
                    priorityQueue[2].enqueue(injury)



    elif option == "n":
        priorityQueue[0].displayQueue()
        paitentFound = False
        for i in range(3):
            nextPaitent = priorityQueue[i].dequeue()
            if not nextPaitent == -1:
                print("Your Next Paitent Has: ", nextPaitent)
                paitentFound = True 
                break

        if not paitentFound: 
            print("There are no paitents watiting at the moment!")
    elif option == "s":
        priorityQueue[0].enqueue("d")
        priorityQueue[0].enqueue("injury")
        priorityQueue[0].enqueue("injury")
        priorityQueue[0].enqueue("injury")
        priorityQueue[0].displayQueue()
        rebuildQueue(tempQueue,priorityQueue[0],"Broken Leg" )
        priorityQueue[0].displayQueue()
