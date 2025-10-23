#!/bin/bash
#
# add_summary.sh - Create a new summary note from template
#
# Usage: add_summary.sh <MODULE> "<TOPIC>" <WEEK>
# Example: add_summary.sh CS814 "Bayes Theorem" w03
#

set -e

VAULT_DIR="$HOME/Documents/UniCourse"
TEMPLATE="$VAULT_DIR/_templates/summary-template.md"

# Check arguments
if [ "$#" -ne 3 ]; then
    echo "Usage: $0 <MODULE> \"<TOPIC>\" <WEEK>"
    echo ""
    echo "Examples:"
    echo "  $0 CS814 \"Bayes Theorem\" w03"
    echo "  $0 CS982 \"MapReduce\" w02"
    echo ""
    echo "Available modules: CS814, CS982, CS801, CS978"
    exit 1
fi

MODULE="$1"
TOPIC="$2"
WEEK="$3"

# Validate module
case "$MODULE" in
    CS814) MODULE_DIR="$VAULT_DIR/CS814 - AI for Autonomous Systems" ;;
    CS982) MODULE_DIR="$VAULT_DIR/CS982 - Big Data Technologies" ;;
    CS801) MODULE_DIR="$VAULT_DIR/CS801 - Quantitative Methods for AI" ;;
    CS978) MODULE_DIR="$VAULT_DIR/CS978 - Legal, Ethical and Professional Issues" ;;
    *)
        echo "❌ Error: Invalid module '$MODULE'"
        echo "   Valid modules: CS814, CS982, CS801, CS978"
        exit 1
        ;;
esac

# Normalize week number (add 'w' prefix if missing)
if [[ ! "$WEEK" =~ ^w ]]; then
    WEEK="w$WEEK"
fi

# Convert topic to kebab-case
TOPIC_KEBAB=$(echo "$TOPIC" | tr '[:upper:]' '[:lower:]' | sed 's/[^a-z0-9]/-/g' | sed 's/--*/-/g' | sed 's/^-//' | sed 's/-$//')

# Generate filename
FILENAME="summary-${WEEK}-${TOPIC_KEBAB}.md"
TARGET_PATH="$MODULE_DIR/summaries/$FILENAME"

# Check if file already exists
if [ -f "$TARGET_PATH" ]; then
    echo "⚠️  File already exists: $FILENAME"
    echo "📂 Location: $TARGET_PATH"
    read -p "Open it anyway? (y/n) " -n 1 -r
    echo
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        open "$TARGET_PATH"
    fi
    exit 0
fi

# Copy template
cp "$TEMPLATE" "$TARGET_PATH"

# Replace placeholders
sed -i '' "s/<Replace Me>/$TOPIC/" "$TARGET_PATH"
sed -i '' "s/CS###/$MODULE/g" "$TARGET_PATH"
sed -i '' "s/# Topic/# $TOPIC/" "$TARGET_PATH"

echo "✅ Created summary note: $FILENAME"
echo "📂 Location: $TARGET_PATH"
echo ""

# Open in default editor (optional)
read -p "Open in default editor? (y/n) " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]; then
    open "$TARGET_PATH"
fi
