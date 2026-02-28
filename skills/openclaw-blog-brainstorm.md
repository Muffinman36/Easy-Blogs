---
name: openclaw-blog-brainstorm
description: "Brainstorm article ideas for the openclaw blog. Use this skill when the user asks to brainstorm blog ideas, generate a content calendar, come up with article topics, or create a list of blog post ideas. The skill runs a collaborative brainstorming session and saves ideas to a shared queue that the blog publisher uses."
---

# OpenClaw Blog Brainstorm

This skill runs a brainstorming session with the user to generate more than 10 article ideas. The ideas are saved to a shared idea store (a table in the backend) that the blog publisher skill uses when publishing articles.

---

## Step 1: Start the Brainstorming Session

Begin by asking about the user's audience, themes, or constraints. For example:

> "Let's brainstorm some blog ideas. Who's your target audience, and are there any themes or topics you'd like to focus on?"

Adapt based on the user's response.

---

## Step 2: Generate More Than 10 Ideas

Work iteratively with the user until you have **more than 10** article ideas. Suggest ideas, refine them together, and encourage the user to add their own. Each idea should have:

- **title**: A clear headline or topic (required)
- **content**: A brief one-line description or outline (optional, can be empty)

---

## Step 3: Format Ideas as JSON

Once you have more than 10 ideas, format them as a JSON array:

```json
[
  {"title": "<idea 1 title>", "content": "<brief description>", "status": "Not done"},
  {"title": "<idea 2 title>", "content": "<brief description>", "status": "Not done"}
]
```

Include the `status` field as `"Not done"` for each idea. The `content` field can be an empty string if no description was captured.

---

## Step 4: Write Ideas to the Store

From the directory that contains `manage_ideas.py`, run:

```bash
python manage_ideas.py add << 'JSONEOF'
<paste the exact JSON array from Step 3 here>
JSONEOF
```

This appends the ideas to `article_ideas.json` (the shared idea store).

---

## Step 5: Confirm to the User

Tell the user how many ideas were added and that they can now use the blog publisher skill to publish articles from the queue, one at a time.
