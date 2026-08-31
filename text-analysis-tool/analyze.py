from random_username.generate import generate_username
def welcome():
    print("Welcome to the text analysis tool")

def callUserName():
    username = input("Enter your username: ")
    
    if len(username) > 4 and  username.isidentifier():
        return username
    
    print("The username you choosed is invalid a new username has been Assigned to you")
    username = generate_username()[0]
    
    
    return username

def greetUser(name):
    print("Hello ", name)
    
    
welcome()
username = callUserName()
greetUser(username)
