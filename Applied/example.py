scores = [
    [10,5,2,3,5,6],
    [35, 55, 32, 66,32,52],
    [10,5,2,3,5,6],
    [35, 55, 32, 66,32,52],
]

num = int(input("Enter Student Number: "))

if num <= 10: 
    total = 0 
    for i in range(len(scores)):
        total += scores[i][num-1]

    avg = total / 4
    if total < 60: 
        print("Fail")
    else: 
        print("Pass ")