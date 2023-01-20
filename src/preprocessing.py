import re

punctuations = r'''!()-[]{};:'"\,<>./?@#$%^&*_~'''

url_patterns = r'https?://\S+|www\.\S+'

html_patterns = r'<.*?>'

def remove_from(text:str, pattern:str) -> str:
    return re.sub(pattern, '', text)

def remove_whitespaces(text:str) -> str:
    return re.sub(r'\s+', ' ', text).strip()

def remove_punctuations(text:str) -> str:
    
    return ''.join([letter for letter in text if letter not in punctuations])

def remove_stopwords(text:str) -> str:
    stopwords = [word.strip() for word in open("utils/stopwords.txt", 'r')]
    
    return ' '.join([word for word in text.split() if word not in stopwords])

def text_preprocessing(text:str) -> str:
    text = text.lower()
    
    text = remove_from(text, url_patterns)
    text = remove_from(text, html_patterns)
    text = remove_punctuations(text)
    
    text = remove_stopwords(text)
    
    text = remove_whitespaces(text)
    
    return text