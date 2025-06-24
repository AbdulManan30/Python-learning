# Create a snake water gun Game
# To generate a random number
import random
computerNum = random.choice([1, 2, 3])
yourNum = int(input("Please Enter Your Number: 1 for Snake, 2 for Water, 3 for Gun: ")) 
dictForNumber = {
    1: 'Snake',
    2: "Water",
    3: "Gun"
}
you = dictForNumber[yourNum]
comp = dictForNumber[computerNum]
if(comp == you):
    print(f"Draw Computer choice is also {comp}")
else:
    # First method
    
    # if(comp == "Snake" and you == "Water"):
    #     print(f"You Lose! you chose {you} and Computer chose {comp}")
    # elif(comp == "Water" and you == "Gun"):
    #     print(f"You Lose! you chose {you} and Computer chose {comp}")
    # elif(comp == "Gun" and you == "Snake"):
    #     print(f"You Lose! you chose {you} and Computer chose {comp}")
    # elif(comp == "Water" and you == "Snake"): #1
    #     print(f"You Win! you chose {you} and Computer chose {comp}")
    # elif(comp == "Gun" and you == "Water"): #1
    #     print(f"You Win! you chose {you} and Computer chose {comp}")
    # elif(comp == "Snake" and you == "gun"): #-2
    #     print(f"You Win! you chose {you} and Computer chose {comp}")
    
    # Second Method
    
    if(computerNum - yourNum == 1 or computerNum - yourNum == -2):
        print(f"You Win! you chose {you} and Computer chose {comp}")
    else:
        print(f"You Lose! you chose {you} and Computer chose {comp}")
    