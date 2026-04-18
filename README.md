# 🚀 Auto Resume Updater

Automatically generate and update your resume website using GitHub data with CI/CD.

---

## 🌐 Live Demo

👉 https://Ayushraj2319.github.io/auto-resume-updater/

---

## 📌 Project Overview

This project dynamically fetches data from GitHub and generates a professional resume website.
It uses automation pipelines to keep the resume updated without manual effort.

---

## ✨ Features

* 🔄 Fetch GitHub profile & repositories
* 📊 Extract skills based on languages used
* 🧠 Smart project selection (latest + relevant)
* 🌐 Auto-generate portfolio website
* 📄 Downloadable resume (PDF)
* 🌙 Dark mode toggle
* ⚙️ CI/CD automation using GitHub Actions
* 📧 Email notification after update

---

## 🖼️ Screenshots

### 💻 Resume Website

![Resume](assets/resume.png)

### ⚙️ CI/CD Pipeline

![Pipeline](assets/pipeline.png)

---

## 🛠️ Tech Stack

* Python 🐍
* Jinja2 (Templating)
* GitHub API
* GitHub Actions (CI/CD)
* HTML + CSS

---

## ⚙️ How It Works

```
GitHub API → Fetch Data → Process → Generate HTML → Deploy via GitHub Pages
```

---

## 🚀 Setup Instructions

### 1. Clone Repository

```
git clone https://github.com/Ayushraj2319/auto-resume-updater.git
cd auto-resume-updater
```

---

### 2. Create Virtual Environment

```
python3 -m venv venv
source venv/bin/activate
```

---

### 3. Install Dependencies

```
pip install requests jinja2
```

---

### 4. Add GitHub Token (Important)

```
export GITHUB_TOKEN=your_token_here
```

---

### 5. Run Project

```
python run.py
```

---

## 🔄 CI/CD Pipeline

The project uses GitHub Actions to automate updates.

### Trigger Methods:

* Manual → Actions → Run workflow
* Automatic → Daily (cron job)

---

## 📂 Project Structure

```
auto-resume-updater/
│
├── scripts/
│   └── fetch_github.py
├── templates/
│   └── resume.html
├── output/
├── data/
├── assets/
│   ├── resume.png
│   └── pipeline.png
├── index.html
├── resume.pdf
├── run.py
└── .github/workflows/update.yml
```

---

## 🧠 Key Concepts Used

* API Integration
* Data Processing & Filtering
* Template Rendering
* CI/CD Automation
* Git Version Control

---

## 🎯 Use Case

* Portfolio automation
* Resume auto-update system
* DevOps learning project
* GitHub-based portfolio builder

---

## 🧑‍💻 Author

**Ayush Raj**
GitHub: https://github.com/Ayushraj2319

---

## ⭐ If you like this project

Give it a ⭐ on GitHub!
