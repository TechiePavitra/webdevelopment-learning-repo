# update_progress.py
import os
import re
from datetime import datetime

TOTAL_LESSONS = 137
README_PATH = "README.md"

def list_lessons():
    # Count all folders that start with 'lesson'
    return [d for d in os.listdir('.') if d.lower().startswith("lesson") and os.path.isdir(d)]

def main():
    lessons = list_lessons()
    completed = len(lessons)
    percent = round((completed / TOTAL_LESSONS) * 100, 1)

    if percent < 10:
        rank = "🎓 Beginner"
    elif percent < 40:
        rank = "🚀 Intermediate"
    elif percent < 80:
        rank = "🔥 Advanced"
    else:
        rank = "🏆 Master"

    section = f"""
## 📚 Learning Progress

![Progress](https://img.shields.io/badge/Progress-{percent}%25-brightgreen)

<progress value="{completed}" max="{TOTAL_LESSONS}"></progress>

**{completed} / {TOTAL_LESSONS} lessons completed**

### 🏅 Current Rank: {rank}
"""

    if os.path.exists(README_PATH):
        with open(README_PATH, "r", encoding="utf-8") as f:
            content = f.read()
    else:
        content = ""

    # Replace or add section
    pattern = r"## 📚 Learning Progress[\s\S]*?(?=\n## |\Z)"
    if re.search(pattern, content):
        new_content = re.sub(pattern, section.strip(), content)
    else:
        new_content = content + "\n\n---\n" + section

    with open(README_PATH, "w", encoding="utf-8") as f:
        f.write(new_content)

    print(f"✅ Updated README: {completed}/{TOTAL_LESSONS} lessons ({percent}%). Rank: {rank}")

if __name__ == "__main__":
    main()
