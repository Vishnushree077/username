user={'ram':'1234','ravi':'4567','vijay':'6789'}
while True:
    username=input('enter the username:')
    password=input('enter the password:')
    space=password.strip()
    if user[username]==space:
        print('logedin')
        break
    else:
        print('invalid username or password')
