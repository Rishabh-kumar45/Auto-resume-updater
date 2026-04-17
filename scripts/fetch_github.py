import requests
import os
from collections import Counter

def fetch_data(username):
    try:
        user_url = f"https://api.github.com/users/{username}"
        repo_url = f"https://api.github.com/users/{username}/repos"

        # 🔐 Use token to avoid rate limit
        token = os.getenv("GITHUB_TOKEN")

        headers = {
            "Accept": "application/vnd.github+json"
        }

        if token:
            headers["Authorization"] = f"Bearer {token}"

        # 🔹 API requests
        user_res = requests.get(user_url, headers=headers)
        repo_res = requests.get(repo_url, headers=headers)

        # 🔍 Debug
        print("User API status:", user_res.status_code)
        print("Repo API status:", repo_res.status_code)

        if user_res.status_code != 200:
            print("❌ User fetch failed:", user_res.text)
            return None

        if repo_res.status_code != 200:
            print("❌ Repo fetch failed:", repo_res.text)
            return None

        # 🔹 Convert to JSON
        user_data = user_res.json()
        repos = repo_res.json()

        # 🔹 Basic info
        avatar = user_data.get("avatar_url")
        bio = user_data.get("bio") or "Passionate developer."

        # 🔹 Sort repos (latest first)
        repos = sorted(repos, key=lambda x: x["updated_at"], reverse=True)

        projects = []
        languages = []

        for repo in repos:
            desc = repo.get("description") or "No description available"

            projects.append({
                "name": repo.get("name"),
                "description": desc,
                "url": repo.get("html_url")
            })

            if repo.get("language"):
                languages.append(repo["language"])

        # 🔹 Default fallback
        if not languages:
            languages = ["Python", "Git", "Automation"]

        # 🔹 Skill extraction
        skill_count = Counter(languages)
        top_skills = [skill for skill, _ in skill_count.most_common(5)]

        # 🔹 Final structured data
        data = {
            "name": user_data.get("name") or username,
            "role": "Software Developer",
            "github_url": f"https://github.com/{username}",
            "linkedin": "your-linkedin-id",  # 🔥 change this
            "avatar": avatar,
            "summary": bio,
            "repos": projects[:5],
            "skills": top_skills
        }

        print("✅ Data fetched successfully!")
        return data

    except Exception as e:
        print("❌ ERROR:", e)
        return None
