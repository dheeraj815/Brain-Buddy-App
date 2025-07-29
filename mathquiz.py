import streamlit as st
import random


def main(pro=False):
    st.title("➕ Math Quiz")

    # Define questions
    questions = [
        {"question": "5 + 3 =", "answer": "8"},
        {"question": "10 - 6 =", "answer": "4"},
        {"question": "7 x 2 =", "answer": "14"},
        {"question": "12 ÷ 3 =", "answer": "4"},
        {"question": "9 + 4 =", "answer": "13"},
        {"question": "15 - 9 =", "answer": "6"},
        {"question": "3 x 3 =", "answer": "9"},
        {"question": "16 ÷ 4 =", "answer": "4"},
        {"question": "8 + 7 =", "answer": "15"},
        {"question": "14 - 5 =", "answer": "9"},
        {"question": "6 x 2 =", "answer": "12"},
        {"question": "18 ÷ 3 =", "answer": "6"},
        {"question": "7 + 5 =", "answer": "12"},
        {"question": "20 - 8 =", "answer": "12"},
        {"question": "4 x 4 =", "answer": "16"},
        {"question": "9 ÷ 3 =", "answer": "3"},
        {"question": "10 + 11 =", "answer": "21"},
        {"question": "13 - 7 =", "answer": "6"},
        {"question": "5 x 5 =", "answer": "25"},
        {"question": "24 ÷ 4 =", "answer": "6"},
    ]

    # Shuffle questions
    random.shuffle(questions)

    total_qs = 20 if pro else 10
    questions = questions[:total_qs]

    if "math_answers" not in st.session_state:
        st.session_state.math_answers = {}

    with st.form("math_quiz_form"):
        for i, q in enumerate(questions):
            st.session_state.math_answers[i] = st.text_input(
                f"{i+1}. {q['question']}", key=f"q{i}")

        submitted = st.form_submit_button("✅ Submit")

    if submitted:
        score = 0
        for i, q in enumerate(questions):
            user_answer = st.session_state.math_answers.get(i, "").strip()
            correct_answer = q['answer']
            if user_answer == correct_answer:
                score += 1

        st.success(f"✅ You scored {score} out of {total_qs}!")

        # Optional: Store to session or parent tracking here

    if st.button("🔁 Restart Quiz"):
        for i in range(total_qs):
            st.session_state.pop(f"q{i}", None)
        st.session_state.pop("math_answers", None)
        st.rerun()
