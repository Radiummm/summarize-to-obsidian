# Conversation to Obsidian

A Codex skill for distilling a meaningful conversation into a concise, searchable Markdown note and saving it safely in an Obsidian vault.

## Install

Copy or symlink this directory into your Codex skills directory, then restart Codex if it is already running.

```bash
cp -R summarize-to-obsidian ~/.codex/skills/
```

## Use

Ask Codex to save, archive, capture, or summarize a conversation to Obsidian. The skill will identify the durable information, automatically classify the note into the most relevant existing vault folder, use a normalized `time - topic - agent` filename, record the exact agent and model in the note, and save it using the included collision-safe script.

The script requires an existing vault directory and will not overwrite an existing note. It creates a numbered sibling when the requested filename already exists.

```bash
python3 scripts/save_obsidian_note.py \
  --vault "/absolute/path/to/vault" \
  --filename "2026-08-14 1530 - topic - Codex.md" \
  --source "/absolute/path/to/draft.md" \
  --folder "Inbox/Conversations"
```

## License

MIT
