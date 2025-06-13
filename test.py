username = 'J3t4x'
password = '489736520'
enter_chances = 3
print('Enter the username:')
name = input()
if name == username:
    print('Enter the password:')
    while enter_chances > 0:
        password = input()
        if password == '489736520':
            print('Wellcome back J3t4x!')
            break
        else:
            enter_chances -= 1
            print('wrong password, please try again, you still have ' + str(enter_chances) + ' chances:')
            if enter_chances == 0:
                print('System closed, you have to wait 3mins to try again later.')
                break
else:
    print('Sorry, system closed.')

