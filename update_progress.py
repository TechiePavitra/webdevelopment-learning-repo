import os
import re

# === Configuration ===
TOTAL_LESSONS = 137  # total lessons in your course
README_PATH = "README.md"

# === Step 1: Count completed lessons ===
lesson_folders = [d for d in os.listdir('.') if re.match(r'lesson-\d+', d)]
completed = len(lesson_folders)
percent = round((completed / TOTAL_LESSONS) * 100, 1)

# === Step 2: Define achievement level ===
if percent < 10:
    rank = "🎓 Beginner"
elif percent < 40:
    rank = "🚀 Intermediate"
elif percent < 80:
    rank = "🔥 Advanced"
else:
    rank = "🏆 Master"

# === Step 3: Generate new progress section ===
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

# === Step 4: Read README ===
with open(README_PATH, "r", encoding="utf-8") as f:
    content = f.read()

# === Step 5: Replace or append progress section ===
if "## 📚 Learning Progress" in content:
    # Replace existing progress section
    content = re.sub(r"## 📚 Learning Progress[\s\S]*?(?=\n## |$)", progress_section, content)
else:
    # Append at end if missing
    content += "\n\n---\n" + progress_section

# === Step 6: Write back updated README ===
with open(README_PATH, "w", encoding="utf-8") as f:
    f.write(content)

print(f"✅ Updated README with {completed}/{TOTAL_LESSONS} lessons ({percent}%). Rank: {rank}")
