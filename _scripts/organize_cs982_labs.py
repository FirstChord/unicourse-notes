#!/usr/bin/env python3
"""
Organize CS982 lab .md files from Desktop to Obsidian with proper formatting.
"""

import os
from pathlib import Path

# Configuration
DESKTOP_BASE = Path("/Users/finnlemarinel/Desktop/Strathclyde /Uni Course Raw")
OBSIDIAN_BASE = Path("/Users/finnlemarinel/Documents/UniCourse")

# Lab mappings
CS982_LABS = {
    "CS989_ Big Data Fundamentals Lab (week 1).md": {
        "week": "01",
        "title": "Python Intro",
        "date": "2025-09-24"
    },
    "CS989_ Big Data Fundamentals Lab (week 2).md": {
        "week": "02",
        "title": "Exploring Data",
        "date": "2025-10-01"
    },
    "CS989_ Big Data Fundamentals Lab (week 3).md": {
        "week": "03",
        "title": "Visualization",
        "date": "2025-10-08"
    },
    "CS989_ Big Data Fundamentals Lab (week 4).md": {
        "week": "04",
        "title": "Supervised Learning",
        "date": "2025-10-15"
    },
    "CS989_ Big Data Fundamentals Lab (week 5).md": {
        "week": "05",
        "title": "Unsupervised Learning",
        "date": "2025-10-22"
    }
}

def create_frontmatter(module, week, title, date):
    """Create YAML frontmatter for lab content."""
    return f"""---
title: "Week {week} — {title} (Lab Content)"
module: "{module}"
tags: [module/{module}, type/labs, week-{week}, content]
date: {date}
---

# {title}
*Week {week} Lab*

"""

def process_lab(source_path, dest_base, module, week, title, date):
    """Process a single lab file."""
    # Read original content
    with open(source_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Create new filename
    title_slug = title.lower().replace(' ', '-')
    new_filename = f"lab-w{week}-{title_slug}-content.md"
    dest_path = dest_base / new_filename

    # Create formatted content
    formatted_content = create_frontmatter(module, week, title, date) + content

    # Write to destination
    with open(dest_path, 'w', encoding='utf-8') as f:
        f.write(formatted_content)

    return new_filename

def main():
    print("🔧 Organizing CS982 Lab Files...\n")

    # Process CS982 labs
    print("📚 Processing CS982 Labs:")
    cs982_source = DESKTOP_BASE / "CS982 - Big Data Technologies" / "Labs" / "Lab Pdfs" / "Lab mds"
    cs982_dest = OBSIDIAN_BASE / "CS982 - Big Data Technologies" / "labs"

    created_files = []
    for filename, info in CS982_LABS.items():
        source_file = cs982_source / filename
        if source_file.exists():
            new_name = process_lab(
                source_file,
                cs982_dest,
                "CS982",
                info["week"],
                info["title"],
                info["date"]
            )
            created_files.append(new_name)
            print(f"  ✅ Week {info['week']}: {info['title']}")
        else:
            print(f"  ⚠️  Not found: {filename}")

    print("\n" + "="*60)
    print("📊 SUMMARY")
    print("="*60)
    print(f"\n✅ Created {len(created_files)} lab content files in Obsidian:\n")
    for file in created_files:
        print(f"  - {file}")

    print("\n💡 These files are now AI-readable and searchable in Obsidian!")
    print("💡 Original files remain on Desktop as backup.")
    print("\n✅ Organization complete!")

if __name__ == "__main__":
    main()
