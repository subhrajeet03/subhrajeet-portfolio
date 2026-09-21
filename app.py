import streamlit as st


st.set_page_config(
    page_title="Subhrajeet Swain | Entry-Level IT Professional",
    page_icon="SS",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=DM+Mono:wght@400;500&family=Manrope:wght@400;600;700;800&display=swap');
    :root { --ink:#f4f7fb; --muted:#93a0b5; --line:#263246; --panel:#111722; --green:#9cff45; --blue:#6c7cff; }
    .stApp { background: radial-gradient(circle at 90% 0%,#1d2340 0,transparent 32rem), #0a0d14; color:var(--ink); }
    .boot-screen { position:fixed; inset:0; z-index:999; display:grid; place-items:center; background:#070a10; pointer-events:none; animation:boot-out .8s 2.1s forwards; }
    .boot-window { width:min(560px, calc(100vw - 2rem)); border:1px solid var(--line); border-radius:16px; overflow:hidden; background:#0b1019; box-shadow:0 30px 100px rgba(0,0,0,.55); animation:boot-in .7s ease-out both; }
    .boot-top { padding:.8rem 1rem; border-bottom:1px solid var(--line); color:var(--muted); font:.7rem 'DM Mono',monospace; }
    .boot-code { padding:1.4rem; color:#d7e0ef; font:.8rem/2 'DM Mono',monospace; }
    .boot-code b { color:var(--green); font-weight:500; }
    .boot-code i { color:#71809b; font-style:normal; }
    @keyframes boot-in { from { opacity:0; transform:translateY(18px); } to { opacity:1; transform:none; } }
    @keyframes boot-out { to { opacity:0; visibility:hidden; } }
    [data-testid="stHeader"] { background:transparent; }
    [data-testid="stSidebar"] { display:none; }
    .block-container { max-width:1120px; padding:2rem 2rem 3rem; }
    * { font-family:Manrope, sans-serif; }
    h1,h2,h3 { letter-spacing:-.07em!important; color:var(--ink)!important; }
    h1 { font-size:clamp(3.4rem,8vw,7rem)!important; line-height:.92!important; }
    h2 { font-size:clamp(1.8rem,3vw,2.5rem)!important; }
    .brand-row { display:flex; align-items:center; justify-content:space-between; margin-bottom:5rem; }
    .brand { color:var(--ink); font-weight:800; font-size:1rem; }
    .nav-links { display:flex; gap:1.2rem; }
    .nav-links a { color:var(--muted); font-size:.76rem; text-decoration:none; }
    .nav-links a:hover { color:var(--green); }
    .mark { display:inline-grid; place-items:center; width:30px; height:30px; margin-right:9px; border-radius:9px; background:var(--green); color:#10150d; font-size:.75rem; }
    .eyebrow { color:var(--green); font-size:.72rem; font-weight:800; letter-spacing:.16em; text-transform:uppercase; }
    .muted { color:var(--muted); }
    .hero-copy { max-width:410px; margin-top:2rem; color:var(--muted); font-size:1.08rem; line-height:1.65; }
    .hero-role { margin-top:1rem; color:#d7e0ef; font-size:.9rem; font-weight:700; letter-spacing:.02em; }
    .hero-actions { display:flex; flex-wrap:wrap; gap:.7rem; margin-top:1.7rem; }
    .hero-actions a { display:inline-block; padding:.72rem 1rem; border:1px solid var(--line); border-radius:10px; color:var(--muted); font-size:.78rem; font-weight:700; text-decoration:none; }
    .hero-actions a.primary { border-color:var(--green); background:var(--green); color:#10150d; }
    .hero-actions a:hover { border-color:var(--green); color:var(--green); }
    .hero-actions a.primary:hover { color:#10150d; }
    .pill { display:inline-block; margin:.35rem .35rem 0 0; padding:.42rem .65rem; border:1px solid var(--line); border-radius:99px; color:var(--muted); font-size:.72rem; }
    .terminal { margin-top:2rem; border:1px solid var(--line); border-radius:16px; overflow:hidden; background:#070a10; }
    .term-bar { padding:.7rem 1rem; border-bottom:1px solid var(--line); color:var(--muted); font: .7rem 'DM Mono',monospace; }
    .term-body { padding:1rem; color:#d7e0ef; font:.73rem/1.8 'DM Mono',monospace; }
    .prompt { color:var(--green); } .comment { color:#71809b; } .code { color:#b6c7ff; }
    .marquee { margin:5rem 0; padding:1rem 0; overflow:hidden; border-top:1px solid var(--line); border-bottom:1px solid var(--line); white-space:nowrap; }
    .marquee-track { display:flex; width:max-content; animation:marquee-scroll 24s linear infinite; }
    .marquee span { display:inline-block; margin-right:2.1rem; color:var(--muted); font-size:.7rem; font-weight:800; letter-spacing:.12em; text-transform:uppercase; }
    .marquee span:nth-child(even) { color:var(--green); }
    .card { height:100%; padding:1.6rem; border:1px solid var(--line); border-radius:20px; background:rgba(17,23,34,.82); }
    .card h3 { margin:0 0 1rem; font-size:1.25rem; }
    .card p { color:var(--muted); font-size:.88rem; line-height:1.7; }
    .project-label { color:var(--green); font-size:.7rem; font-weight:800; letter-spacing:.12em; text-transform:uppercase; }
    .project-tile { min-height:145px; padding:1rem; border:1px solid var(--line); border-radius:13px; background:#0e141e; }
    .project-tile strong { display:block; margin-bottom:.45rem; font-size:.9rem; }
    .project-tile p { margin:0; font-size:.78rem; }
    .contact { margin-top:7rem; padding:2rem 0; border-top:1px solid var(--line); border-bottom:1px solid var(--line); }
    .contact a { color:var(--green); font-weight:700; text-decoration:none; }
    .social-row { display:flex; flex-wrap:wrap; gap:.7rem; margin-top:1.3rem; }
    .social-row a { padding:.5rem .75rem; border:1px solid var(--line); border-radius:9px; color:var(--muted); font-size:.73rem; text-decoration:none; }
    .social-row a:hover { border-color:var(--green); color:var(--green); }
    .system-map { display:grid; grid-template-columns:repeat(4,1fr); gap:.7rem; margin-top:1.5rem; }
    .system-node { padding:1rem; border:1px solid var(--line); border-radius:12px; background:linear-gradient(145deg,rgba(108,124,255,.12),#0e141e); }
    .system-node small { display:block; margin-bottom:.55rem; color:var(--green); font:.65rem 'DM Mono',monospace; }
    .system-node strong { font-size:.8rem; }
    .card, .project-tile, .system-node { animation:surface-rise .7s ease both; transition:transform .2s ease, border-color .2s ease, box-shadow .2s ease; }
    .card:hover, .project-tile:hover, .system-node:hover { transform:translateY(-5px); border-color:var(--green); box-shadow:0 18px 50px rgba(0,0,0,.24); }
    .project-tile:nth-child(2), .system-node:nth-child(2) { animation-delay:.1s; }
    .project-tile:nth-child(3), .system-node:nth-child(3) { animation-delay:.2s; }
    .project-tile:nth-child(4), .system-node:nth-child(4) { animation-delay:.3s; }
    .terminal { animation:terminal-glow 3s ease-in-out infinite; }
    .availability-dot { display:inline-block; width:7px; height:7px; margin-right:6px; border-radius:50%; background:var(--green); animation:status-pulse 1.8s ease-in-out infinite; }
    @keyframes marquee-scroll { from { transform:translateX(0); } to { transform:translateX(-50%); } }
    @keyframes surface-rise { from { opacity:0; transform:translateY(18px); } to { opacity:1; transform:translateY(0); } }
    @keyframes terminal-glow { 0%,100% { box-shadow:0 0 0 rgba(156,255,69,0); } 50% { box-shadow:0 0 32px rgba(108,124,255,.14); } }
    @keyframes status-pulse { 0%,100% { box-shadow:0 0 0 0 rgba(156,255,69,.5); } 50% { box-shadow:0 0 0 7px rgba(156,255,69,0); } }
    div.stButton > button { border:1px solid var(--line); border-radius:10px; background:transparent; color:var(--muted); }
    div.stButton > button:hover { border-color:var(--green); color:var(--green); }
    @media (max-width:700px) { .block-container { padding:1.2rem 1rem 2rem; } .brand-row { margin-bottom:3.5rem; } .nav-links { gap:.6rem; } .system-map { grid-template-columns:1fr 1fr; } }
    @media (prefers-reduced-motion:reduce) { .boot-screen, .boot-window, .marquee-track, .card, .project-tile, .system-node, .terminal, .availability-dot { animation:none; } .boot-screen { display:none; } }
    </style>
    """,
    unsafe_allow_html=True,
)


if "tasks" not in st.session_state:
    st.session_state.tasks = [
        {"text": "Plan the week ahead", "done": False},
        {"text": "Take a proper lunch break", "done": False},
        {"text": "Read 10 pages", "done": True},
    ]


st.markdown(
    '<div class="boot-screen"><div class="boot-window"><div class="boot-top">portfolio_boot.py · ready</div><div class="boot-code"><b>></b> loading profile...<br><b>></b> initializing skills...<br><b>></b> opening workspace...<br><i>hello, I’m Subhrajeet Swain.</i></div></div></div>'
    '<div class="brand-row"><div class="brand"><span class="mark">SS</span> Subhrajeet Swain</div><div class="nav-links"><a href="#work">Work</a><a href="#experience">Experience</a><a href="#contact">Contact</a></div></div>',
    unsafe_allow_html=True,
)
hero_left, hero_right = st.columns([1.1, 0.9], gap="large")
with hero_left:
    st.markdown('<div class="eyebrow">Entry-level IT professional</div>', unsafe_allow_html=True)
    st.markdown('<h1>Hi, I’m<br><span style="color:var(--green)">Subhrajeet.</span></h1>', unsafe_allow_html=True)
with hero_right:
    st.markdown(
        '<p class="hero-role"><span class="availability-dot"></span>Python · QA Testing · SQL · IT Support</p>'
        '<p class="hero-copy">A motivated and detail-oriented BCA and MCA graduate applying software development, testing, and data-driven problem solving.</p>'
        '<div class="hero-actions"><a class="primary" href="#work">Explore my work →</a><a href="mailto:subhrajeet03@gmail.com">Get in touch ↗</a></div>'
        '<div class="social-row"><a href="https://github.com/subhrajeet-swain">GitHub ↗</a><a href="https://linkedin.com/in/subhrajeet-swain">LinkedIn ↗</a><a href="tel:+919776445055">+91 9776445055</a></div>'
        '<span class="pill">QA & testing</span><span class="pill">Software development</span><span class="pill">IT support</span>'
        '<div class="terminal"><div class="term-bar">● ● ● &nbsp; subhrajeet@portfolio:~</div><div class="term-body"><div><span class="prompt">$</span> whoami</div><div class="code">Subhrajeet Swain · entry-level IT professional</div><div><span class="prompt">$</span> focus --on</div><div class="comment"># learn, test, document, improve</div></div></div>',
        unsafe_allow_html=True,
    )

st.markdown(
    '<div class="marquee"><div class="marquee-track">' + "".join(
        f"<span>{item}</span>" for item in [
            "Python", "Manual testing", "SQL", "UI/UX testing", "MySQL",
            "Defect tracking", "HTML & CSS", "Data-driven problem solving",
        ] * 2
    ) + "</div></div>",
    unsafe_allow_html=True,
)

st.markdown('<div class="eyebrow">Selected work</div>', unsafe_allow_html=True)
st.header("Projects with purpose.")
work_col, about_col = st.columns([1.2, 0.8], gap="medium")
with work_col:
    st.markdown('<div class="card"><div class="project-label">Interactive demo</div><h3>Local task list</h3>', unsafe_allow_html=True)
    task_text = st.text_input("Add a task", placeholder="What needs doing?", label_visibility="collapsed")
    if st.button("Add task", key="add_task") and task_text.strip():
        st.session_state.tasks.insert(0, {"text": task_text.strip(), "done": False})
        st.rerun()
    remaining = sum(not task["done"] for task in st.session_state.tasks)
    st.caption(f"{remaining} {'task' if remaining == 1 else 'tasks'} left")
    for index, task in enumerate(st.session_state.tasks):
        checked = st.checkbox(task["text"], value=task["done"], key=f"task_{index}")
        st.session_state.tasks[index]["done"] = checked
    if st.button("Clear completed", key="clear_tasks"):
        st.session_state.tasks = [task for task in st.session_state.tasks if not task["done"]]
        st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)
with about_col:
    st.markdown(
        '<div class="card"><h3>Motivated to learn. Ready to contribute.</h3><p>Quick learner and team player with a strong foundation in computer applications, testing, troubleshooting, and documentation.</p><p><strong>Based in</strong><br>Aska, Ganjam, Odisha</p></div>',
        unsafe_allow_html=True,
    )

st.markdown('<div class="eyebrow" style="margin-top:7rem">Experience & toolkit</div>', unsafe_allow_html=True)
st.header("Background that compounds.")
experience, skills = st.columns(2, gap="medium")
with experience:
    st.markdown(
        '<div class="card"><h3>QA Intern · Team Pumpkin (Tech.)</h3><p class="project-label">Apr 2025 — Mar 2026</p><p>Performed functional and UI/UX testing for web and mobile applications. Designed test cases and scenarios, logged defects in Acedboard, documented outcomes, and collaborated on fix validation and retesting.</p><h3>Education</h3><p><strong>Master of Computer Applications</strong><br>Presidency College, Berhampur · Completed, result awaited</p><p><strong>Bachelor of Computer Applications</strong><br>Science College (Autonomous), Hinjilicut · CGPA 7.08</p><p><strong>Class XII / Class X</strong><br>CHSE Odisha · 56% / CBSE · 52%</p></div>',
        unsafe_allow_html=True,
    )
with skills:
    st.markdown(
        '<div class="card"><h3>Technical skills</h3><p><strong>Programming</strong><br>Python · C · C++ · JavaScript (basic)</p><p><strong>Databases & web</strong><br>SQL · MySQL · HTML · CSS · Web application testing</p><p><strong>Testing & support</strong><br>Manual testing · Test case design · Defect tracking · UI/UX testing · Troubleshooting · Documentation</p><p><strong>Tools & AI</strong><br>Excel · Word · PowerPoint · Power BI · Tableau · ChatGPT · Gemini · Claude · GitHub Copilot · Antigravity · Perplexity AI</p></div>',
        unsafe_allow_html=True,
    )

st.markdown('<div class="eyebrow" style="margin-top:4rem">Technical toolkit</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="system-map">'
    '<div class="system-node"><small>01 / CODE</small><strong>Python · C · C++</strong></div>'
    '<div class="system-node"><small>02 / DATA</small><strong>SQL · MySQL · Excel</strong></div>'
    '<div class="system-node"><small>03 / QUALITY</small><strong>Test cases · Defects · UI/UX</strong></div>'
    '<div class="system-node"><small>04 / TOOLS</small><strong>Power BI · Tableau · AI tools</strong></div>'
    '</div>',
    unsafe_allow_html=True,
)

st.markdown('<div class="eyebrow" style="margin-top:7rem">Academic & personal work</div>', unsafe_allow_html=True)
st.header("Built to solve real needs.")
projects = [
    ("E-Hospital Management System", "System concept for doctors, patients, appointments, lab results, billing, insurance, and medical supplies."),
    ("College Event Management System", "System concept for events, registrations, schedules, participants, and coordination."),
    ("IT Help Desk Ticketing System", "Ticket workflow with priority levels, SLA monitoring, search, status updates, and resolution notes."),
    ("Student Attendance & Result Management", "Database-driven records with attendance calculation and report generation for faculty."),
]
project_columns = st.columns(4, gap="small")
for column, (title, description) in zip(project_columns, projects):
    with column:
        st.markdown(f'<div class="project-tile"><strong>{title}</strong><p>{description}</p></div>', unsafe_allow_html=True)

st.markdown(
    '<div class="contact"><div class="eyebrow">Let’s connect</div><h2>Ready to learn & contribute.</h2><p class="muted">Open to opportunities in software development, QA, testing, and IT support.</p><p><a href="mailto:subhrajeet03@gmail.com">subhrajeet03@gmail.com</a><br><a href="tel:+919776445055">+91 9776445055</a></p><p><a href="https://linkedin.com/in/subhrajeet-swain">LinkedIn</a> · <a href="https://github.com/subhrajeet-swain">GitHub</a></p></div>',
    unsafe_allow_html=True,
)
st.caption("© 2026 Subhrajeet Swain · English · Hindi · Odia")
