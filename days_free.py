from datetime import datetime
import re

START_DATE = datetime(2025, 11, 20)

def compute_days():
    today = datetime.now()
    return (today - START_DATE).days

def update_readme(days):
    with open("README.md", "r") as f:
        content = f.read()

    # Update badge: Days_Free-###-<color>
    content = re.sub(
        r"(Days_Free-)(\d+)(-[a-zA-Z]+)",
        rf"\g<1>{days}\g<3>",
        content
    )

    # Update sentence: It has been _### days_
    content = re.sub(
        r"It has been _\d+ days_",
        f"It has been _{days} days_",
        content
    )

    with open("README.md", "w") as f:
        f.write(content)

if __name__ == "__main__":
    days = compute_days()
    update_readme(days)
