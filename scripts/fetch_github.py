import requests
import json

username = "Ayushraj2319"
url = f"https://api.github.com/users/{username}/repos"

response = requests.get(url)

projects = []
languages = set()

if response.status_code == 200:
    repos = response.json()

    # ✅ FIX: inside the if block
    repos = sorted(repos, key=lambda x: x["updated_at"], reverse=True)

    for repo in repos:
        projects.append(repo["name"])

        if repo["language"]:   # ignore None
            languages.add(repo["language"])

    data = {
        "projects": projects[:5],   # top 5 projects
        "skills": list(languages)
    }

    with open("data/github_data.json", "w") as f:
        json.dump(data, f, indent=2)

    print("Data saved successfully ✅")

else:
    print("Error fetching data")


