import os
import shutil
import smtplib
from email.mime.text import MIMEText

print("🚀 Starting Resume Automation...\n")

# Step 1: Fetch GitHub data
print("📡 Fetching GitHub data...")
os.system("python scripts/fetch_github.py")

# Step 2: Generate Resume
print("\n📝 Generating Resume...")
os.system("python scripts/generate_resume.py")

# Step 3: Update Website
print("\n🌐 Updating website...")
shutil.copy("output/resume.html", "index.html")

# Step 4: Email Notification
print("\n📧 Sending email notification...")

# 🔐 Get from GitHub Secrets
sender_email = os.getenv("EMAIL_USER")
receiver_email = "araj84265@gmail.com"   # your email
app_password = os.getenv("EMAIL_PASS")

# 🔍 Debug prints (IMPORTANT)
print("DEBUG EMAIL:", sender_email)
print("DEBUG PASS:", "Loaded" if app_password else None)

# Email content
message = MIMEText("Your resume has been updated successfully!")
message["Subject"] = "Resume Update Notification"
message["From"] = sender_email
message["To"] = receiver_email

try:
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(sender_email, app_password)
    server.send_message(message)
    server.quit()
    print("Email sent successfully ✅")
except Exception as e:
    print("❌ Email failed:", e)

print("\n✅ Resume & website updated successfully!")
