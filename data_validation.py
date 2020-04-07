# Import random
import random

# Import String
import string

def user_validation():
      # Containers for users
    users_list = []

    while True:
        # User input first name
        first_name = input('Enter your first name: ')

        # User input last name
        last_name = input('Enter your last name: ')

        # User input email
        email = input('Enter your email address: ')
        
        # Generate random string
        lettters = lettters = ''.join(random.sample(string.ascii_letters,5))
            
        # Generate password for the user
        password = first_name[0:2]+last_name[-2:]+lettters
            
        while True:
            # Show the generated password to the user and prompt whether they are satisfied or not
            user_response = input('Do you like the password ' + password + ' (y/n)? ')
            # If response is yes print user's details
            if user_response.lower() == 'y':
                user_details = {'firstname': first_name, 'lastname': last_name, 'email': email, 'password': password}
                users_list.append(user_details)
                print('Your details are First Name: {firstname}, Last Name: {lastname}, Email: {email}, Password: {password}'.format(**user_details))
                break
            # if response is no ask for new password
            elif user_response.lower() == 'n':
                while True:
                    new_password = input('Enter new password: ')
                    # If new password is less than 7 characters, prompt new password
                    if len(new_password) >= 7:
                        password = new_password
                        user_details = {'firstname': first_name, 'lastname': last_name, 'email': email, 'password': password}
                        users_list.append(user_details)
                        print('Your details are First Name: {firstname}, Last Name: {lastname}, Email: {email}, Password: {password}'.format(**user_details))
                        break    
                    # If new password is greater >= 7, print user's detail
                    elif len(new_password) < 7:
                        print('Password must be 7 characters or more')
                break
            else:
                print('Please enter (y/n)')
                
        new_response = input('Do you want to register another user (y/n)? ')
        if new_response.lower() == 'y':
            continue
        elif new_response.lower() == 'n':
            break
        else:
            break
            
    for i, user in enumerate(users_list, start=1):          
        print( 'User ' + str(i), " - ", ' First Name: {firstname}, Last Name: {lastname}, Email: {email}, Password: {password}'.format(**user))      

user_validation()