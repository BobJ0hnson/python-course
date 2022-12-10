
str1 = input('Enter text: ')
print(str1)
print(type(str1))
if type(str1) == int or type(str1) == float:
    if str1%2==0:
        print('even')
    else: print('odd')
elif type(str1) == str:
    print(len(str1))