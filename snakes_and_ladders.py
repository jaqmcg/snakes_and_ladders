import json, random
class Dice:
    '''This is a dice class'''
    def __init__(self, s = 6):
        self.sides = s

    def roll(self):
        self.diceNo = random.randrange(1, self.sides + 1)
        return self.diceNo

def rollDice():
    diceNo = game_dice.roll()
    return diceNo

def playTurn(boardPos, player):
    newPosition = 0
    diceNo = rollDice()
    intPosition = boardPos + diceNo
    if intPosition > 100:
        newPosition = boardPos
        print("Must land on exactly 100, staying where you are on", boardPos)
	
    else:
        print(player, " rolled a ", diceNo, ", and ", player, " moves to ", intPosition, sep = "")
        for i in range(len(snakes_and_ladders["boardPosition"])):
            if snakes_and_ladders["boardPosition"][i]["position"] == intPosition:
                newPosition = snakes_and_ladders["boardPosition"][i]["moveTo"]
                if snakes_and_ladders["boardPosition"][i]["position"] > snakes_and_ladders["boardPosition"][i]["moveTo"]:
                    print("Landed on a Snake and moving down to", newPosition, ". . . .")
                else:
                    print("Landed on a Ladder and moving up to", newPosition, ". . . .")
            else:
                newPosition = intPosition
        
    return newPosition

def checkWin(player, player_pos):
    if player_pos == 100:
        print("!!!!", player, "won !!!!!! End of Game")
        return True

def getUserInput():
    user_input = input("Player1: Hit enter to roll: ")
    return user_input

def playGame():
    player1_pos = 0
    computer_pos = 0
    user_input = 0
    while True:
        user_input = getUserInput()
        while user_input != "":
            user_input = getUserInput()
        player1_pos = playTurn(player1_pos, "Player1")
        won = checkWin("Player1", player1_pos)
        if won == True:
            break
        computer_pos = playTurn(computer_pos, "Computer")
        won = checkWin("Computer", computer_pos)
        if won == True:
            break
        if won != True:
            print("...")
            
if __name__ == "__main__":
    game_dice = Dice()
    s_a_l = '{"name": "snake_lader_Positions","boardPosition": [{"position": 3,"moveTo": 15},{"position": 8,"moveTo": 2},{"position": 11,"moveTo": 9},{"position": 12,"moveTo": 20},{"position": 30,"moveTo": 10},{"position": 45,"moveTo": 55},{"position": 60,"moveTo": 75}]}'
    snakes_and_ladders = json.loads(s_a_l)
    print("Welcome to Jack's game of Snakes and Ladders You are playing the computer - all the Best ")
    playGame()
    
