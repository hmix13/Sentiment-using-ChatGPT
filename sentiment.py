import streamlit as st
import openai

# Use the OpenAI API to analyze the sentiment of text
@st.cache(allow_output_mutation=True)
def analyze_sentiment(prompt):
    openai.api_key = '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'

    completions = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=1024,
        stop=None,
        temperature=0.5,
    )

    message = completions.choices[0].text
    return message

# Create the Streamlit app
st.set_page_config(page_title="Sentiment Analyzer", page_icon=":guardsman:", layout="wide")
st.title("Sentiment Analyzer")

# Get user input
text = st.text_area("Enter the text you want to analyze:")

# Analyze sentiment
if text:
    sentiment = analyze_sentiment(f"Analyze the sentiment of: {text}")
    st.success(sentiment)
