import nltk
from random_username.generate import generate_username
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.stem import WordNetLemmatizer
import re
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_PATH = os.path.join(BASE_DIR, "files", "financial_analysis.txt")
MAX_ATTEMPTS = 3
MIN_USERNAME_LENGTH = 4

wordLemmatizer = WordNetLemmatizer()
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
    nltk.download('wordnet')
    for resource in ("punkt_tab",):
        try:
            nltk.data.find(f"tokenizers/{resource}")
        except LookupError:
            nltk.download(resource)
            
            
            
PATTERNS = {
    "percentage": r"[+-]?\d+(\.\d+)?%",
    "currency_naira": r"N\d[\d,]*(\.\d+)?\s?(trillion|billion|million)?",
    "index_points": r"\d[\d,]*\.\d+\s?points?",
    "ticker": r"\b[A-Z]{3,10}\b",              # NGX, ASI, YTD, GTCO
    "date": r"\b(January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{1,2}",
}            

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

def sentenceSeaech(sentences):
    matched = []
    for sentence in sentences:
        if re.search(PATTERNS['date'], sentence):
            matched.append(sentence)
    return matched

def average_word_per_sentences(sentences):
    word_count = 0
    for sentence in sentences:
        word_count += len(sentence.split(" "))
    return word_count / len(sentences)

def cleansed_word_list(words):
    cleansed_words = []
    cleansed = ''
    invalid = '[^a-zA-Z+]'
    for word in words:
        cleansed = word.replace(".", "").replace(",", "").lower()
        if not re.search(invalid, cleansed) and len(word) > 1:
            cleansed_words.append(wordLemmatizer.lemmatize(cleansed))
    return cleansed_words

# User Identification
welcome()
username = callUserName()
greetUser(username)

#Download resources
ensure_nltk_data()

#Text Extraction
text_for_analysis = text_reader()


#Tokenization
tokenized_sentences =  text_tokenization(text_for_analysis)
tokenized_words = word_tokenizer(tokenized_sentences)
word_per_sentence = average_word_per_sentences(tokenized_sentences)
#print(tokenized_words)
#print(word_per_sentence)
#print(sentenceSeaech(tokenized_sentences))

#Cleansed Word list
word_list = cleansed_word_list(tokenized_words)
print(word_list)
    