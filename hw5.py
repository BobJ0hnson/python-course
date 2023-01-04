str1 = input('Enter text: ')
for s in str1:
    if s.isnumeric() == True:
        if int(s) % 2 == 0:
            print('even')
        else:
            print('odd')
    elif s.isalpha() == True:
            if s.isupper() == True:
                print('Capital')
            else:
                    print('lower')
    else:
        print('Symbol')

### infinite while loop ###

from time import sleep
while true:
print('I love python')
sleep(4.2)
