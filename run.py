import os
import smtplib
import shutil
from email.mime.text import MIMEText
from jinja2 import Environment, FileSystemLoader
from scripts.fetch_github import fetch_data

print("🚀 Starting Resume Automation...\n")

# 🔹 Username (no input for CI/CD)
username = os.getenv("GITHUB_USERNAME") or "Ayushraj2319"

print(f"📡 Fetching GitHub data for {username}...")
data = fetch_data(username)

if not data:
    print("❌ Failed to fetch data")
    exit()

# 🔹 Generate HTML
print("\n📝 Generating Resume Website...")

env = Environment(loader=FileSystemLoader("templates"))
template = env.get_template("resume.html")

output = template.render(data)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(output)

print("✅ index.html generated")

# 🔹 Copy PDF to root (IMPORTANT FIX)
if os.path.exists("output/resume.pdf"):
    shutil.copy("output/resume.pdf", "resume.pdf")
    print("📄 PDF copied to root")
else:
    print("⚠️ resume.pdf not found")

# 🔹 Email notification
print("\n📧 Sending email notification...")

sender_email = os.getenv("EMAIL_USER")
receiver_email = sender_email
app_password = os.getenv("EMAIL_PASS")

if sender_email and app_password:
    try:
        message = MIMEText("✅ Resume updated successfully!")
        message["Subject"] = "Resume Update"
        message["From"] = sender_email
        message["To"] = receiver_email

        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender_email, app_password)
        server.send_message(message)
        server.quit()

        print("✅ Email sent successfully")

    except Exception as e:
        print("❌ Email failed:", e)
else:
    print("⚠️ Email skipped (no credentials set)")

print("\n🎉 Resume Website Updated Successfully!")
