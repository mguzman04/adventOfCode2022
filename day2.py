#### Part 1 solution

# # dict of shapes to point
# shapePoints = {
#     "X" : 1, # rock
#     "Y" : 2, # paper
#     "Z" : 3  # scissors
# }

# # dict to translate
# translation = {
#     "A" : "rock",
#     "B" : "paper",
#     "C" : "scissors",
#     "X" : "rock",
#     "Y" : "paper",
#     "Z" : "scissors"
# }

# totalScore = 0
# # read in file
# with open('input2.txt', 'r') as f:
#     # insert here
#     choices = []
#     for line in f:
#         # remove whitespaces and make into array
#         choices = line.strip().split()
#         opponent = choices[0]
#         player = choices[1]
#         # tie
#         if (translation[player] == translation[opponent]):
#             totalScore += 3 + shapePoints[player]
#         # winning scenario 
#         elif ( (translation[player] == "rock" and translation[opponent] == "scissors") or 
#             (translation[player] == "paper" and translation[opponent] == "rock") or
#             (translation[player] == "scissors" and translation[opponent] == "paper")):
#             totalScore += 6 + shapePoints[player]
#         # loss
#         else :
#             totalScore += shapePoints[player]

# print(totalScore)

#### Part 2 Solution

shapePoints = {
    'A' : 1, # rock
    'B' : 2, # paper
    'C' : 3  # scissors
}

# what opponent picks : what player picks to win
winChoice = {
    'A' : 'B',
    'B' : 'C',
    'C' : 'A'
}

loseChoice = {
    'A' : 'C',
    'B' : 'A',
    'C' : 'B'
}


totalScore = 0
with open('input2.txt', 'r') as f:
    choices = []
    for line in f:
        choices = line.strip().split()
        opponent = choices[0]
        result = choices[1]
        # Draw
        if (result == 'Y'):
            totalScore += 3 + shapePoints[opponent]
        # win scenario
        elif (result == 'Z') :
            totalScore += 6 + shapePoints[winChoice[opponent]]
        # lose scenario
        else:
            totalScore += shapePoints[loseChoice[opponent]]

print(totalScore)