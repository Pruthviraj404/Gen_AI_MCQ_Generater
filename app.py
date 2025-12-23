import streamlit as st
from text_extracter import extract_text_from_pdf, chunck_text
from generate import generate_mcq

st.set_page_config(page_title="GenAI MCQ Generator")
st.title("📘 GenAI MCQ Generator")

uploaded_file = st.file_uploader("Upload PDF", type=["pdf"])
difficulty = st.selectbox("Select Difficulty", ["Easy", "Medium", "Hard"])

if uploaded_file:
    text = extract_text_from_pdf(uploaded_file)
    chunks = chunck_text(text)

    if st.button("Generate MCQs"):
        with st.spinner("Generating MCQs..."):
            mcqs = generate_mcq(chunks[0], difficulty)

            if isinstance(mcqs, list) and mcqs:
                st.session_state.mcqs = mcqs
                st.session_state.answers = {}




if "mcqs" in st.session_state:
    st.subheader("📝 Quiz")

    for i, mcq in enumerate(st.session_state.mcqs):
        st.markdown(f"### Q{i+1}. {mcq['question']}")

        options = mcq["options"]
        option_labels = [f"{k}. {v}" for k, v in options.items()]

        selected = st.radio(
            "Choose an option:",
            option_labels,
            key=f"q{i}"
        )

        st.session_state.answers[i] = selected[0]

        st.divider()


    if st.button("Submit Quiz"):
        score = 0
        st.subheader("📊 Results")

        for i, mcq in enumerate(st.session_state.mcqs):
            correct = mcq["answer"]
            user_ans = st.session_state.answers.get(i)

            if user_ans == correct:
                score += 1
                st.success(f"Q{i+1}: Correct ✅")
            else:
                st.error(
                    f"Q{i+1}: Wrong ❌ | "
                    f"Your answer: {user_ans} | "
                    f"Correct answer: {correct}"
                )

        st.markdown(f"## 🎯 Final Score: **{score} / {len(st.session_state.mcqs)}**")
