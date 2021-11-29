from vemno1 import *

def build_dict():
    with open('user_list.txt', 'r') as x:
        data = x.read().split('\n')
        users = {}
        for y in data:
            info = y.split('|')
            users[info[0]] = info[1:]
    return users

def write_to_file(users):
    with open('user_list.txt', 'w') as x:
        for i in users:
            temp = i
            for j in range(len(users[i])):
                temp += '|' + users[i][j]
            temp += '\n'
            x.write(temp)

def main():
    print('\n\n********** Welcome to miniVenmo! **********')
    users = build_dict()
    option = 0
    QUICK_TRANSFER_TO_BANK_AMOUNT = 20

    #Main menu loop
    while option != 3:
        print('Main Menu\n1. New User\n2. Existing User Sign In\n3. Exit\n')
        option = int(input('Enter option (1-3): '))
        #Main menu user options tree
        if option == 1:
            new_user(users)
        elif option == 2:
            user = validate_existing_user(users)
            if user[0]:
                while True:
                    print('Existing User Menu\n1. Add Money\n2. Transfer to bank\n3. Quick transfer to bank\n4. Send Money\n5. Account Summary\n6. Sign out')
                    submenu_option = int(input('Enter option (1-6): '))
                    if submenu_option == 1:
                        addition = input('Enter amount to add: ')
                        deposit(users, user[1], addition)
                    elif submenu_option == 2:
                        transfer = input('Enter amount to transfer to bank: ')
                        withdraw(users, user[1], transfer)
                    elif submenu_option == 3:
                        withdraw(users, user[1], 20)
                    elif submenu_option == 4:
                        receiver = input('Enter username to send money: ')
                        send = input('Enter amount to send: ')
                        send_money(users, user[1], receiver, send)
                    elif submenu_option == 5:
                        summary(users, user[1])
                    elif submenu_option == 6:
                        print('Signing out. Returning to main menu.\n')
                        break
                    else:
                        print('Invalid Option. Returning to main menu.\n')
                        break
        elif option == 3:
            print('\n********** Thanks for using miniVenmo! **********\nUpdating information to file ....')
            write_to_file(users)
        else:
            print('Invalid option! Returning to main menu.\n')

if __name__ == '__main__':
    main()
