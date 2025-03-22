import streamlit as st
from transformers import pipeline

# Load sentiment analysis model
sent_pipeline = pipeline("sentiment-analysis")

# Dark theme CSS
st.markdown("""
    <style>
        .main {background-color: #000000; color: #ffffff;}
        .stTextArea textarea {background-color: #1a1a1a; color: #ffffff; border: 1px solid #4a4a4a;}
        .st-b7 {color: #00ff00;}
        .st-b8 {color: #ff4444;}
        .reportview-container .markdown-text-container {color: #ffffff;}
        .header {color: #00b4d8;}
        .confidence-bar {background-color: #2d2d2d; border-radius: 10px; padding: 3px;}
        .confidence-fill {background-color: #00b4d8; height: 20px; border-radius: 8px;}
        .stButton>button {background-color: #1a1a1a; color: #ffffff; border: 1px solid #4a4a4a;}
        .stButton>button:hover {background-color: #2d2d2d; border-color: #5a5a5a;}
        .footer {color: #888888;}
    </style>
""", unsafe_allow_html=True)

# App Layout
st.markdown("<h1 class='header'>📊 Sentiment Analyzer</h1>", unsafe_allow_html=True)
st.markdown("""
    <div style='color: #cccccc;'>
    This Streamlit WebApp analyze the reviews with their confidence level.
    </div>
""", unsafe_allow_html=True)


# Input Text Section
st.markdown("### ✍️ Enter your text below to analyze:")
txt = st.text_area(
    "",
    height=170,
    placeholder="Type or paste your text here...\n(Example: 'I absolutely love this product! It's amazing!')",
    key="input_text"
)



  

# Analysis Section
if st.button("🚀 Analyze Sentiment", use_container_width=True):
    if txt:
        with st.spinner("🔍 Analyzing text sentiment..."):
            result = sent_pipeline(txt)[0]
            sentiment = result['label']
            confidence = result['score']
            
            st.markdown("---")
            st.subheader("Analysis Results")
            
            # Sentiment display
            emoji = "😊" if sentiment == "POSITIVE" else "😠"
            color = "#00ff00" if sentiment == "POSITIVE" else "#ff4444"
            
            st.markdown(f"""
                <div style="padding: 20px; border-radius: 10px; background: {color}20; border-left: 5px solid {color};">
                    <h3 style="color: {color}; margin:0;">{sentiment.title()} {emoji}</h3>
                    <p style="color: #cccccc; margin: 10px 0 0 0;">Confidence Level:</p>
                    <div class="confidence-bar">
                        <div class="confidence-fill" style="width: {confidence*100:.1f}%;"></div>
                    </div>
                    <p style="color: #cccccc; margin: 5px 0 0 0; text-align: right;"><b>{confidence*100:.1f}%</b></p>
                </div>
            """, unsafe_allow_html=True)
            
            # Additional insights
            st.markdown("### 📌 Key Insights")
            if sentiment == "POSITIVE":
                st.success("This text appears very favorable! Consider highlighting these positive aspects in your marketing materials.")
            else:
                st.error("This text contains negative sentiment. You might want to follow up for more details or address these concerns.")
    else:
        st.warning("Please enter some text to analyze!")

# Add footer
st.markdown("---")
st.markdown("""
    <div class="footer" style="text-align: center; font-size: 0.9em;">
        Powered by Hugging Face Transformers • 
        <a href="https://huggingface.co/docs/transformers/main/en/model_doc/distilbert" target="_blank" style="color: #00b4d8;">DistilBERT Model</a> •
        Made with ❤️ using Streamlit
    </div>
""", unsafe_allow_html=True)