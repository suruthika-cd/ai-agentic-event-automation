from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from google import genai
import json

# -----------------------------
# Gemini client (NO env usage)
# -----------------------------
client = genai.Client(
    api_key="AIzaSyByIO8NwsmP7z8I-PKq629BOlTJQ5IV6Ps"
)

app = FastAPI()


# -----------------------------
# Input schema
# -----------------------------
class ResumeInput(BaseModel):
    resume_text: str
    target_role: str = "AI / ML Intern"


# -----------------------------
# Helper: clean + parse JSON
# -----------------------------
def safe_json_parse(text: str):
    """
    Ensures Gemini output is valid JSON.
    Handles cases like:
    json
    { ... }
    or ```json { ... } ```
    """
    text = text.strip()

    # Remove markdown fences if present
    if text.startswith("```"):
        text = text.replace("```", "").replace("json", "").strip()

    try:
        return json.loads(text)
    except json.JSONDecodeError:
        raise ValueError("Gemini did not return valid JSON")


# -----------------------------
# API endpoint
# -----------------------------
@app.post("/analyze-resume")
def analyze_resume(data: ResumeInput):
    prompt = f"""
You are an AI recruitment agent.

Your task:
1. Extract key technical skills
2. Give a score out of 100
3. Decide SHORTLIST or REJECT
4. Give a concise reason

Target role:
{data.target_role}

Resume:
{data.resume_text}

Return ONLY valid JSON.
Do NOT add explanations.
Do NOT add markdown.
Do NOT add the word json.
Do NOT wrap in code blocks.

Return EXACTLY in this format:

{{
  "skills": [],
  "score": 0,
  "decision": "",
  "reason": ""
}}
"""

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        raw_text = response.text
        parsed = safe_json_parse(raw_text)
        return parsed

    except ValueError as ve:
        return {
            "error": str(ve),
            "raw_output": raw_text
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
