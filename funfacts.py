import streamlit as st
import random


def main(pro=False):
    st.title("🎉 Fun Facts Quiz")

    all_questions = [
        {"question": "What is the hottest planet in our solar system?", "answer": "Venus"},
        {"question": "How many legs does a spider have?", "answer": "8"},
        {"question": "Which animal is known as the king of the jungle?", "answer": "Lion"},
        {"question": "Which planet is known as the Red Planet?", "answer": "Mars"},
        {"question": "What do bees collect from flowers?", "answer": "Nectar"},
        {"question": "Which bird is known for mimicking sounds?", "answer": "Parrot"},
        {"question": "Which gas do plants absorb from the air?",
            "answer": "Carbon dioxide"},
        {"question": "How many bones are in the human body?", "answer": "206"},
        {"question": "What is the largest mammal on Earth?", "answer": "Blue whale"},
        {"question": "What’s the name of our galaxy?", "answer": "Milky Way"},
        {"question": "Which ocean is the biggest?", "answer": "Pacific Ocean"},
        {"question": "What’s the smallest planet in our solar system?",
            "answer": "Mercury"},
        {"question": "Which instrument has 88 keys?", "answer": "Piano"},
        {"question": "What is the freezing point of water?", "answer": "0"},
        {"question": "Which color absorbs the most heat?", "answer": "Black"},
        {"question": "What is a baby frog called?", "answer": "Tadpole"},
        {"question": "Which planet has rings?", "answer": "Saturn"},
        {"question": "What vitamin do we get from sunlight?", "answer": "Vitamin D"},
        {"question": "Which month has the fewest days?", "answer": "February"},
        {"question": "Which metal is liquid at room temperature?", "answer": "Mercury"},
    ]

    total_questions = 20 if pro else 10
    if "funfacts_questions" not in st.session_state:
        st.session_state.funfacts_questions = random.sample(
            all_questions, total_questions)
        st.session_state.funfacts_answers = [""] * total_questions
        st.session_state.funfacts_submitted = False

    questions = st.session_state.funfacts_questions

    st.markdown("### Answer the following questions:")

    for i, q in enumerate(questions):
        st.session_state.funfacts_answers[i] = st.text_input(
            f"{i+1}. {q['question']}",
            value=st.session_state.funfacts_answers[i],
            key=f"funfacts_q{i}"
        )

    col1, col2 = st.columns([1, 1])
    with col1:
        if not st.session_state.funfacts_submitted:
            if st.button("✅ Submit"):
                st.session_state.funfacts_submitted = True
        else:
            st.success("✅ Quiz already submitted.")

    with col2:
        if st.button("🔁 Restart"):
            for key in list(st.session_state.keys()):
                if key.startswith("funfacts_q") or key.startswith("funfacts_"):
                    del st.session_state[key]
            st.rerun()

    if st.session_state.funfacts_submitted:
        score = 0
        st.markdown("---")
        st.subheader("📋 Results:")
        for i, q in enumerate(questions):
            user_answer = st.session_state.funfacts_answers[i].strip().lower()
            correct_answer = q['answer'].strip().lower()
            is_correct = user_answer == correct_answer
            if is_correct:
                score += 1
            result = "✅ Correct" if is_correct else f"❌ Incorrect (Answer: {q['answer']})"
            st.markdown(
                f"**Q{i+1}: {q['question']}**  \nYour Answer: *{st.session_state.funfacts_answers[i]}*  \n{result}")

        st.success(f"🎉 You scored {score} out of {total_questions}!")

        # Update Parent Dashboard score
        if "child_progress" not in st.session_state:
            st.session_state.child_progress = {}
        st.session_state.child_progress["Fun Facts Quiz"] = {
            "completed": score,
            "total": total_questions
        }
