# Conversation to Obsidian

A Codex skill for distilling a meaningful conversation into a concise, searchable Markdown note and saving it safely in an Obsidian vault.

## Install

Copy or symlink this directory into your Codex skills directory, then restart Codex if it is already running.

```bash
cp -R summarize-to-obsidian ~/.codex/skills/
```

## Use

Ask Codex to save, archive, capture, or summarize a conversation to Obsidian. The skill first identifies the conversation's primary focus, then uses that focus to determine the note title, retained information, folder, and summary. It saves notes in `/Users/junjett/Downloads/learning/obsidian`, uses a normalized `time - topic - agent` filename, records the exact agent and model, and writes with the included collision-safe script.

The script requires an existing vault directory and will not overwrite an existing note. It creates a numbered sibling when the requested filename already exists.

```bash
python3 scripts/save_obsidian_note.py \
  --vault "/Users/junjett/Downloads/learning/obsidian" \
  --filename "2026-08-14 1530 - topic - Codex.md" \
  --source "/absolute/path/to/draft.md" \
  --folder "Inbox/Conversations"
```

## License

MIT
