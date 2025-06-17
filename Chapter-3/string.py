# there are 3 ways to write a string
a = 'Manan'
b = "Manan"
c = '''Manan'''
# Slice Start
print(a[0: 3]) # slice method in python
print(a[-3: 0])
print(a[0: 3]) # agr mujhe koy negative slice deta hu to mujhe sirf usko reciprocal karn he like this
print(a[:3]) # it means it starts from 0 index to 3 index but except 3 index
print(a[3:]) # it means it starts from 3 index to string lenght -1
# slice with skip value
x = "abcdefghijklmnopqrstuvwxyz" # first ye [0:10] wala operation karega jiska output hoga abcdefghij iske baad wo 3 values ko skip karke result dega is case mein iska result aaiga adgj
print(x[0:10:3])
# Slice End