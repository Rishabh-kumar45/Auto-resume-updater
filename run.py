import os
import smtplib
import shutil
from email.mime.text import MIMEText
from jinja2 import Environment, FileSystemLoader
from scripts.fetch_github import fetch_data

print("🚀 Starting Resume Automation...\n")

# ✅ No input (CI/CD safe)
username = os.getenv("GITHUB_USERNAME", "Ayushraj2319")

print(f"📡 Fetching GitHub data for {username}...")
data = fetch_data(username)

if not data:
    print("❌ Failed to fetch data")
    exit(1)

# ✅ Generate HTML
print("\n📝 Generating Resume Website...")

env = Environment(loader=FileSystemLoader("templates"))
template = env.get_template("resume.html")

output = template.render(data)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(output)

print("✅ index.html generated")

# ✅ SAFE PDF handling (no crash)
if os.path.exists("output/resume.pdf"):
    shutil.copy("output/resume.pdf", "resume.pdf")
    print("📄 PDF copied")
else:
    print("⚠️ No PDF found (skipping)")

# ✅ Email (safe)
print("\n📧 Sending email notification...")

sender_email = os.getenv("EMAIL_USER")
receiver_email = sender_email
app_password = os.getenv("EMAIL_PASS")

if sender_email and app_password:
    try:
        msg = MIMEText("✅ Resume updated successfully!")
        msg["Subject"] = "Resume Update"
        msg["From"] = sender_email
        msg["To"] = receiver_email

        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender_email, app_password)
        server.send_message(msg)
        server.quit()

        print("✅ Email sent")
    except Exception as e:
        print("❌ Email failed:", e)
else:
    print("⚠️ Email skipped")

print("\n🎉 Done!")
