import os
import re

# === CONFIGURATION ===
TOTAL_LESSONS = 137
README_PATH = "README.md"

# === STEP 1: Count folders named lesson-XX ===
lesson_folders = [d for d in os.listdir('.') if re.match(r'lesson-\d+', d)]
completed = len(lesson_folders)
percent = round((completed / TOTAL_LESSONS) * 100, 1)

# === STEP 2: Decide current rank ===
if percent < 10:
    rank = "🎓 Beginner"
elif percent < 40:
    rank = "🚀 Intermediate"
elif percent < 80:
    rank = "🔥 Advanced"
else:
    rank = "🏆 Master"

# === STEP 3: Build the progress section ===
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

# === STEP 4: Load README content ===
with open(README_PATH, "r", encoding="utf-8") as f:
    content = f.read()

# === STEP 5: Replace or append progress section ===
pattern = r"##\s*📚\s*Learning Progress[\s\S]*?(?=\n##\s|\Z)"
if re.search(pattern, content):
    content = re.sub(pattern, progress_section.strip(), content)
    print("🔁 Updated existing progress section in README.")
else:
    content += "\n\n---\n" + progress_section
    print("➕ Added new progress section to README.")

# === STEP 6: Save file ===
with open(README_PATH, "w", encoding="utf-8") as f:
    f.write(content)

print(f"✅ {completed}/{TOTAL_LESSONS} lessons ({percent}%). Rank: {rank}")
