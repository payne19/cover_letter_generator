# Cover Letter Generator

A Streamlit application that generates tailored cover letters using a large language model via the Groq API. The user provides a job description and resume, and the system produces a structured cover letter with options to download in multiple formats.

---

## Features

- AI-generated cover letters using Groq LLM
- Input fields for job description and resume
- Customizable system prompt
- Export formats:
  - TXT
  - DOCX
  - PDF
- Clear and regenerate functionality
- Streamlit-based UI

---

## Tech Stack

- Streamlit
- Groq API
- Python
- python-docx
- reportlab
- python-dotenv

---

## Setup

### 1. Clone the repository
```bash
git clone <repo-url>
cd cover-letter-generator
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Environment variables
Create a `.env` file:
```
GROQ_API_KEY=your_api_key_here
```

### 4. Configuration
Create a `config.json` file:
```json
{
  "system_prompt": "You are a professional cover letter writer.",
  "default_model": "llama-3.1-70b-versatile",
  "models": [
    "llama-3.1-70b-versatile",
    "llama-3.1-8b-instant"
  ]
}
```

### 5. Run the application
```bash
streamlit run app.py
```

---

## How It Works

1. Enter job description
2. Paste resume
3. Generate cover letter using LLM
4. Download output in desired format

---

## Output Formats

- Plain text (.txt)
- Word document (.docx)
- PDF (.pdf)

---

## Notes

- Better results come from detailed resumes and job descriptions
- System prompt strongly influences output quality
- Requires valid Groq API key

---

## Possible Improvements

- Tone selection (formal, neutral, concise)
- Multiple variations per generation
- ATS optimization scoring
- Template-based generation
