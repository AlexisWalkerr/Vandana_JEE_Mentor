"""
====================================================================================
    Part of     : Vandana_JEE_Mentor — Tools Module
    Purpose     : Track & update single-user learning progress in JSON storage.

    Team Name   : Anagha_Vandana
------------------------------------------------------------------------------------
    Description : Enables evaluator agent to update topic-wise mastery levels
                  to improve future study planning decisions.
====================================================================================
"""


import json
from pathlib import Path

# Data file: Vandana_JEE_Mentor/data/progress.json
DATA_PATH = Path(__file__).resolve().parent.parent / "data" / "progress.json"


def _default_progress() -> dict:
    # Basic starter structure; you can customize later.
    return {
        "physics": {"mechanics": 0, "waves": 0, "electromagnetism": 0},
        "chemistry": {"physical": 0, "organic": 0, "inorganic": 0},
        "maths": {"algebra": 0, "calculus": 0, "coordinate_geometry": 0},
    }


def _load_progress() -> dict:
    if not DATA_PATH.exists():
        return _default_progress()
    try:
        with open(DATA_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        # If file is corrupted, reset to default
        return _default_progress()


def _save_progress(data: dict) -> None:
    DATA_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(DATA_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)


def get_progress() -> str:
    """
    Tool function for planner_agent.
    Returns a human-readable summary of current progress.
    Single-user only.
    """
    prog = _load_progress()
    lines: list[str] = []

    for subject, topics in prog.items():
        parts = [f"{name} {pct}%" for name, pct in topics.items()]
        lines.append(f"{subject.title()}: " + ", ".join(parts))

    summary = "\n".join(lines)
    return (
        "Current preparation progress (approximate):\n"
        f"{summary}\n\n"
        "You can assume 0% means untouched, 100% means fully mastered."
    )


def update_progress(subject: str, topic: str, percent: int) -> str:
    """
    Update the progress for a specific subject/topic.
    - subject: 'Physics', 'Chemistry', 'Maths'
    - topic: any string label (e.g. 'mechanics', 'limits', 'organic')
    - percent: 0–100
    Returns a short confirmation string.
    """
    s = subject.strip().lower()
    t = topic.strip().lower()
    pct = max(0, min(100, int(percent)))  # clamp 0–100

    data = _load_progress()

    if s not in data:
        data[s] = {}

    data[s][t] = pct
    _save_progress(data)

    return (
        f"Updated progress: {subject.title()} → {topic} = {pct}% complete.\n"
        "This will be used in future planning."
    )
