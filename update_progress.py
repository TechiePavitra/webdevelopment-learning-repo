# update_progress.py
import os
import re
from datetime import datetime

TOTAL_LESSONS = 137
README_PATH = "README.md"
DEBUG_PATH = "update_progress_debug.txt"

def list_lesson_folders():
    items = sorted([d for d in os.listdir('.') if re.match(r'lesson-\d+$', d)])
    return items

def read_readme():
    if not os.path.exists(README_PATH):
        return ""
    with open(README_PATH, "r", encoding="utf-8") as f:
        return f.read()

def write_debug(msg):
    with open(DEBUG_PATH, "a", encoding="utf-8") as f:
        f.write(f"{datetime.utcnow().isoformat()} UTC - {msg}\n")

def main():
    write_debug("Script started")
    lessons = list_lesson_folders()
    completed = len(lessons)
    percent = round((completed / TOTAL_LESSONS) * 100, 1) if TOTAL_LESSONS > 0 else 0.0

    if percent < 10:
        rank = "🎓 Beginner"
    elif percent < 40:
        rank = "🚀 Intermediate"
    elif percent < 80:
        rank = "🔥 Advanced"
    else:
        rank = "🏆 Master"

    progress_section = f"""
## 📚 Learning Progress

![Progress](https://img.shields.io/badge/Progress-{percent}%25-brightgreen)

<progress value="{completed}" max="{TOTAL_LESSONS}"></progress>

**{completed} / {TOTAL_LESSONS} lessons completed**

### 🏅 Current Rank: {rank}

---

### 🏆 Achievements
- ✅ Completed {completed} lessons so far  
- 💻 Uploaded source code to GitHub  
- 🌱 Maintaining steady learning pace  
- 🔜 Next: Start Lesson {completed + 1 if completed < TOTAL_LESSONS else TOTAL_LESSONS}
"""

    content = read_readme()
    write_debug(f"Found lesson folders: {lessons}")
    write_debug(f"README exists: {bool(content)}")
    # flexible pattern
    pattern = r"##\s*📚\s*Learning Progress[\s\S]*?(?=\n##\s|\Z)"
    if re.search(pattern, content):
        new_content = re.sub(pattern, progress_section.strip(), content)
        action = "updated"
    else:
        new_content = content + "\n\n---\n" + progress_section
        action = "added"

    # Write README only if changed
    if new_content.strip() != content.strip():
        with open(README_PATH, "w", encoding="
