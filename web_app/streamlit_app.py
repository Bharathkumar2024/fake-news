"""
Streamlit Web App
Alternative web interface using Streamlit

Command: streamlit run web_app/streamlit_app.py
"""

import streamlit as st
import os
import sys

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

import config
from src.fact_checker import fact_checker
from src.utils import ensure_models_exist, get_project_stats

# Page config
st.set_page_config(
    page_title="🔥 Fact-Checker AI",
    page_icon="🔍",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .main {
        max-width: 900px;
    }
    .stTextArea textarea {
        font-size: 1.1em;
    }
    h1 {
        color: #ff6b6b;
        text-align: center;
    }
    .success {
        background-color: #d4edda;
        padding: 1rem;
        border-radius: 0.5rem;
        border-left: 4px solid #51cf66;
    }
    .danger {
        background-color: #f8d7da;
        padding: 1rem;
        border-radius: 0.5rem;
        border-left: 4px solid #ff7675;
    }
    .info {
        background-color: #d1ecf1;
        padding: 1rem;
        border-radius: 0.5rem;
        border-left: 4px solid #4ecdc4;
    }
</style>
""", unsafe_allow_html=True)

# Header
st.title("🔥 Fact-Checker AI")
st.markdown("### Detect Fake News in Real-Time | Multi-Language Support")

# Sidebar
with st.sidebar:
    st.header("ℹ️ Information")
    
    # Project info
    stats = get_project_stats()
    st.write(f"**Model**: Logistic Regression on BERT")
    st.write(f"**Embedding Dimension**: {config.EMBEDDING_DIMENSION}")
    st.write(f"**Supported Languages**: {', '.join(config.SUPPORTED_LANGUAGES)}")
    
    st.divider()
    
    st.header("📖 How It Works")
    st.write("""
    1. **Language Detection** 🌍
       - Detects input language
       - Translates to English if needed
    
    2. **Text Processing** 🧹
       - Removes URLs and special characters
       - Removes stopwords
       - Cleans and normalizes
    
    3. **Semantic Analysis** 🔎
       - Generates embeddings
       - Searches for similar facts
       - Compares with verified database
    
    4. **Prediction** 🤖
       - ML model evaluates authenticity
       - Provides confidence score
       - Shows related facts
    """)
    
    st.divider()
    
    st.header("⚠️ Disclaimer")
    st.warning("""
    This tool is for educational and entertainment purposes only.
    Always verify important news with official sources.
    """)

# Check if models are available
models_ok, missing = ensure_models_exist()

if not models_ok:
    st.error("""
    ❌ **Models Not Found!**
    
    Please run the training pipeline first:
    ```
    python notebooks/Step_0_Install.py
    python notebooks/Step_1_Load_Data.py
    ... (complete all steps)
    ```
    """)
    st.stop()

# Main content
col1, col2 = st.columns([1, 1])

with col1:
    st.header("📝 Enter News Text")
    st.write("Supports English, Tamil, and Hindi")
    
    news_text = st.text_area(
        "Paste the news text here:",
        height=250,
        placeholder="Enter news text...",
        label_visibility="collapsed"
    )

with col2:
    st.header("📊 Results")
    
    if news_text:
        if st.button("🔍 Check Authenticity", use_container_width=True, type="primary"):
            with st.spinner("🔄 Analyzing text..."):
                result = fact_checker.check_fact(news_text)
            
            if result['status'] == 'success':
                # Prediction
                prediction = result['prediction']
                is_real = "Real" in prediction
                
                col1, col2, col3 = st.columns(3)
                
                with col1:
                    if is_real:
                        st.success(prediction)
                    else:
                        st.error(prediction)
                
                with col2:
                    confidence = result['confidence']
                    st.metric("Confidence", f"{confidence}%")
                
                with col3:
                    language = result.get('language', 'Unknown')
                    st.metric("Language", language.upper())
                
                st.divider()
                
                # Processed text
                with st.expander("👀 See Processed Text"):
                    st.code(result['processed_text'], language="text")
                
                # Similar facts
                st.subheader("📚 Similar Verified Facts")
                if result['similar_facts']:
                    for i, fact in enumerate(result['similar_facts'], 1):
                        with st.container():
                            st.write(f"**Fact {i}**")
                            st.write(f"📌 {fact['fact']}")
                            st.write(f"**Similarity**: {fact['similarity_score']:.4f}")
                            st.divider()
                else:
                    st.info("No similar facts found in database")
                
            else:
                st.error(f"❌ Error: {result.get('message', 'Unknown error')}")
    else:
        st.info("👆 Enter news text in the left column to get started")

# Footer
st.divider()
st.markdown("""
<div style="text-align: center; color: gray; font-size: 0.9em;">
    🔬 Powered by AI | Machine Learning Fact-Checking System<br>
    Made with ❤️ for better informed society
</div>
""", unsafe_allow_html=True)
