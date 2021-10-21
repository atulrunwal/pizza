# start stop car program
while True:
    user_input = input('>').lower()
    if user_input == 'help':
        print('''   start car--->to start the car
    stop car---->to stop the car
    quit---->to exit''')
    elif user_input == 'start car':
        print('car started---->ready to go')
    elif user_input == 'stop car':
        print('car stopped')
    elif user_input == 'quit':
        break
    # if user_input != 'help' and user_input != 'start car' and user_input != 'quit' and user_input != 'stop car':
    else:
        print('sorry i cant understand this')
