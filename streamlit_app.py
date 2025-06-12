import streamlit as st
import re
st.set_page_config(page_title="cc kitty 😼 Emotional Book of Answers", layout="centered")
st.title("Mew~ I'm cc kitty 😼 mew")
st.markdown("""
**Hey human~**  
CC knows you've been carrying so much, and you're doing so amazing!  
No worries! CC kitty is always here for you — no judgment, no pressure. Just cozy paws, gentle purrs, and open ears instead.  
**Ready to share something? Just type it here, mew~** 😽
""")
user_input = st.text_area(
    label="",
    height=150,
    placeholder="Type your thoughts here, mew~"
)
book_of_answers = [
    "🐾 On page 1, it says: 'Trust your instincts and leap forward.'  \nThat means the opportunity is right ahead of you! What are you waiting for? Mew~",
    "🐾 On page 2, it says: 'Wait until the moon is full.'  \nThat means if you wait patiently for the right time—not pouncing too soon—you might just be rewarded, mew~",
    "🐾 On page 3, it says: 'Ask someone you love.'",
    "🐾 On page 4, it says: 'Maybe… but wear your lucky socks!'",
    "🐾 On page 5, it says: 'Not now, but soon enough.'",
    "🐾 On page 6, it says: 'Only if you meow three times!'",
    "🐾 On page 7, it says: 'Patience brings the best treats.'",
    "🐾 On page 8, it says: 'Definitely — but watch your tail.'",
    "🐾 On page 9, it says: 'Sleep on it, then decide.'",
    "🐾 On page 10, it says: 'Yes, and it will be purr-fect!'"
]

explanations = [
    "It means: now is the best time to act bravely, even if you're scared. A leap of faith, mew~",
    "It means: some things need time. Be patient, just like the moon grows slowly~",
    "It means: if unsure, talk to someone you trust with your heart 🫶",
    "It means: luck and coziness go together! Don't forget your socks~",
    "It means: not now, but the chance will come. Wait a bit more mew~",
    "It means: be playful! Magic needs a little silliness sometimes 😹",
    "It means: rewards come to those who wait. Hold on, treat is near!",
    "It means: yes, but be careful and aware of your surroundings!",
    "It means: let your dream guide you! A nap clears the mind mew~",
    "It means: it's all gonna work out—trust the process, kitty style!"
]

stories = [
    "One time, I jumped from a windowsill chasing a firefly... and found a fishball! Brave leap, yummy reward, mew~",
    "I once waited four nights by the window for the full moon… and then got tuna. Patience is tasty~",
    "I asked my cat bro where my toy went. He helped me find it under the sofa~ teamwork mew!",
    "I wore rainbow socks and found a cookie under the couch. Coincidence? 😼",
    "I wanted to sneak out, but the wind was scary. Waited till sunshine—and caught a butterfly!",
    "I meowed three times in front of the fridge... and got my treat! Magic, right?",
    "Waited all day by the door, then my human came home with a blanket just for me~",
    "Ran too fast once and bumped the table! Now I watch my tail before leaping 😹",
    "I napped on a tough problem... and dreamed of the answer! Zzz~ mew~",
    "Followed a sparkle and ended up in the sunniest spot ever. Best nap spot mew~"
]

# ---------- 状态管理 ----------
if "mode" not in st.session_state:
    st.session_state.mode = None
if "step" not in st.session_state:
    st.session_state.step = 0
if "last_answer_index" not in st.session_state:
    st.session_state.last_answer_index = None

# ---------- 主逻辑 ----------
if user_input:
    user_input_clean = user_input.lower().strip()

    if st.session_state.mode == "book_of_answers":
        if st.session_state.step == 0:
            try:
                num = int(user_input_clean)
                if 1 <= num <= 10:
                    idx = num - 1
                    st.session_state.last_answer_index = idx
                    st.markdown(f"✨ cc kitty whispers: {book_of_answers[idx]}")
                    st.markdown("❓ Would you like an explanation mew? Say 'yes' or 'explain'~")
                    st.session_state.step = 1
                else:
                    st.markdown("😿 That number doesn't work, mew. Pick between 1 and 10.")
            except:
                st.markdown("🙀 That's not a number, mew. Try again~")

        elif st.session_state.step == 1:
            if user_input_clean in ["yes", "explain"]:
                idx = st.session_state.last_answer_index
                st.markdown(f"📖 Explanation: {explanations[idx]}")
                st.markdown("💭 Want me to share a little cat story about this? Say 'yes' or 'share'~")
                st.session_state.step = 2
            else:
                st.markdown("🙀 Say 'yes' if you'd like an explanation~")

        elif st.session_state.step == 2:
            if user_input_clean in ["yes", "share"]:
                idx = st.session_state.last_answer_index
                st.markdown(f"🧶 Kitty Storytime: {stories[idx]}")
                st.markdown("🌸 That’s my story... mew~ now I’m curious — would you like to share your story too?")
                st.markdown("💌 If yes, just type anything you'd like to share~")
                st.session_state.step = 3
            else:
                st.markdown("🙀 Say 'yes' or 'share' if you'd like to hear my story~")

        elif st.session_state.step == 3:
            if user_input_clean in ["no", "not now", "nope"]:
                st.markdown("😺 That’s okay, mew~ maybe next time! The book is always here for you 💕")
            else:
                st.markdown(f"😻 Wow, that sounds meaningful! Thanks for sharing with cc kitty~")
                st.markdown("✨ Want to ask the Book of Answers again? Just say 'book' or 'answer' anytime mew~")
            st.session_state.mode = None
            st.session_state.step = 0

    elif any(keyword in user_input_clean for keyword in ["book", "answer"]):
        st.session_state.mode = "book_of_answers"
        st.session_state.step = 0
        st.markdown("🔮 cc kitty: The Book of Answers is opening... Choose a number between 1 and 10 🎲")

    else:
        # ---------- 情绪分析 ----------
        def analyze_emotion(text):
            greetings = ["hi", "hello", "hey", "lol", "what's up", "how do you do"]
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

        # ---------- 数学计算 ----------
        def convert_to_expression(text):
            text = text.lower()
            text = text.replace("plus", "+").replace("add", "+")
            text = text.replace("minus", "-").replace("subtract", "-")
            text = text.replace("times", "*").replace("multiplied by", "*")
            text = text.replace("divided by", "/").replace("over", "/")
            cleaned = re.sub(r"[^\d\+\-\*/\.\(\)\s]", "", text)
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
            except Exception:
                return None

        # ---------- 响应输出 ----------
        response = analyze_emotion(user_input)
        if response:
            st.markdown(f"😼: {response}")
        else:
            calc_response = try_calculate(user_input)
            if calc_response:
                st.markdown(f"😼: {calc_response}")
            else:
                st.markdown("😿: I didn't quite get that... try again mew~")
