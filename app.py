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

# ---------- GLOBAL CSS + JS ----------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Pacifico&family=Quicksand:wght@400;600&display=swap');

html, body, [class*="css"]  {
    font-family: 'Quicksand', sans-serif;
    background: linear-gradient(135deg, #ffe4f1, #ffd1e8);
    overflow-x: hidden;
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

/* Card UI */
.card {
    background: rgba(255,255,255,0.92);
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
}

.emoji {
    font-size: 65px;
    animation: float 2s infinite ease-in-out;
}

/* BIG CUTE BUTTONS */
div.stButton > button {
    width: 100%;
    padding: 20px 0;
    font-size: 22px;
    border-radius: 50px;
    border: none;
    font-weight: 600;
    transition: all 0.3s ease;
    animation: pulse 2.5s infinite;
}

/* YES button */
div.stButton:nth-of-type(1) > button {
    background: linear-gradient(45deg, #ff6fae, #ffb6d5);
    color: white;
    box-shadow: 0 0 25px rgba(255,111,174,0.6);
}

/* NO button */
div.stButton:nth-of-type(2) > button {
    background: white;
    color: #ff6fae;
    border: 3px dashed #ff6fae;
}

/* Hover effect */
div.stButton > button:hover {
    transform: scale(1.08);
    box-shadow: 0 0 35px rgba(255,105,180,0.8);
}

/* Click effect */
div.stButton > button:active {
    transform: scale(0.95);
}

/* Button pulse animation */
@keyframes pulse {
    0% {box-shadow: 0 0 15px rgba(255,105,180,0.4);}
    50% {box-shadow: 0 0 30px rgba(255,105,180,0.8);}
    100% {box-shadow: 0 0 15px rgba(255,105,180,0.4);}
}

@keyframes pop {
    from {transform: scale(0.9); opacity: 0;}
    to {transform: scale(1); opacity: 1;}
}
</style>

<!-- Floating Teddies -->
<div class="teddy teddy1">🧸</div>
<div class="teddy teddy2">🧸</div>
<div class="teddy teddy3">🧸</div>
<div class="teddy teddy4">🧸</div>

<!-- Sparkle Cursor -->
<script>
document.addEventListener("mousemove", function(e) {
    let sparkle = document.createElement("div");
    sparkle.innerHTML = "✨";
    sparkle.style.position = "fixed";
    sparkle.style.left = e.clientX + "px";
    sparkle.style.top = e.clientY + "px";
    sparkle.style.pointerEvents = "none";
    sparkle.style.fontSize = "14px";
    sparkle.style.opacity = "0.8";
    sparkle.style.animation = "sparkFade 1s ease-out forwards";
    sparkle.style.zIndex = "9999";
    document.body.appendChild(sparkle);

    setTimeout(() => {
        sparkle.remove();
    }, 1000);
});
</script>

<style>
@keyframes sparkFade {
    0% {transform: scale(1); opacity: 1;}
    100% {transform: scale(2); opacity: 0;}
}
</style>
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
    c1, c2 = st.columns(2)

    with c1:
        if st.button("YES 🥰🧁"):
            go("yes")

    with c2:
        if st.button("NO 🙈"):
            go("no")

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

    st.write("")
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

    time.sleep(1.3)
    st.info("Redirecting you to love central... 💕🧁")
    time.sleep(1.3)
    go("question")
