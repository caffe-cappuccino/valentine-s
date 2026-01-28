import streamlit as st
import random
import time

# ---------- PAGE CONFIG ----------
st.set_page_config(
    page_title="Be My Valentine 💕",
    page_icon="🧁",
    layout="centered"
)

# ---------- SESSION STATE ----------
if "page" not in st.session_state:
    st.session_state.page = "question"

# ---------- GLOBAL CSS ----------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Pacifico&family=Quicksand:wght@400;600&display=swap');

html, body, [class*="css"]  {
    font-family: 'Quicksand', sans-serif;
    background: linear-gradient(135deg, #ffe4f1, #ffd1e8);
    cursor: url('https://cur.cursors-4u.net/symbols/sym-1/sym46.cur'), auto;
}

/* Floating teddy bears */
.teddy {
    position: fixed;
    font-size: 45px;
    animation: float 6s infinite ease-in-out;
    opacity: 0.7;
    z-index: 0;
}
.teddy1 { left: 5%; top: 10%; animation-delay: 0s;}
.teddy2 { left: 85%; top: 20%; animation-delay: 1s;}
.teddy3 { left: 10%; top: 70%; animation-delay: 2s;}
.teddy4 { left: 80%; top: 75%; animation-delay: 3s;}

@keyframes float {
    0% {transform: translateY(0px);}
    50% {transform: translateY(-25px);}
    100% {transform: translateY(0px);}
}

/* Card */
.card {
    background: rgba(255,255,255,0.94);
    padding: 45px;
    border-radius: 35px;
    text-align: center;
    box-shadow: 0 0 40px rgba(255,105,180,0.3);
    animation: pop 1s ease;
    position: relative;
    z-index: 2;
}

.title {
    font-family: 'Pacifico', cursive;
    font-size: 46px;
    color: #ff5fa2;
}

.text {
    font-size: 18px;
    color: #555;
    line-height: 1.8;
}

.emoji {
    font-size: 65px;
    animation: float 2s infinite ease-in-out;
}

/* Envelope animation */
.envelope {
    font-size: 120px;
    animation: pop 1s ease;
}

.letter {
    background: #fffafc;
    border-radius: 25px;
    padding: 35px;
    margin-top: 20px;
    box-shadow: 0 0 25px rgba(255,105,180,0.25);
    animation: slide 1.5s ease;
}

@keyframes slide {
    from {transform: translateY(40px); opacity: 0;}
    to {transform: translateY(0); opacity: 1;}
}

@keyframes pop {
    from {transform: scale(0.85); opacity: 0;}
    to {transform: scale(1); opacity: 1;}
}
</style>

<div class="teddy teddy1">🧸</div>
<div class="teddy teddy2">🧸</div>
<div class="teddy teddy3">🧸</div>
<div class="teddy teddy4">🧸</div>
""", unsafe_allow_html=True)

# ---------- NAV ----------
def go(page):
    st.session_state.page = page
    st.rerun()

# ---------- QUESTION PAGE ----------
if st.session_state.page == "question":
    st.markdown("""
    <div class="card">
        <div class="emoji">🧁🎀</div>
        <div class="title">Will You Be My Valentine?</div>
        <p class="text">
        I baked this website just for you 🥺🧁<br>
        Extra love, extra sugar, extra us 💕✨
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.write("")
    c1, c2, c3 = st.columns(3)

    with c1:
        if st.button("YES 🥰🧁"):
            go("yes")

    with c2:
        if st.button("NO 🙈"):
            go("no")

    with c3:
        if st.button("💌 Open Love Letter"):
            go("letter")

# ---------- YES PAGE ----------
elif st.session_state.page == "yes":
    st.balloons()
    st.snow()
    st.markdown("""
    <div class="card">
        <div class="emoji">💞🧸</div>
        <div class="title">YAYYYYY 💖</div>
        <p class="text">
        My heart just turned into cupcakes 🧁😭<br><br>
        You’re my favorite human, my safe place,<br>
        my forever Valentine 🥰💍<br><br>
        I love you more than desserts 🧁💗
        </p>
    </div>
    """, unsafe_allow_html=True)

    if st.button("Again Again 🥺💗"):
        go("question")

# ---------- NO PAGE ----------
elif st.session_state.page == "no":
    cute_no = [
        "Hehe wrong cupcake 🤭",
        "Oopsie 🧁😶‍🌫️",
        "Try again cutie 🥺",
        "System glitch 💻💔",
        "Not allowed 😌",
        "Teddy says no 🧸🚫",
        "Cupcake disapproves 🧁🙄"
    ]

    st.markdown(f"""
    <div class="card">
        <div class="emoji">🥺🧸</div>
        <div class="title">{random.choice(cute_no)}</div>
        <p class="text">
        That button is just decoration 🎀<br>
        Destiny already clicked YES 💞✨
        </p>
    </div>
    """, unsafe_allow_html=True)

    time.sleep(1.2)
    go("question")

# ---------- LOVE LETTER PAGE ----------
elif st.session_state.page == "letter":
    st.markdown("""
    <div class="card">
        <div class="envelope">✉️💗</div>
        <div class="title">A Letter For You</div>
    </div>
    """, unsafe_allow_html=True)

    time.sleep(1.2)

    st.markdown("""
    <div class="letter">
        <p class="text">
        I would also like to talk a bit about how I feel about you.  
        I adore you. Everything you do amazes me.  
        I cherish you......respect you.....love you.....care for you......  
        wanna protect you......take care of you.  
        <br><br>
        Not to be dramatic or anything but I worship the ground you walk on.  
        You are literally the prince charming they talk about in the fairy tales.  
        <br><br>
        I want u to forever know ur worth.  
        I know ur value.....I know ur worth.....  
        So I know how to cherish you....  
        and once again ur heart is safe with me.....  
        <br><br>
        I love you baby with everything I have in me......  
        every bit of love that I have left in me  
        I'll pour it into you. 💖
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.write("")
    if st.button("Back to Valentine 💕"):
        go("question")
