# for i in range(1,20):
#     print(i)
    
# for i in range(1,20,2):
#     print(i)

# we can iterate list, tuple, string, set, and also dict
# l = [1,2,3,4,5,6, "Manan"]

# for item in l:
#     print(item)
    
# for i in range(len(l)): # we can also use like this
#     print(l[i])

# s = "Manan"
# for item in s:
#     print(item)

# For loop with else
# for i in range(1,10):
#     print(i)
# else:
#     print("done")

# For loop with dict
# d = {
#     'name': "manan",
#     "caste": "Pirzado",
#     'income': 1000000
# }
# for i in d:
#     print(f" {i} : {d[i]}") # we can also use like this d.get(i) or d[i

# breake, continue, pass

# for x in range(1,20):
#     if(x==5):
#         break # exit from the loop imeditaly
#     print(x)
    
# continue
for x in range(1,20):
    if(x==5):
        continue # skip this iteration and continue
    print(x)
    
for z in range(1,20):
    pass # it means it hold the loop when i am working an other work