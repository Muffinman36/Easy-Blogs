#!/usr/bin/env python3
"""Manage the article ideas store (placeholder database)."""

import json
import os
import sys

STORE_PATH = os.path.join(os.path.dirname(__file__), "article_ideas.json")
STATUS_NOT_DONE = "Not done"
STATUS_DONE = "Done"


def _load():
    if not os.path.exists(STORE_PATH):
        return []
    with open(STORE_PATH, "r") as f:
        return json.load(f)


def _save(ideas):
    with open(STORE_PATH, "w") as f:
        json.dump(ideas, f, indent=2)


def cmd_list(incomplete_only=False):
    ideas = _load()
    if incomplete_only:
        ideas = [i for i in ideas if i.get("status") == STATUS_NOT_DONE]
    for i, idea in enumerate(ideas, 1):
        status = idea.get("status", STATUS_NOT_DONE)
        content = idea.get("content", "")
        print(f"{i}. {idea['title']} [{status}]")
        if content:
            print(f"   {content}")
    return 0


def cmd_next():
    ideas = _load()
    for idea in ideas:
        if idea.get("status") == STATUS_NOT_DONE:
            print(json.dumps(idea))
            return 0
    return 1  # No incomplete ideas


def cmd_add():
    try:
        new_ideas = json.load(sys.stdin)
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON on stdin: {e}", file=sys.stderr)
        return 1
    if not isinstance(new_ideas, list):
        print("Error: Expected a JSON array", file=sys.stderr)
        return 1
    ideas = _load()
    for item in new_ideas:
        idea = {
            "title": item.get("title", ""),
            "content": item.get("content", ""),
            "status": STATUS_NOT_DONE,
        }
        ideas.append(idea)
    _save(ideas)
    print(f"Added {len(new_ideas)} idea(s).")
    return 0


def cmd_done(title):
    if not title:
        print("Error: Title required", file=sys.stderr)
        return 1
    ideas = _load()
    found = False
    for idea in ideas:
        if idea.get("title") == title:
            idea["status"] = STATUS_DONE
            found = True
            break
    if not found:
        print(f"Error: No idea with title '{title}' found", file=sys.stderr)
        return 1
    _save(ideas)
    print(f"Marked '{title}' as Done.")
    return 0


def main():
    if len(sys.argv) < 2:
        print("Usage: manage_ideas.py <list|next|add|done> [options]", file=sys.stderr)
        return 1
    subcommand = sys.argv[1].lower()
    if subcommand == "list":
        incomplete_only = "--incomplete" in sys.argv
        return cmd_list(incomplete_only=incomplete_only)
    if subcommand == "next":
        return cmd_next()
    if subcommand == "add":
        return cmd_add()
    if subcommand == "done":
        # Title can be passed as remaining args (in case it has spaces)
        title = " ".join(sys.argv[2:]).strip()
        if title.startswith('"') and title.endswith('"'):
            title = title[1:-1]
        return cmd_done(title)
    print(f"Unknown subcommand: {subcommand}", file=sys.stderr)
    return 1


if __name__ == "__main__":
    sys.exit(main())
