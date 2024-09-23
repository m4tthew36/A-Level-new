health = 100 

def takeDamage(ammount): 
    global health 
    if (health - ammount) >= 0: 
        health =- ammount 
    else: 
        health = 0 

def takePotion(health, ammount): 
    if not (health + ammount) > 100: 
        return health + ammount 
    else: 
        return 100 
    

takeDamage(30)
health = takePotion(health, 20)

print(health)