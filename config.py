"""
Configuration File for Fact-Checker System
"""

import os

# Paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
MODELS_DIR = os.path.join(BASE_DIR, "models")
SRC_DIR = os.path.join(BASE_DIR, "src")

# Model Files
MODEL_PATH = os.path.join(MODELS_DIR, "model.pkl")
FAISS_INDEX_PATH = os.path.join(MODELS_DIR, "faiss_index.pkl")
FACTS_PATH = os.path.join(MODELS_DIR, "facts.pkl")
EMBEDDER_PATH = os.path.join(MODELS_DIR, "embedder.pkl")
LABEL_ENCODER_PATH = os.path.join(MODELS_DIR, "label_encoder.pkl")

# Data Files
FAKE_CSV = os.path.join(DATA_DIR, "Fake.csv")
TRUE_CSV = os.path.join(DATA_DIR, "True.csv")

# ML Model Configuration
EMBEDDING_MODEL = 'all-MiniLM-L6-v2'
EMBEDDING_DIMENSION = 384
FAISS_K = 5  # Number of similar facts to retrieve

# Text Processing
SAMPLE_SIZE = 10000  # Use first 10K samples for training (adjust based on data)
TEST_SIZE = 0.2

# Language Detection
SUPPORTED_LANGUAGES = ['en', 'ta', 'hi']  # English, Tamil, Hindi

# Flask Configuration
FLASK_HOST = '0.0.0.0'
FLASK_PORT = 5000
DEBUG_MODE = True

# Streamlit Configuration
STREAMLIT_THEME = "light"
STREAMLIT_WIDE_MODE = True

print("Configuration loaded")
