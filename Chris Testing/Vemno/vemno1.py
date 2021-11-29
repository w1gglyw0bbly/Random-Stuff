import random, string

def is_username_taken(username, users):
    if username in users:
        return False
    return True

def validate_username_password(username, password, users):
    if username not in users or password not in users[username]:
        return False
    return True

def new_user(users):
    print('\nNew user')
    first_name = input('Enter first name: ')
    last_name = input('Enter last name: ')
    while True:
        username = input('Enter your username: ').lower()
        if is_username_taken(username, users) == False:
            print('Username already taken. Please choose another username.')
            continue
        password = input('Enter your password (between 6-12 characters): ')
        break
    account_number = generate_miniVenmo_account_number()
    print(f'Your random miniVenmo account number is {account_number}')
    deposit = input('Enter initial miniVenmo account balance to deposit: ')
    print(f'Account for {username} created\nPlease sign in again to start using your miniVenmo account.\n')
    users[username] = [first_name, last_name, password, account_number, deposit]

def validate_existing_user(users):
    max_chance = 3
    for x in range(max_chance):
        username = input('\nEnter username: ').lower()
        password = input('Enter password: ')
        if validate_username_password(username, password, users) == True:
            print(f'Sign in successful. Welcome {username}.\n')
            return (True, username)
        elif x == 2:
            print('Username and password do not match.\nYou tried to sign in three times. Taking you to main menu.\n')
            return (False,)
        else:
            print('Username and password do not match.') 

def validate_amount(users, username, amount):
    if int(amount) <= int(users[username][4]):
        return True
    return False

def deposit(users, username, amount):
    try:
        users[username][4] = str(int(amount) + int(users[username][4]))
        print(f'\nDeposit: ${amount}.0')
        print(f'User {username} current account balance: ${users[username][4]}.0\n')
    except:
        print('Invalid amount. Amount must be numeric.\n')

def withdraw(users, username, amount):
    if validate_amount(users, username, amount):
        users[username][4] = str(int(users[username][4]) - int(amount))
        print(f'\nWithdraw: ${amount}.0')
        print(f'User {username} current account balance: ${users[username][4]}.0\n')
    else:
        print('Invalid transaction. Insufficient balance in your account.\n')

def summary(users, username):
    print(f'\n********** {username} Account Summary **********')
    print(f'FirstName: {users[username][0]}\nLast Name: {users[username][1]}\nPassword: {users[username][2]}\nAccount Number: {users[username][3]}\nCurrent Account Balance: ${users[username][4]}.0\n')

def send_money(users, sender, receiver, amount):
    if validate_amount(users, sender, amount) and is_username_taken(receiver, users) == False:
        users[sender][4] = str(int(users[sender][4]) - int(amount))
        users[receiver][4] = str(int(amount) + int(users[receiver][4]))
        print(f'\nWithdraw: ${amount}.0')
        print(f'User {sender} current account balance: ${users[sender][4]}.0\nSent ${amount}.0 from {sender} to {receiver}.\n')
    else:
        print(f'User {receiver} does not exist.\n')
def generate_miniVenmo_account_number():
    return ''.join(random.choices(string.ascii_letters.upper() + string.digits, k = 4))
