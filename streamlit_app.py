import streamlit as st
import streamlit.components.v1 as components
import re
st.markdown(
    """
    <style>
    .stApp {
        background-color: light pink;
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True
)
SHOW_DEBUG = False
def debug(*args, **kwargs):
    if SHOW_DEBUG:
        st.write(*args, **kwargs)
def contains_chinese(text):
    return any('\u4e00' <= char <= '\u9fff' for char in text)
def contains_english(text):
    return any('a' <= char.lower() <= 'z' for char in text)
def analyze_emotion(text):
    greetings = ["hi", "hello", "hey", "lol", "what's up", "how do you do"]
    sad_words = ["sad", "tired", "unhappy", "cry", "not good", "upset"]
    happy_words = ["happy", "great", "excited", "good", "not bad", "emmm"]
    care_words = ["care about", "feel better", "cure the pain"]
    suggest_words = ["you'd better", "you should", "suggest"]
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
        return "Aha, such a good plan! You must be an excellent P person! Heard of MBTI, mew😹?"
    else:
        return None
def convert_to_expression(text):
    text = text.lower()
    text = text.replace("plus", "+").replace("add", "+")
    text = text.replace("minus", "-").replace("subtract", "-")
    text = text.replace("times", "*").replace("multiplied by", "*")
    text = text.replace("divided by", "/").replace("over", "/")
    text = text.replace("加", "+").replace("减", "-").replace("乘", "*").replace("除", "/")
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
st.set_page_config(page_title="cc kitty 😼 Emotional Book of Answers", layout="centered")
st.title("Mew~ I'm CC Kitty😼Mew~")
st.markdown("""
#### Hey human~  
CC knows you've been carrying so much, and you're doing so amazing!  
No worries! CC kitty is always here for you — no judgment, no pressure.  
**Just cozy paws, gentle purrs, and open ears instead.**  
**Ready to share something? Just type it here, mew~** 🐱
""")
user_input = st.text_area(label="", height=150, placeholder="Type your thoughts here, mew~")
user_input_clean = user_input.lower().strip() if user_input else ""
book_of_answers = {
    "en": [
        "🐾 On page 1, it says: 'Trust your instincts and leap forward.' \nDo you want me to explain it? Just reply 'explain' or 'yes', CC will do it for you!",
        "🐾 On page 2, it says: 'Wait until the moon is full.' \nDo you want me to explain it? Just reply 'explain' or 'yes', CC will do it for you!",
        "🐾 On page 3, it says: 'Ask someone you love.' \nDo you want me to explain it? Just reply 'explain' or 'yes', CC will do it for you!",
        "🐾 On page 4, it says: 'Maybe… but wear your lucky socks!' \nDo you want me to explain it? Just reply 'explain' or 'yes', CC will do it for you!",
        "🐾 On page 5, it says: 'Not now, but soon enough.' \nDo you want me to explain it? Just reply 'explain' or 'yes', CC will do it for you!",
        "🐾 On page 6, it says: 'Only if you meow three times!' \nDo you want me to explain it? Just reply 'explain' or 'yes', CC will do it for you!",
        "🐾 On page 7, it says: 'Patience brings the best treats.' \nDo you want me to explain it? Just reply 'explain' or 'yes', CC will do it for you!",
        "🐾 On page 8, it says: 'Definitely — but watch your tail.' \nDo you want me to explain it? Just reply 'explain' or 'yes', CC will do it for you!",
        "🐾 On page 9, it says: 'Sleep on it, then decide.' \nDo you want me to explain it? Just reply 'explain' or 'yes', CC will do it for you!",
        "🐾 On page 10, it says: 'Yes, and it will be purr-fect!' \nDo you want me to explain it? Just reply 'explain' or 'yes', CC will do it for you!"
    ],
    "zh": [
        "🐾 第1页写着：'相信你的直觉，然后大胆行动' \n想让CC酱解释一下吗？回复 '解释' 或 '好' 就行，喵~",
        "🐾 第2页写着：'等到满月的时候' \n想让CC酱解释一下吗？回复 '解释' 或 '好' 就行，喵~",
        "🐾 第3页写着：'问问你所爱的人' \n想让CC酱解释一下吗？回复 '解释' 或 '好' 就行，喵~",
        "🐾 第4页写着：'也许吧……但要穿上你幸运的袜子' \n想让CC酱解释一下吗？回复 '解释' 或 '好' 就行，喵~",
        "🐾 第5页写着：'现在不行，但很快就会行了' \n想让CC酱解释一下吗？回复 '解释' 或 '好' 就行，喵~",
        "🐾 第6页写着：'只要你喵三声!' \n想让CC酱解释一下吗？回复 '解释' 或 '好' 就行，喵~",
        "🐾 第7页写着：'耐心会带来最棒的奖励.' \n想让CC酱解释一下吗？回复 '解释' 或 '好' 就行，喵~",
        "🐾 第8页写着：'当然啦——但要注意尾巴!' \n想让CC酱解释一下吗？回复 '解释' 或 '好' 就行，喵~",
        "🐾 第9页写着：'睡一觉再做决定.' \n想让CC酱解释一下吗？回复 '解释' 或 '好' 就行，喵~",
        "🐾 第10页写着：'会的喵~一切都会很完美!' \n想让CC酱解释一下吗？回复 '解释' 或 '好' 就行，喵~"
    ]
}
explanations = {
    "en": [
        "💡 page 1 means: now is the best time to act bravely, even if you're scared. A leap of faith, mew~ \nThe opportunity is right ahead of you!",
        "💡 page 2 means: some things need time. \nBe patient, just like the moon grows slowly~",
        "💡 page 3 means: if unsure, talk to someone you trust with your heart 🫶",
        "💡 page 4 means: luck and coziness go together! Don't forget your socks~",
        "💡 page 5 means: not now, but the chance will come. Wait a bit more mew~",
        "💡 page 6 means: be playful! Magic needs a little silliness sometimes 😹",
        "💡 page 7 means: rewards come to those who wait. Hold on, treat is near!",
        "💡 page 8 means: yes, but be careful and aware of your surroundings!",
        "💡 page 9 means: let your dream guide you! A nap clears the mind mew~",
        "💡 page 10 means: it's all gonna work out—trust the process, kitty style!"
    ],
    "zh": [
        "这意思是：现在就是行动的最佳时机，哪怕你有点害怕，也要勇敢一跳，喵~",
        "这意思是：有些事情需要时间，像月亮慢慢变圆一样，慢慢来，才会有好结果~",
        "这意思是：如果你不确定，就找个你真心信任的人聊一聊吧~",
        "这意思是：幸运和舒服总是一起出现！别忘了袜子喵~",
        "这意思是：现在还不是时候，但再等等就会有机会了，别急~",
        "这意思是：要有点调皮和魔法的心情，才能发现奇迹喵~",
        "这意思是：等一等，奖励马上就来了喵~",
        "这意思是：当然可以，但要留心周围的变化喵~",
        "这意思是：做梦有时候能带来灵感，喵睡一觉再说~",
        "这意思是：放心吧，一切都会顺利的，喵式信仰开启!"
    ]
}
stories = {
    "en": [
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
    ],
    "zh": [
        "有次我从窗台跳下去追萤火虫, 结果发现了一个鱼丸!喵呜~",
        "我曾经等了四天四夜看满月, 然后吃到了金枪鱼罐头, 等得值喵~",
        "我问我哥我的玩具去哪了, 他帮我从沙发底下找出来了, 好队友喵~",
        "我穿着彩虹袜子, 在沙发底下发现了一块饼干, 神奇吗? 喵~",
        "我本来想偷偷溜出去, 但外面风好大, 等到晴天就追上了蝴蝶~",
        "我对着冰箱喵了三声……结果真的拿到小鱼干了! 神奇吧喵~",
        "我等了一整天, 我的铲屎官回来时给了我一条软绵绵的小毯子~",
        "我以前跑太快撞到桌角了, 现在每次跳跃前都会注意尾巴喵~",
        "我梦到了解题方法, 醒来立刻写下来, 果然对了! 梦里有答案喵~",
        "我追着阳光跑, 跑到了一处最暖的窗边, 太舒服了喵~"
    ]
}
if "mode" not in st.session_state:
    st.session_state.mode = None
if "step" not in st.session_state:
    st.session_state.step = 0
if "last_answer_index" not in st.session_state:
    st.session_state.last_answer_index = None
book_keywords = ["book", "answer", "book of answers", "答案之书"]
lang = "zh" if contains_chinese(user_input_clean) else "en"
response = analyze_emotion(user_input_clean) or try_calculate(user_input_clean)
if any(keyword in user_input_clean for keyword in book_keywords):
    st.session_state.mode = "book_of_answers"
    st.session_state.step = 0
    st.markdown("🔮 " + ("请从 1 到 10 中选择一个数字喵~ 🎲（你也可以输入 '退出' 离开~）" if lang == "zh" else "Choose a number between 1 and 10, mew~ 🎲 (You can type 'exit' anytime to leave)"))
elif st.session_state.mode == "book_of_answers":
    if user_input_clean in ["退出", "exit"]:
        st.session_state.mode = None
        st.session_state.step = 0
        st.markdown("🙀 已退出答案之书模式~ 想再回来随时输入“答案之书”喵~" if lang == "zh" else "🙀 Book of Answers mode exited~ Just type again to come back, mew~")
    elif st.session_state.step == 0:
        try:
            num = int(user_input_clean)
            if 1 <= num <= 10:
                st.session_state.last_answer_index = num - 1
                st.session_state.step = 1
                st.markdown(f"<div style='font-size: 18px; font-weight: bold'>{book_of_answers[lang][num - 1]}</div>", unsafe_allow_html=True)
                st.markdown("🧐 需要本喵解释一下嘛？快回复 '解释' 或 '好'。你也可以输入 '退出' 离开噢~" if lang == "zh" else "❓ Would you like an explanation mew? Say 'yes' or 'explain'~ You can also say 'exit' to leave~")
            else:
                st.markdown("😿 数字要在 1-10 哦~" if lang == "zh" else "😿 Number out of range! Try 1-10 mew~")
        except:
            st.markdown("🙀 这不是个有效的数字喵~" if lang == "zh" else "🙀 That's not a valid number, mew~")
    elif st.session_state.step == 1:
        if user_input_clean in ["yes", "explain", "讲故事", "我想听", "行"]:
            idx = st.session_state.last_answer_index
            st.markdown(f"<div style='font-size: 24px; font-weight: bold'>🧶 {'CC故事时间' if lang == 'zh' else 'Kitty Storytime'}: {stories[lang][idx]}</div>", unsafe_allow_html=True)
            st.markdown("🌸 酱紫就是CC的故事啦喵～你想分享你的故事嘛亲亲~" if lang == "zh" else "🌸 That’s my story... mew~ now I’m curious — would you like to share your story too?")
            st.markdown("💌 如果你想，把你想说的话打字在这里叭喵～" if lang == "zh" else "💌 If yes, just type anything you'd like to share~")
            st.session_state.step = 2
        else:
            st.session_state.mode = None
            st.session_state.step = 0
    elif st.session_state.step == 2:
        if user_input_clean:
            st.markdown("😻 天哪，原来你还有这样的故事！谢谢你，人！" if lang == "zh" else "😻 Wow, that sounds meaningful! Thanks for sharing with cc kitty~")
        st.markdown("✨ 想再问一次答案之书？再打 '答案之书' 就好啦~" if lang == "zh" else "✨ Want to ask the Book of Answers again? Just say 'book' or 'answer' anytime mew~")
        st.session_state.mode = None
        st.session_state.step = 0
elif response:
    st.markdown(f"<div style='font-size: 18px; font-weight: bold'>😼: {response}</div>", unsafe_allow_html=True)
with open("data_cat_3d.html", "r", encoding="utf-8") as f:
    html_code = f.read()
components.html(html_code, height=700)
