import random
# user input
def get_guess():
    return list(input("your guess: "))

#gererate num
def gen_num():
    digits = [str(num) for num in range (10)]
    random.shuffle(digits)
    return digits[:3]

#generate clues
def clues(code,user_guess):
    
    if user_guess==code:
        return "Code Cracked!"
    
    clue = []
    
    for ind,num in enumerate(user_guess):
        if num == code[ind]:
            clue.append("Match")
        elif num in code:
            clue.append("Close")

    if clue == []:
        return ["Nope"]
    else:
        return clue
    
#game logic
print ("Welcome to Guess Game!!")

secret_num = gen_num()

clue_report = []

while clue_report != "Code Cracked!":
    guess = get_guess()
    
    clue_report = clues(guess,secret_num)
    print("Result of ur Guess: ")
    for clue in clue_report:
        print(clue)

