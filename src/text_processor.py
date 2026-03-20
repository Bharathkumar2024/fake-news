"""
Text Processing and Cleaning Module
"""

import re

try:
    import nltk
    from nltk.corpus import stopwords
    
    # Download required NLTK data
    try:
        nltk.data.find('corpora/stopwords')
    except LookupError:
        nltk.download('stopwords', quiet=True)
    
    stop_words = set(stopwords.words("english"))
except ImportError:
    print("⚠️  NLTK not installed. Using basic stopword removal.")
    stop_words = {'the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for', 'is', 'are', 'was', 'were', 'be', 'been', 'have', 'has', 'had', 'do', 'does', 'did'}

def clean_text(text):
    """
    Clean text by:
    1. Converting to lowercase
    2. Removing URLs
    3. Removing special characters
    4. Removing extra whitespace
    5. Removing stopwords
    """
    try:
        # Convert to lowercase
        text = text.lower()
        
        # Remove URLs
        text = re.sub(r'http\S+|www\S+|https\S+', '', text, flags=re.MULTILINE)
        
        # Remove email addresses
        text = re.sub(r'\S+@\S+', '', text)
        
        # Remove special characters and digits, keep only letters and spaces
        text = re.sub(r'[^a-zA-Z\s]', '', text)
        
        # Remove extra whitespace
        text = re.sub(r'\s+', ' ', text).strip()
        
        # Remove stopwords
        words = text.split()
        words = [w for w in words if w not in stop_words and len(w) > 2]
        
        return " ".join(words)
    except Exception as e:
        print(f"⚠️  Text cleaning error: {e}")
        return text

def preprocess_text(text):
    """
    Complete preprocessing pipeline
    """
    cleaned = clean_text(text)
    return cleaned
