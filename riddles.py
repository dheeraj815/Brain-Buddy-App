import streamlit as st
import random


def main(pro=False):
    st.title("🧩 Riddles Quiz")

    questions = [
        {"question": "What has keys but can't open locks?", "answer": "piano"},
        {"question": "What can travel around the world while staying in the corner?",
            "answer": "stamp"},
        {"question": "What comes down but never goes up?", "answer": "rain"},
        {"question": "What has to be broken before you can use it?", "answer": "egg"},
        {"question": "What gets wetter the more it dries?", "answer": "towel"},
        {"question": "What has hands but can’t clap?", "answer": "clock"},
        {"question": "I’m tall when I’m young and short when I’m old. What am I?",
            "answer": "candle"},
        {"question": "What has a head, a tail, but no body?", "answer": "coin"},
        {"question": "What begins with T, ends with T, and has T in it?",
            "answer": "teapot"},
        {"question": "What has one eye but cannot see?", "answer": "needle"},
        {"question": "What has a neck but no head?", "answer": "bottle"},
        {"question": "What gets bigger the more you take away?", "answer": "hole"},
        {"question": "What has four legs in the morning, two in the afternoon and three in the evening?", "answer": "human"},
        {"question": "What goes up but never comes down?", "answer": "age"},
        {"question": "What can fill a room but takes up no space?", "answer": "light"},
        {"question": "The more you take, the more you leave behind. What are they?",
            "answer": "footsteps"},
        {"question": "What has cities, but no houses; forests, but no trees; and water, but no fish?", "answer": "map"},
        {"question": "I speak without a mouth and hear without ears. What am I?",
            "answer": "echo"},
        {"question": "What building has the most stories?", "answer": "library"},
        {"question": "What invention lets you look right through a wall?",
            "answer": "window"}
    ]

    random.shuffle(questions)
    total_qs = 20 if pro else 10
    questions = questions[:total_qs]

    if "riddle_answers" not in st.session_state:
        st.session_state.riddle_answers = {}

    with st.form("riddle_quiz_form"):
        for i, q in enumerate(questions):
            st.session_state.riddle_answers[i] = st.text_input(
                f"{i+1}. {q['question']}", key=f"r{i}")

        submitted = st.form_submit_button("✅ Submit")

    if submitted:
        score = 0
        for i, q in enumerate(questions):
            user_answer = st.session_state.riddle_answers.get(
                i, "").strip().lower()
            correct_answer = q['answer'].lower()
            if user_answer == correct_answer:
                score += 1

        st.success(f"✅ You scored {score} out of {total_qs}!")

    if st.button("🔁 Restart Quiz"):
        for i in range(total_qs):
            st.session_state.pop(f"r{i}", None)
        st.session_state.pop("riddle_answers", None)
        st.rerun()
