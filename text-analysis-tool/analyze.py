import nltk
from random_username.generate import generate_username
from nltk.tokenize import word_tokenize, sent_tokenize
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_PATH = os.path.join(BASE_DIR, "files", "financial_analysis.txt")
MAX_ATTEMPTS = 3
MIN_USERNAME_LENGTH = 4
def welcome():
    print("Welcome to the text analysis tool")


def callUserName():
    attempt = 0
    while attempt < MAX_ATTEMPTS:
        
        input_prompt = ""
        if attempt == 0:
            input_prompt = "\n To begin enter username\n"
        else:
            input_prompt = "\n Please try again\n"
        username = input(input_prompt)
        
        if len(username) > MIN_USERNAME_LENGTH  and  username.isidentifier():
            return username
        attempt += 1
    
    print("The username you choosed is invalid a new username has been Assigned to you")
    username = generate_username()[0]
    
    
    return username

def greetUser(name):
    print("Hello ", name)
    

def ensure_nltk_data():
    for resource in ("punkt_tab",):
        try:
            nltk.data.find(f"tokenizers/{resource}")
        except LookupError:
            nltk.download(resource)
            
def text_reader(path=FILE_PATH):
    out_put_text = ""
    try:
        with open(path) as text:
            out_put_text = text.read()
    except FileNotFoundError:
        print(f"{path} not found")
    return out_put_text.replace('\n', '').replace('\r', '')

def text_tokenization(text):
    return sent_tokenize(text)

def word_tokenizer(sentences):
    words = []
    for sentence in sentences:
        words.extend(word_tokenize(sentence))
    return words
# User Identification
welcome()
username = callUserName()
greetUser(username)
#Text Extraction
text_for_analysis = text_reader()
#print(text_for_analysis)
#Tokenization
#ensure_nltk_data()
tokenized_sentences =  text_tokenization(text_for_analysis)
tokenized_words = word_tokenizer(tokenized_sentences)
print(tokenized_words)

    