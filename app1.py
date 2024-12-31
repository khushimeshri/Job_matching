#importing all the requirements 
from docx import Document
import streamlit as st
import google.generativeai as genai
import os
import PyPDF2 as pdf
from dotenv import load_dotenv

load_dotenv()  #this will load all environment variables

#configuring my google Generative AI using an API key
genai.configure(api_key="AIzaSyCui4RYLVhW9BfWkHZf2eitcbXgBcPzlWg")

# Function to get response from Gemini model
def get_gemini_repsonse(input):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(input)
    return response.text

#this function has been used to extract text from uploaded PDF
def input_pdf_text(uploaded_file):
    reader = pdf.PdfReader(uploaded_file)
    text = ""
    for page in range(len(reader.pages)):
        page = reader.pages[page]
        text += str(page.extract_text())
    return text

#this function has been used to extract test from uploaded docx file 
def input_docx_text(file_path):
    doc = Document(file_path)
    return " ".join([p.text for p in doc.paragraphs])

#Prompt to generate the required analytics 
formatted_prompt = """
Hey, act like a highly skilled and experienced ATS (Application Tracking System) with a deep understanding of the diverse industries such as 
software engineering, data science, software development engineer, business analyst, project manager,data analysis etc.
Your task is to evaluate the resume based on the given job description. 
Provide a structured response and complete analytics to show why a candidate is a good fit for a particular job by comparing the uploaded resume 
with the job description and identify the best matching roles based on the following factors:

1. Skill Match: Calculate the percentage of required skills in the job description that the candidate's resume contains. Highlight any missing skills.
2. Experience Match: Assess how the candidate's experience aligns with the job's requirements (e.g., years of experience, specific project mentions, etc.).
3. Education Fit: Evaluate if the candidate's education level and certifications match the job's educational requirements.
4. Technological Fit: Check for matching tools, platforms, and technologies mentioned in both the resume and the job description.

resume: {text}
description: {jd}

I want the response in the following structure:
{
  "Skill Match": 
    "percentage": "XX%", "missing_skills": ["skill1", "skill2"]
  
  "Experience Match": 
    "percentage": "XX%", "justification": "Detailed explanation of how the experience aligns."
  
  "Education Fit": 
    "percentage": "XX%", "justification": "Detailed explanation of how the education aligns."
  
  "Technological Fit":
     "percentage": "XX%", "matching_technologies": ["tech1", "tech2"]
}

"""
#Now inorder to provide a user-interface we have used "streamlit"
st.title("JobFit")
st.text("Geta complete comparative analysis of your profile with respective to the job requirements using JobFit")
jd = st.text_area("Paste the Job Description", help="Enter the job description for which your resume will be evaluated.")
uploaded_file = st.file_uploader("Upload Your Resume", type=['docx','pdf'], help="Please upload your resume in PDF or format.")

# Submit button action
if st.button("Submit"):
    if jd.strip() == "":
        st.error("Please provide a job description.")
    elif uploaded_file is None:
        st.error("Please upload a resume.")
    else:
        #extracting the text from the uploaded resume based on the file type
        file_type = uploaded_file.type
        if file_type == "application/pdf":
            text = input_pdf_text(uploaded_file) 
        elif file_type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
            text = input_docx_text(uploaded_file)
        else:
            st.error("Unsupported file type. Please upload a PDF or DOCX file.")
            text = None
      
            #This will show the response from the LLM
        try:
            response = get_gemini_repsonse(formatted_prompt)
            st.subheader("JobMatch Analytics")
            st.text(response)
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")

