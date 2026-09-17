import streamlit as st
import PyPDF2
import io
import os
from google import genai
from dotenv import load_dotenv

load_dotenv()


st.set_page_config(page_title="AI Resume Reviewer", page_icon="📃", layout="centered")

st.title("AI Resume Reviewer")
st.markdown("Upload your resume to receive personalized, actionable feedback tailored to your target role.")

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

uploaded_file = st.file_uploader("Upload your resume (PDF or TXT)", type=["pdf", "txt"])
job_role = st.text_input("Enter the job role that you are targeting (optional).")

analyze = st.button("Analyze Resume")


def extract_text_from_pdf(uploaded_file):
    pdf_reader = PyPDF2.PdfReader(uploaded_file)
    text=""
    for page in pdf_reader.pages:
        text+= page.extract_text() + '\n'
    return text



def extract_text_from_file(uploaded_file):
    if uploaded_file.type == "application/pdf":
        return extract_text_from_pdf(io.BytesIO(uploaded_file.read()))
    return uploaded_file.read().decode("utf-8")


if analyze and uploaded_file:
    try:
        if not GEMINI_API_KEY:
            st.error("GEMINI_API_KEY is missing. Add it to your .env file and restart the app.")
            st.stop()

        file_content = extract_text_from_file(uploaded_file)

        if not file_content.strip():
            st.error("File does not have any content...")
            st.stop()

        prompt = f"""Please analyze this resume and provide constructive feedback.
        Focus on the following aspects:
        1. Content clarity and impact
        2. Skills presentation
        3. Experience description
        4. Specific improvements for {job_role if job_role else 'general job applications'}

        Resume content:
        {file_content}

        Please provide your analysis in a clear, structured format with specific recommendations."""

        client = genai.Client(api_key=GEMINI_API_KEY)
        response = client.models.generate_content(
            model="gemini-3.6-flash",
            contents=(
                "You are an expert resume reviewer with years of experience in HR and recruitment.\n\n"
                + prompt
            )
        )
        st.markdown("### Analysis Results")
        st.markdown(response.text)
    except Exception as e:
        st.error(f"An error occured: {str(e)}")

