"""
Language Detection and Translation Module
Supports English, Tamil, Hindi
"""

try:
    from googletrans import Translator
    translator = Translator()
except ImportError:
    print("googletrans not installed. Translation disabled.")
    translator = None

try:
    import langdetect
except ImportError:
    print("langdetect not installed. Language detection disabled.")
    langdetect = None

def detect_language(text):
    """
    Detect language of input text
    Returns: 'en', 'ta', 'hi', or 'unknown'
    """
    if not text or len(text) < 5:
        return 'unknown'
    
    try:
        if langdetect:
            lang = langdetect.detect(text)
            if lang in ['en', 'ta', 'hi']:
                return lang
        return 'en'  # Default to English if detection fails
    except Exception as e:
        print(f"Language detection error: {e}")
        return 'en'

def translate_to_english(text, source_lang='auto'):
    """
    Translate text to English using Google Translate
    """
    try:
        if not translator or not text:
            return text
            
        detected = detect_language(text)
        if detected == 'en' or detected == 'unknown':
            return text
        
        translated = translator.translate(text, dest='en')
        return translated['text'] if isinstance(translated, dict) else str(translated)
    except Exception as e:
        print(f"Translation error: {e}")
        return text

def get_language_name(lang_code):
    """Convert language code to name"""
    names = {'en': 'English', 'ta': 'Tamil', 'hi': 'Hindi', 'unknown': 'Unknown'}
    return names.get(lang_code, 'Unknown')
