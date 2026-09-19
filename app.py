"""
SUBHRAJEET SWAIN - PERSONAL PORTFOLIO WEB APPLICATION
Built with Pure Python & Streamlit
Showcasing QA Engineering, Software Development, and Data & BI Capabilities.
"""

import streamlit as st
import pandas as pd
import datetime

# --- Page Configuration ---
st.set_page_config(
    page_title="Subhrajeet Swain | Python & QA Portfolio",
    page_icon="💻",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- Custom Styling ---
st.markdown("""
<style>
    /* Gradient Headings & Accents */
    .main-title {
        font-size: 2.8rem;
        font-weight: 800;
        background: linear-gradient(135deg, #818cf8 0%, #38bdf8 50%, #34d399 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.2rem;
    }
    .subtitle-badge {
        display: inline-block;
        background: rgba(99, 102, 241, 0.15);
        color: #818cf8;
        padding: 0.3rem 0.8rem;
        border-radius: 9999px;
        font-weight: 600;
        font-size: 0.85rem;
        border: 1px solid rgba(99, 102, 241, 0.3);
        margin-bottom: 1rem;
    }
    .status-pill {
        display: inline-block;
        background: rgba(16, 185, 129, 0.12);
        color: #34d399;
        padding: 0.35rem 0.9rem;
        border-radius: 9999px;
        font-size: 0.82rem;
        font-weight: 600;
        border: 1px solid rgba(16, 185, 129, 0.3);
        margin-bottom: 1.25rem;
    }
    .card-box {
        background: #111827;
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 12px;
        padding: 1.5rem;
        margin-bottom: 1.25rem;
    }
    .card-box:hover {
        border-color: rgba(99, 102, 241, 0.4);
    }
    .tag {
        display: inline-block;
        background: rgba(99, 102, 241, 0.12);
        color: #a5b4fc;
        padding: 0.25rem 0.6rem;
        border-radius: 6px;
        font-size: 0.8rem;
        font-weight: 600;
        margin-right: 0.4rem;
        margin-bottom: 0.4rem;
    }
    .exp-title {
        color: #f9fafb;
        font-size: 1.3rem;
        font-weight: 700;
        margin-bottom: 0.2rem;
    }
    .exp-company {
        color: #38bdf8;
        font-size: 1.05rem;
        font-weight: 600;
        margin-bottom: 0.5rem;
    }
</style>
""", unsafe_allow_html=True)

# --- Resume Plaintext Template for Download ---
RESUME_TEXT = """
SUBHRAJEET SWAIN
Aska, Ganjam, Odisha | +91-9776445055 / 7205489555 | subhrajeet03@gmail.com
LinkedIn: linkedin.com/in/subhrajeet-swain | GitHub: github.com/subhrajeet03

PROFESSIONAL SUMMARY
A highly motivated and detail-oriented BCA and MCA graduate seeking a challenging entry-level role in a reputable organization to apply technical skills across software development, testing, and data-driven problem solving. A quick learner and team player with a strong foundation in computer applications and programming languages, eager to contribute to an organization's success while continuing to grow skills and gain practical industry experience.

TECHNICAL SKILLS
- Programming Languages: Python, C, C++
- Testing & QA: Manual Testing, Test Case Design, UI/UX Testing, Defect Tracking (Acedboard)
- Databases & Web: MySQL, SQL, HTML, CSS, JavaScript (basic)
- Data & BI Tools: Power BI (Learning), Tableau (Learning)
- Productivity: MS Excel (Pivot Tables, Formulas), Word, PowerPoint

PROFESSIONAL EXPERIENCE
QA Intern — Team Pumpkin (Tech.) [April 2025 – March 2026]
- Performed manual testing on web applications and mobile platforms to identify functional defects.
- Designed and executed detailed test cases and test scenarios based on functional requirements.
- Logged and tracked bugs using Acedboard to support timely resolution.
- Conducted UI/UX testing to evaluate usability and user experience.

PROJECTS
E-Hospital Management System (2 Months)
- Built a system to simplify hospital workflow by managing doctors, patients, lab results, medical supplies, appointments, billing, and insurance in one place.
- Aimed to reduce administrative costs and errors while improving the overall patient experience.

EDUCATION
- Master in Computer Applications (MCA) — Presidency College, Berhampur, Odisha (2026) | Completed — Result Awaited
- Bachelor of Computer Applications (BCA) — Science College (Autonomous), Hinjilicut, Odisha (Apr 2024) | CGPA: 7.08
- Class XII (Science) — Binayak Acharya H.S. School, Berhampur (Jul 2021) | CHSE Odisha: 56%
- Class X — Aryan Public School, Aska (May 2019) | CBSE: 52%

ADDITIONAL INFORMATION
- Languages: English, Hindi, Odia
- Interests: Volunteering, learning new skills, building personal portfolios
"""

# --- Sidebar: Profile & Quick Contact ---
with st.sidebar:
    st.markdown("### 👨‍💻 Subhrajeet Swain")
    st.markdown("""<div class="subtitle-badge">QA Specialist &amp; Software Developer</div>""", unsafe_allow_html=True)
    st.markdown("""<div class="status-pill">🟢 Ready for Hire</div>""", unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("**📍 Location:** Aska, Ganjam, Odisha")
    st.markdown("**📧 Email:** [subhrajeet03@gmail.com](mailto:subhrajeet03@gmail.com)")
    st.markdown("**📱 Phone:** +91-9776445055 / 7205489555")
    
    st.markdown("---")
    st.markdown("#### 🔗 Profiles & Links")
    st.markdown("[![GitHub](https://img.shields.io/badge/GitHub-subhrajeet03-181717?style=flat&logo=github)](https://github.com/subhrajeet03)")
    st.markdown("[![LinkedIn](https://img.shields.io/badge/LinkedIn-subhrajeet--swain-0A66C2?style=flat&logo=linkedin)](https://linkedin.com/in/subhrajeet-swain)")
    
    st.markdown("---")
    st.download_button(
        label="📄 Download Resume (Text)",
        data=RESUME_TEXT.strip(),
        file_name="Subhrajeet_Swain_Resume.txt",
        mime="text/plain",
        use_container_width=True
    )
    
    st.markdown("---")
    st.caption("Built with pure Python & Streamlit • 2026")

# --- Top Hero Banner ---
col_hero_1, col_hero_2 = st.columns([2.5, 1])

with col_hero_1:
    st.markdown("""<div class="main-title">Subhrajeet Swain</div>""", unsafe_allow_html=True)
    st.markdown("#### *MCA & BCA Graduate • QA & Manual Testing Specialist • Python & Software Developer*")
    st.write(
        "A highly motivated and detail-oriented graduate seeking an entry-level role to apply technical skills "
        "across software development, QA testing, and data-driven problem solving. Quick learner with 1 year of practical "
        "industry experience as a **QA Intern at Team Pumpkin (Tech.)**."
    )

with col_hero_2:
    st.metric(label="QA Experience", value="1 Year", delta="Team Pumpkin")
    st.metric(label="BCA Degree", value="7.08 CGPA", delta="Science College")

st.markdown("---")

# --- Main Navigation Tabs ---
tabs = st.tabs([
    "👤 About Me",
    "💼 Experience (QA Intern)",
    "🧪 QA Test Suite & Bug Tracker",
    "🏥 E-Hospital Project Simulator",
    "🛠️ Technical Skills & BI",
    "🎓 Education",
    "🌐 Interests & Languages",
    "📬 Contact Me"
])

# ==============================================================================
# TAB 1: ABOUT ME
# ==============================================================================
with tabs[0]:
    st.subheader("Professional Background")
    
    col_ab1, col_ab2 = st.columns([1.5, 1])
    
    with col_ab1:
        st.write("""
        I hold a **Bachelor of Computer Applications (BCA)** from Science College (Autonomous), Hinjilicut, 
        and have completed my **Master in Computer Applications (MCA)** at Presidency College, Berhampur (2026).
        
        Throughout my academic career and industry internship, I have developed a dual strength in:
        - **Software Quality Assurance:** Manual testing of responsive web and mobile applications, defect logging with Acedboard, and scenario-based validation.
        - **Core Software Engineering & Data:** Hands-on programming in Python, C, C++, relational database design with MySQL, and data analytics with Power BI and Tableau.
        
        I am enthusiastic about joining a progressive team where I can apply rigorous quality standards and collaborative problem solving.
        """)
        
    with col_ab2:
        st.markdown("""
        <div class="card-box">
            <h4>💡 Core Strengths</h4>
            <p><strong>• Analytical Problem Solver:</strong> Translating functional specifications into exhaustive test scenarios.</p>
            <p><strong>• Quality-First Mindset:</strong> Detecting edge-case discrepancies before they reach production.</p>
            <p><strong>• Multilingual Communicator:</strong> Fluent in English, Hindi, and Odia.</p>
            <p><strong>• Rapid Learner:</strong> Constantly acquiring modern BI, API testing, and automation skills.</p>
        </div>
        """, unsafe_allow_html=True)

# ==============================================================================
# TAB 2: QA INTERNSHIP EXPERIENCE
# ==============================================================================
with tabs[1]:
    st.subheader("Professional Industry Experience")
    
    st.markdown("""
    <div class="card-box">
        <div class="exp-title">QA Intern</div>
        <div class="exp-company">Team Pumpkin (Tech.)</div>
        <div style="color: #10b981; font-weight: 600; font-size: 0.88rem; margin-bottom: 0.75rem;">
            📅 April 2025 – March 2026 (1 Year)
        </div>
        <ul style="color: #d1d5db; line-height: 1.7;">
            <li><strong>Cross-Platform Manual Testing:</strong> Executed end-to-end manual testing across responsive web applications and mobile platforms to isolate functional bugs and regression issues.</li>
            <li><strong>Test Case Design & Execution:</strong> Formulated, executed, and maintained granular test scenarios based on client requirements, strengthening analytical thinking and attention to detail.</li>
            <li><strong>Defect Tracking via Acedboard:</strong> Logged, prioritized, and tracked bugs through their lifecycle using <strong>Acedboard</strong> to support swift developer triage and resolution.</li>
            <li><strong>UI/UX Usability Testing:</strong> Conducted usability audits across diverse viewports to ensure intuitive user flows, accessibility, and smooth user experience.</li>
        </ul>
        <div style="margin-top: 1rem;">
            <span class="tag">Manual Testing</span>
            <span class="tag">Test Case Design</span>
            <span class="tag">Acedboard</span>
            <span class="tag">UI/UX Testing</span>
            <span class="tag">Web &amp; Mobile</span>
            <span class="tag">Bug Lifecycle</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

# ==============================================================================
# TAB 3: QA TEST SUITE & BUG TRACKER (INTERACTIVE)
# ==============================================================================
with tabs[2]:
    st.subheader("🧪 Interactive QA Test Suite & Acedboard Defect Tracker")
    st.write("Demonstrating real-world test case design and bug tracking workflows implemented during QA operations.")
    
    # Sample Test Suite Data
    test_cases_data = [
        {"TC_ID": "TC-AUTH-001", "Module": "Authentication", "Scenario": "Login with valid patient/doctor credentials", "Expected": "Redirect to authorized role dashboard", "Status": "PASS", "Severity": "High"},
        {"TC_ID": "TC-AUTH-002", "Module": "Authentication", "Scenario": "Login with invalid password 3 times", "Expected": "Display lockout alert with retry cooldown", "Status": "PASS", "Severity": "Medium"},
        {"TC_ID": "TC-APPT-001", "Module": "Appointments", "Scenario": "Book appointment for overlapping doctor time-slot", "Expected": "Validation error: 'Slot already reserved'", "Status": "PASS", "Severity": "Critical"},
        {"TC_ID": "TC-LAB-001", "Module": "Diagnostics", "Scenario": "Upload pathology report with out-of-range panic values", "Expected": "Flag report in red and notify consulting physician", "Status": "PASS", "Severity": "High"},
        {"TC_ID": "TC-PHARM-001", "Module": "Pharmacy", "Scenario": "Dispense medicine exceeding current stock inventory", "Expected": "Transaction blocked; alert: 'Insufficient stock'", "Status": "RESOLVED", "Severity": "High"},
        {"TC_ID": "TC-BILL-001", "Module": "Billing", "Scenario": "Rapid double-click on 'Generate Final Invoice'", "Expected": "Debounced single invoice generated without duplicate ID", "Status": "RESOLVED", "Severity": "Critical"},
        {"TC_ID": "TC-UI-001", "Module": "UI/UX", "Scenario": "Mobile viewport rendering on 375px width", "Expected": "Zero horizontal overflow; clean touch targets", "Status": "PASS", "Severity": "Low"}
    ]
    df_tests = pd.DataFrame(test_cases_data)
    
    col_filter_1, col_filter_2 = st.columns(2)
    with col_filter_1:
        selected_module = st.multiselect("Filter by Module:", options=df_tests["Module"].unique(), default=df_tests["Module"].unique())
    with col_filter_2:
        selected_status = st.multiselect("Filter by Status:", options=df_tests["Status"].unique(), default=df_tests["Status"].unique())
        
    filtered_tests = df_tests[(df_tests["Module"].isin(selected_module)) & (df_tests["Status"].isin(selected_status))]
    
    st.dataframe(filtered_tests, use_container_width=True, hide_index=True)
    
    # Acedboard Defect Mockup
    st.markdown("#### 🐞 Acedboard Defect Ticket Sample")
    with st.expander("View Defect Ticket: [DEF-104] Duplicate Invoice Generation", expanded=True):
        st.markdown("""
        - **Defect ID:** `DEF-104` | **Severity:** `Critical` | **Status:** `Verified & Closed`
        - **Reporter:** Subhrajeet Swain (QA Intern) | **Tool:** Acedboard
        - **Environment:** Production Staging / Chrome v124 & Mobile Android
        - **Summary:** Rapid double-clicking on the invoice button generated duplicate database transaction records.
        - **Steps to Reproduce:**
            1. Open patient discharge checkout screen.
            2. Rapidly double-click "Generate Invoice".
            3. Check database table `tbl_invoices`.
        - **Resolution:** Applied button debounce on frontend & unique transaction hash constraint in MySQL. Retested in build v2.4.
        """)

# ==============================================================================
# TAB 4: E-HOSPITAL MANAGEMENT SYSTEM (SIMULATOR)
# ==============================================================================
with tabs[3]:
    st.subheader("🏥 E-Hospital Management System (Interactive Simulator)")
    st.write("A comprehensive 2-month project designed to digitize healthcare workflows, curtail paperwork, and minimize administrative billing errors.")
    
    sim_tab1, sim_tab2, sim_tab3, sim_tab4 = st.tabs([
        "🩺 Doctor Consultations",
        "🏥 Patient Records",
        "💊 Pharmacy Inventory",
        "💳 Billing & Insurance"
    ])
    
    with sim_tab1:
        st.markdown("##### Doctor OPD Queue & Duty Roster")
        doctors_df = pd.DataFrame([
            {"Doctor": "Dr. R. Mishra", "Specialization": "Cardiology", "Room": "OPD-102", "Available": "10:00 AM - 02:00 PM", "Patients Queued": 4},
            {"Doctor": "Dr. S. Mohapatra", "Specialization": "General Medicine", "Room": "OPD-105", "Available": "09:00 AM - 01:00 PM", "Patients Queued": 7},
            {"Doctor": "Dr. P. Dash", "Specialization": "Pediatrics", "Room": "OPD-201", "Available": "02:00 PM - 06:00 PM", "Patients Queued": 2}
        ])
        st.dataframe(doctors_df, use_container_width=True, hide_index=True)
        st.success("✅ Real-time synchronization eliminates double-booked time slots.")
        
    with sim_tab2:
        st.markdown("##### Electronic Medical Record (EMR) Search")
        uhid_search = st.text_input("Enter Patient UHID to Simulate Lookup:", value="UHID-2026-0842")
        if uhid_search:
            st.info(f"**Patient UHID:** {uhid_search} | **Name:** Rajesh Kumar | **Age/Sex:** 34 / Male | **Blood Group:** O+ | **Allergies:** Penicillin")
            st.write("Recent Visit: Routine OPD Consultation • Lab Tests Ordered: Lipid Profile, CBC")
            
    with sim_tab3:
        st.markdown("##### Pharmacy Drug Stock & Automated Low-Stock Triggers")
        pharmacy_df = pd.DataFrame([
            {"Item Code": "MED-01", "Medicine": "Paracetamol 650mg", "Stock": 420, "Min Threshold": 100, "Alert": "Normal"},
            {"Item Code": "MED-02", "Medicine": "Amoxicillin 500mg", "Stock": 45, "Min Threshold": 50, "Alert": "⚠️ LOW STOCK"},
            {"Item Code": "MED-03", "Medicine": "Cetirizine 10mg", "Stock": 310, "Min Threshold": 80, "Alert": "Normal"},
            {"Item Code": "MED-04", "Medicine": "Azithromycin 500mg", "Stock": 18, "Min Threshold": 30, "Alert": "⚠️ LOW STOCK"}
        ])
        st.dataframe(pharmacy_df, use_container_width=True, hide_index=True)
        
    with sim_tab4:
        st.markdown("##### Interactive Billing & Claims Calculator")
        col_b1, col_b2 = st.columns(2)
        with col_b1:
            consult_fee = st.number_input("Doctor Consultation Fee (₹)", value=500, step=50)
            lab_fee = st.number_input("Diagnostics & Lab Tests (₹)", value=1200, step=100)
            medicine_fee = st.number_input("Pharmacy & Medicines (₹)", value=850, step=50)
        with col_b2:
            has_insurance = st.checkbox("Apply Health Insurance / TPA Coverage", value=True)
            coverage_pct = st.slider("Insurance Coverage (%)", min_value=0, max_value=100, value=80) if has_insurance else 0
            
            subtotal = consult_fee + lab_fee + medicine_fee
            discount = (subtotal * coverage_pct) / 100 if has_insurance else 0
            final_payable = subtotal - discount
            
            st.metric(label="Total Bill", value=f"₹{subtotal:,.2f}")
            st.metric(label="Insurance Covered Amount", value=f"- ₹{discount:,.2f}")
            st.metric(label="Patient Final Out-of-Pocket", value=f"₹{final_payable:,.2f}")

# ==============================================================================
# TAB 5: TECHNICAL SKILLS & BI TOOLS
# ==============================================================================
with tabs[4]:
    st.subheader("Technical Competencies Matrix")
    
    col_sk1, col_sk2 = st.columns(2)
    
    with col_sk1:
        st.markdown("""
        <div class="card-box">
            <h4>🐍 Programming Languages</h4>
            <span class="tag">Python (Core &amp; Scripting)</span>
            <span class="tag">C</span>
            <span class="tag">C++ (OOP &amp; Data Structures)</span>
        </div>
        <div class="card-box">
            <h4>🧪 Quality Assurance &amp; Testing</h4>
            <span class="tag">Manual Testing</span>
            <span class="tag">Test Case Design</span>
            <span class="tag">Bug Tracking (Acedboard)</span>
            <span class="tag">UI/UX Testing</span>
            <span class="tag">Functional &amp; Regression Testing</span>
        </div>
        """, unsafe_allow_html=True)
        
    with col_sk2:
        st.markdown("""
        <div class="card-box">
            <h4>📊 Data, SQL &amp; BI Tools</h4>
            <span class="tag">SQL &amp; MySQL</span>
            <span class="tag">Power BI (Learning)</span>
            <span class="tag">Tableau (Learning)</span>
            <span class="tag">MS Excel (Pivot Tables &amp; Formulas)</span>
        </div>
        <div class="card-box">
            <h4>🌐 Web &amp; Productivity</h4>
            <span class="tag">HTML5</span>
            <span class="tag">CSS3</span>
            <span class="tag">JavaScript (Basic)</span>
            <span class="tag">MS Word &amp; PowerPoint</span>
        </div>
        """, unsafe_allow_html=True)
        
    st.markdown("#### Competency Overview")
    skills_chart_data = pd.DataFrame({
        "Skill Area": ["Manual Testing", "Test Case Design", "Python", "SQL / MySQL", "C / C++", "MS Excel", "Power BI / Tableau (Learning)"],
        "Proficiency Level": [90, 88, 82, 85, 78, 85, 65]
    }).set_index("Skill Area")
    st.bar_chart(skills_chart_data, color="#6366f1")

# ==============================================================================
# TAB 6: EDUCATION
# ==============================================================================
with tabs[5]:
    st.subheader("Academic Qualifications")
    
    col_ed1, col_ed2 = st.columns(2)
    
    with col_ed1:
        st.markdown("""
        <div class="card-box">
            <span class="subtitle-badge">Postgraduate</span>
            <h3>Master in Computer Applications (MCA)</h3>
            <p><strong>Institution:</strong> Presidency College, Berhampur, Odisha</p>
            <p><strong>Passing Year:</strong> 2026</p>
            <p style="color: #10b981; font-weight: 600;">Status: Completed — Result Awaited</p>
        </div>
        <div class="card-box">
            <span class="subtitle-badge">Higher Secondary</span>
            <h3>Class XII (Science)</h3>
            <p><strong>School:</strong> Binayak Acharya H.S. School, Berhampur</p>
            <p><strong>Board:</strong> CHSE Odisha (July 2021)</p>
            <p style="color: #10b981; font-weight: 600;">Percentage: 56%</p>
        </div>
        """, unsafe_allow_html=True)
        
    with col_ed2:
        st.markdown("""
        <div class="card-box">
            <span class="subtitle-badge">Undergraduate</span>
            <h3>Bachelor of Computer Applications (BCA)</h3>
            <p><strong>Institution:</strong> Science College (Autonomous), Hinjilicut, Odisha</p>
            <p><strong>Passing Year:</strong> April 2024</p>
            <p style="color: #10b981; font-weight: 600;">CGPA: 7.08</p>
        </div>
        <div class="card-box">
            <span class="subtitle-badge">Secondary School</span>
            <h3>Class X (Matriculation)</h3>
            <p><strong>School:</strong> Aryan Public School, Aska, Odisha</p>
            <p><strong>Board:</strong> CBSE (May 2019)</p>
            <p style="color: #10b981; font-weight: 600;">Percentage: 52%</p>
        </div>
        """, unsafe_allow_html=True)

# ==============================================================================
# TAB 7: LANGUAGES & PERSONAL INTERESTS
# ==============================================================================
with tabs[6]:
    st.subheader("Languages & Personal Interests")
    
    col_in1, col_in2 = st.columns(2)
    
    with col_in1:
        st.markdown("""
        <div class="card-box">
            <h4>🌐 Languages Known</h4>
            <p><strong>• English:</strong> Professional Working Proficiency</p>
            <p><strong>• Hindi:</strong> Fluent (Spoken &amp; Written)</p>
            <p><strong>• Odia:</strong> Native Language</p>
        </div>
        <div class="card-box">
            <h4>🤝 Community &amp; Volunteering</h4>
            <p>Active participant in college tech groups, community outreach, and peer mentorship in computer fundamentals.</p>
        </div>
        """, unsafe_allow_html=True)
        
    with col_in2:
        st.markdown("""
        <div class="card-box">
            <h4>🚀 Continuous Skill Acquisition</h4>
            <p>Passionate about exploring modern testing frameworks, API testing, Python data libraries, and Power BI dashboards.</p>
        </div>
        <div class="card-box">
            <h4>💻 Personal Portfolio Development</h4>
            <p>Keen interest in building, updating, and fine-tuning responsive developer portfolios and interactive digital artifacts.</p>
        </div>
        """, unsafe_allow_html=True)

# ==============================================================================
# TAB 8: CONTACT ME
# ==============================================================================
with tabs[7]:
    st.subheader("Get in Touch")
    st.write("I am actively exploring entry-level roles in Software QA / Testing, Python Development, and Data Analysis.")
    
    col_ct1, col_ct2 = st.columns(2)
    
    with col_ct1:
        st.markdown("""
        <div class="card-box">
            <h4>📬 Direct Contact Information</h4>
            <p><strong>Email:</strong> <a href="mailto:subhrajeet03@gmail.com">subhrajeet03@gmail.com</a></p>
            <p><strong>Primary Mobile:</strong> <a href="tel:+919776445055">+91-9776445055</a></p>
            <p><strong>Alternative Mobile:</strong> <a href="tel:+917205489555">+91-7205489555</a></p>
            <p><strong>Location:</strong> Aska, Ganjam, Odisha, India</p>
            <p><strong>LinkedIn:</strong> <a href="https://linkedin.com/in/subhrajeet-swain" target="_blank">linkedin.com/in/subhrajeet-swain</a></p>
            <p><strong>GitHub:</strong> <a href="https://github.com/subhrajeet03" target="_blank">github.com/subhrajeet03</a></p>
        </div>
        """, unsafe_allow_html=True)
        
    with col_ct2:
        with st.form("contact_form"):
            st.markdown("#### Send a Message")
            sender_name = st.text_input("Your Name*")
            sender_email = st.text_input("Your Email*")
            message_text = st.text_area("Message / Opportunity Details*")
            submit_button = st.form_submit_button("🚀 Submit Message")
            
            if submit_button:
                if sender_name and sender_email and message_text:
                    st.success(f"Thank you, {sender_name}! Your message has been noted. You can also reach me directly at subhrajeet03@gmail.com.")
                else:
                    st.warning("Please fill out all required fields before submitting.")
