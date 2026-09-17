# AI Resume Reviewer

A Streamlit application that uses Google Gemini to review PDF or TXT resumes and provide personalized, actionable feedback for a target job role.

## Features

- Upload a resume in PDF or TXT format
- Optionally enter a target job role
- Receive feedback on clarity, skills, experience descriptions, and improvements
- Uses Google Gemini for AI-powered analysis

## Requirements

- Python 3.9 or newer
- A Google Gemini API key

## Setup

1. Clone the repository and open its folder:

   ```powershell
   git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git
   cd YOUR_REPOSITORY
   ```

2. Create and activate a virtual environment:

   ```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```

   If PowerShell blocks activation, run this once in the current terminal:

   ```powershell
   Set-ExecutionPolicy -Scope Process Bypass
   .\.venv\Scripts\Activate.ps1
   ```

3. Install the dependencies:

   ```powershell
   python -m pip install --upgrade pip
   pip install streamlit PyPDF2 google-genai python-dotenv
   ```

4. Create a `.env` file in the project folder:

   ```env
   GEMINI_API_KEY=your_gemini_api_key_here
   ```

   Never commit `.env` or share the API key. The repository `.gitignore` excludes it from Git.

## Run the app

```powershell
python -m streamlit run main.py
```

Open the URL shown in the terminal, usually `http://localhost:8501`.

## Project structure

```text
AI_Resume_Analyzer/
├── main.py
├── README.md
├── .gitignore
└── .env                 # Local only; do not commit
```

## Security

If an API key is accidentally exposed, revoke it immediately in Google AI Studio and create a replacement. Updating `.gitignore` does not remove secrets that were already committed to Git history.
