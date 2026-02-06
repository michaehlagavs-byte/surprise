import streamlit as st
import random

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="For You ❤️", page_icon="💌", layout="centered")

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>
body {
    background-color: #ff4b4b;
    background-image: url('https://i.imgur.com/f1Z5m6M.png');
    background-size: 80px;
    background-repeat: repeat;
}

/* Button animation */
@keyframes pulse {0%{transform:scale(1);}50%{transform:scale(1.08);}100%{transform:scale(1);}}
.stButton>button {background-color:#ff8b8b;color:white;font-size:18px;padding:12px 30px;border-radius:30px;border:none;animation:pulse 2s infinite;transition:all 0.3s ease-in-out;}
.stButton>button:hover {background-color:#ffb3b3;transform:scale(1.12);}

/* Floating animation */
@keyframes floatUp {0%{transform:translateY(0);}100%{transform:translateY(-100vh);}}
.balloon {position:absolute;font-size:40px;animation:floatUp 3s ease-in forwards;}
.hearts {position:fixed;bottom:0;width:100%;text-align:center;font-size:22px;animation:floatUp 6s infinite;opacity:0.6;}

/* Envelope / letter */
.envelope {
    width: 80%;
    max-width: 600px;
    margin: 20px auto;
    padding: 20px;
    background-color: #fff0f0;
    border: 2px solid #ff4b4b;
    border-radius: 15px;
    box-shadow: 0 0 20px rgba(0,0,0,0.2);
    text-align: left;
    position: relative;
    z-index: 1000;
}
.envelope h3 {text-align:center;color:#ff4b4b;}
.envelope p {color:black; font-size:16px; line-height:1.7;}
.fade-in {animation:fadeIn 2s ease-in forwards;}
@keyframes fadeIn {from{opacity:0;}to{opacity:1;}}

/* Gerbera flowers */
.gerbera {position:absolute; font-size:30px; animation: floatGerbera 4s linear forwards;}
@keyframes floatGerbera {0% {transform: translateY(0);} 100% {transform: translateY(100vh);}}
</style>
""", unsafe_allow_html=True)

# ---------------- PASSWORD ----------------
if "unlocked" not in st.session_state:
    st.session_state.unlocked = False

if not st.session_state.unlocked:
    st.markdown("<h1 style='text-align:center;'>🔐 A Secret Just for You</h1>", unsafe_allow_html=True)
    password = st.text_input("Enter the password", type="password")
    if password == "1213":
        st.session_state.unlocked = True
        st.rerun()
    else:
        st.info("Hint: date of second day DSPC 2025 ❤️")
    st.stop()

# ---------------- MUSIC ----------------
if "music_played" not in st.session_state:
    st.session_state.music_played = False

if not st.session_state.music_played:
    if st.button("🎵 Play Background Music"):
        try:
            with open("music.mp3", "rb") as audio_file:
                st.audio(audio_file.read(), format="audio/mp3", autoplay=True, loop=True)
            st.session_state.music_played = True
        except:
            st.warning("🎶 Music file not found. The surprise still works!")
else:
    try:
        with open("music.mp3", "rb") as audio_file:
            st.audio(audio_file.read(), format="audio/mp3", autoplay=True, loop=True)
    except:
        st.warning("🎶 Music file not found. The surprise still works!")

# ---------------- WELCOME MESSAGE ----------------
st.markdown("<h1 style='text-align:center; color:#fff;'>Hi, Zeqq ❤️</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:#fff;'>I made this little quiz just for you 🥰</p>", unsafe_allow_html=True)
st.markdown("---")

# ---------------- QUIZ STATE ----------------
if "q1_done" not in st.session_state:
    st.session_state.q1_done = False
if "q2_done" not in st.session_state:
    st.session_state.q2_done = False

# ---------------- LETTER STATE ----------------
if "letter_opened" not in st.session_state:
    st.session_state.letter_opened = False

# ---------------- HELPER FUNCTIONS ----------------
def heart_confetti():
    hearts = ["💖","💘","💕","💗","💞"]
    confetti_html = ""
    for i in range(30):
        heart = random.choice(hearts)
        left = random.randint(0,90)
        top = random.randint(0,90)
        size = random.randint(20,40)
        confetti_html += f'<div style="position:absolute; top:{top}%; left:{left}%; font-size:{size}px;">{heart}</div>'
    st.markdown(confetti_html, unsafe_allow_html=True)

def balloon_animation():
    for i in range(5):
        left_pos = random.randint(0,90)
        st.markdown(f'<div class="balloon" style="left:{left_pos}%;">💖</div>', unsafe_allow_html=True)

def gerbera_animation():
    flowers = ["🌸","💛"]  # pink and yellow
    gerbera_html = ""
    for i in range(20):
        flower = random.choice(flowers)
        left = random.randint(0,95)
        gerbera_html += f'<div class="gerbera" style="left:{left}%;">{flower}</div>'
    st.markdown(gerbera_html, unsafe_allow_html=True)

# ---------------- QUIZ ----------------
if not st.session_state.q1_done:
    st.subheader("1️⃣ What is my favorite activity?")
    answer1 = st.text_input("Your answer here", key="answer1")

    if st.button("Submit Answer 1"):
        if answer1.lower() in ["matulog", "sleeping", "reading", "magbasa"]:
            st.success("Correct! 🥰")
            heart_confetti()
            balloon_animation()
            gerbera_animation()
            st.session_state.q1_done = True
            st.rerun()
        else:
            st.error("Hmm… try again 😏")
elif not st.session_state.q2_done:
    st.subheader("2️⃣ When was the first time you saw me?")
    answer2 = st.text_input("Type the date (MM/DD/Y)", key="answer2")
    if st.button("Submit Answer 2"):
        if answer2 in ["08/29/25", "August 29 2025"]:
            st.success("Correct! 🥰")
            heart_confetti()
            balloon_animation()
            gerbera_animation()
            st.session_state.q2_done = True
            st.rerun()
        else:
            st.error("Close, but not quite 😏")

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

# ---------------- FLOATING HEARTS (only during quiz) ----------------
if not st.session_state.letter_opened:
    st.markdown('<div class="hearts">💖 💕 💘 💗 💞</div>', unsafe_allow_html=True)

# ---------------- CONTINUOUS CONFETTI AND BALLOONS (only during quiz) ----------------
if not st.session_state.letter_opened:
    heart_confetti()
    balloon_animation()

