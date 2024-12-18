import random

class Game: 
    def __init__(self, players, order) -> None:
        self.nplayers = players 
        self.order = order 



class Player:
    def __init__(self, name) -> None:
        self.name = name 
        self.score = 0 
 


player1 = Player("Theo")
player2 = Player("Ollie")
player3 = Player("Matthew")

numPlayers = 3 
scores = []


for i in range(numPlayers):
    score = 0 
    for i in range(5):
        print(i)
        score += random.randint(1,6)

    scores.append(score)


orderedScores = sorted(scores, reverse=True)
