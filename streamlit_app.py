import streamlit as st
st.set_page_config(page_title="EmotionBot", layout="centered")
st.title("Mew~ I'm cc kitty 😼mew")
user_input = st.text_input("Say something to me:")
def analyze_emotion(text):
    greetings = ["hi", "hello", "hey", "lol", "What's up", "How do you do"]
    sad_words = ["sad", "tired", "unhappy", "cry", "not good", "upset"]
    happy_words = ["happy", "great", "excited", "good", "not bad", "emmm"]
    care_words = ["care about", "feel better", "cure the pain"]
    suggest_words = ["you'd better", "you should", "suggest you to"]
    text = text.lower()
    if any(g in text for g in greetings):
        return "Hello there! How are you feeling today. Mew~😸"
    elif any(s in text for s in sad_words):
        return "I'm sorry to hear you're not feeling great. How can I help you mew?🙀"
    elif any(h in text for h in happy_words):
        return "Ah~ I'm happy that you're feeling good today mew!😽"
    elif any(c in text for c in care_words):
        return "Would you like to talk about it, mate?😻"
    elif any(s in text for s in suggest_words):
        return "Aha, such a good plan! You must be an excellent P person! Have you heard of MBTI mew😹?"
    else:
        return None
def convert_to_expression(text):
    text = text.lower()
    text = text.replace("plus", "+").replace("add", "+")
    text = text.replace("minus", "-").replace("subtract", "-")
    text = text.replace("times", "*").replace("multiplied by", "*")
    text = text.replace("divided by", "/").replace("over", "/")
    cleaned = re.sub(r"[^\d\+\-\*/\.()\s]", "", text)
    return cleaned.strip()
def try_calculate(text):
    try:
        expression = convert_to_expression(text)
        allowed_chars = "0123456789+-*/.() "
        if expression and all(c in allowed_chars for c in expression):
            result = eval(expression)
            return f"Emmm... I did the math! The result is 😾: {result}"
        else:
            return None
    except Exception as e:
        return None
if user_input:
    response = analyze_emotion(user_input)
    if response:
        st.markdown(f"😼: {response}")
    else:
        calc_response = try_calculate(user_input)
        if calc_response:
            st.markdown(f"😼: {calc_response}")
        else:
            st.markdown("😿: I didn't quite get that... try again mew~")
