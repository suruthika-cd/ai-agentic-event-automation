# AI Agentic Event Automation

An agentic AI system that automates resume screening, event registration, confirmations, attendance tracking, and certificate generation using Gemini LLM and n8n workflows.

---

## 🧩 Problem Statement
Recruitment and event management processes involve handling large volumes of resumes, registrations, confirmations, reminders, attendance tracking, and certificate distribution.  
These tasks are often manual, time-consuming, error-prone, and lack intelligent decision-making.

---

## 💡 Solution Overview
This project introduces an **agentic AI-driven automation platform** where:
- Gemini LLM acts as the reasoning brain for resume analysis and decision-making.
- n8n orchestrates workflows, branching logic, and scheduled actions.
- The system automates the entire lifecycle from screening to certification.

---

## 🧠 Agentic AI Implementation
- **LLM Used:** Gemini (as the reasoning and decision-making agent)
- **Agent Behavior:**
  - Analyzes resumes and computes ATS scores
  - Classifies candidates (Shortlisted / Rejected)
  - Triggers actions based on decisions
  - Handles follow-ups and reminders autonomously

---

## 🔄 Agent Workflow
1. Candidate submits resume or event registration form  
2. Resume Parsing Agent extracts skills and details  
3. Decision Agent evaluates ATS score using Gemini LLM  
4. n8n executes conditional workflows  
5. Emails sent for selection, rejection, or reminders  
6. Attendance tracked automatically  
7. Certificates generated and distributed  

---

## 🏗️ Architecture
The system follows a layered architecture:
- **User Layer:** Candidate / Participant
- **AI Agent Layer:** Gemini LLM (reasoning & decisions)
- **Automation Layer:** n8n workflows
- **Service Layer:** Email, Certificate, Attendance services
- **Storage Layer:** Google Drive & Google Sheets

(Architecture diagram available in `/docs/architecture.png`)

---

## 🛠️ Tech Stack
- **LLM:** Gemini
- **Automation:** n8n
- **Backend:** FastAPI (Python)
- **Storage:** Google Drive, Google Sheets
- **Email:** Gmail API
- **Certificates:** PDF generation

---


