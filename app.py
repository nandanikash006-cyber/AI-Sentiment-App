import streamlit as st
from textblob import TextBlob

# Page Configuration
st.set_page_config(page_title="Ai Sentiment Analyzer", page_icon="🤖", layout="centered")

# App Header
st.title("🤖 AI Text Sentiment Analyzer")
st.write("Type any sentence or review below, and our AI will analyze whether the emotion is **Positive**, **Negative**, or **Neutral**!")

#User Input Text Box
user_text = st.text_area("Enter you text here:", placeholder="e.g., I love learning AI and programming, it's so exciting!")

# Analyze Button
if st.button("Analyze sentiment"):
    if user_text.strip() == "":
        st.warning("⚠️ Please enter some text first!")
    else:
        # Performing Sentiment Analysis using Textblob
        analysis = TextBlob(user_text)
        polarity = analysis.sentiment.polarity  # Returns value between -1.0 and 1.0

        # Determining Sentiment Category
        if polarity > 0.1:
            sentiment = "Positive"
            emoji = "😊 🎉"
            color = "green"
        elif polarity < -0.1:
            sentiment = "Negative"
            emoji = "😞 💔"
            color = "red"
        else:
            sentiment = "Neutral"
            emoji = "😐 🔍"
            color = "orange"
        # Display Results
        st.subheader("Analysis Results:")
        st.markdown(f"**Sentiment:** :{color}[{sentiment}] {emoji}")
        st.metric(label="Polarity Score (Range: -1 to +1)", value=round(polarity, 2))
# Footer
st.markdown("---")
st.markdown("🚀 Built with Python & Streamlit | Perfect for AI Portfolios")
    

        

