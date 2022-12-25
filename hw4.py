
str1 = input('Enter text: ')
print(str1)
print(type(str1))
if str1.isnumeric() == True:
    int(str1)
    if str1 % 2 == 0:
        print('even')
    else: print('odd')
else: print(len(str1))
