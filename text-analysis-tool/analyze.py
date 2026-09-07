"""
Text analysis tool
"""
import nltk # type: ignore
from random_username.generate import generate_username # type: ignore
from nltk.tokenize import word_tokenize, sent_tokenize # type: ignore
from nltk.stem import WordNetLemmatizer # type: ignore
from nltk.corpus import wordnet, stopwords # type: ignore
import re
import os
from wordcloud import WordCloud # type: ignore
import matplotlib.pyplot as plt # type: ignore
from nltk.sentiment.vader import SentimentIntensityAnalyzer #type: ignore
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_PATH = os.path.join(BASE_DIR, "files", "financial_analysis.txt")
MAX_ATTEMPTS = 3
MIN_USERNAME_LENGTH = 4
wordLemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words('english'))
sentiment_analyzer = SentimentIntensityAnalyzer()


#Welcomes the user
def welcome():
    print("Welcome to the text analysis tool")

#Accepts user name and ensures that user name  is a valid name 
def callUserName():
    """
        Accepts user name and returns valid user name
    Returns:
        Valid user name
    """
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

#Greets the user by name
def greetUser(name):
    print("Hello ", name)
    

#Downloads nltk packages
def ensure_nltk_data():
    #nltk.download('wordnet')
    #nltk.download('averaged_perceptron_tagger_eng')
    #nltk.download('stopwords')
    #nltk.download('vader_lexicon')
    for resource in ("punkt_tab",):
        try:
            nltk.data.find(f"tokenizers/{resource}")
        except LookupError:
            nltk.download(resource)
            

#Regex pattern            
PATTERNS = {
    "percentage": r"[+-]?\d+(\.\d+)?%",
    "currency_naira": r"N\d[\d,]*(\.\d+)?\s?(trillion|billion|million)?",
    "index_points": r"\d[\d,]*\.\d+\s?points?",
    "ticker": r"\b[A-Z]{3,10}\b",              # NGX, ASI, YTD, GTCO
    "date": r"\b(January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{1,2}",
}            

#Convert part os speech from pos function to wordnet compatible
pos_tagges = {
    "J":wordnet.ADJ,
    "N":wordnet.NOUN,
    "V":wordnet.VERB,
    "R":wordnet.ADV
}
def pos_tag_analyzer(pos_tags):
    first_char = pos_tags[0]
    if first_char in pos_tagges:
        return pos_tagges[first_char]
    return wordnet.NOUN

#Text file reader
def text_reader(path=FILE_PATH):
    out_put_text = ""
    try:
        with open(path) as text:
            out_put_text = text.read()
    except FileNotFoundError:
        print(f"{path} not found")
    return out_put_text.replace('\n', '').replace('\r', '')

#Sentence analysis function
def text_tokenization(text):
    return sent_tokenize(text)

#Word analysis function
def word_tokenizer(sentences):
    words = []
    for sentence in sentences:
        words.extend(word_tokenize(sentence))
    return words

#Stock sentence searchb base on regex
def sentenceSeaech(sentences):
    matched = []
    for sentence in sentences:
        if re.search(PATTERNS['date'], sentence):
            matched.append(sentence)
    return matched

#Average word persentence search
def average_word_per_sentences(sentences):
    word_count = 0
    for sentence in sentences:
        word_count += len(sentence.split(" "))
    return word_count / len(sentences)

#Cleased data function
def cleansed_word_list(words_tuples_list):
    cleansed_words = []
    cleansed = ''
    invalid = '[^a-zA-Z+]'
    for word_tuple in words_tuples_list:
        word = word_tuple[0]
        pos = word_tuple[1]
        cleansed = word.replace(".", "").replace(",", "").lower()
        if not re.search(invalid, cleansed) and len(word) > 1 and cleansed not in stop_words:
            cleansed_words.append(wordLemmatizer.lemmatize(cleansed, pos_tag_analyzer(pos)))
    return cleansed_words


# User Identification
welcome()
username = callUserName()
greetUser(username)

#Download resources
#ensure_nltk_data()

#Text Extraction
text_for_analysis = text_reader()


#Tokenization
tokenized_sentences =  text_tokenization(text_for_analysis)
tokenized_words = word_tokenizer(tokenized_sentences)
word_per_sentence = average_word_per_sentences(tokenized_sentences)
#print(tokenized_words)
#print(word_per_sentence)
#print(sentenceSeaech(tokenized_sentences))

#create list word tuples for data wrangling
wordsPosTagged = nltk.pos_tag(tokenized_words)

#Cleansed Word list
word_list = cleansed_word_list(wordsPosTagged)
#print(word_list)

cleaned_text = " ".join(word_list)
wordcloud = WordCloud(
    width=800,
    height=400,
    random_state=1,
    background_color="white",
    colormap="Pastel2",
    collocations=False
).generate(cleaned_text)

wordcloud.to_file('result/wordcloud.png')
sentiment_score = sentiment_analyzer.polarity_scores(text_for_analysis)
print(sentiment_score)


#print(wordsPosTagged)
    