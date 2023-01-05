phonebook = {}
while True:
    user_input = input('Enter command: ')   # format command name phone
    split_input = user_input.split()
    command = split_input[0]
    if len(split_input) > 1:
        name = split_input[1]
    if len(split_input) > 2:
        phone = split_input[2]

    if command == 'add':
        if phonebook.get(name) is None:
            phonebook[name] = phone
        else:
            print(f'{name} already recorded')

    elif command == 'delete':
        del phonebook[name]

    elif command == 'show':
        for name in phonebook:
            print(name, phonebook[name])

    elif command == 'stats':
        print(len(phonebook))

    elif command == 'list':
        print(phonebook.keys())
