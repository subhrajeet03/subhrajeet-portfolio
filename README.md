# Subhrajeet Swain — Personal Portfolio Website

A sleek, responsive, modern personal developer and QA portfolio created for **Subhrajeet Swain** (BCA & MCA Graduate, QA Intern at Team Pumpkin).

---

## 🌟 Key Features

- **Dynamic Hero Section**: Interactive typewriter effect highlighting key roles (`QA Specialist`, `Python Developer`, `MCA Graduate`, `Data & BI Enthusiast`), active job-seeking status badge, and direct call-to-actions.
- **Dark & Light Mode**: Seamless theme toggle with local storage persistence and system preference detection.
- **Experience Timeline**: Detailed highlight of QA Internship at **Team Pumpkin (Tech.)** with testing competencies, defect tracking (**Acedboard**), and UI/UX validation.
- **Project Showcase & Modal**: Featured breakdown of the **E-Hospital Management System** with sub-modules, impact metrics, and interactive architecture view.
- **Interactive Skills Matrix**: Filterable skills by category (*Programming*, *Testing & QA*, *Data & BI*, *Web & Databases*, *Productivity & Tools*).
- **Education Section**: Complete timeline for MCA (Presidency College), BCA (Science College Autonomous - CGPA 7.08), Class XII, and Class X.
- **One-Click Contact & Copy**: Instant clipboard copy for phone numbers and email with toast notifications, plus a functional contact inquiry form.
- **Print / PDF Friendly**: Styled `@media print` rules allow saving or printing a clean, formatted CV directly (`Ctrl + P`).
- **Zero Build Dependencies**: Pure HTML5, CSS3, and modern Vanilla ES6+ JavaScript. No `npm`, `node_modules`, or complex build steps required!

---

## 📂 Project Structure

```
subhrajeet-portfolio/
│
├── index.html            # Main website markup & semantic structure
├── css/
│   └── style.css         # Design system, CSS variables, dark/light themes, animations
├── js/
│   └── main.js           # Theme toggle, typewriter, filter, modal, clipboard toasts
├── assets/
│   └── avatar.svg        # Custom modern tech avatar SVG
└── README.md             # Documentation and deployment guide
```

---

## 🚀 How to View Locally

### Option 1: Direct File Open
Simply double-click `index.html` or right-click and choose **Open with > Chrome / Edge / Firefox**.

### Option 2: Local HTTP Server (Python)
If you have Python installed, open PowerShell or Terminal in this folder and run:
```powershell
python -m http.server 8000
```
Then visit: [http://localhost:8000](http://localhost:8000)

---

## 🌐 Free One-Click Deployment

### Deploy to GitHub Pages (Recommended)
1. Initialize git in this folder:
   ```bash
   git init
   git add .
   git commit -m "Initial portfolio commit"
   ```
2. Create a new repository on [GitHub](https://github.com/new) named `subhrajeet-swain.github.io` (or any name).
3. Link and push:
   ```bash
   git remote add origin https://github.com/<your-username>/<repo-name>.git
   git branch -M main
   git push -u origin main
   ```
4. In GitHub repository **Settings > Pages**, set the source branch to `main` and save. Your site is live!

### Deploy to Netlify / Vercel
- **Netlify**: Drag-and-drop this entire folder into [Netlify Drop](https://app.netlify.com/drop).
- **Vercel**: Run `vercel` in terminal or import your GitHub repository into Vercel.

---

## 🎨 How to Customize

- **Add Your Real Photo**: Place a photo named `photo.jpg` in the `assets/` folder, then in `index.html`, change `src="assets/avatar.svg"` to `src="assets/photo.jpg"`.
- **Add a Downloadable PDF Resume**: Place your PDF file in `assets/Subhrajeet_Swain_Resume.pdf`, and link it to the "Print / Save Resume" button:
  ```html
  <a href="assets/Subhrajeet_Swain_Resume.pdf" download class="btn btn-secondary">Download Resume</a>
  ```
- **Update GitHub / Social Links**: Add your GitHub link inside the `.hero-cta-group` or footer in `index.html`.
