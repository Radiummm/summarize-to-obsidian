---
name: summarize-to-obsidian
description: Distill meaningful conversations into high-signal Obsidian Markdown notes and save them in the user's vault. Use when the user asks to summarize, archive, capture, record, or save a conversation/chat/discussion to Obsidian, especially when important decisions, research, plans, insights, requirements, or follow-up actions should be retained while irrelevant chatter is omitted or compressed.
---

# Conversation to Obsidian

Turn a conversation into a durable note that preserves what will matter later. Write for the user's future self, not as a chronological transcript.

## Workflow

1. Read the whole in-scope conversation and identify its main topic or topics.
2. Classify content before drafting:
   - **Retain in detail:** conclusions, decisions and rationale, user preferences, requirements, constraints, factual findings, technical designs, examples that establish an idea, unresolved questions, risks, and concrete next actions.
   - **Compress:** background context, alternatives rejected with a short reason, routine progress, and supporting examples that add little new information.
   - **Omit:** greetings, acknowledgements, duplicate statements, abandoned tangents, generic filler, and material unrelated to the note's topic.
3. If the conversation has no durable value, say so succinctly and do not create a note unless the user explicitly wants even low-value chats archived.
4. Write a self-contained Markdown note in the user's language. Do not claim facts that were not established in the conversation.
5. If the conversation is executing a task, record the current state rather than only the final goal: completed work, work in progress, planned work, blockers or failures, important files or commands changed, and the next concrete step. Mark the state as of the end of the conversation.
6. Resolve the Obsidian vault and destination folder. Use a path the user supplied or previously confirmed. If none is known, inspect likely local vault locations only when appropriate; otherwise ask for the vault path before writing.
7. Save the note with `scripts/save_obsidian_note.py`. Report the created file path and a concise summary of what was captured.

## Note Quality

- Give the note a specific, searchable H1 rather than a generic title such as "Conversation summary".
- Start with `## 摘要` (or the equivalent in the note language) containing 2-6 sentences that state the result and stakes.
- Use informative sections only when they have content. Typical sections are `## 核心结论`, `## 关键讨论`, `## 决策与理由`, `## 实施要点`, `## 待办`, `## 未决问题`, and `## 参考`.
- Preserve exact dates, numbers, names, commands, code identifiers, paths, and links when they affect later work.
- Separate confirmed conclusions from proposals, assumptions, and open questions.
- For an active task, include a `## 当前进度` section with status, completed items, in-progress items, blockers, and next steps. Include only categories that have meaningful content.
- Prefer concise prose plus bullets. Include enough rationale that a future reader can understand why a decision was made.
- Use `- [ ]` only for genuinely actionable, unfinished items. Do not manufacture tasks.
- Add `## 对话元数据` only when useful, with the conversation date and a short scope statement. Do not add metadata merely to fill space.

## Suggested Note Shape

```markdown
# Specific topic title

## 摘要

## 核心结论

## 当前进度
- 状态：进行中 / 已完成 / 已阻塞
- 已完成：
- 进行中：
- 阻塞点：
- 下一步：

## 决策与理由

## 实施要点

## 待办
- [ ] Owner: action

## 未决问题

## 对话元数据
- 日期：YYYY-MM-DD
- 范围：What this note covers
```

Adapt this shape. Remove empty sections and add domain-specific ones such as `研究洞见`, `技术方案`, or `写作素材` when they improve retrieval.

## File Naming and Safety

- Use a concise, descriptive filename: `YYYY-MM-DD - topic.md` unless the vault follows another convention.
- Save below the confirmed vault root; default to the root only when no folder convention is known.
- Never overwrite an existing note without explicit permission. The save script creates a numbered sibling when the intended filename already exists.
- Do not modify existing vault indexes, daily notes, templates, or unrelated notes unless requested.

## Save Command

Draft the complete note into a temporary Markdown file, then save it:

```bash
python3 /path/to/summarize-to-obsidian/scripts/save_obsidian_note.py \
  --vault "/absolute/path/to/vault" \
  --filename "YYYY-MM-DD - topic.md" \
  --source "/absolute/path/to/draft.md"
```

Use `--folder "Inbox/Conversations"` when the user has a preferred subfolder. The command prints the final absolute path.
