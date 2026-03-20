"""
Utility Functions
"""

import os

def ensure_models_exist():
    """Check if all required model files exist"""
    import config
    required_files = [
        config.MODEL_PATH,
        config.FAISS_INDEX_PATH,
        config.FACTS_PATH
    ]
    
    missing = [f for f in required_files if not os.path.exists(f)]
    if missing:
        return False, missing
    return True, []

def get_project_stats():
    """Get project statistics"""
    import config
    stats = {
        'data_dir': config.DATA_DIR,
        'models_dir': config.MODELS_DIR,
        'embedding_dim': config.EMBEDDING_DIMENSION,
        'supported_langs': config.SUPPORTED_LANGUAGES
    }
    return stats
