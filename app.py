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
    st.session_state.page = "intro"

# ---------- GLOBAL CSS + JS ----------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Pacifico&family=Quicksand:wght@400;600&display=swap');

html, body, [class*="css"]  {
    font-family: 'Quicksand', sans-serif;
    background: linear-gradient(135deg, #ffe4f1, #ffd1e8);
}

/* Hide default cursor */
body { cursor: none; }

/* Custom heart cursor */
.heart-cursor {
    position: fixed;
    width: 22px;
    height: 22px;
    background: pink;
    transform: rotate(45deg);
    pointer-events: none;
    z-index: 9999;
}
.heart-cursor::before,
.heart-cursor::after {
    content: "";
    position: absolute;
    width: 22px;
    height: 22px;
    background: pink;
    border-radius: 50%;
}
.heart-cursor::before { top: -11px; left: 0; }
.heart-cursor::after { left: -11px; top: 0; }

/* Sparkles */
.sparkle {
    position: fixed;
    font-size: 12px;
    pointer-events: none;
    animation: fadeOut 1s forwards;
    z-index: 9998;
}
@keyframes fadeOut {
    from {opacity: 1; transform: scale(1);}
    to {opacity: 0; transform: scale(2);}
}

/* Floating teddy bears */
.teddy-float {
    position: fixed;
    font-size: 45px;
    animation: float 6s infinite ease-in-out;
    opacity: 0.7;
    z-index: 0;
}
.t1 { left: 5%; top: 10%; }
.t2 { left: 85%; top: 20%; }
.t3 { left: 10%; top: 70%; }
.t4 { left: 80%; top: 75%; }

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

/* Glow buttons */
.glow-btn {
    background: linear-gradient(45deg, #ff7eb3, #ffb3d9);
    color: white;
    border-radius: 40px;
    padding: 14px 35px;
    font-size: 17px;
    border: none;
    cursor: pointer;
    animation: glow 2s infinite alternate;
}
@keyframes glow {
    from { box-shadow: 0 0 10px #ff7eb3; }
    to { box-shadow: 0 0 25px #ffb3d9; }
}

/* Envelope + Letter */
.envelope { font-size: 120px; }
.letter {
    background: #fffafc;
    border-radius: 25px;
    padding: 35px;
    margin-top: 20px;
    box-shadow: 0 0 25px rgba(255,105,180,0.25);
}

/* Animations */
@keyframes pop {
    from {transform: scale(0.85); opacity: 0;}
    to {transform: scale(1); opacity: 1;}
}
</style>

<div class="teddy-float t1">🧸</div>
<div class="teddy-float t2">🧸</div>
<div class="teddy-float t3">🧸</div>
<div class="teddy-float t4">🧸</div>

<script>
const cursor = document.createElement("div");
cursor.classList.add("heart-cursor");
document.body.appendChild(cursor);

document.addEventListener("mousemove", e => {
    cursor.style.left = e.clientX + "px";
    cursor.style.top = e.clientY + "px";

    const sparkle = document.createElement("div");
    sparkle.classList.add("sparkle");
    sparkle.innerHTML = "✨";
    sparkle.style.left = e.clientX + "px";
    sparkle.style.top = e.clientY + "px";
    document.body.appendChild(sparkle);

    setTimeout(() => sparkle.remove(), 900);
});
</script>
""", unsafe_allow_html=True)

# ---------- NAV ----------
def go(page):
    st.session_state.page = page
    st.rerun()

# ---------- INTRO PAGE ----------
if st.session_state.page == "intro":
    st.markdown("""
    <div class="card">
        <div class="title">For the boy who owns my heart 💕</div>
        <p class="text">A little digital love story just for you 🎬</p>
    </div>
    """, unsafe_allow_html=True)

    if st.button("Enter My Heart 💗"):
        go("question")

# ---------- QUESTION PAGE ----------
elif st.session_state.page == "question":
    st.markdown("""
    <div class="card">
        <div class="title">Will You Be My Valentine?</div>
        <p class="text">I made all of this just for you 🥺💗</p>
    </div>
    """, unsafe_allow_html=True)

    c1, c2, c3 = st.columns(3)
    with c1:
        if st.button("YES 🥰", key="yes"):
            go("yes")
    with c2:
        if st.button("NO 🙈", key="no"):
            go("no")
    with c3:
        if st.button("💌 Open Love Letter"):
            go("letter")

# ---------- YES PAGE ----------
elif st.session_state.page == "yes":
    st.balloons()
    st.markdown("""
    <div class="card">
        <div class="title">YAYYYYY 💖</div>
        <p class="text">You just made my heart the happiest place on earth 🥹💗</p>
    </div>
    """, unsafe_allow_html=True)

    if st.button("Final Scene 🎬"):
        go("end")

# ---------- NO PAGE ----------
elif st.session_state.page == "no":
    st.markdown("""
    <div class="card">
        <div class="title">Wrong Answer 😌</div>
        <p class="text">That option is just decoration 💕</p>
    </div>
    """, unsafe_allow_html=True)

    time.sleep(1.2)
    go("question")

# ---------- LOVE LETTER PAGE (TYPEWRITER EFFECT) ----------
elif st.session_state.page == "letter":
    st.markdown("""
    <div class="card">
        <div class="envelope">✉️💗</div>
        <div class="title">A Letter For You</div>
    </div>
    """, unsafe_allow_html=True)

    letter_lines = [
        "I would also like to talk a bit about how I feel about you.",
        "I adore you. Everything you do amazes me.",
        "I cherish you... respect you... love you... care for you...",
        "wanna protect you... take care of you.",
        "Not to be dramatic or anything but I worship the ground you walk on.",
        "You are literally the prince charming they talk about in fairy tales.",
        "I want you to forever know your worth.",
        "I know your value... I know your worth...",
        "So I know how to cherish you...",
        "and once again your heart is safe with me...",
        "I love you baby with everything I have in me...",
        "every bit of love I have left in me, I'll pour it into you 💖"
    ]

    placeholder = st.empty()
    full_text = ""
    for line in letter_lines:
        full_text += line + "\n\n"
        placeholder.markdown(f"<div class='letter'><p class='text'>{full_text}</p></div>", unsafe_allow_html=True)
        time.sleep(0.9)

    if st.button("Back 💕"):
        go("question")

# ---------- ENDING PAGE ----------
elif st.session_state.page == "end":
    st.markdown("""
    <div class="card">
        <div class="title">No matter what happens in life…</div>
        <p class="text">
        You will always be my Valentine 💕<br><br>
        Always chosen. Always safe. Always loved. 💗
        </p>
    </div>
    """, unsafe_allow_html=True)
