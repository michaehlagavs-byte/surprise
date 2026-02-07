import streamlit as st
import random

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
    st.title("🔐 A Secret Just for You")
    st.caption("💡 Hint: month and day of the second day of DSPC")

    pwd = st.text_input("Enter the password", type="password", placeholder="MMDD")

    if pwd == "1213":
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

    photos = ["memory.jfif", "memory2.jfif", "memory3.jfif", "memory4.jfif"]
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
    st.subheader("💌 Your reward: My letter")

    if not st.session_state.letter_opened:
        st.image("d02276b6-733b-490f-9994-6628b8628641.webp", width=300)
        gerbera_animation()

        if st.button("💖 Open Letter"):
            st.session_state.letter_opened = True
            st.rerun()

    else:
        st.markdown("""
        <h3>📩 Opened with love</h3>
        <p>
       Dear Zeqq,<br><br>

        I’ve been carrying these thoughts in my heart for a while now, and I think it’s finally time I let them out.<br><br>

        I only recently realized how much you mean to me—and maybe that’s what makes this confession feel so real.
        Nothing was rushed, nothing was forced. It grew quietly, gently, until one day I just knew.<br><br>

        Since we started talking on <b>September 28</b>, everything slowly changed. What began as something unexpected—
        because of a dare—turned into something I’m deeply grateful for. You were there during <b>DSPC</b>, and your
        presence meant more than you probably realized. In moments when things felt overwhelming, you were someone I
        could look at and feel calm. Safe.<br><br>

        And then there were the gifts. The thought you put into them. But most of all… the flowers.<br><br>

        The <b>six gerberas</b> you gave me—<b>three pink and three yellow</b>—will always stay with me. That was my first
        time receiving flowers. Ever. And I don’t think you understand how much that meant to someone like me.
        Pink for warmth and affection, yellow for happiness and light—you gave me both. That moment changed something
        in me. It made me feel valued, appreciated, and cared for in a way I had never experienced before.<br><br>

        I’ve always been someone who kept her guard up. I used to say I was a “man hater,” and maybe in some ways I was—
        because I was scared. Scared of trusting, scared of being disappointed, scared of opening my heart.
        You’re the <b>first guy I ever truly talked to</b>, the first one I allowed close, and that wasn’t easy for me.
        But you made it feel natural. You were patient. Kind. Gentle.<br><br>

        Thinking back to <b>August 29</b>, the first time you saw me—and when you confessed—I didn’t realize then how much
        that moment would matter. I didn’t realize how your sincerity would slowly break down walls I thought would
        always stay up.<br><br>

        Now I understand.<br><br>

        I like you, Zeqq. Truly. Deeply. In a way that feels honest and real. You’ve changed how I see things—how I see
        people, how I see love, how I see the possibility of trusting someone. You didn’t force your way into my heart.
        You earned your place there.<br><br>

        Thank you for being there. Thank you for the gifts, the flowers, the effort, the presence. Thank you for being
        patient with someone who was learning how to feel again.<br><br>

        This is my confession, from the heart. And I hope you know how special you are to me.<br><br>

        Always,<br>
        <b>Ehla ❤️</b>
        </p>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div style="text-align:center; font-size:40px;">
            🌸 🌸 💛 💛 🌹 🌹
        </div>
        """, unsafe_allow_html=True)























