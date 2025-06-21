
# a1 = int(input("Enter your number: "))
# a2 = int(input("Enter your number: "))
# a3 = int(input("Enter your number: "))
# a4 = int(input("Enter your number: "))
# if(a1>a2 and a1>a3 and a1>a4):
#     print(f"a1 is the gretest number: {a1}")
# elif(a2>a1 and a2>a3 and a2>a4):
#     print(f"a2 is the gretest number: {a2}")
# elif(a3>a1 and a3>a2 and a3>a4):
#     print(f"a3 is the gretest number: {a3}")
# else:
#     print(f"a4 is the gretest number: {a4}")



# sub1 = int(input("Dear Student Plaese Enter You Maths Number: "))
# sub2 = int(input("Dear Student Plaese Enter You Science Number: "))
# sub3 = int(input("Dear Student Plaese Enter You GK Number: "))
# totalPercent = (sub1 + sub2 + sub3) / (300) * (100)
# if totalPercent < 33:
#     print("Sorry but dear you are fail your percentage is: ", str(totalPercent) + "%")
# elif totalPercent > 33 and totalPercent < 80:
#     print(
#         "Good your result is B+ grade and your total percentage is: ",
#         str(totalPercent) + "%",
#     )
# elif totalPercent > 100:
#     print("Dear please enter valid marks")
# else:
#     print(
#         "Excellent your reslt is A+ and you total percentage is: ",
#         str(totalPercent) + "%",
#     )

# p1 = "Click this"
# p2 = "Buy now"
# p3 = "Fuck"
# p4 = "Mother fucker"
# message = input("Please enter a message: ")
# if((p1 in message) or (p2 in message) or (p3 in message) or (p4 in message)):
#     print("This message is a spam")
# else:
#     print("This message is not a sapm")

name = input("Enter your name: ")
post = input("Enter a post: ")
if(name.lower() in post.lower()):
    print("Okay")
else:
    print("Not Okay")