---
name: openclaw-blog-publisher
description: "Write and publish a new blog article to the openclaw website from the idea queue. Use this skill whenever a user asks to write, create, generate, or post a blog article or blog post. The skill pulls the next idea from the queue, writes an SEO-optimized article, and posts it via API. If the queue is empty, it prompts the user to run the brainstorm skill first. Trigger this skill for any request involving blog creation, content writing for the site, or publishing a new post."
---

# OpenClaw Blog Publisher

This skill publishes articles from the idea queue: it picks the next incomplete idea, writes an SEO-optimized article, posts it via API, and marks the idea done. If the queue is empty, it prompts the user to run the brainstorm skill.

Scripts such as `manage_ideas.py` and `post_blog.py` live in the parent of this skill folder. Use the directory that contains them (one level up from `{baseDir}`) when running commands below.

---

## Step 0: Check the Idea Queue

From the directory that contains `manage_ideas.py` (parent of `{baseDir}`), run:

```bash
python manage_ideas.py next
```

- **If the command fails or returns nothing** (exit code 1): There are no incomplete ideas. Tell the user the queue is empty and suggest running the brainstorm skill first, e.g. "There are no ideas in the queue. Would you like to have a brainstorming session to generate some article ideas?"
- **If it outputs JSON**: Use the `title` (and optionally `content`) of that idea as the topic for the article. Continue to Step 1.

---

## Step 1: Confirm the Topic

The topic comes from the idea returned in Step 0. Confirm with a brief message such as:

> "Got it — I'll write a blog post about [topic from the idea]. Writing it now..."

---

## Step 2: Write the Article

Write the blog article with the following requirements:

- **Length**: 200–300 words
- **Title**: Attention-grabbing, clear, and keyword-rich. Use formats like questions, "how to", lists, or compelling statements.
- **SEO**: Naturally weave in 3–5 relevant keywords throughout the article. Choose keywords based on what a person would search for to find content on this topic. Do not keyword-stuff — keywords should read naturally.
- **Structure**: Short paragraphs (2–4 sentences each). Use a brief intro that hooks the reader, a body that delivers value, and a closing sentence or call-to-action. Use "/n" for new lines.
- **Tone**: Clear, engaging, and accessible. Avoid jargon unless the topic demands it.

---

## Step 3: Format as JSON

Once the article is written, format it as the following JSON structure:

```json
{
  "blog_title": "<The article title>",
  "blog_content": "<The full article body as plain text>",
  "slug": "<url-friendly version of the title>"
}
```

- `blog_title`: The article title only (no markdown, no quotes)
- `blog_content`: The article body only — do not include the title again inside the content. Plain text; no markdown formatting.
- `slug`: A URL-friendly version of the title. Rules: lowercase only, spaces replaced with hyphens, remove all special characters and punctuation, no leading or trailing hyphens. Example: "10 Simple Ways to Travel More Sustainably in 2025" → `10-simple-ways-to-travel-more-sustainably-in-2025`

---

## Step 4: Post to the API Using `post_blog.py`

Send the JSON from Step 3 directly to the API by piping it into `post_blog.py`. From the directory that contains `post_blog.py` (parent of `{baseDir}`), run:

```bash
python post_blog.py << 'JSONEOF'
<paste the exact JSON from Step 3 here>
JSONEOF
```

The script reads JSON from stdin, posts it to the blog API endpoint (configured inside `post_blog.py`), and prints success or error messages.

**Step 5: Confirm to the user.** After the script runs, relay the outcome in natural language: confirm success (e.g. "✅ Your blog post '[title]' has been published successfully.") or share any error details and ask how they would like to proceed.

**Step 6: Mark the idea done.** If the publish succeeded, run:

```bash
python manage_ideas.py done "<exact title from the idea in Step 0>"
```

This ensures the idea will not be picked again. Use the exact title returned by `manage_ideas.py next`.

---

## Example Output (before posting)

**Topic**: sustainable travel tips

```json
{
  "blog_title": "10 Simple Ways to Travel More Sustainably in 2025",
  "slug": "10-simple-ways-to-travel-more-sustainably-in-2025",
  "blog_content": "Sustainable travel is no longer a niche concept — it's becoming a necessity. As more people explore the world, the environmental impact of tourism is growing. The good news? Small changes in how you travel can make a big difference.\n\nStart by choosing direct flights when possible. Layovers increase fuel consumption significantly, and a non-stop route is one of the easiest ways to cut your carbon footprint. When you land, opt for public transportation, cycling, or walking instead of rental cars.\n\nAccommodation matters too. Look for eco-certified hotels or locally owned guesthouses that reinvest in their communities. Many sustainable lodges now operate on solar power and use rainwater collection systems.\n\nPack light. Heavier luggage means more fuel burned on flights. A capsule wardrobe for travel not only saves weight but makes packing faster. Choose reusable items — a water bottle, tote bag, and bamboo cutlery set go a long way.\n\nFinally, be mindful of where you spend your money. Eating at local restaurants, buying from local artisans, and booking local guides keeps tourism dollars in the community and supports the places you visit.\n\nSustainable travel doesn't mean sacrificing comfort — it means being intentional. With a few simple swaps, you can explore the world while helping to protect it."
}
```
