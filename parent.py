import streamlit as st

# --- Initialize Progress for All Quizzes ---


def initialize_progress():
    st.session_state.child_progress = {
        "🧮 Math Quiz": {"completed": 0, "total": 10},
        "🐾 Animal Quiz": {"completed": 0, "total": 10},
        "🌍 Fun Facts Quiz": {"completed": 0, "total": 10},
        "🧩 Riddles Quiz": {"completed": 0, "total": 10},
        "✏️ Spelling Quiz": {"completed": 0, "total": 10},
        "📖 Story Time": {"completed": 0, "total": 10}
    }

# --- Main Function ---


def main():
    st.title("👨‍👩‍👧 Parent Dashboard")
    st.markdown("#### 📊 Track your child’s learning progress in real-time!")

    if "child_progress" not in st.session_state:
        initialize_progress()

    st.markdown("### 🏆 Quiz Performance Overview")

    for quiz, progress in st.session_state.child_progress.items():
        completed = progress.get("completed", 0)
        total = progress.get("total", 10)
        percentage = int((completed / total) * 100) if total > 0 else 0

        top_badge = " 🌟 Top Rated" if percentage >= 80 else ""
        progress_text = f"**{quiz}**: {completed} / {total} completed ({percentage}%) {top_badge}"

        st.markdown(progress_text)
        st.progress(percentage)

    st.markdown("---")
    st.info("💡 This dashboard gives you insight into your child's learning journey across all Brain Buddy activities.")

    if st.button("🔄 Reset All Progress"):
        initialize_progress()
        st.success("✅ All progress has been reset.")
        st.rerun()


# --- Run as Main ---
if __name__ == "__main__":
    main()
