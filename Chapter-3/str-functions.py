# Some String Functions
a = "Manan"
print(len(a)) # lenght of string
print(a.endswith('an')) # check if string ends with 'an'
print(a.startswith('Ma')) # check if string starts with 'Ma'
print(a.lower()) # convert string to lower case
print(a.upper()) # convert string to upper case
print(a.capitalize()) # convert first character to upper case and rest to lower case
print(a.replace('a', 'A')) # replace 'a' with 'A'
print(a.split('a')) # split string at 'a'
print(a.join('koki')) # join string with 'koki'
print(a.count('a')) # count number of 'a' in string
print(a.find('a')) # find index of first 'a' in string
print(a.rfind('a')) # find index of last 'a' in string
print(a.index('a')) # find index of first 'a' in string
print(a.rindex('a')) # find index of last 'a' in string
print(a.isalpha()) # check if string contains only alphabets
print(a.isdigit()) # check if string contains only digits
print(a.isalnum()) # check if string contains only alphabets and digits

# escape sequence
print("Hello \n World") # print new line
print("Hello \t World") # print tab
print("Hello \\ World") # print backslash
print("Hello \b World") # print backspace
print("Hello World ")