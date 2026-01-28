import streamlit as st
import random
import time

# ---------- PAGE CONFIG ----------
st.set_page_config(
    page_title="Will You Be My Valentine 💖",
    page_icon="💘",
    layout="centered"
)

# ---------- SESSION STATE ----------
if "page" not in st.session_state:
    st.session_state.page = "question"

# ---------- GLOBAL CSS ----------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Pacifico&family=Poppins:wght@300;400;600&display=swap');

html, body, [class*="css"]  {
    font-family: 'Poppins', sans-serif;
    background: linear-gradient(135deg, #ffd6e8, #ffe6f2);
}

.main-card {
    background: rgba(255, 255, 255, 0.85);
    padding: 40px;
    border-radius: 25px;
    text-align: center;
    box-shadow: 0px 0px 40px rgba(255, 105, 180, 0.25);
    animation: fadeIn 1.2s ease-in-out;
}

.title {
    font-family: 'Pacifico', cursive;
    font-size: 48px;
    color: #ff4f9a;
}

.subtitle {
    font-size: 18px;
    color: #444;
}

.btn-yes {
    background: linear-gradient(45deg, #ff4f9a, #ff85b3);
    color: white;
    padding: 12px 35px;
    border-radius: 30px;
    font-size: 18px;
    border: none;
    cursor: pointer;
    box-shadow: 0 0 15px rgba(255,79,154,0.6);
}

.btn-no {
    background: #fff;
    color: #ff4f9a;
    padding: 12px 35px;
    border-radius: 30px;
    font-size: 18px;
    border: 2px solid #ff4f9a;
    cursor: pointer;
}

.heart {
    font-size: 60px;
    animation: pulse 1.5s infinite;
}

@keyframes pulse {
    0% {transform: scale(1);}
    50% {transform: scale(1.15);}
    100% {transform: scale(1);}
}

@keyframes fadeIn {
    from {opacity: 0; transform: translateY(20px);}
    to {opacity: 1; transform: translateY(0);}
}
</style>
""", unsafe_allow_html=True)

# ---------- FUNCTIONS ----------
def go_to(page):
    st.session_state.page = page
    st.rerun()

# ---------- QUESTION PAGE ----------
if st.session_state.page == "question":
    st.markdown("""
    <div class="main-card">
        <div class="heart">💖</div>
        <div class="title">Will You Be My Valentine?</div>
        <p class="subtitle">From the girl who already chose you every day 💕</p>
    </div>
    """, unsafe_allow_html=True)

    st.write("")
    col1, col2 = st.columns(2)

    with col1:
        if st.button("YES 💘"):
            go_to("yes")

    with col2:
        if st.button("NO 🙄"):
            go_to("no")

# ---------- YES PAGE ----------
elif st.session_state.page == "yes":
    st.balloons()
    st.markdown("""
    <div class="main-card">
        <div class="heart">💞</div>
        <div class="title">YAYYYYY!!! 😭💘</div>
        <p class="subtitle">
        You just made my heart do backflips 🥹<br>
        Best decision of your life tbh 😌💖<br><br>
        Happy Valentine's Day, my love 💕<br>
        I choose you. Today. Tomorrow. Always. 💍✨
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.write("")
    if st.button("Replay 💫"):
        go_to("question")

# ---------- NO PAGE ----------
elif st.session_state.page == "no":
    messages = [
        "Wrong answer bestie 😤",
        "Try again 😏",
        "Think again 💭",
        "System error ❌",
        "This option is disabled 🚫",
        "Unauthorized choice 🔐",
        "Emotionally unavailable option 😌"
    ]

    st.markdown(f"""
    <div class="main-card">
        <div class="title">😒 {random.choice(messages)}</div>
        <p class="subtitle">
        This button is just for decoration 🙄<br>
        There's only one valid answer anyway 💖
        </p>
    </div>
    """, unsafe_allow_html=True)

    time.sleep(1.2)
    st.info("Redirecting you to the correct decision... 💕")
    time.sleep(1.2)
    go_to("question")
