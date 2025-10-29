# update_progress.py
import os
import re

TOTAL_LESSONS = 137
README_PATH = "README.md"

def list_lessons():
    """Return all folders that start with 'lesson'."""
    return [d for d in os.listdir('.') if d.lower().startswith("lesson") and os.path.isdir(d)]

def get_rank(percent):
    """Sigma-themed progress ranks."""
    if percent == 0:
        return "🍼 Beginner Sigma — Just opened VS Code!"
    elif percent < 10:
        return "🐣 HTML Learner — Writing your first!<p>"
    elif percent < 25:
        return "🎨 CSS Explorer — Styling your path to glory!"
    elif percent < 40:
        return "⚙️ JS Rookie — Figuring out the magic of console.log!"
    elif percent < 60:
        return "🚀 DOM Tamer — You move elements like a Jedi!"
    elif percent < 75:
        return "🔥 Project Coder — Websites are coming alive!"
    elif percent < 90:
        return "🧠 Web Dev Pro — CSS, JS, and HTML bow to you!"
    elif percent < 100:
        return "🤖 Sigma Developer — You’re almost at 100!"
    else:
        return "🏆 Ultimate Sigma Legend — Course conquered! CodeWithHarry would be proud!"

def get_achievements(completed):
    """Generate dynamic, funny achievements."""
    ach = []
    if completed >= 1:
        ach.append("✅ First lesson complete — welcome to the Sigma grind!")
    if completed >= 5:
        ach.append("📘 HTML fundamentals — mastered the art of <tags>!")
    if completed >= 10:
        ach.append("🎨 CSS magician — colors and layouts fear you!")
    if completed >= 20:
        ach.append("💡 JavaScript warrior — alert('Learning!');")
    if completed >= 50:
        ach.append("🔥 Halfway done — your code has main character energy!")
    if completed >= 75:
        ach.append("⚡ DOM conqueror — events, forms, and logic are yours!")
    if completed >= 100:
        ach.append("🧩 Full-stack explorer — time to deploy something cool!")
    if completed >= TOTAL_LESSONS:
        ach.append("🏁 All 137 lessons completed — you are the SIGMA LEGEND! 💪")

    if not ach:
        ach.append("🎯 Start learning to unlock achievements!")

    return "\n".join(f"- {a}" for a in ach)

def main():
    lessons = list_lessons()
    completed = len(lessons)
    percent = round((completed / TOTAL_LESSONS) * 100, 1)
    rank = get_rank(percent)
    achievements = get_achievements(completed)

    section = f"""
---

## 📚 Sigma Web Development Progress

![Progress](https://img.shields.io/badge/Progress-{percent}%25-brightgreen?style=for-the-badge)

<progress value="{completed}" max="{TOTAL_LESSONS}"></progress>

**{completed} / {TOTAL_LESSONS} lessons completed**

### 🏅 Current Rank: {rank}

---

### 🏆 Achievements
{achievements}

---

💖 *Special thanks to [CodeWithHarry](https://www.youtube.com/@CodeWithHarry) for creating the Sigma Web Development Course!*
"""

    # read README
    with open(README_PATH, "r", encoding="utf-8") as f:
        content = f.read()

    # replace old section or append after About
    pattern = r"## 📚 Sigma Web Development Progress[\s\S]*?(?=\Z)"
    if re.search(pattern, content):
        new_content = re.sub(pattern, section.strip(), content)
    else:
        new_content = content.strip() + "\n\n" + section.strip()

    # write back
    with open(README_PATH, "w", encoding="utf-8") as f:
        f.write(new_content)

    print(f"✅ Updated README: {completed}/{TOTAL_LESSONS} lessons ({percent}%). Rank: {rank}")

if __name__ == "__main__":
    main()
