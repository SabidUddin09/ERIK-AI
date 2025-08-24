import streamlit as st
import random

# ------------------------------
# Page Config
# ------------------------------
st.set_page_config(
    page_title="E.R.I.K.",
    layout="wide",
    page_icon="🤖"
)

# ------------------------------
# Header
# ------------------------------
st.markdown(
    """
    <div style="background-color:#1f2937;padding:15px;border-radius:10px">
    <h1 style="color:white;text-align:center;">🤖 E.R.I.K.</h1>
    <p style="color:white;text-align:center;">Exceptional Resources & Intelligence Kernel - Your AI Exam Companion</p>
    </div>
    """, unsafe_allow_html=True
)

# ------------------------------
# Sidebar Menu
# ------------------------------
menu = st.sidebar.radio("📚 Choose Feature:", [
    "Topic Analyzer", "Document Upload", "Doubt Solver",
    "Quiz Generator", "Flashcards"
])

# ------------------------------
# 1. Topic Analyzer
# ------------------------------
if menu == "Topic Analyzer":
    st.subheader("📖 Topic Analyzer")
    topic = st.text_area("Enter your exam topic here:")
    if st.button("Analyze Topic"):
        if topic:
            with st.container():
                st.markdown("### 🧠 Key Concepts")
                st.markdown(f"- Concept 1 about {topic}")
                st.markdown(f"- Concept 2 about {topic}")
                st.markdown("### ✏️ Example Questions")
                st.markdown(f"1. Example question 1 on {topic}")
                st.markdown(f"2. Example question 2 on {topic}")
        else:
            st.warning("Please enter a topic to analyze.")

# ------------------------------
# 2. Document Upload
# ------------------------------
elif menu == "Document Upload":
    st.subheader("📂 Upload Study Material")
    uploaded_file = st.file_uploader("Upload PDF/DOC/TXT", type=["pdf", "docx", "txt"])
    if uploaded_file:
        st.success("✅ Document uploaded successfully!")
        with st.expander("Preview Extracted Text"):
            st.write("Preview of your uploaded document will appear here.")
        st.button("Generate Questions")

# ------------------------------
# 3. Doubt Solver
# ------------------------------
elif menu == "Doubt Solver":
    st.subheader("❓ Doubt Solver")
    doubt = st.text_area("Ask your academic question:")
    if st.button("Solve Doubt"):
        if doubt:
            with st.expander("Answer"):
                st.write(f"🔹 Explanation for your doubt: {doubt}")
        else:
            st.warning("Please enter a question.")

# ------------------------------
# 4. Quiz Generator
# ------------------------------
elif menu == "Quiz Generator":
    st.subheader("📝 Quiz Generator")
    quiz_type = st.selectbox("Select Quiz Type:", ["MCQ", "Short Question", "Creative Question"])
    topic = st.text_input("Enter Topic / Notes:")
    num_q = st.slider("Number of Questions:", 3, 15, 5)

    if st.button("Generate Quiz"):
        if topic:
            with st.container():
                st.markdown(f"### {quiz_type} on {topic}")
                for i in range(1, num_q+1):
                    with st.expander(f"Q{i}"):
                        if quiz_type == "MCQ":
                            options = ["a) Option A", "b) Option B", "c) Option C", "d) Option D"]
                            st.write(f"Question {i}: Example MCQ on {topic}?")
                            for opt in options:
                                st.write(opt)
                            st.success(f"✅ Answer: {random.choice(options)}")
                        elif quiz_type == "Short Question":
                            st.write(f"Question {i}: Short answer question on {topic}")
                            st.info("Answer: ...")
                        else:
                            st.write(f"Question {i}: Creative/analytical question on {topic}")
                            st.info("Answer: ...")
        else:
            st.warning("Please enter a topic or notes.")

# ------------------------------
# 5. Flashcards
# ------------------------------
elif menu == "Flashcards":
    st.subheader("🃏 Flashcards")
    notes = st.text_area("Enter your notes:")
    num_cards = st.slider("Number of flashcards:", 3, 20, 5)
    if st.button("Generate Flashcards"):
        if notes:
            for i in range(1, num_cards+1):
                with st.expander(f"Flashcard {i}"):
                    st.markdown(f"**Q:** Example question {i}?")
                    st.markdown(f"**A:** Example answer {i}.")
        else:
            st.warning("Please enter notes to generate flashcards.")
