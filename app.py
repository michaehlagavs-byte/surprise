import streamlit as st
import time

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="For You ❤️", page_icon="💌", layout="centered")

# ---------------- STYLES ----------------
st.markdown("""
<style>
.stApp {
    background: linear-gradient(180deg, #ffe6ee, #fff5f8);
    color: black;
}

h1, h2, h3, h4, h5, h6, p, span, div {
    color: black !important;
}

.stButton>button {
    background-color: #ff4d6d !important;
    color: white !important;
    font-weight: bold;
    border-radius: 8px;
    border: none;
    padding: 8px 20px;
}
.stButton>button:hover {
    background-color: #ff2a4a !important;
}

/* Fade-in animation */
.fade-in {
    animation: fadeIn 2s ease-in-out;
}
@keyframes fadeIn {
    from { opacity: 0; transform: translateY(20px); }
    to { opacity: 1; transform: translateY(0); }
}

/* Envelope */
.envelope {
    width: 220px;
    transition: transform 0.4s ease;
}
.envelope:hover {
    transform: scale(1.05);
}
</style>
""", unsafe_allow_html=True)

# ---------------- EFFECTS ----------------
def floating_hearts():
    st.markdown("""
    <div style="position:fixed; inset:0; pointer-events:none; z-index:9999;">
        <div style="position:absolute; left:10%; top:-10%; animation:fall 7s linear infinite;">💖</div>
        <div style="position:absolute; left:30%; top:-10%; animation:fall 9s linear infinite;">🌸</div>
        <div style="position:absolute; left:50%; top:-10%; animation:fall 8s linear infinite;">💛</div>
        <div style="position:absolute; left:70%; top:-10%; animation:fall 6s linear infinite;">🌹</div>
    </div>

    <style>
    @keyframes fall {
        0% { transform: translateY(-10vh); }
        100% { transform: translateY(110vh); }
    }
    </style>
    """, unsafe_allow_html=True)

# ---------------- SESSION ----------------
defaults = {
    "unlocked": False,
    "q1_done": False,
    "q2_done": False,
    "photo_stage": False,
    "letter_opened": False,
    "photo_index": 0,
}
for k, v in defaults.items():
    st.session_state.setdefault(k, v)

# ---------------- PASSWORD ----------------
if not st.session_state.unlocked:
    st.title("🔐 A Secret Just for You")
    st.caption("💡 Hint: month and day of the second day of DSPC")

    pwd = st.text_input("Enter the password", type="password")

    if pwd == "1213":
        st.session_state.unlocked = True
        st.rerun()
    elif pwd != "":
        st.warning("Almost… think of DSPC 💭")

    st.stop()

# ---------------- QUIZ ----------------
if not st.session_state.q1_done:
    ans = st.text_input("1️⃣ What is my favorite activity?")
    if st.button("Submit"):
        if ans.lower() in ["matulog", "sleeping", "reading", "magbasa"]:
            st.session_state.q1_done = True
            st.rerun()

elif not st.session_state.q2_done:
    ans = st.text_input("2️⃣ When was the first time you saw me? (MM/DD/Y)")
    if st.button("Submit"):
        if ans in ["08/29/25", "August 29 2025"]:
            st.session_state.q2_done = True
            st.rerun()

# ---------------- PHOTOS ----------------
elif not st.session_state.photo_stage:

    photos = ["memory.jfif", "memory2.jfif", "memory3.jfif", "memory4.jfif"]
    st.image(photos[st.session_state.photo_index], use_container_width=True)

    col1, col2 = st.columns(2)
    with col1:
        if st.button("⬅️ Previous"):
            st.session_state.photo_index = max(0, st.session_state.photo_index - 1)
            st.rerun()
    with col2:
        if st.button("➡️ Next"):
            st.session_state.photo_index = min(len(photos)-1, st.session_state.photo_index + 1)
            st.rerun()

    floating_hearts()

    if st.button("💌 Continue"):
        st.session_state.photo_stage = True
        st.rerun()

# ---------------- FINAL LETTER ----------------
else:
    st.subheader("💌 Your reward")

    if not st.session_state.letter_opened:
        st.markdown("""
        <div style="text-align:center;">
            <img src="https://cdn-icons-png.flaticon.com/512/561/561127.png" class="envelope">
            <p>Click to open 💖</p>
        </div>
        """, unsafe_allow_html=True)

        if st.button("💖 Open Letter"):
            st.session_state.letter_opened = True
            st.rerun()

    else:
        # 🎵 Music starts here
        st.audio("special_song.mp3", loop=True)

        floating_hearts()

        # ✨ Typewriter letter
        letter = """
Dear Zeqq,

I’ve been meaning to write this for a while now because there are things I genuinely want to thank you for. Some feelings are hard to say out loud, so I thought writing them might be better. Over time, I realized how much I appreciate what we have. And I didn’t want to let that go unspoken.

What started as something simple and unexpected slowly became meaningful to me. It wasn’t something I planned or overthought, but it grew naturally. Looking back, I’m really glad things turned out this way. Sometimes the best connections really do come when you least expect them.

There were moments when everything felt overwhelming, and somehow, your presence made things feel lighter. You became someone I could rely on in quiet ways. Even without saying much, there was comfort just knowing you were there. And that kind of presence means more than words can explain.

I also appreciate the small things you’ve done along the way. The effort, the thought, and the sincerity behind them didn’t go unnoticed. Those simple moments stayed with me more than you probably think. They made me feel seen and appreciated in a genuine way.

Because of you, I’ve learned to open up a little more. I used to keep my guard up and hesitate to let people in. But with you, things felt different—easier and more natural. You didn’t force anything, and that made it easier for me to trust.

I’m also grateful for the patience and understanding you’ve shown. Not everyone takes the time to understand someone the way you did. You gave me space when I needed it and stayed when it mattered. That balance is something I truly value.

What we have now is something I don’t take for granted. It may seem simple, but it’s real and meaningful to me. It’s built on shared moments, understanding, and genuine presence. And that’s something I want to keep.

Thank you for being there, for your presence, and for everything you’ve shared with me. I’m truly grateful for you and for the bond we’ve built. No matter where things go, I’ll always appreciate what we have.

Always,
Ehla ❤️
"""

        placeholder = st.empty()
        typed = ""

        for char in letter:
            typed += char
            placeholder.markdown(f"<div class='fade-in'><p>{typed}</p></div>", unsafe_allow_html=True)
            time.sleep(0.015)

























