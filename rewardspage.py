import streamlit as st
import random


def main():
    st.set_page_config(page_title="🎉 Rewards Page",
                       page_icon="🎈", layout="centered")

    st.markdown("<h1 style='text-align: center; color: #FF69B4;'>🎉 Congratulations! 🎉</h1>",
                unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center;'>Your child has completed amazing activities!</h3>",
                unsafe_allow_html=True)

    # List of celebratory messages
    messages = [
        "🌟 You're a Superstar!",
        "🎈 Keep up the great work!",
        "🚀 You're learning so fast!",
        "👑 You're a Quiz Master!",
        "📚 Keep exploring and having fun!",
        "🎉 Bravo! More fun awaits!",
        "🦄 Your imagination is magical!",
        "🏆 You’re doing amazing!"
    ]
    st.markdown(
        f"<h2 style='text-align: center; color: #008080;'>{random.choice(messages)}</h2>", unsafe_allow_html=True)

    st.markdown("---")
    st.subheader("🎈 Your Reward Balloons 🎈")

    # Show celebratory balloons in rows
    balloons = ["🎈", "🎈", "🎈", "🎈", "🎈", "🎈", "🎈", "🎈"]
    st.markdown(
        f"<h1 style='text-align: center;'>{' '.join(random.sample(balloons * 3, 15))}</h1>", unsafe_allow_html=True)

    st.balloons()  # 🎉 Add Streamlit's flying balloon animation!

    st.markdown("---")
    st.success("Come back tomorrow for more learning and fun! 🚀")


if __name__ == "__main__":
    main()
