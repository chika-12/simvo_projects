from random_username.generate import generate_username
def welcome():
    print("Welcome to the text analysis tool")


def callUserName():
    maxAttempt = 3
    attempt = 0
    while attempt < maxAttempt:
        
        inputPrompt = ""
        if attempt == 0:
            inputPrompt = "\n To begin enter username\n"
        else:
            inputPrompt = "\n Please try again\n"
        username = input(inputPrompt)
        
        if len(username) > 4 and  username.isidentifier():
            return username
        attempt += 1
    
    print("The username you choosed is invalid a new username has been Assigned to you")
    username = generate_username()[0]
    
    
    return username

def greetUser(name):
    print("Hello ", name)
    
def text_reader():
    text = open("./files/financial_analysis.txt")
    out_put_text = text.read()
    text.close()
    return out_put_text.replace('\n', '').replace('\r', '')

welcome()
username = callUserName()
greetUser(username)
text_for_analysis = text_reader()
print(text_for_analysis)
