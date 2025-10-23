#!/usr/bin/env python3
"""
Organize lecture .md files from Desktop to Obsidian with proper formatting.
"""

import os
import shutil
from pathlib import Path
from datetime import datetime

# Configuration
DESKTOP_BASE = Path("/Users/finnlemarinel/Desktop/Strathclyde /Uni Course Raw")
OBSIDIAN_BASE = Path("/Users/finnlemarinel/Documents/UniCourse")

# Lecture mappings
CS814_LECTURES = {
    "CS814 AI for Autonomous Systems week 1.md": {
        "week": "01",
        "title": "Introduction to Python",
        "date": "2025-09-24"  # Adjust if you know actual dates
    },
    "CS814 AI for Autonomous Systems week 2.md": {
        "week": "02",
        "title": "Autonomous & Intelligent Agents",
        "date": "2025-10-01"
    },
    "CS814 AI for Autonomous Systems week 3 .md": {
        "week": "03",
        "title": "Problems and Algorithms",
        "date": "2025-10-08"
    },
    "CS814 AI for Autonomous Systems week 4 .md": {
        "week": "04",
        "title": "Problems and Search",
        "date": "2025-10-15"
    },
    "CS814 AI for Autonomous Systems week 5 (informed search) .md": {
        "week": "05",
        "title": "Informed Search",
        "date": "2025-10-22"
    }
}

CS982_LECTURES = {
    "CS989 Big Data Fundamentals lecture week 1.md": {
        "week": "01",
        "title": "Introduction to Python",
        "date": "2025-09-24"
    },
    "CS989 Big Data Fundamentals lecture week 2.md": {
        "week": "02",
        "title": "Data Handling",
        "date": "2025-10-01"
    },
    "CS989 Big Data Fundamentals lecture week 3.md": {
        "week": "03",
        "title": "Visualisation",
        "date": "2025-10-08"
    },
    "CS989 Big Data Fundamentals lecture week 4.md": {
        "week": "04",
        "title": "Supervised Learning",
        "date": "2025-10-15"
    },
    "CS989 Big Data Fundamentals lecture week 5.md": {
        "week": "05",
        "title": "Unsupervised Learning",
        "date": "2025-10-22"
    }
}

def create_frontmatter(module, week, title, date):
    """Create YAML frontmatter for lecture notes."""
    return f"""---
title: "Week {week} — {title} (Lecture Content)"
module: "{module}"
tags: [module/{module}, type/lectures, week-{week}, content]
date: {date}
lecturer: "Joseph El Gemayel, Ph.D., FHEA"
---

# {title}
*Week {week} Lecture*

"""

def process_lecture(source_path, dest_base, module, week, title, date):
    """Process a single lecture file."""
    # Read original content
    with open(source_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Create new filename
    title_slug = title.lower().replace(' & ', '-').replace(' ', '-')
    new_filename = f"lecture-w{week}-{title_slug}-content.md"
    dest_path = dest_base / new_filename

    # Create formatted content
    formatted_content = create_frontmatter(module, week, title, date) + content

    # Write to destination
    with open(dest_path, 'w', encoding='utf-8') as f:
        f.write(formatted_content)

    return new_filename

def main():
    print("🔧 Organizing Lecture Files...\n")

    # Process CS814 lectures
    print("📚 Processing CS814 Lectures:")
    cs814_source = DESKTOP_BASE / "CS814 - AI for Autonomous Systems" / "Lectures" / "Lectures md"
    cs814_dest = OBSIDIAN_BASE / "CS814 - AI for Autonomous Systems" / "lectures"

    created_files = []
    for filename, info in CS814_LECTURES.items():
        source_file = cs814_source / filename
        if source_file.exists():
            new_name = process_lecture(
                source_file,
                cs814_dest,
                "CS814",
                info["week"],
                info["title"],
                info["date"]
            )
            created_files.append(f"CS814: {new_name}")
            print(f"  ✅ Week {info['week']}: {info['title']}")
        else:
            print(f"  ⚠️  Not found: {filename}")

    print("\n📊 Processing CS982 Lectures:")
    cs982_source = DESKTOP_BASE / "CS982 - Big Data Technologies" / "Lectures" / "Lecture mds"
    cs982_dest = OBSIDIAN_BASE / "CS982 - Big Data Technologies" / "lectures"

    for filename, info in CS982_LECTURES.items():
        source_file = cs982_source / filename
        if source_file.exists():
            new_name = process_lecture(
                source_file,
                cs982_dest,
                "CS982",
                info["week"],
                info["title"],
                info["date"]
            )
            created_files.append(f"CS982: {new_name}")
            print(f"  ✅ Week {info['week']}: {info['title']}")
        else:
            print(f"  ⚠️  Not found: {filename}")

    print("\n" + "="*60)
    print("📊 SUMMARY")
    print("="*60)
    print(f"\n✅ Created {len(created_files)} lecture content files in Obsidian:\n")
    for file in created_files:
        print(f"  - {file}")

    print("\n💡 These files are now AI-readable and searchable in Obsidian!")
    print("💡 Original PDFs remain on Desktop as backup.")
    print("\n✅ Organization complete!")

if __name__ == "__main__":
    main()
