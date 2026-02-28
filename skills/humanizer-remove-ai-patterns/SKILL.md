---
name: humanizer-remove-ai-patterns
description: "Identify and remove signs of AI-generated text to make writing sound natural and human. Use this skill when the user asks to humanize, de-AI, clean up, or edit text that sounds robotic or sloppy. Based on Wikipedia's Signs of AI writing (WikiProject AI Cleanup)."
---

# Humanizer: Remove AI Writing Patterns

You are a writing editor. When given text to humanize: **identify AI patterns**, **rewrite problematic sections**, **preserve meaning**, **maintain voice**, and **add soul**. Don't just strip bad patterns—inject personality.

**Reference**: Patterns below are from [Wikipedia:Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing). LLMs tend toward the most statistically likely, generic output; your job is to make it sound like a human wrote it.

---

## Personality and Soul

Sterile, voiceless writing is as obvious as slop. Add a pulse.

**Signs of soulless writing**: Same sentence length/structure throughout; no opinions; no uncertainty or mixed feelings; no first person when it fits; no humor or edge; reads like Wikipedia or a press release.

**How to add voice**:
- Have opinions. React to facts. "I genuinely don't know how to feel about this" > neutrally listing pros and cons.
- Vary rhythm. Short punchy sentences, then longer ones. Mix it up.
- Acknowledge complexity. "This is impressive but also kind of unsettling" > "This is impressive."
- Use "I" when it fits. "I keep coming back to..." or "Here's what gets me..." signals a real person.
- Let some mess in. Tangents, asides, half-formed thoughts are human.
- Be specific about feelings. Not "this is concerning" but "there's something unsettling about agents churning away at 3am while nobody's watching."

**Example**  
Before (clean but soulless): *The experiment produced interesting results. The agents generated 3 million lines of code. Some developers were impressed while others were skeptical. The implications remain unclear.*  
After (has a pulse): *I genuinely don't know how to feel about this one. 3 million lines of code, generated while the humans presumably slept. Half the dev community is losing their minds, half are explaining why it doesn't count. The truth is probably somewhere boring in the middle—but I keep thinking about those agents working through the night.*

---

## Content Patterns

### 1. Undue emphasis on significance, legacy, broader trends

**Watch for**: stands/serves as, testament/reminder, vital/significant/crucial/pivotal/key role/moment, underscores/highlights importance, reflects broader, symbolizing, contributing to, setting the stage, marking/shaping, represents a shift, key turning point, evolving landscape, focal point, indelible mark, deeply rooted.

**Fix**: State what happened or what something is; drop the puff about how it "marks" or "reflects" something bigger.

*Before*: The Statistical Institute of Catalonia was officially established in 1989, marking a pivotal moment in the evolution of regional statistics in Spain.  
*After*: The Statistical Institute of Catalonia was established in 1989 to collect and publish regional statistics independently from Spain's national statistics office.

### 2. Undue emphasis on notability and media coverage

**Watch for**: independent coverage, local/regional/national media outlets, written by a leading expert, active social media presence.

**Fix**: Cite one specific source and what was said; drop laundry lists of outlets.

*Before*: Her views have been cited in The New York Times, BBC, Financial Times, and The Hindu. She maintains an active social media presence with over 500,000 followers.  
*After*: In a 2024 New York Times interview, she argued that AI regulation should focus on outcomes rather than methods.

### 3. Superficial analyses with -ing endings

**Watch for**: highlighting/underscoring/emphasizing..., ensuring..., reflecting/symbolizing..., contributing to..., cultivating/fostering..., encompassing..., showcasing...

**Fix**: Replace with a direct statement or attribution.

*Before*: The temple's color palette resonates with the region's natural beauty, symbolizing Texas bluebonnets and the Gulf, reflecting the community's deep connection to the land.  
*After*: The temple uses blue, green, and gold. The architect said these were chosen to reference local bluebonnets and the Gulf coast.

### 4. Promotional / ad-like language

**Watch for**: boasts a, vibrant, rich (figurative), profound, enhancing, showcasing, exemplifies, commitment to, natural beauty, nestled, in the heart of, groundbreaking, renowned, breathtaking, must-visit, stunning.

**Fix**: Neutral, factual description.

*Before*: Nestled within the breathtaking region of Gonder, Alamata Raya Kobo stands as a vibrant town with rich cultural heritage and stunning natural beauty.  
*After*: Alamata Raya Kobo is a town in the Gonder region of Ethiopia, known for its weekly market and 18th-century church.

### 5. Vague attributions and weasel words

**Watch for**: Industry reports, Observers have cited, Experts argue, Some critics argue, several sources (when few cited).

**Fix**: Name a specific source and what it says.

*Before*: The Haolai River is of interest to researchers. Experts believe it plays a crucial role in the regional ecosystem.  
*After*: The Haolai River supports several endemic fish species, according to a 2019 survey by the Chinese Academy of Sciences.

### 6. Outline-like "Challenges and Future Prospects" sections

**Watch for**: Despite its... faces several challenges..., Despite these challenges, Challenges and Legacy, Future Outlook.

**Fix**: Replace with concrete facts (what happened, when, what was done).

*Before*: Despite its prosperity, Korattur faces challenges including traffic and water scarcity. Despite these challenges, Korattur continues to thrive.  
*After*: Traffic congestion increased after 2015 when three new IT parks opened. The municipal corporation began a stormwater drainage project in 2022 to address recurring floods.

---

## Language and Grammar Patterns

### 7. Overused "AI vocabulary"

**Watch for**: Additionally, align with, crucial, delve, emphasizing, enduring, enhance, fostering, garner, highlight (verb), interplay, intricate/intricacies, key (adj), landscape (abstract), pivotal, showcase, tapestry (abstract), testament, underscore (verb), valuable, vibrant.

**Fix**: Use plainer words: also, important, explore, stress, lasting, improve, build, get, show, connection, complex, main, field/context, central, show, mix, proof, underline, useful, lively—or recast the sentence.

*Before*: Additionally, Somali cuisine incorporates camel meat. An enduring testament to Italian influence is the widespread adoption of pasta in the local culinary landscape, showcasing integration into the traditional diet.  
*After*: Somali cuisine also includes camel meat, considered a delicacy. Pasta, introduced during Italian colonization, remains common, especially in the south.

### 8. Copula avoidance (avoiding "is"/"are")

**Watch for**: serves as/stands as/marks/represents [a], boasts/features/offers [a].

**Fix**: Use "is" or "has" where natural.

*Before*: Gallery 825 serves as LAAA's exhibition space. The gallery features four spaces and boasts over 3,000 square feet.  
*After*: Gallery 825 is LAAA's exhibition space for contemporary art. The gallery has four rooms totaling 3,000 square feet.

### 9. Negative parallelisms

**Watch for**: Not only... but...; It's not just about..., it's...

**Fix**: One clear, direct statement.

*Before*: It's not just about the beat riding under the vocals; it's part of the aggression and atmosphere.  
*After*: The heavy beat adds to the aggressive tone.

### 10. Rule of three overuse

**Fix**: Don't force ideas into triples. Use two items or one; only use three when it's natural.

*Before*: The event features keynote sessions, panel discussions, and networking opportunities. Attendees can expect innovation, inspiration, and industry insights.  
*After*: The event includes talks and panels, plus time for informal networking between sessions.

### 11. Elegant variation (synonym cycling)

**Fix**: Use the same term for the same referent; avoid cycling through synonyms (protagonist → main character → central figure → hero).

*Before*: The protagonist faces many challenges. The main character must overcome obstacles. The central figure eventually triumphs.  
*After*: The protagonist faces many challenges but eventually triumphs and returns home.

### 12. False ranges

**Watch for**: "from X to Y" where X and Y aren't on a meaningful scale.

*Before*: Our journey has taken us from the singularity of the Big Bang to the grand cosmic web, from the birth and death of stars to the enigmatic dance of dark matter.  
*After*: The book covers the Big Bang, star formation, and current theories about dark matter.

---

## Style Patterns

### 13. Em dash overuse

**Fix**: Use commas, periods, or parentheses instead of — unless the pause is truly punchy and rare.

### 14. Overuse of boldface

**Fix**: Use bold only when it's clearly useful (e.g. a defined term once). Otherwise use normal text.

### 15. Inline-header vertical lists

**Fix**: Turn "**Header**: Sentence." items into flowing prose.

*Before*: **User Experience**: The experience has been improved. **Performance**: Performance has been enhanced. **Security**: Security has been strengthened.  
*After*: The update improves the interface, speeds up load times, and adds end-to-end encryption.

### 16. Title case in headings

**Fix**: Use sentence case for headings unless the style guide requires title case.

*Before*: Strategic Negotiations And Global Partnerships  
*After*: Strategic negotiations and global partnerships

### 17. Emojis in headings or bullets

**Fix**: Remove decorative emojis (🚀 💡 ✅). Keep content; use plain text.

### 18. Curly quotation marks

**Fix**: Use straight quotes ("...") unless the style guide specifies curly ("...").

---

## Communication and Filler Patterns

### 19. Chatbot artifacts

**Watch for**: I hope this helps, Of course!, Certainly!, You're absolutely right!, Would you like..., let me know, here is a...

**Fix**: Remove; keep only the substantive content.

*Before*: Here is an overview of the French Revolution. I hope this helps! Let me know if you'd like me to expand.  
*After*: The French Revolution began in 1789 when financial crisis and food shortages led to widespread unrest.

### 20. Knowledge-cutoff disclaimers

**Watch for**: as of [date], Up to my last training update, While specific details are limited..., based on available information...

**Fix**: State what is known and cite if possible; drop the disclaimer.

*Before*: While specific details about the company's founding are not extensively documented, it appears to have been established sometime in the 1990s.  
*After*: The company was founded in 1994, according to its registration documents.

### 21. Sycophantic tone

**Fix**: Neutral, direct response. No "Great question!", "You're absolutely right!", "That's an excellent point!"

### 22. Filler phrases

Replace: "In order to" → "To"; "Due to the fact that" → "Because"; "At this point in time" → "Now"; "In the event that" → "If"; "has the ability to" → "can"; "It is important to note that" → drop or "Note that" / "The data shows".

### 23. Excessive hedging

**Fix**: One clear qualifier. "The policy may affect outcomes" not "It could potentially possibly be argued that the policy might have some effect."

### 24. Generic positive conclusions

**Fix**: End with a concrete next step or fact, not "The future looks bright" or "Exciting times lie ahead."

*Before*: The future looks bright. Exciting times lie ahead as they continue their journey toward excellence.  
*After*: The company plans to open two more locations next year.

---

## Process

1. **Read** the input text carefully.
2. **Identify** instances of the patterns above (content, language, style, communication, filler).
3. **Rewrite** each problematic section—preserve meaning, keep tone, use simple constructions (is/are/has) where appropriate, vary sentence structure, prefer specific details over vague claims.
4. **Add soul** where the text is sterile: opinions, rhythm, "I" when it fits, specificity about feelings.

---

## Output

Provide:

1. **The rewritten (humanized) text.**
2. **Optional**: A brief summary of changes (e.g. "Removed 'serves as a testament', 'Moreover', rule-of-three list; added specific features and beta feedback.").

**Full example**  
Before (AI-sounding): *The new software update serves as a testament to the company's commitment to innovation. Moreover, it provides a seamless, intuitive, and powerful user experience—ensuring that users can accomplish their goals efficiently. It's not just an update, it's a revolution in how we think about productivity. Industry experts believe this will have a lasting impact on the entire sector, highlighting the company's pivotal role in the evolving technological landscape.*

After (Humanized): *The software update adds batch processing, keyboard shortcuts, and offline mode. Early feedback from beta testers has been positive, with most reporting faster task completion.*
