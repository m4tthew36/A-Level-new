def traverseList():
    if not start == None:
        next = start 
        while not next == None: 
            print(linkedList[next]["data"])
            next = linkedList[next]["pointer"]
                     
def find(item) -> bool :
    if not start == None:
        next = start 
        while not next == None: 
            if linkedList[next]["data"] == item: 
                return True 
            next = linkedList[next]["pointer"]
    return False 

def insert(position,item): 
    global nextFree, start 
    if position == 0:
        linkedList[nextFree]["data"] = item 
        temp = linkedList[nextFree]["pointer"]
        linkedList[nextFree]["pointer"] = start 
        start = nextFree 
        nextFree = temp      
    else: 
        next = start 
        while not next == None: 
            if (next == position -1):
                currentPointer = linkedList[next]["pointer"]
                linkedList[next]["pointer"] = nextFree  
                linkedList[nextFree]["data"] = item 
                linkedList[nextFree]["pointer"] = currentPointer
                nextFree = linkedList[nextFree]["pointer"]
                break

            next = linkedList[next]["pointer"]
    

start = 0
nextFree = 7
linkedList = [
    {"data": "Ocean", "pointer": 1},    #0
    {"data": "dog", "pointer": 2},      #1
    {"data": "cat", "pointer": 3},      #2
    {"data": "that", "pointer": 4},     #3
    {"data": "snow", "pointer": 5},     #4
    {"data": "ice", "pointer": None},   #5
    {"data": "-", "pointer": 7},        #6
    {"data": "-", "pointer": 8},     #7
    {"data": "-", "pointer": 9},     #8
    {"data": "-", "pointer": None},   #9
]

insert(0, "Pop")
insert(3, "soop")
traverseList()