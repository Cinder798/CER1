import streamlit as st
st.set_page_config(page_title="EmotionBot", layout="centered")
st.title("HiHiHi~ I'm cc darling😊")
user_input = st.text_input("Say something to me:")
def analyze_emotion(text):
    greetings = ["hi", "hello", "hey", "lol", "What's up", "How do you do"]
    sad_words = ["sad", "tired", "unhappy", "cry", "not good", "upset"]
    happy_words = ["happy", "great", "excited", "good", "not bad", "emmm"]
    care_words = ["care about", "feel better", "cure the pain"]
    suggest_words = ["you'd better", "you should", "suggest you to"]
    text = text.lower()
    if any(g in text for g in greetings):
        return "Hello there! How are you feeling today?🥰"
    elif any(s in text for s in sad_words):
        return "I'm sorry to hear you're not feeling great. How can I help you?🤗"
    elif any(h in text for h in happy_words):
        return "Ah~ I'm happy that you're feeling good today!🤭"
    elif any(c in text for c in care_words):
        return "Would you like to talk about it, mate?🥹"
    elif any(s in text for s in suggest_words):
        return "Aha, such a good plan! You must be an excellent P person! Have you heard of MBTI🤩?"
    else:
        return "I'm here for you. Tell me more.🙂"
if user_input:
    response = analyze_emotion(user_input)
    st.markdown(f"cc: {response}")
