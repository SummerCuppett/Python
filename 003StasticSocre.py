# Corrected functions

def averagescore(examinescores):
    averageScore = sum(examinescores.values()) / len(examinescores)
    return averageScore

def sortedscore(examinescores):
    scorelist = [(k, v) for k, v in examinescores.items()]
    sortlist = sorted(scorelist, key=lambda x: x[1], reverse=True)
    return sortlist

def maxscore(examinescores):
    list = sortedscore(examinescores)
    maxscore = list[0]
    return maxscore

def minscore(examinescores):
    list = sortedscore(examinescores)
    minscore = list[-1]  # -1 accesses the last element
    return minscore

# Corrected dictionary
examinescores = {
    "TIM": 98,
    "TOM": 92,
    "TIGER": 95,
    "TAN": 97,
    "JERRY": 89,
    "SUMMER": 99,
    "SPRINT": 79,
    "WEN": 85,
    "TID": 89
}

# Using the functions
sor = sortedscore(examinescores)
print("List of the scores:", sor)

ave = averagescore(examinescores)
print("The average score is:", ave)

scholarlord = maxscore(examinescores)
print("Scholarlord is:", scholarlord)

studyslacker = minscore(examinescores)
print("Study slacker is:", studyslacker)
