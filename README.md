Smart ATS

Smart ATS is a Streamlit-based application that evaluates candidate resumes against job descriptions using Google's Generative AI (Gemini) for intelligent analysis. The tool calculates detailed match analytics, including skill match, experience alignment, education fit, and technological match, providing actionable insights for resume improvement.


**Features**

1.Resume Evaluation:

Upload resumes in PDF or DOCX format.

Extracts and processes text from resumes for analysis.

2.Job Description Parsing:

Accepts job descriptions via a text area input.

3.AI-Driven Analytics:

Skill Match: Percentage of required skills in the resume.

Experience Match: Alignment of candidate's experience with job requirements.

Education Fit: Evaluation of degrees and certifications.

Technological Fit: Tools and technologies match.

4.File Support:

Supports PDF (.pdf) and Word Document (.docx) formats for resumes.

5.Google Generative AI Integration:

Uses Gemini LLM to generate insights and analytics.


**Installation**

1.Prerequisites:

Python 3.8+

Streamlit

Required Python libraries (see requirements)

Google API Key for Generative AI

2.Steps to follow

Clone the Repository:

git clone https://github.com/your-username/smart-ats.git
cd smart-ats

Install Dependencies:

pip install -r requirements.txt

Set Up Environment Variables:

Create a .env file in the project directory.

Add your Google API Key:

GOOGLE_API_KEY=your_google_api_key

3.Run the Application:

streamlit run app.py

4.Access the App:

Open your browser and navigate to: http://localhost:8501

5.Usage

Open the app in your browser.

Paste the job description in the provided text area.

Upload your resume in PDF or DOCX format.

Click the "Submit" button to get detailed analytics.


**Requirements**

Python libraries:

streamlit

python-docx

PyPDF2

google-generativeai

python-dotenv

To install the required libraries, run:

pip install -r requirements.txt

File Structure

smart-ats/
├── app.py              # Main application code
├── requirements.txt    # Python dependencies
├── README.md           # Project documentation
├── .env                # Environment variables (not included in version control)
└── assets/             # Static assets (if any)


**Example**

Input:

Job Description: "Looking for a software engineer with experience in Python, AWS, and data analysis."

Resume: PDF or DOCX file uploaded by the user.

Output:

{
  "Skill Match": {
    "percentage": "80%",
    "missing_skills": ["AWS"]
  },
  "Experience Match": {
    "percentage": "90%",
    "justification": "Candidate has 3 years of experience in Python and data analysis."
  },
  "Education Fit": {
    "percentage": "100%",
    "justification": "Candidate holds a degree in Computer Science."
  },
  "Technological Fit": {
    "percentage": "75%",
    "missing_technologies": ["AWS"]
  }
}

Contributing

Fork the repository.

Create a feature branch:

git checkout -b feature-name

Commit your changes:

git commit -m "Add feature-name"

Push to the branch:

git push origin feature-name

Create a Pull Request.

Acknowledgments

Google Generative AI for providing the Gemini LLM.

Streamlit for enabling a simple and interactive UI.

