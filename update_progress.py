# update_progress.py
import os
import re
import sys
from datetime import datetime

TOTAL_LESSONS = 137
README_PATH = "README.md"
DEBUG_PATH = "update_progress_debug.txt"

def now_ts():
    return datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")

def write_debug(msg):
    try:
        with open(DEBUG_PATH, "a", encoding="utf-8") as f:
            f.write(f"{now_ts()} - {msg}\n")
    except Exception as e:
        print(f"⚠️ Failed to write debug log: {e}")

def list_lesson_folders():
    try:
        items = sorted([d for d in os.listdir('.') if re.match(r'lesson-\d+$', d) and os.path.isdir(d)])
        return items
    except Exception as e:
        write_debug(f"Error listing folders: {e}")
        return []

def read_readme():
    if not os.path.exists(README_PATH):
        write_debug("README.md not found.")
        return ""
    try:
        with open(README_PATH, "r", encoding="utf-8") as f:
            return f.read()
    except Exception as e:
        write_debug(f"Error reading README.md: {e}")
        return ""

def write_readme(content):
    try:
        with open(README_PATH, "w", encoding="utf-8") as f:
            f.write(content)
        write_debug("Wrote updated README.md")
        return True
    except Exception as e:
        write_debug(f"Error writing README.md: {e}")
        return False

def build_progress_section(completed):
    percent = round((completed / TOTAL_LESSONS) * 100, 1) if TOTAL_LESSONS > 0 else 0.0
    if percent < 10:
        rank = "🎓 Beginner"
    elif percent < 40:
        rank = "🚀 Intermediate"
    elif percent < 80:
        rank = "🔥 Advanced"
    else:
        rank = "🏆 Master"

    next_lesson = completed + 1 if completed < TOTAL_LESSONS else TOTAL_LESSONS

    # Use %25 to encode the percent sign for shields.io badge
    section = f"""
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
- 🔜 Next: Start Lesson {next_lesson}
"""
    return section

def replace_or_append_progress(readme_text, progress_section):
    # Flexible pattern to find an existing "Learning Progress" section
    pattern = r"##\s*📚\s*Learning Progress[\s\S]*?(?=\n##\s|\Z)"
    if re.search(pattern, readme_text):
        new_content = re.sub(pattern, progress_section.strip() + "\n", readme_text)
        return new_content, "updated"
    else:
        # Append at the end with separator
        sep = "\n\n---\n"
        new_content = readme_text + sep + progress_section
        return new_content, "added"

def main():
    write_debug("Script started")
    try:
        lessons = list_lesson_folders()
        write_debug(f"Found lesson folders: {lessons}")
        completed = len(lessons)
        readme_text = read_readme()
        write_debug(f"README length: {len(readme_text)}")
        progress_section = build_progress_section(completed)

        new_readme, action = replace_or_append_progress(readme_text, progress_section)

        if new_readme.strip() != readme_text.strip():
            success = write_readme(new_readme)
            if success:
                print(f"✅ README {action}: {completed}/{TOTAL_LESSONS} lessons ({round((completed/TOTAL_LESSONS)*100,1) if TOTAL_LESSONS else 0}%).")
                write_debug(f"README {action} successfully. Completed: {completed}")
            else:
                print("❌ Failed to write README.md. See debug file.")
                write_debug("Failed to write README.md")
                sys.exit(1)
        else:
            print("ℹ️ No changes required in README.md")
            write_debug("No changes required")

    except Exception as e:
        write_debug(f"Unhandled exception: {e}")
        print(f"❌ Error: {e}")
        sys.exit(1)
    finally:
        write_debug("Script finished")

if __name__ == "__main__":
    main()
