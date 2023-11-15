# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# This program takes scores from the user and uses them to determine if the Celts or Suns won.

# Inputs for the celts scores

print('Please enter how many 1 point shots the Celtics made.')

celtics_score = int(input())

print('Please enter how many 2 point shots the Celtics made.')

celtics_score2 = int(input())

print('Please enter how many 3 point shots the Celtics made.')

celtics_score3 = int(input())

# Input for the Suns scores

print('Please enter how many 1 point shots the Suns made.')

suns_score = int(input())

print('Please enter how many 2 point shots the Suns made.')

suns_score2 = int(input())

print('Please enter how many 3 point shots the Suns made.')

suns_score3 = int(input())

# this calculates the Celtics total score
celtics_total = celtics_score + (celtics_score2 * 2) + (celtics_score3 * 3)
print('The Celtics total score is: ', celtics_total)

# this calculates the Suns total score
suns_total = suns_score + (suns_score2 * 2) + (suns_score3 * 3)
print('The Suns total score is: ', suns_total)

# this evaulates which team is the winner by seeing who has the bigger score
if celtics_total > suns_total:
    print('With a score of: ' + str(celtics_total) + '. The Celtics win!')
elif celtics_total < suns_total:
    print('With a score of: ' + str(suns_total) + '. The Suns win!')
else:
    print('Somehow the teams managed to draw.')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
