import streamlit as st
import google.generativeai as genai
import os
import PyPDF2 as pdf
from dotenv import load_dotenv

load_dotenv()  # Load all environment variables

# Configure Google Generative AI
genai.configure(api_key=os.getenv("AIzaSyCui4RYLVhW9BfWkHZf2eitcbXgBcPzlWg"))

# Function to get response from Gemini model
def get_gemini_repsonse(input):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(input)
    return response.text

# Function to extract text from uploaded PDF
def input_pdf_text(uploaded_file):
    reader = pdf.PdfReader(uploaded_file)
    text = ""
    for page in range(len(reader.pages)):
        page = reader.pages[page]
        text += str(page.extract_text())
    return text

# Prompt Template
input_prompt = """
Hey Act Like a skilled or very experienced ATS (Application Tracking System)
with a deep understanding of tech fields, software engineering, data science, data analysis,
and big data engineering. Your task is to evaluate the resume based on the given job description.
You must consider that the job market is very competitive, and you should provide
the best assistance for improving the resumes. Assign the percentage matching based
on the JD and
the missing keywords with high accuracy.
resume: {text}
description: {jd}

I want the response in the following structure
{"JD Match": "%", "MissingKeywords": [], "Profile Summary": ""}
"""
# Streamlit app

st.title("Smart ATS")
st.text("Improve Your Resume for ATS")
jd = st.text_area("Paste the Job Description", help="Enter the job description for which your resume will be evaluated.")
uploaded_file = st.file_uploader("Upload Your Resume", type="pdf", help="Please upload your resume in PDF format.")

# Submit button action
if st.button("Submit"):
    if jd.strip() == "":
        st.error("Please provide a job description.")
    elif uploaded_file is None:
        st.error("Please upload a resume.")
    else:
        # Extract text from the uploaded resume
        text = input_pdf_text(uploaded_file)

        # Format the input prompt with resume and job description
        formatted_prompt = input_prompt.format(text=text, jd=jd)

        # Get the response from the LLM
        try:
            response = get_gemini_repsonse(formatted_prompt)
            st.subheader("ATS Evaluation Results")
            st.text(response)
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")
