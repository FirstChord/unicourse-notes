#!/usr/bin/env python3
"""
Create link-notes for external course materials.
Scans external docs and creates Markdown link-notes in the Obsidian vault.
"""

import os
import re
from pathlib import Path

# Configuration
EXTERNAL_DOCS = Path("/Users/finnlemarinel/Desktop/Strathclyde /Uni Course Raw")
OB_VAULT = Path("/Users/finnlemarinel/Documents/UniCourse")

# Module mapping - now using consistent naming
MODULE_MAP = {
    "CS814 - AI for Autonomous Systems": "CS814",
    "CS982 - Big Data Technologies": "CS982",
    "CS801 - Quantitative Methods for AI": "CS801",
    "CS978 - Legal, Ethical and Professional Issues": "CS978"
}

MODULE_NAMES = {
    "CS814": "CS814 - AI for Autonomous Systems",
    "CS982": "CS982 - Big Data Technologies",
    "CS801": "CS801 - Quantitative Methods for AI",
    "CS978": "CS978 - Legal, Ethical and Professional Issues"
}

def sanitize_filename(text):
    """Convert text to kebab-case filename."""
    # Remove special chars, convert to lowercase
    text = re.sub(r'[^\w\s-]', '', text.lower())
    # Replace spaces with hyphens
    text = re.sub(r'[-\s]+', '-', text)
    return text.strip('-')

def extract_week_number(filename):
    """Extract week number from filename."""
    patterns = [
        r'[Ww]eek\s*(\d+)',
        r'[Ww]k\s*(\d+)',
        r'[Ww](\d+)',
        r'[Ll]ab\s*(\d+)',
        r'[Ll]ecture\s*(\d+)'
    ]

    for pattern in patterns:
        match = re.search(pattern, filename)
        if match:
            return int(match.group(1))
    return None

def create_link_note(file_path, module_code, note_type):
    """Create a link-note for an external file."""
    filename = file_path.name
    week_num = extract_week_number(filename)

    # Generate title
    title_parts = []
    if week_num:
        title_parts.append(f"Week {week_num:02d}")

    # Extract topic from filename
    topic = re.sub(r'[Ll]ab\s*\d+', '', filename)
    topic = re.sub(r'[Ll]ecture\s*\d+', '', topic)
    topic = re.sub(r'[Ww]eek\s*\d+', '', topic)
    topic = re.sub(r'\.(pdf|ppt|pptx|doc|docx)$', '', topic, flags=re.IGNORECASE)
    topic = re.sub(r'[-_\s]+', ' ', topic).strip()

    if topic and topic not in ['', 'slides', 'notes']:
        title_parts.append(topic)
    else:
        title_parts.append(note_type.capitalize())

    title = " — ".join(title_parts) if title_parts else filename

    # Generate filename
    filename_parts = [note_type]
    if week_num:
        filename_parts.append(f"w{week_num:02d}")
    if topic and topic not in ['', 'slides', 'notes']:
        filename_parts.append(sanitize_filename(topic))

    note_filename = "-".join(filename_parts) + ".md"

    # Determine target folder
    module_folder = OB_VAULT / MODULE_NAMES[module_code]
    if 'lab' in note_type.lower():
        target_folder = module_folder / "labs"
    elif 'reading' in note_type.lower():
        # For reading materials, put in the appropriate week folder
        if week_num:
            target_folder = module_folder / "reading" / f"week-{week_num:02d}"
        else:
            target_folder = module_folder / "reading"
    else:
        target_folder = module_folder / "lectures"

    target_path = target_folder / note_filename

    # Check if already exists - overwrite to update paths
    if target_path.exists():
        # Read existing file to check if it needs updating
        existing_content = target_path.read_text()
        # Check if path matches current external docs location
        if "Desktop/Strathclyde /Uni Course Raw/CS" in existing_content:
            return None, "skipped"  # Already up to date
        # Otherwise, regenerate with new path

    # Create note content with proper file URL
    from urllib.parse import quote
    file_url = "file://" + quote(str(file_path.absolute()))

    neighbors = '["CS814","CS982","CS801","CS978"]'
    content = f"""---
title: "{title}"
module: "{module_code}"
tags: [module/{module_code}, type/{note_type}s]
neighbors: {neighbors}
---

# {title} (Link Note)

**External file**: [{file_path.name}]({file_url})

📂 Location: `{file_path.absolute()}`

## My Notes
-

## Related
-
"""

    # Write file
    target_path.write_text(content)
    return note_filename, "created"

def scan_and_create_links():
    """Scan external docs and create link-notes."""
    stats = {
        "created": 0,
        "skipped": 0,
        "total_files": 0
    }

    module_stats = {code: {"created": 0, "skipped": 0} for code in MODULE_NAMES.keys()}

    # Scan each module folder
    for module_folder in EXTERNAL_DOCS.iterdir():
        if not module_folder.is_dir():
            continue

        module_name = module_folder.name
        module_code = MODULE_MAP.get(module_name)

        if not module_code:
            print(f"⚠️  Unknown module: {module_name}")
            continue

        print(f"\n📁 Scanning {module_name} ({module_code})...")

        # Look for Lectures, Labs, Notes, and Reading folders
        for subfolder in ["Lectures", "lectures", "Labs", "labs", "Notes", "notes", "Reading", "reading"]:
            subfolder_path = module_folder / subfolder
            if not subfolder_path.exists():
                continue

            # Determine note type
            if "lecture" in subfolder.lower():
                note_type = "lecture"
            elif "lab" in subfolder.lower():
                note_type = "lab"
            elif "reading" in subfolder.lower():
                note_type = "reading"
            else:
                note_type = "lecture"  # Default for notes

            # Find all PDF/PPT files (including in Week subfolders for Reading)
            for ext in ['*.pdf', '*.ppt', '*.pptx', '*.doc', '*.docx']:
                for file_path in subfolder_path.rglob(ext):
                    stats["total_files"] += 1
                    note_name, status = create_link_note(file_path, module_code, note_type)

                    if status == "created":
                        stats["created"] += 1
                        module_stats[module_code]["created"] += 1
                        print(f"  ✅ Created: {note_name}")
                    elif status == "skipped":
                        stats["skipped"] += 1
                        module_stats[module_code]["skipped"] += 1

    return stats, module_stats

if __name__ == "__main__":
    print("🔍 Scanning external course materials...")
    print(f"📂 External docs: {EXTERNAL_DOCS}")
    print(f"📓 Vault: {OB_VAULT}")

    stats, module_stats = scan_and_create_links()

    print("\n" + "="*60)
    print("📊 LINK-NOTES CREATION REPORT")
    print("="*60)
    print(f"\nTotal files scanned: {stats['total_files']}")
    print(f"Link-notes created: {stats['created']}")
    print(f"Already existed (skipped): {stats['skipped']}")

    print("\n📈 By Module:")
    for code in sorted(MODULE_NAMES.keys()):
        created = module_stats[code]["created"]
        skipped = module_stats[code]["skipped"]
        total = created + skipped
        if total > 0:
            print(f"  {code}: {created} created, {skipped} skipped ({total} total)")

    print("\n✅ Link-notes creation complete!")
