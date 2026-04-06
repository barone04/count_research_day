from datetime import date, datetime, timedelta, timezone
from pathlib import Path
import re

TIMEZONE = timezone(timedelta(hours=7), name="Asia/Bangkok")
START_DATE = date(2025, 9, 5)
README_PATH = Path(__file__).resolve().with_name("README.md")


def compute_days(today: date | None = None) -> int:
    if today is None:
        today = datetime.now(TIMEZONE).date()
    return (today - START_DATE).days


def replace_once(content: str, pattern: str, replacement: str) -> str:
    updated, count = re.subn(pattern, replacement, content, count=1)
    if count != 1:
        raise ValueError(f"Pattern not found: {pattern}")
    return updated


def format_start_date() -> str:
    return f"{START_DATE.day} {START_DATE.strftime('%B %Y')}"


def update_readme(days: int) -> None:
    content = README_PATH.read_text(encoding="utf-8")

    content = replace_once(
        content,
        r"(Days_Free-)(\d+)(-[a-zA-Z]+)",
        rf"\g<1>{days}\g<3>",
    )
    content = replace_once(
        content,
        r"It has been _\d+ days_",
        f"It has been _{days} days_",
    )
    content = replace_once(
        content,
        r"counts the number of days since \*\*.*?\*\*",
        f"counts the number of days since **{format_start_date()}**",
    )

    README_PATH.write_text(content, encoding="utf-8", newline="\n")


if __name__ == "__main__":
    update_readme(compute_days())
