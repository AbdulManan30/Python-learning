# Lambda
# square = lambda x: x*x
# print(square(5))
sum = lambda x, y: x + y + x
print(sum(2, 3))

# Join method
lis = ["Manan", "Rohan", "Noman"]
res = ":::".join(lis)  # it will join like this Manan:::Rohan:::Noman

# Formate method in Python
# result = "{} is a handsome {}".format("Manan", "Boy")
result = "{1} is a handsome {0}".format("Manan", "Boy")
