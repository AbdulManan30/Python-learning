# Q1

"""
import random
def game():
    print("You are playing an game")
    score = random.randint(1, 100)
    with open('practice-question.txt') as f:
       hiscore = f.read()
    if(hiscore != ""):
        hiscore = int(hiscore)
    else:
        hiscore = 0

    if(score>hiscore):
        with open('practice-question.txt', 'w') as x:
            x.write(str(score))
    return score

print(game())
"""

# Q2
"""
for i in range(2, 21):
    with open(f"table-question/table-{i}.txt", "w") as f:
        for j in range(1, 11):
            f.write(f"{i} x {j} = {i*j}\n")
            
"""

# Q3
"""
word = "Donkey"
with open("file.txt") as f:
    content = f.read().lower()

newContent = content.replace(word.lower(), "#####")
with open("file.txt", "w") as j:
    j.write(newContent)

"""
# Q4
"""
words = ['Donkey', 'Ganda', 'Kuta', 'Fuck']
with open("file.txt") as f:
    content = f.read().lower()
    print(content)
    for word in words:
        newContent = content.replace(word.lower(), "#" * len(word))
        
    print(newContent)
with open("file.txt", "w") as j:
    j.write(newContent)
"""

# Q5
"""
with open('log.html') as f:
    content = f.read()
    if('python' in content):
        print('Yes')
    else:
        print('No')
"""

# Q6
with open("log.html") as f:
    content = f.readlines()
    lineNo = 1
    for item in content:
        if("python" in item):
            print(f"Yes Python is Present in line no: {lineNo}")
            break
        lineNo += 1
