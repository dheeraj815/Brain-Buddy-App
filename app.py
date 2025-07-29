import streamlit as st
import os
import mathquiz
import riddles
import animal
import funfacts
import spelling
import storypage
import rewardspage
import parent

# Set Streamlit page configuration
st.set_page_config(page_title="Brain Buddy Kids App 🧠",
                   page_icon="🧠", layout="centered")


# Load Pro Unlock status from session
def is_pro_user():
    return st.session_state.get("is_pro_user", False)


# Sidebar unlock system
st.sidebar.markdown("### 🔓 Unlock Features")
if st.sidebar.checkbox("✅ Unlock All Features (Pro - ₹199one-time)", value=is_pro_user()):
    st.session_state["is_pro_user"] = True
else:
    st.session_state["is_pro_user"] = False


# Sidebar Menu
menu = st.sidebar.radio("👉 Choose Activity", [
    "🏠 Home",
    "➕ Math Quiz",
    "🧠 Riddles",
    "🦁 Animal Quiz",
    "🎉 Fun Facts",
    "📝 Spelling Quiz",
    "📖 Story Time",
    "🏆 Rewards",
    "👨‍👩‍👧 Parent Dashboard"
])

# --- Main Content ---
if menu == "🏠 Home":
    st.markdown("<h1 style='text-align: center;'>🧠 Brain Buddy Kids App</h1>",
                unsafe_allow_html=True)
    st.subheader("Welcome to Brain Buddy!")
    st.markdown("""
        Choose an activity from the sidebar to begin your fun learning journey! 🎓🌟  
        Please unlock to access all 20 advanced questions and premium features.
    """)

elif menu == "➕ Math Quiz":
    mathquiz.main(pro=is_pro_user())

elif menu == "🧠 Riddles":
    riddles.main(pro=is_pro_user())

elif menu == "🦁 Animal Quiz":
    animal.main(pro=is_pro_user())

elif menu == "🎉 Fun Facts":
    funfacts.main(pro=is_pro_user())

elif menu == "📝 Spelling Quiz":
    spelling.main(pro=is_pro_user())

elif menu == "📖 Story Time":
    storypage.main(pro=is_pro_user())

elif menu == "🏆 Rewards":
    rewardspage.main()

elif menu == "👨‍👩‍👧 Parent Dashboard":
    parent.main()
