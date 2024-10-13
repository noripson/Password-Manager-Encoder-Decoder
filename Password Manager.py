def add_passwords(username, password):
    username=input("your username :") 
    password=input("your password :")
    



while True:
    user_input = input("Enter the mode (a)=Add | (v)=View | (q)=Quit \n")
    list = ['a', 'v', 'q']
    
    if user_input == 'a':
        print("Your selected Add mode ...")
        
        
    elif user_input == 'v':
        pass
    elif user_input == 'q':
        pass
    else:
        print("Wrong... Please enter the mode (a)=Add | (v)=View | (q)=Quit \n")