import streamlit as st
st.set_page_config(page_title="EmotionBot", layout="centered")
st.title("EmotionBot - Your Mood Companion")
user_input = st.text_input("Say something to me:")
def analyze_emotion(text):
    greetings = ["hi, "hello", "hey", "lol"]
    sad_words = ["sad", "tired", "unhappy", "rip"]
    happy_words = ["happy", "great", "excited", "good"]
    text = text.lower()
    if any(g in text for g in greetings):
        return "Hello there! How are you feeling today?"
    elif any(s in text for s in sad_words):
        return "I'm sensing you're not feeling great. Want to talk about it? "
    elif any(h in text for h in happy_words):
        return "Yay! I'm happy that you're feeling good today!"
    else:
        return "I'm here for you. Tell me more."
if user_input:
    response = analyze_emotion(user_input)
    st.markdown(f"AI: {response}")
