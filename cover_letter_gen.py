import streamlit as st
import os
import json
from groq import Groq
from dotenv import load_dotenv

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

with open("config.json", "r") as f:
    config = json.load(f)

st.set_page_config(page_title="Cover Letter Generator", layout="wide")
st.title("Cover Letter Generator")

# ---- Session State ----
defaults = {
    "job_description": "",
    "resume": "",
    "cover_letter": "",
    "system_prompt": config["system_prompt"],
    "model": config["default_model"]
}

for k, v in defaults.items():
    if k not in st.session_state:
        st.session_state[k] = v


def generate():
    if not st.session_state.job_description or not st.session_state.resume:
        st.warning("Fill both inputs.")
        return

    with st.spinner("Generating..."):
        response = client.chat.completions.create(
            model=st.session_state.model,
            messages=[
                {
                    "role": "system",
                    "content": st.session_state.system_prompt
                },
                {
                    "role": "user",
                    "content": f"""
Job Description:
{st.session_state.job_description}

Resume:
{st.session_state.resume}
"""
                }
            ]
        )

        st.session_state.cover_letter = response.choices[0].message.content


def clear():
    for k in ["job_description", "resume", "cover_letter"]:
        st.session_state[k] = ""


with st.sidebar:
    st.header("Settings")

    st.selectbox(
        "Model",
        options=config["models"],
        key="model"
    )

    st.text_area(
        "System Prompt",
        height=200,
        key="system_prompt"
    )

    st.caption("Tip: Keep prompts strict to avoid generic output.")


col1, col2 = st.columns(2)

with col1:
    st.subheader("Input")

    st.text_area("Job Description", height=250, key="job_description")
    st.text_area("Resume", height=250, key="resume")

    col_btn1, col_btn2 = st.columns(2)

    with col_btn1:
        if st.button("⚡ Generate", use_container_width=True):
            generate()

    with col_btn2:
        if st.button("🧹 Clear", use_container_width=True):
            clear()


with col2:
    st.subheader("Output")

    st.text_area("Cover Letter", height=520, key="cover_letter")

    if st.session_state.cover_letter:
        st.download_button(
            "Download TXT",
            data=st.session_state.cover_letter.encode("utf-8"),
            file_name="cover_letter.txt",
            use_container_width=True
        )