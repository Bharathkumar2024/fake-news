"""
Main Fact-Checking Prediction Module
"""

import pickle
import numpy as np
from .language_detector import detect_language, translate_to_english
from .text_processor import preprocess_text
from .embedder import get_single_embedding
import config

# Try to import demo checker for fallback
try:
    from .demo_fact_checker import demo_fact_checker
    has_demo = True
except ImportError:
    has_demo = False

class FactChecker:
    def __init__(self):
        """Initialize fact-checker with saved models"""
        try:
            self.model = pickle.load(open(config.MODEL_PATH, 'rb'))
            self.index = pickle.load(open(config.FAISS_INDEX_PATH, 'rb'))
            self.facts = pickle.load(open(config.FACTS_PATH, 'rb'))
            print("All models loaded successfully")
        except Exception as e:
            print(f"❌ Model loading error: {e}")
            self.model = None
            self.index = None
            self.facts = None

    def check_fact(self, user_text):
        """
        Main prediction function for fact-checking
        
        Uses ML models if available, otherwise uses demo mode
        
        Args:
            user_text: News text (can be in any language)
        
        Returns:
            {
                'original_text': str,
                'language': str,
                'prediction': 'Likely Real' or 'Likely Fake',
                'confidence': float (0-100),
                'similar_facts': list,
                'status': 'success' or 'error',
                'mode': 'production' or 'demo'
            }
        """
        try:
            # If no model available, use demo mode
            if self.model is None or self.index is None:
                if has_demo:
                    result = demo_fact_checker.check_fact(user_text)
                    result['mode'] = 'demo'
                    return result
                else:
                    return {
                        'status': 'error',
                        'message': 'Models not available and demo mode unavailable'
                    }
            
            # 1️⃣ Detect language
            detected_lang = detect_language(user_text)
            
            # 2️⃣ Translate to English if needed
            if detected_lang != 'en' and detected_lang != 'unknown':
                text_en = translate_to_english(user_text)
            else:
                text_en = user_text
            
            # 3️⃣ Clean text
            text_clean = preprocess_text(text_en)
            
            if not text_clean or len(text_clean) < 5:
                return {
                    'status': 'error',
                    'message': 'Text too short after cleaning'
                }
            
            # 4️⃣ Generate embedding
            query_embedding = get_single_embedding(text_clean)
            if query_embedding is None:
                return {
                    'status': 'error',
                    'message': 'Could not generate embedding'
                }
            
            query_embedding = query_embedding.reshape(1, -1)
            
            # 5️⃣ Retrieve similar facts
            similar_facts = []
            try:
                D, I = self.index.search(query_embedding, k=config.FAISS_K)
                similar_facts = [
                    {
                        'fact': self.facts[i][:200] + '...',
                        'similarity_score': float(D[0][j])
                    }
                    for j, i in enumerate(I[0]) if i < len(self.facts)
                ]
            except Exception as e:
                print(f"⚠️  FAISS search error: {e}")
                similar_facts = []
            
            # 6️⃣ Predict authenticity
            try:
                prediction = self.model.predict(query_embedding)[0]
                confidence = self.model.predict_proba(query_embedding)[0].max()
                label = "✅ Likely Real" if prediction == 1 else "❌ Likely Fake"
            except Exception as e:
                print(f"⚠️  Model prediction error: {e}")
                return {
                    'status': 'error',
                    'message': str(e)
                }
            
            return {
                'status': 'success',
                'original_text': user_text[:100] + '...' if len(user_text) > 100 else user_text,
                'language': detected_lang,
                'prediction': label,
                'confidence': round(confidence * 100, 2),
                'similar_facts': similar_facts,
                'processed_text': text_clean[:200] + '...',
                'mode': 'production'
            }
            
        except Exception as e:
            return {
                'status': 'error',
                'message': str(e)
            }

# Create global instance
fact_checker = FactChecker()
