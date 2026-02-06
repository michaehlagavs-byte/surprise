import streamlit as st
import random

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="For You ❤️", page_icon="💌", layout="centered")

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
    <div class="gerbera-container">
        🌸 💛 🌸 💛 🌸 💛
    </div>
    """, unsafe_allow_html=True)

def floating_hearts_flowers():
    st.markdown("""
    <style>
    .float-confetti {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        pointer-events: none;
        z-index: 9999;
    }
    .float-confetti span {
        position: absolute;
        font-size: 24px;
        animation: floatUpConfetti linear infinite;
        opacity: 0.8;
    }
    @keyframes floatUpConfetti {
        0% { transform: translateY(100vh) rotate(0deg); opacity: 1; }
        100% { transform: translateY(-10vh) rotate(360deg); opacity: 0; }
    }
    </style>
    <div class="float-confetti">
        <span style="left:10%; animation-duration:6s;">🌸</span>
        <span style="left:20%; animation-duration:8s;">💛</span>
        <span style="left:30%; animation-duration:7s;">💖</span>
        <span style="left:40%; animation-duration:9s;">🌹</span>
        <span style="left:50%; animation-duration:6s;">🌸</span>
        <span style="left:60%; animation-duration:8s;">💛</span>
        <span style="left:70%; animation-duration:7s;">💖</span>
        <span style="left:80%; animation-duration:9s;">🌹</span>
    </div>
    """, unsafe_allow_html=True)

def confetti_burst():
    st.markdown("""
    <style>
    .confetti {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        pointer-events: none;
        z-index: 9999;
    }
    .confetti span {
        position: absolute;
        font-size: 24px;
        animation: confettiFall linear infinite;
        opacity: 0.8;
    }
    @keyframes confettiFall {
        0% { transform: translateY(0vh) rotate(0deg); opacity: 1; }
        100% { transform: translateY(100vh) rotate(360deg); opacity: 0; }
    }
    </style>
    <div class="confetti">
        """ + "".join([f'<span style="left:{i*10}%; animation-duration:{random.randint(3,8)}s;">{random.choice(["💖","🌸","💛","🌹"])}</span>' for i in range(10)]) + """
    </div>
    """, unsafe_allow_html=True)

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>
body {
    background-color: #ff4b4b;
    background-image: url('https://i.imgur.com/f1Z5m6M.png');
    background-size: 80px;
    background-repeat: repeat;
}
@keyframes pulse {0%{transform:scale(1);}50%{transform:scale(1.08);}100%{transform:scale(1);}}
.stButton>button {
    background-color:#ff8b8b;
    color:white;
    font-size:18px;
    padding:12px 30px;
    border-radius:30px;
    border:none;
    animation:pulse 2s infinite;
}
.envelope {
    width: 80%;
    max-width: 600px;
    margin: 20px auto;
    padding: 20px;
    background-color: #fff0f0;
    border: 2px solid #ff4b4b;
    border-radius: 15px;
    box-shadow: 0 0 20px rgba(0,0,0,0.2);
}
.fade-in {animation: fadeIn 2s ease-in forwards;}
@keyframes fadeIn {from{opacity:0;}to{opacity:1;}}
</style>
""", unsafe_allow_html=True)

# ---------------- SESSION STATES ----------------
for key in ["unlocked","q1_done","q2_done","photo_shown","letter_opened","photo_index","photo_music_playing"]:
    if key not in st.session_state:
        st.session_state[key] = False
st.session_state.setdefault("photo_index", 0)
st.session_state.setdefault("photo_music_playing", False)

# ---------------- PASSWORD ----------------
if not st.session_state.unlocked:
    st.markdown("<h1 style='text-align:center;'>🔐 A Secret Just for You</h1>", unsafe_allow_html=True)
    pwd = st.text_input("Enter the password", type="password")
    if pwd == "1213":
        st.session_state.unlocked = True
        st.rerun()
    else:
        st.info("Hint: date of second day DSPC 2025 ❤️")
    st.stop()

# ---------------- WELCOME ----------------
st.markdown("<h1 style='text-align:center; color:white;'>Hi, Zeqq ❤️</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:white;'>I made this little quiz just for you 🥰</p>", unsafe_allow_html=True)
st.markdown("---")

# ---------------- STAGE 1: QUIZ ----------------
if not st.session_state.q1_done:
    st.audio("music.mp3", autoplay=True, loop=True)
    ans1 = st.text_input("1️⃣ What is my favorite activity?")
    if st.button("Submit Answer 1"):
        if ans1.lower() in ["matulog", "sleeping", "reading", "magbasa"]:
            st.success("Correct! 🥰")
            confetti_burst()
            st.session_state.q1_done = True
            st.rerun()
        else:
            st.error("Try again 😏")

elif not st.session_state.q2_done:
    st.audio("music.mp3", autoplay=True, loop=True)
    ans2 = st.text_input("2️⃣ When was the first time you saw me? (MM/DD/Y)")
    if st.button("Submit Answer 2"):
        if ans2 in ["08/29/25", "August 29 2025"]:
            st.success("Correct! 🥰")
            confetti_burst()
            st.session_state.q2_done = True
            st.rerun()
        else:
            st.error("Almost 😏")

# ---------------- STAGE 2: PHOTO ----------------
elif not st.session_state.photo_shown:
    # play special song once when entering photo stage
    if not st.session_state.photo_music_playing:
        st.session_state.photo_music_playing = True
        st.audio("special_song.mp3", autoplay=True, loop=True)
    st.markdown("<h2 style='text-align:center; color:white;'>A memory I want to share 🤍</h2>", unsafe_allow_html=True)
    
    # Multiple photos example (collage/scrollable)
    photos = ["memory.jfif","memory2.jfif","memory3.jfif","memory4.jfif"]
    st.image(photos[st.session_state.photo_index], use_container_width=True)
    
    col1, col2 = st.columns([1,1])
    with col1:
        if st.button("⬅️ Previous"):
            st.session_state.photo_index = max(0, st.session_state.photo_index - 1)
    with col2:
        if st.button("➡️ Next"):
            st.session_state.photo_index = min(len(photos)-1, st.session_state.photo_index + 1)
    
    floating_hearts_flowers()  # floating hearts and flowers
    
    if st.button("💌 Continue"):
        st.session_state.photo_shown = True
        st.session_state.photo_music_playing = False  # stop special_song
        st.rerun()

# ---------------- STAGE 3: LETTER ----------------
elif not st.session_state.letter_opened:
    st.audio("music.mp3", autoplay=True, loop=True)
    st.subheader("💌 Your reward: My letter")
    st.image("d02276b6-733b-490f-9994-6628b8628641.webp", width=300)
    gerbera_animation()
    
    if st.button("💖 Open Letter"):
        st.session_state.letter_opened = True
        st.rerun()

# ---------------- FINAL CONFESSION LETTER ----------------
else:
    st.subheader("💌 Your reward: My letter")

    if not st.session_state.letter_opened:
        # Show uploaded envelope image first
        st.image("d02276b6-733b-490f-9994-6628b8628641.webp", width=300)

        # Gerbera animation behind the envelope (optional)
        gerbera_animation()

        if st.button("💖 Open Letter"):
            st.session_state.letter_opened = True
            st.rerun()
    else:
        # Show the white paper with confession
        st.markdown('<div class="fade-in envelope">', unsafe_allow_html=True)
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

        # 🌸 End-of-letter flourish: 2 pink, 2 yellow, 2 red flowers
        st.markdown("""
        <div style="text-align:center; font-size:40px;">
            🌸 🌸 💛 💛 🌹 🌹
        </div>
        """, unsafe_allow_html=True)

        st.markdown('</div>', unsafe_allow_html=True)











