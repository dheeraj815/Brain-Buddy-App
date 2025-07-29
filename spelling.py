import streamlit as st
import random


def main(pro=False):
    st.title("📝 Spelling Quiz (Fill in the Blank)")

    questions = [
        "Elephant", "Beautiful", "Balloon", "Rainbow", "Butterfly",
        "Animal", "Garden", "Monkey", "Family", "Friend",
        "Holiday", "Window", "Yellow", "Kitchen", "Bicycle",
        "Father", "Mother", "School", "Flower", "Planet",
        "Market", "Jungle", "Teacher", "Rocket", "Cookie",
        "Laptop", "Umbrella", "Helmet", "Pencil", "Morning",
        "Basket", "Button", "Candle", "Ladder", "Mountain",
        "Picture", "Ocean", "Turtle", "Castle", "Doctor"
    ]

    total = 20 if pro else 10

    if "spelling_set" not in st.session_state:
        st.session_state.spelling_set = random.sample(questions, total)
        st.session_state.submitted = False
        st.session_state.answers = {}

    def hide_letters(word):
        letters = list(word)
        num_to_hide = max(2, int(len(word) * 0.4))
        indices = random.sample(range(len(word)), num_to_hide)
        for idx in indices:
            letters[idx] = "_"
        return "".join(letters)

    if not st.session_state.submitted:
        st.markdown("### Fill in the blanks with correct spelling:")

        for i, word in enumerate(st.session_state.spelling_set):
            question = hide_letters(word)
            st.text_input(f"{i+1}. {question}", key=f"spell_{i}")

        if st.button("✅ Submit"):
            st.session_state.submitted = True
            for i, word in enumerate(st.session_state.spelling_set):
                user_input = st.session_state.get(f"spell_{i}", "")
                st.session_state.answers[i] = {
                    "correct": word,
                    "user": user_input.strip()
                }
            st.rerun()

    else:
        st.markdown("### ✅ Results:")

        score = 0
        for i in range(total):
            correct_word = st.session_state.answers[i]["correct"]
            user_word = st.session_state.answers[i]["user"]

            if user_word.lower() == correct_word.lower():
                st.success(f"{i+1}. ✅ {user_word} — Correct!")
                score += 1
            else:
                st.error(
                    f"{i+1}. ❌ Your answer: {user_word} | Correct: **{correct_word}**")

        st.info(f"🎉 You got {score} out of {total} correct!")

    if st.button("🔁 Restart"):
        for key in list(st.session_state.keys()):
            if key.startswith("spell_") or key in ["spelling_set", "submitted", "answers"]:
                del st.session_state[key]
        st.rerun()
