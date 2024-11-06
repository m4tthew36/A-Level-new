def prettyStack():
    print("top: ", top)
    print("------------")
    for i,v in enumerate(stack):
        print(i, ":", v)

def push(data):
    global top 
    
    if not top == maxSize -1: 
        top +=1 
        stack[top] = data 
    else: 
        print(data, "Couldnt be pushed, Stack Full")
    
    prettyStack()

def pop():
    global top 

    if not top ==  -1: 
        data = stack[top]
        top -= 1 
        return data




## initialise stack 
maxSize = 10
stack = ["-" for _ in range(maxSize)]
top = -1


push("pookie")
push("cat")
push("dog")

print(pop())

print(0 is not 1 and 0 is 2)