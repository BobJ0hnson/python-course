phonebook = {}
while True:
    user_input = input('Enter command: ')   # format command name phone
    split_input = user_input.split()
    command = split_input[0]
    name = split_input[1]
    phone = split_input[2]
    if phonebook.get(name) is None:
        if command == 'add':
            phonebook[name] = phone

        elif command == 'delete':
            del phonebook[name]

        elif command == 'show':
            for name in phonebook:
                print(name, phonebook[name])

        elif command == 'stats':
            print(len(phonebook))

        elif command == 'list':
            print(phonebook.keys())

    else:
        print(f'{name} already recorded')
