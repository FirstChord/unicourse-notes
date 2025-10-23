#!/usr/bin/env python3
"""
Organize CS982 assignment materials from Desktop to Obsidian.
"""

import os
from pathlib import Path
from urllib.parse import quote

# Configuration
DESKTOP_BASE = Path("/Users/finnlemarinel/Desktop/Strathclyde /Uni Course Raw")
OBSIDIAN_BASE = Path("/Users/finnlemarinel/Documents/UniCourse")

# Assignment instruction .md files (Tier 1 - Full Content)
ASSIGNMENT_MDS = {
    "CS989_ Big Data Fundamentals Group Assignment.md": {
        "title": "Assignment Brief",
        "type": "brief"
    },
    "CS989_ Big Data Fundamentals Group Assignment_ FAQ's.md": {
        "title": "Assignment FAQs",
        "type": "faq"
    },
    "CS989_ Big Data Fundamentals Assignment Marking Scheme.md": {
        "title": "Marking Scheme",
        "type": "marking"
    },
    "CS989_ Big Data Fundamentals Group Assignment_ Report and Layout.md": {
        "title": "Report Guidelines",
        "type": "guidelines"
    }
}

# Sample submissions (Tier 2 - Link Notes)
SAMPLE_SUBMISSIONS = {
    "Sample Assignment 1 - Graded as Distinction.pdf": {
        "title": "Sample 1 (Distinction)",
        "grade": "Distinction"
    },
    "Sample Assignment 2 - Graded as Merit.pdf": {
        "title": "Sample 2 (Merit)",
        "grade": "Merit"
    },
    "Sample Assignment 3 - Graded as Pass.pdf": {
        "title": "Sample 3 (Pass)",
        "grade": "Pass"
    }
}

def create_assignment_frontmatter(title, doc_type):
    """Create YAML frontmatter for assignment documents."""
    return f"""---
title: "{title}"
module: "CS982"
tags: [module/CS982, type/assignments, assignment-{doc_type}]
date: 2025-10-23
deadline: 2025-11-03 18:00
---

# {title}

"""

def process_assignment_md(source_path, dest_base, title, doc_type):
    """Process an assignment .md file."""
    # Read original content
    with open(source_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Create new filename
    filename_slug = doc_type
    new_filename = f"assignment-{filename_slug}.md"
    dest_path = dest_base / new_filename

    # Create formatted content
    formatted_content = create_assignment_frontmatter(title, doc_type) + content

    # Write to destination
    with open(dest_path, 'w', encoding='utf-8') as f:
        f.write(formatted_content)

    return new_filename

def create_sample_link_note(file_path, title, grade):
    """Create a link-note for a sample submission."""
    # Generate file URL
    file_url = "file://" + quote(str(file_path.absolute()))

    content = f"""---
title: "{title}"
module: "CS982"
tags: [module/CS982, type/assignments, sample-submission, grade-{grade.lower()}]
date: 2025-10-23
---

# {title}

**Grade Achieved:** {grade}

**Sample submission**: [{file_path.name}]({file_url})

📂 Location: `{file_path.absolute()}`

---

## Why This Grade?

**Key Strengths** (from marking scheme):
-

**What Could Be Improved:**
-

---

## My Analysis Notes

**What I can learn from this:**
-

**Techniques to adopt:**
-

**Mistakes to avoid:**
-

---

## Related

- [[assignment-brief]] - Assignment requirements
- [[assignment-marking]] - Marking scheme
- [[assignment-guidelines]] - Report formatting

---

**Use this:** Study this sample while working on your own assignment to understand what's expected at each grade level.
"""

    return content

def main():
    print("🔧 Organizing CS982 Assignment Materials...\n")

    cs982_source_mds = DESKTOP_BASE / "CS982 - Big Data Technologies" / "Assignments" / "Assignment mds"
    cs982_source_samples = DESKTOP_BASE / "CS982 - Big Data Technologies" / "Assignments" / "Sample Submissions - Part I-20251023"
    cs982_dest = OBSIDIAN_BASE / "CS982 - Big Data Technologies" / "assignments"

    created_files = []

    # Process assignment .md files (Tier 1)
    print("📄 Processing Assignment Documents:")
    for filename, info in ASSIGNMENT_MDS.items():
        source_file = cs982_source_mds / filename
        if source_file.exists():
            new_name = process_assignment_md(
                source_file,
                cs982_dest,
                info["title"],
                info["type"]
            )
            created_files.append(f"  ✅ {new_name} ({info['title']})")
            print(f"  ✅ {info['title']}")
        else:
            print(f"  ⚠️  Not found: {filename}")

    # Create link-notes for sample submissions (Tier 2)
    print("\n🔗 Creating Link-Notes for Sample Submissions:")
    for filename, info in SAMPLE_SUBMISSIONS.items():
        source_file = cs982_source_samples / filename

        if source_file.exists():
            # Create link-note filename
            grade_slug = info["grade"].lower()
            link_note_name = f"assignment-sample-{grade_slug}.md"
            dest_path = cs982_dest / link_note_name

            # Generate content
            content = create_sample_link_note(
                source_file,
                info["title"],
                info["grade"]
            )

            # Write file
            with open(dest_path, 'w', encoding='utf-8') as f:
                f.write(content)

            created_files.append(f"  ✅ {link_note_name} ({info['grade']})")
            print(f"  ✅ {info['title']}")
        else:
            print(f"  ⚠️  Not found: {filename}")

    print("\n" + "="*60)
    print("📊 SUMMARY")
    print("="*60)
    print(f"\n✅ Created {len(created_files)} files in Obsidian assignments folder:\n")
    for file in created_files:
        print(file)

    print("\n📋 Assignment Structure:")
    print("  📄 Tier 1 (Full Content):")
    print("    - assignment-brief.md")
    print("    - assignment-faq.md")
    print("    - assignment-marking.md")
    print("    - assignment-guidelines.md")
    print("\n  🔗 Tier 2 (Link-Notes to Samples):")
    print("    - assignment-sample-distinction.md")
    print("    - assignment-sample-merit.md")
    print("    - assignment-sample-pass.md")

    print("\n💡 All assignment materials now accessible in Obsidian!")
    print("💡 Original PDFs remain on Desktop.")
    print("💡 Use sample submissions to understand grade expectations.")
    print("\n🎯 Deadline: 18:00, Monday November 3rd, 2025")
    print("\n✅ Organization complete!")

if __name__ == "__main__":
    main()
