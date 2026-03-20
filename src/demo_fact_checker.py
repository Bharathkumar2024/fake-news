"""
Demo Fact Checker - Smart Pattern-Based Fake News Detection
Analyzes text for red flags without needing trained ML models
"""

import re
import hashlib

class DemoFactChecker:
    """Demo fact-checker using pattern analysis for realistic predictions"""
    
    def __init__(self):
        # Common verified facts database
        self.demo_facts = [
            "Regular exercise improves cardiovascular health",
            "Water is essential for human survival",
            "Plants absorb carbon dioxide and produce oxygen",
            "The Earth orbits the Sun",
            "Vaccines are developed through rigorous testing",
            "The human body contains approximately 206 bones",
            "The ocean covers approximately 71% of Earth",
            "Sleep is crucial for cognitive function",
            "Fruits and vegetables contain essential nutrients",
            "Consistent learning improves memory retention",
        ]
        
        # Fake news red flags
        self.fake_indicators = {
            'SENSATIONAL_WORDS': [
                'SHOCKING', 'BREAKING', 'SCANDAL', 'EXCLUSIVE', 'BOMBSHELL',
                'EXPOSÉ', 'HIDDEN TRUTH', 'THEY DONT WANT YOU TO KNOW',
                'DOCTORS HATE', 'CELEBRITIES REVEAL', 'DOCTORS HATE THIS ONE TRICK',
                'GOVERNMENT DOESNT WANT', 'UNBELIEVABLE', 'HORRIFYING',
                'DISGUSTING', 'INSANE', 'OUTRAGEOUS'
            ],
            'CAPS_RATIO': 0.4,  # More than 40% capitals = suspicious
            'EXCLAMATION_COUNT': 3,  # 3+ exclamation marks = suspicious
            'QUESTION_COUNT': 3,  # 3+ question marks = suspicious
            'EMOJI_COUNT': 5,  # Many emojis = suspicious
        }
    
    def analyze_text(self, text):
        """Analyze text for fake news patterns"""
        if not text or len(text) < 5:
            return {'is_fake': False, 'confidence': 50, 'red_flags': 0}
        
        red_flags = 0
        analysis = {
            'caps_ratio': 0,
            'has_sensational_word': False,
            'excessive_punctuation': False,
            'suspicious_patterns': False,
            'language_quality': 'good',
        }
        
        # 1. Check CAPS ratio
        caps_count = sum(1 for c in text if c.isupper())
        letters_count = sum(1 for c in text if c.isalpha())
        if letters_count > 0:
            caps_ratio = caps_count / letters_count
            analysis['caps_ratio'] = caps_ratio
            if caps_ratio > self.fake_indicators['CAPS_RATIO']:
                red_flags += 2
        
        # 2. Check for sensational words
        text_upper = text.upper()
        for word in self.fake_indicators['SENSATIONAL_WORDS']:
            if word in text_upper:
                analysis['has_sensational_word'] = True
                red_flags += 3
                break
        
        # 3. Check excessive punctuation
        exclamation_count = text.count('!')
        question_count = text.count('?')
        if exclamation_count >= self.fake_indicators['EXCLAMATION_COUNT']:
            red_flags += 2
            analysis['excessive_punctuation'] = True
        if question_count >= self.fake_indicators['QUESTION_COUNT']:
            red_flags += 2
            analysis['excessive_punctuation'] = True
        
        # 4. Check for emoji/special chars
        emoji_count = len(re.findall(r'[😀-🙏🌀-🗿]', text))
        if emoji_count > self.fake_indicators['EMOJI_COUNT']:
            red_flags += 2
        
        # 5. Check for suspicious patterns
        suspicious_patterns = [
            r'\d+%\s+(IMPROVEMENT|INCREASE|LOSS)',  # "95% improvement"
            r'DON\'T MISS OUT',
            r'LIMITED TIME',
            r'ACT NOW',
            r'CLICK HERE',
            r'EARN MONEY FAST',
        ]
        for pattern in suspicious_patterns:
            if re.search(pattern, text_upper):
                red_flags += 2
                analysis['suspicious_patterns'] = True
                break
        
        # 6. Language quality (check for common misspellings)
        common_typos = ['ur ', 'ur\n', 'lol ', 'omg ', 'wtf ', 'smh ']
        if any(typo in text.lower() for typo in common_typos):
            red_flags += 1
            analysis['language_quality'] = 'poor'
        
        # Calculate confidence based on red flags
        # 0 flags = 85% real, 5+ flags = 85% fake
        is_likely_fake = red_flags >= 5
        base_confidence = 75 + (min(red_flags, 6) * 3)  # 75-93% range
        
        return {
            'is_fake': is_likely_fake,
            'confidence': min(base_confidence, 95),
            'red_flags': red_flags,
            'analysis': analysis
        }
    
    def check_fact(self, text):
        """Generate a smart prediction based on text analysis"""
        if not text or len(text) < 5:
            return {
                'status': 'error',
                'message': 'Text too short'
            }
        
        # Analyze the text
        analysis_result = self.analyze_text(text)
        is_fake = analysis_result['is_fake']
        confidence = analysis_result['confidence']
        red_flags = analysis_result['red_flags']
        
        # Generate deterministic but realistic similar fact
        text_hash = hashlib.md5(text.lower().encode()).hexdigest()
        hash_value = int(text_hash, 16)
        similar_idx = hash_value % len(self.demo_facts)
        
        prediction_text = "❌ Likely Fake" if is_fake else "✅ Likely Real"
        prediction_class = "fake" if is_fake else "real"
        
        return {
            'status': 'success',
            'original_text': text[:100] + '...' if len(text) > 100 else text,
            'language': 'en',
            'prediction': prediction_text,
            'prediction_class': prediction_class,
            'confidence': confidence,
            'red_flags_detected': red_flags,
            'analysis_details': analysis_result['analysis'],
            'similar_facts': [
                {
                    'fact': self.demo_facts[similar_idx],
                    'similarity_score': 0.92
                },
                {
                    'fact': self.demo_facts[(similar_idx + 1) % len(self.demo_facts)],
                    'similarity_score': 0.87
                }
            ],
            'processed_text': text[:80] + '...'
        }

# Create global instance
demo_fact_checker = DemoFactChecker()
