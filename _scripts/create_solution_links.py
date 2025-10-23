#!/usr/bin/env python3
"""
Create link-notes for CS982 lab solution notebooks.
"""

import os
from pathlib import Path
from urllib.parse import quote

# Configuration
DESKTOP_BASE = Path("/Users/finnlemarinel/Desktop/Strathclyde /Uni Course Raw")
OBSIDIAN_BASE = Path("/Users/finnlemarinel/Documents/UniCourse")

# Solution notebook info
SOLUTIONS = {
    "Lab 1 - Solutions (1).ipynb": {
        "week": "01",
        "title": "Lab 1 Solutions",
        "topics": ["Python basics", "NumPy fundamentals", "Basic data structures"],
        "dataset": "None (Python exercises)"
    },
    "Lab 2 - Solutions (1).ipynb": {
        "week": "02",
        "title": "Lab 2 Solutions",
        "topics": ["Pandas DataFrame operations", "Handling missing data", "Data manipulation and filtering"],
        "dataset": "pokemon_alopez247.csv"
    },
    "Lab 3 - Solutions.ipynb": {
        "week": "03",
        "title": "Lab 3 Solutions",
        "topics": ["Data visualization with matplotlib/seaborn", "Bar charts, histograms, scatter plots", "Boxplots and violin plots"],
        "dataset": "pokemon_alopez247.csv"
    },
    "Lab 4 - Solutions.ipynb": {
        "week": "04",
        "title": "Lab 4 Solutions",
        "topics": ["Supervised learning algorithms", "Linear regression", "Model evaluation"],
        "dataset": "Life Satisfaction GDP Dataset.csv"
    }
}

def create_solution_link_note(file_path, week, title, topics, dataset):
    """Create a link-note for a solution notebook."""
    # Generate file URL
    file_url = "file://" + quote(str(file_path.absolute()))

    # Create topics list
    topics_md = "\n".join([f"- {topic}" for topic in topics])

    content = f"""---
title: "{title}"
module: "CS982"
tags: [module/CS982, type/labs, solutions, week-{week}]
date: 2025-10-23
---

# {title} (Official Solution)

**Solution notebook**: [{file_path.name}]({file_url})

📂 Location: `{file_path.absolute()}`

---

## Topics Covered
{topics_md}

## Dataset Used
{dataset}

---

## My Notes
*Add your observations about the solution approach here*

-

## Questions
*Note any questions or differences from your implementation*

-

## Related
- [[lab-w{week}-exploring-data-content]] - Lab instructions
"""

    return content

def main():
    print("🔗 Creating Solution Link-Notes...\n")

    solutions_source = DESKTOP_BASE / "CS982 - Big Data Technologies" / "Labs" / "Lab Pdfs" / "Lab Solutions"
    obsidian_dest = OBSIDIAN_BASE / "CS982 - Big Data Technologies" / "labs"

    created_files = []

    for filename, info in SOLUTIONS.items():
        source_file = solutions_source / filename

        if source_file.exists():
            # Create link-note filename
            link_note_name = f"lab-w{info['week']}-solutions.md"
            dest_path = obsidian_dest / link_note_name

            # Generate content
            content = create_solution_link_note(
                source_file,
                info["week"],
                info["title"],
                info["topics"],
                info["dataset"]
            )

            # Write file
            with open(dest_path, 'w', encoding='utf-8') as f:
                f.write(content)

            created_files.append(link_note_name)
            print(f"  ✅ Week {info['week']}: {info['title']}")
        else:
            print(f"  ⚠️  Not found: {filename}")

    print("\n" + "="*60)
    print("📊 SUMMARY")
    print("="*60)
    print(f"\n✅ Created {len(created_files)} solution link-notes in Obsidian:\n")
    for file in created_files:
        print(f"  - {file}")

    print("\n💡 Solution notebooks remain on Desktop (runnable with data files)")
    print("💡 Link-notes provide quick access and note-taking space")
    print("\n✅ Link creation complete!")

if __name__ == "__main__":
    main()
