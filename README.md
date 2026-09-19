# Subhrajeet Swain — Interactive Python Portfolio Web Application

A modern, interactive developer and QA engineering portfolio built with **Pure Python** and **Streamlit** for **Subhrajeet Swain** (BCA & MCA Graduate, QA Intern at Team Pumpkin).

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://streamlit.io)
[![GitHub](https://img.shields.io/badge/GitHub-subhrajeet03-181717?style=flat&logo=github)](https://github.com/subhrajeet03)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-subhrajeet--swain-0A66C2?style=flat&logo=linkedin)](https://linkedin.com/in/subhrajeet-swain)

---

## 🌟 What's Inside

- **No HTML required!** Powered completely by Python data science and web components.
- **Dynamic Profile & Sidebar**: Status badge (`🟢 Ready for Hire`), quick contact actions, and 1-click plain text resume download.
- **QA Engineering Showcase**: Interactive test case matrix with real-time module & status filters, plus a realistic **Acedboard** defect tracking ticket mockup.
- **E-Hospital Management System (Live Simulator)**:
  - 🩺 Doctor Consultation & OPD Duty Roster
  - 🏥 Patient EMR Record Search Simulation
  - 💊 Pharmacy Drug Inventory & Low-Stock Alerts
  - 💳 Interactive Billing & Health Insurance / TPA Claims Calculator
- **Skills Matrix & Visual Analytics**: Interactive bar chart comparing competencies across QA testing, Python, SQL, C/C++, and BI tools.
- **Education Timeline**: Full academic credentials (MCA 2026, BCA CGPA 7.08, Class XII Science, Class X).
- **Languages & Interests**: English, Hindi, Odia, Community Volunteering, and Continuous Upskilling.
- **Interactive Contact Form**: Direct form submission and contact links.

---

## 🚀 How to Run Locally

1. Open your terminal or PowerShell in this folder:
   ```powershell
   cd C:\Users\HP\.gemini\antigravity\scratch\subhrajeet-portfolio
   ```

2. Run the Streamlit application:
   ```powershell
   streamlit run app.py
   ```
   Or using python module syntax:
   ```powershell
   python -m streamlit run app.py
   ```

3. Your default web browser will automatically open:
   `http://localhost:8501`

---

## 🌐 Deploy to GitHub & Streamlit Community Cloud

### Step 1: Push to GitHub
```bash
git add .
git commit -m "feat: complete pure Python Streamlit portfolio app"
git remote add origin https://github.com/subhrajeet03/subhrajeet-portfolio.git
git branch -M main
git push -u origin main
```

### Step 2: 1-Click Free Hosting on Streamlit Cloud
1. Go to [share.streamlit.io](https://share.streamlit.io/) and log in with your GitHub account (`subhrajeet03`).
2. Click **New App**.
3. Select your repository: `subhrajeet03/subhrajeet-portfolio`.
4. Set Main file path: `app.py`.
5. Click **Deploy!** Your Python portfolio will be live at `https://subhrajeet-portfolio.streamlit.app`!

---

## 📂 Project Architecture

```
subhrajeet-portfolio/
│
├── app.py                     # Main Python Streamlit application
├── requirements.txt           # Python dependencies (streamlit, pandas, altair)
├── .streamlit/
│   └── config.toml            # Theme and server configuration
├── assets/
│   └── avatar.svg             # Vector profile graphic
├── .gitignore                 # Standard Python & OS ignore rules
└── README.md                  # Instructions & deployment guide
```
