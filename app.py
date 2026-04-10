import streamlit as st
import random
import time

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="For You ❤️", page_icon="💌", layout="centered")
st.markdown("""
<style>
/* Global background + font color */
.stApp {
    background: linear-gradient(180deg, #ffe6ee, #fff5f8);
    color: black;
}

/* All headings and text */
h1, h2, h3, h4, h5, h6, p, span, div {
    color: black !important;
}

/* Streamlit buttons */
.stButton>button {
    background-color: #ff4d6d !important; /* red */
    color: white !important;               /* font color */
    font-weight: bold;
    border-radius: 8px;
    border: none;
    padding: 8px 20px;
}
.stButton>button:hover {
    background-color: #ff2a4a !important; /* darker red on hover */
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<style>
.stApp {
    background: linear-gradient(180deg, #ffe6ee, #fff5f8);
    color: black;  /* sets font color globally */
}

/* Optional: make all headings also black */
h1, h2, h3, h4, h5, h6, p, span, div {
    color: black !important;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<style>
.stApp {
    background: linear-gradient(180deg, #ffe6ee, #fff5f8);
}
</style>
""", unsafe_allow_html=True)

# ---------------- FUNCTIONS ----------------
def gerbera_animation():
    st.markdown("""
    <style>
    .gerbera-container {
        position: fixed;
        bottom: -10%;
        left: 0;
        width: 100%;
        text-align: center;
        font-size: 38px;
        animation: floatUp 8s linear infinite;
        opacity: 0.6;
        pointer-events: none;
        z-index: -1;
    }
    @keyframes floatUp {
        0% { transform: translateY(0); opacity: 0; }
        20% { opacity: 0.8; }
        100% { transform: translateY(-120vh); opacity: 0; }
    }
    </style>
    <div class="gerbera-container">🌸 💛 🌸 💛 🌸 💛</div>
    """, unsafe_allow_html=True)

def floating_hearts_flowers():
    st.markdown("""
    <style>
    .confetti {
        position: fixed;
        inset: 0;
        pointer-events: none;
        z-index: 9999;
    }
    .confetti span {
        position: absolute;
        top: -10%;
        font-size: 26px;
        animation: fall linear infinite;
        opacity: 0.85;
    }
    @keyframes fall {
        0% {
            transform: translateY(-10vh) rotate(0deg);
            opacity: 1;
        }
        100% {
            transform: translateY(110vh) rotate(360deg);
            opacity: 0;
        }
    }
    </style>

    <div class="confetti">
        <span style="left:5%;  animation-duration:6s;">🌸</span>
        <span style="left:15%; animation-duration:8s;">💖</span>
        <span style="left:30%; animation-duration:7s;">💛</span>
        <span style="left:45%; animation-duration:9s;">🌹</span>
        <span style="left:60%; animation-duration:6.5s;">🌸</span>
        <span style="left:75%; animation-duration:8.5s;">💖</span>
        <span style="left:90%; animation-duration:7.5s;">💛</span>
    </div>
    """, unsafe_allow_html=True)

def confetti_burst():
    st.markdown("""
    <div style="position:fixed;top:0;width:100%;text-align:center;font-size:32px;">
        🎉 💖 🌸 💛 🌹 🎉
    </div>
    """, unsafe_allow_html=True)

# ---------------- SESSION STATES ----------------
defaults = {
    "unlocked": False,
    "q1_done": False,
    "q2_done": False,
    "photo_stage": False,
    "letter_opened": False,
    "photo_index": 0,
    "photo_music_playing": False
}
for k, v in defaults.items():
    st.session_state.setdefault(k, v)

# ---------------- PASSWORD ----------------
if not st.session_state.unlocked:
    st.title("🔐 Letters the Heart Never Sent")
    st.caption("💡 Hint: my birthday")

    pwd = st.text_input("Enter the password", type="password", placeholder="MMDD")

    if pwd == "1214":
        st.session_state.unlocked = True
        st.rerun()
    elif pwd != "":
        st.warning("Almost… think of DSPC 💭")

    st.stop()

# ---------------- QUIZ ----------------
if not st.session_state.q1_done:
    st.audio("music.mp3", autoplay=True, loop=True)
    ans = st.text_input("1️⃣ What is my favorite activity?")
    if st.button("Submit"):
        if ans.lower() in ["matulog", "sleeping", "reading", "magbasa"]:
            confetti_burst()
            st.session_state.q1_done = True
            st.rerun()

elif not st.session_state.q2_done:
    st.audio("music.mp3", autoplay=True, loop=True)
    ans = st.text_input("2️⃣ When was the first time you saw me? (MM/DD/Y)")
    if st.button("Submit"):
        if ans in ["08/29/25", "August 29 2025"]:
            confetti_burst()
            st.session_state.q2_done = True
            st.rerun()

# ---------------- PHOTOS ----------------
elif not st.session_state.photo_stage:
    if not st.session_state.photo_music_playing:
        st.session_state.photo_music_playing = True

    st.audio("special_song.mp3", autoplay=True, loop=True)

    photos = ["memory.jfif", "memory2.jfif", "memory3.jfif", "memory4.jfif", "memory5.jfif", "memory6.jfif"]
    st.image(photos[st.session_state.photo_index], use_container_width=True)

    col1, col2 = st.columns(2)
    with col1:
        if st.button("⬅️ Previous"):
            st.session_state.photo_index = max(0, st.session_state.photo_index - 1)
            st.rerun()
    with col2:
        if st.button("➡️ Next"):
            confetti_burst()
            st.session_state.photo_index = min(len(photos)-1, st.session_state.photo_index + 1)
            st.rerun()

    floating_hearts_flowers()

    if st.button("💌 Continue"):
        st.session_state.photo_music_playing = False
        st.session_state.photo_stage = True
        st.rerun()

# ---------------- FINAL CONFESSION LETTER ----------------
else:
    st.subheader("💌 Your reward")

    if not st.session_state.letter_opened:
        st.markdown("""
        <div style="text-align:center;">
            <img src="https://cdn-icons-png.flaticon.com/512/561/561127.png">
            <p>Click to open 💖</p>
        </div>
        """, unsafe_allow_html=True)

        if st.button("💖 Open Letter"):
            st.session_state.letter_opened = True
            st.rerun()

    else:
        # 🎵 Music starts ONLY when letter is opened
        st.audio("Maybe The Night.mp3", autoplay=True, loop=True)

        floating_hearts_flowers()

        letter = """
Dear Zeqq,<br><br>

I’ve been meaning to write this for a while now because there are things I genuinely want to thank you for. Some feelings are hard to say out loud, so I thought writing them might be better. Over time, I realized how much I appreciate what we have. And I didn’t want to let that go unspoken.<br><br>

What started as something simple and unexpected slowly became meaningful to me. It wasn’t something I planned or overthought, but it grew naturally. Looking back, I’m really glad things turned out this way. Sometimes the best connections really do come when you least expect them.<br><br>

There were moments when everything felt overwhelming, and somehow, your presence made things feel lighter. You became someone I could rely on in quiet ways. Even without saying much, there was comfort just knowing you were there. And that kind of presence means more than words can explain.<br><br>

I also appreciate the small things you’ve done along the way. The effort, the thought, and the sincerity behind them didn’t go unnoticed. Those simple moments stayed with me more than you probably think. They made me feel seen and appreciated in a genuine way.<br><br>

Because of you, I’ve learned to open up a little more. I used to keep my guard up and hesitate to let people in. But with you, things felt different—easier and more natural. You didn’t force anything, and that made it easier for me to trust.<br><br>

I’m also grateful for the patience and understanding you’ve shown. Not everyone takes the time to understand someone the way you did. You gave me space when I needed it and stayed when it mattered. That balance is something I truly value.<br><br>

What we have now is something I don’t take for granted. It may seem simple, but it’s real and meaningful to me. It’s built on shared moments, understanding, and genuine presence. And that’s something I want to keep.<br><br>

Thank you for being there, for your presence, and for everything you’ve shared with me. I’m truly grateful for you and for the bond we’ve built. No matter where things go, I’ll always appreciate what we have.<br><br>

Always,<br>
<b>Ehla ❤️</b>
</p>
"""
        
        placeholder = st.empty()
        typed = ""

        for char in letter:
            typed += char
            placeholder.markdown(
                f"<div class='fade-in'><p>{typed}</p></div>",
                unsafe_allow_html=True
            )
            time.sleep(0.015)
























