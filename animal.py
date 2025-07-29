import streamlit as st
import random


def main(pro=False):
    st.title("🐾 Animal Quiz")

    questions = [
        {"question": "Which animal is known as the King of the Jungle?", "answer": "lion"},
        {"question": "What is the tallest animal in the world?", "answer": "giraffe"},
        {"question": "Which animal has a trunk?", "answer": "elephant"},
        {"question": "What do pandas mostly eat?", "answer": "bamboo"},
        {"question": "Which animal is known for changing its color?",
            "answer": "chameleon"},
        {"question": "Which bird is known for mimicking human speech?", "answer": "parrot"},
        {"question": "Which animal is the fastest on land?", "answer": "cheetah"},
        {"question": "What is a baby dog called?", "answer": "puppy"},
        {"question": "Which sea creature has eight legs?", "answer": "octopus"},
        {"question": "Which animal lives both in water and on land?", "answer": "frog"},
        {"question": "What is the largest mammal in the world?", "answer": "blue whale"},
        {"question": "Which insect makes honey?", "answer": "bee"},
        {"question": "Which animal is known for its black and white stripes?",
            "answer": "zebra"},
        {"question": "What is the only mammal that can fly?", "answer": "bat"},
        {"question": "What animal is known as man's best friend?", "answer": "dog"},
        {"question": "Which animal roars?", "answer": "lion"},
        {"question": "Which reptile has a hard shell?", "answer": "turtle"},
        {"question": "What animal says 'meow'?", "answer": "cat"},
        {"question": "Which animal has humps on its back?", "answer": "camel"},
        {"question": "Which bird cannot fly?", "answer": "ostrich"}
    ]

    random.shuffle(questions)
    total_qs = 20 if pro else 10
    questions = questions[:total_qs]

    if "animal_answers" not in st.session_state:
        st.session_state.animal_answers = {}

    with st.form("animal_quiz_form"):
        for i, q in enumerate(questions):
            st.session_state.animal_answers[i] = st.text_input(
                f"{i+1}. {q['question']}", key=f"a{i}")

        submitted = st.form_submit_button("✅ Submit")

    if submitted:
        score = 0
        for i, q in enumerate(questions):
            user_answer = st.session_state.animal_answers.get(
                i, "").strip().lower()
            correct_answer = q['answer'].lower()
            if user_answer == correct_answer:
                score += 1

        st.success(f"✅ You scored {score} out of {total_qs}!")

    if st.button("🔁 Restart Quiz"):
        for i in range(total_qs):
            st.session_state.pop(f"a{i}", None)
        st.session_state.pop("animal_answers", None)
        st.rerun()
