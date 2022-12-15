
# dict of shapes to point
shapePoints = {
    "X" : 1, # rock
    "Y" : 2, # paper
    "Z" : 3  # scissors
}

# dict to translate
translation = {
    "A" : "rock",
    "B" : "paper",
    "C" : "scissors",
    "X" : "rock",
    "Y" : "paper",
    "Z" : "scissors"
}

totalScore = 0
# read in file
with open('input2.txt', 'r') as f:
    # insert here
    choices = []
    for line in f:
        # remove whitespaces and make into array
        choices = line.strip().split()
        opponent = choices[0]
        player = choices[1]
        # tie
        if (translation[player] == translation[opponent]):
            totalScore += 3 + shapePoints[player]
        # winning scenario 
        elif ( (translation[player] == "rock" and translation[opponent] == "scissors") or 
            (translation[player] == "paper" and translation[opponent] == "rock") or
            (translation[player] == "scissors" and translation[opponent] == "paper")):
            totalScore += 6 + shapePoints[player]
        # loss
        else :
            totalScore += shapePoints[player]

print(totalScore)

