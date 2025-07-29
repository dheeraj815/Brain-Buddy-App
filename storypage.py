import streamlit as st
import random


def main(pro=False):
    st.title("📖 Story Time")
    st.markdown("### Enjoy a new short story!")

    stories = [
        """**The Flying Fox**  
Once upon a time in a quiet forest, a little fox looked up at the birds and wished to fly.  
He tried using leaves, feathers, even jumping from hills—but nothing worked.  
One day, he met an owl who gave him the secret: “Sometimes flying means dreaming big!”  
And from then on, the fox would fly in his dreams every night.""",

        """**The Magic Pen**  
In a village far away, a young girl found a pen that could write the future.  
She used it to help her neighbors, fix broken things, and even bring rain during dry days.  
But she learned that kindness is the real magic, not the pen itself.""",

        """**The Painting Robot**  
A little robot was built in a lab, meant only to do math.  
But it loved colors and used sunflower seeds as paint.  
The scientists laughed at first, but soon people came from everywhere to see the beautiful seed-paintings.""",

        """**The Moon’s Earth Visit**  
One night, the moon came down to Earth just to see what fun is like.  
It danced at a beach party, laughed with kids, and glowed brighter than ever.  
Since then, it visits secretly to light up our night skies with joy."""
    ]

    story_choices = stories if pro else stories[:2]
    selected_story = random.choice(story_choices)

    st.markdown(
        f"<div style='font-size:18px; line-height:1.7'>{selected_story}</div>", unsafe_allow_html=True)

    st.markdown("### 💬 What did you learn from the story?")
    user_input = st.text_area("Write your thoughts here:")

    col1, col2 = st.columns(2)
    with col1:
        if st.button("✅ Submit Response"):
            st.success("Wonderful! Your thoughts have been recorded.")

    with col2:
        if st.button("🔁 Read Another Story"):
            st.rerun()
