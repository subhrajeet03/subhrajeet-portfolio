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
    .stApp::before, .stApp::after { position:fixed; z-index:0; pointer-events:none; content:""; }
    .stApp::before { inset:-25%; background:radial-gradient(circle at 20% 20%,rgba(156,255,69,.11),transparent 18%),radial-gradient(circle at 80% 8%,rgba(108,124,255,.2),transparent 25%),radial-gradient(circle at 70% 85%,rgba(162,91,255,.12),transparent 22%); filter:blur(35px); animation:aurora-drift 18s ease-in-out infinite alternate; }
    .stApp::after { inset:0; opacity:.18; background-image:linear-gradient(rgba(255,255,255,.035) 1px,transparent 1px),linear-gradient(90deg,rgba(255,255,255,.035) 1px,transparent 1px); background-size:72px 72px; mask-image:linear-gradient(to bottom,black,transparent 88%); animation:grid-drift 22s linear infinite; }
    .background-layer { position:fixed; inset:0; z-index:0; pointer-events:none; overflow:hidden; }
    .background-layer::before { position:absolute; inset:0; opacity:.2; background:repeating-linear-gradient(0deg,transparent 0 5px,rgba(255,255,255,.025) 6px 7px); content:""; animation:scanline 8s linear infinite; }
    .orb { position:absolute; width:8px; height:8px; border-radius:50%; background:var(--green); box-shadow:0 0 18px 3px rgba(156,255,69,.42); animation:particle-float 11s ease-in-out infinite; }
    .orb:nth-child(1) { top:22%; left:12%; animation-delay:-2s; }
    .orb:nth-child(2) { top:66%; left:82%; background:var(--blue); box-shadow:0 0 18px 3px rgba(108,124,255,.5); animation-delay:-6s; }
    .orb:nth-child(3) { top:38%; left:91%; width:5px; height:5px; animation-delay:-9s; }
    .orb:nth-child(4) { top:80%; left:24%; width:4px; height:4px; background:#d394ff; box-shadow:0 0 16px 3px rgba(211,148,255,.45); animation-delay:-4s; }
    .page-content { position:relative; z-index:1; }
    .hero-stage { min-height:72vh; display:flex; flex-direction:column; justify-content:center; align-items:center; text-align:center; padding:3rem 0 5rem; }
    .hero-stage .eyebrow { margin-bottom:1.4rem; }
    .hero-title { margin:0!important; font-size:clamp(3.8rem,10vw,8.5rem)!important; line-height:.84!important; }
    .hero-title .accent { color:var(--green); }
    .hero-subtitle { max-width:720px; margin:1.8rem auto 0; color:#d7e0ef; font-size:clamp(.9rem,2vw,1.2rem); font-weight:700; letter-spacing:.03em; }
    .hero-intro { max-width:620px; margin:1.2rem auto 0; color:var(--muted); font-size:1rem; line-height:1.7; }
    .hero-terminal { width:min(680px,100%); margin:2rem auto 0; text-align:left; }
    .hero-social { display:flex; justify-content:center; flex-wrap:wrap; gap:.7rem; margin-top:1.4rem; }
    .hero-social a { color:var(--muted); font-size:.75rem; text-decoration:none; }
    .hero-social a:hover { color:var(--green); }
    .section-divider { display:flex; align-items:center; gap:1rem; margin:2rem 0 3rem; color:var(--muted); font: .7rem 'DM Mono',monospace; }
    .section-divider::before, .section-divider::after { height:1px; flex:1; background:var(--line); content:""; }
    .editor-card { border:1px solid var(--line); border-radius:16px; overflow:hidden; background:#070a10; }
    .editor-top { display:flex; justify-content:space-between; padding:.75rem 1rem; border-bottom:1px solid var(--line); color:var(--muted); font:.7rem 'DM Mono',monospace; }
    .editor-code { padding:1.2rem; color:#d7e0ef; font:.78rem/2 'DM Mono',monospace; }
    .editor-code .line-no { display:inline-block; width:2rem; color:#52617b; }
    .editor-code .key { color:#b6c7ff; } .editor-code .value { color:var(--green); } .editor-code .comment { color:#71809b; }
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
    @keyframes aurora-drift { 0% { transform:translate3d(-3%, -2%, 0) rotate(0deg) scale(1); } 100% { transform:translate3d(3%, 3%, 0) rotate(8deg) scale(1.08); } }
    @keyframes grid-drift { from { background-position:0 0,0 0; } to { background-position:72px 72px,72px 72px; } }
    @keyframes scanline { from { transform:translateY(-8%); } to { transform:translateY(8%); } }
    @keyframes particle-float { 0%,100% { transform:translate3d(0,0,0) scale(1); opacity:.45; } 50% { transform:translate3d(34px,-48px,0) scale(1.5); opacity:1; } }
    div.stButton > button { border:1px solid var(--line); border-radius:10px; background:transparent; color:var(--muted); }
    div.stButton > button:hover { border-color:var(--green); color:var(--green); }
    @media (max-width:700px) { .block-container { padding:1.2rem 1rem 2rem; } .brand-row { margin-bottom:3.5rem; } .nav-links { gap:.6rem; } .system-map { grid-template-columns:1fr 1fr; } }
    @media (prefers-reduced-motion:reduce) { .stApp::before, .stApp::after, .background-layer::before, .boot-screen, .boot-window, .marquee-track, .card, .project-tile, .system-node, .terminal, .availability-dot, .orb { animation:none; } .boot-screen { display:none; } }
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
    '<div class="background-layer" aria-hidden="true"><span class="orb"></span><span class="orb"></span><span class="orb"></span><span class="orb"></span></div><div class="page-content">'
    ,
    unsafe_allow_html=True,
)
st.markdown(
    '<div class="boot-screen"><div class="boot-window"><div class="boot-top">portfolio_boot.py · ready</div><div class="boot-code"><b>></b> loading profile...<br><b>></b> initializing skills...<br><b>></b> opening workspace...<br><i>hello, I’m Subhrajeet Swain.</i></div></div></div>'
    '<div class="brand-row"><div class="brand"><span class="mark">SS</span> Subhrajeet Swain</div><div class="nav-links"><a href="#work">Work</a><a href="#experience">Experience</a><a href="#contact">Contact</a></div></div>',
    unsafe_allow_html=True,
)
st.markdown(
    '<section class="hero-stage">'
    '<div class="eyebrow">Entry-level IT professional · 2026</div>'
    '<h1 class="hero-title">Hi, I’m<br><span class="accent">Subhrajeet.</span></h1>'
    '<p class="hero-subtitle">Python Developer · QA Tester · Data & IT Support</p>'
    '<p class="hero-intro">I turn requirements into tested, documented, and useful digital systems—with a detail-oriented approach and a constant willingness to learn.</p>'
    '<div class="hero-actions"><a class="primary" href="#work">Explore my work →</a><a href="mailto:subhrajeet03@gmail.com">Get in touch ↗</a></div>'
    '<div class="hero-social"><a href="https://github.com/subhrajeet-swain">GitHub ↗</a><span class="muted">·</span><a href="https://linkedin.com/in/subhrajeet-swain">LinkedIn ↗</a><span class="muted">·</span><a href="tel:+919776445055">+91 9776445055</a></div>'
    '<div class="hero-terminal terminal"><div class="term-bar">● ● ● &nbsp; subhrajeet@portfolio:~</div><div class="term-body"><div><span class="prompt">$</span> whoami</div><div class="code">Subhrajeet Swain · entry-level IT professional</div><div><span class="prompt">$</span> focus --on</div><div class="comment"># learn, test, document, improve</div></div></div>'
    '</section>',
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

st.markdown('<div class="section-divider">profile.py · system summary</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="editor-card">'
    '<div class="editor-top"><span>subhrajeet_profile.py</span><span>Python 3.11 · ready</span></div>'
    '<div class="editor-code">'
    '<div><span class="line-no">01</span><span class="key">profile</span> = {</div>'
    '<div><span class="line-no">02</span>&nbsp;&nbsp;<span class="key">"location"</span>: <span class="value">"Aska, Odisha"</span>,</div>'
    '<div><span class="line-no">03</span>&nbsp;&nbsp;<span class="key">"strength"</span>: <span class="value">"quality-minded execution"</span>,</div>'
    '<div><span class="line-no">04</span>&nbsp;&nbsp;<span class="key">"approach"</span>: <span class="value">"learn · test · document · improve"</span>,</div>'
    '<div><span class="line-no">05</span>&nbsp;&nbsp;<span class="key">"next_step"</span>: <span class="value">"ready to contribute"</span>,</div>'
    '<div><span class="line-no">06</span>}</div>'
    '<div><span class="line-no">07</span><span class="comment"># built with curiosity and consistency</span></div>'
    '</div></div>',
    unsafe_allow_html=True,
)

st.markdown('<div id="work"></div><div class="eyebrow">Selected work</div>', unsafe_allow_html=True)
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

st.markdown('<div id="experience"></div><div class="eyebrow" style="margin-top:7rem">Experience & toolkit</div>', unsafe_allow_html=True)
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
    '<div id="contact" class="contact"><div class="eyebrow">Let’s connect</div><h2>Ready to learn & contribute.</h2><p class="muted">Open to opportunities in software development, QA, testing, and IT support.</p><p><a href="mailto:subhrajeet03@gmail.com">subhrajeet03@gmail.com</a><br><a href="tel:+919776445055">+91 9776445055</a></p><p><a href="https://linkedin.com/in/subhrajeet-swain">LinkedIn</a> · <a href="https://github.com/subhrajeet-swain">GitHub</a></p></div>',
    unsafe_allow_html=True,
)
st.caption("© 2026 Subhrajeet Swain · English · Hindi · Odia")
st.markdown("</div>", unsafe_allow_html=True)
