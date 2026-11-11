<div align="center">

# ✨ Free AI Prompts

**60 free, tested, copy-paste prompts for ChatGPT, Gemini, Nano Banana, Claude, Midjourney, Sora, Veo and more.**
Photos · Video · Writing · Code — organised by category and by AI tool.

[![License: MIT](https://img.shields.io/badge/License-MIT-6d5efc.svg)](LICENSE)
[![Prompts](https://img.shields.io/badge/prompts-60-ff5fa2.svg)](data/prompts.json)
[![Validate](https://github.com/freeaiprompts/free-ai-prompts/actions/workflows/validate.yml/badge.svg)](https://github.com/freeaiprompts/free-ai-prompts/actions/workflows/validate.yml)
[![PRs welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)

[Browse by category](#-categories) · [Dataset (JSON / CSV)](#-use-the-dataset) · [How to write better prompts](#-how-to-get-better-results) · [Contribute](CONTRIBUTING.md)

</div>

---

## Why this repo?

Most prompt lists are untested one-liners. Every prompt here is:

- **Tested** on at least one real AI tool (listed under each prompt)
- **Detailed** — lighting, camera, style and aspect ratio are already written for you
- **Customisable** — parts in `[square brackets]` are placeholders you replace
- **Face-safe** — photo prompts that use your picture always include *"keep the face exactly the same"*
- **Machine-readable** — the full collection is available as [JSON](data/prompts.json) and [CSV](data/prompts.csv)

| Type | Prompts |
|---|---|
| 📸 Image | 51 |
| 🎬 Video | 1 |
| ✍️ Text / chat | 7 |
| 💻 Code | 1 |

## 📂 Categories

| Category | Prompts |
|---|---|
| 🎄 [#](prompts/christmas.md) | 14 |
| 🎆 [#](prompts/new-year.md) | 7 |
| 🎉 [#](prompts/holidays.md) | 2 |
| 🔥 [#](prompts/trends.md) | 6 |
| 📸 [#](prompts/portraits.md) | 7 |
| 🎨 [#](prompts/art.md) | 13 |
| 💼 [#](prompts/business.md) | 1 |
| ✏️ [#](prompts/design.md) | 3 |
| 📱 [#](prompts/social-media.md) | 3 |
| 🎯 [#](prompts/career.md) | 1 |
| 🎬 [#](prompts/video.md) | 1 |
| 💻 [#](prompts/coding.md) | 1 |
| 📚 [#](prompts/education.md) | 1 |

## ⚡ Quick example

**Christmas Family Photo by the Fireplace** — works with Nano Banana, ChatGPT Images, Gemini, Midjourney

```text
Transform the uploaded photo into a warm Christmas family portrait. Keep every person's face, hairstyle and identity exactly the same. Place [the family] on a cozy sofa in front of a crackling fireplace with stockings, a tall decorated Christmas tree with warm fairy lights and wrapped gifts. Everyone wears matching [red knitted Christmas sweaters]. Soft golden light, shallow depth of field, shot on an 85mm lens, photorealistic, magazine quality, 4:5.
```

1. Open your AI tool (for this one: Gemini with Nano Banana, or ChatGPT).
2. Upload a clear photo.
3. Paste the prompt, replace the `[brackets]`, and send.

## 🧠 How to get better results

| Do | Why |
|---|---|
| Use a sharp, well-lit photo where faces are visible | Image models copy what they can see |
| Keep the line *"keep the face exactly the same"* | Stops the AI from changing identity |
| Replace **every** `[bracket]` | Specific details = better images |
| End with an aspect ratio (`4:5`, `9:16`, `16:9`) | Fits Instagram, Stories or YouTube |
| Generate 2–3 versions and pick the best | Results vary on every run |
| For text in images (names, titles) use ChatGPT Images or Ideogram | They render letters most accurately |

**Tool-specific formatting:** Midjourney likes parameters at the end (`--ar 4:5 --v 7`), ChatGPT Images works well with *"Create an image:"* in front, and video models (Sora, Veo, Kling) give the best results with **one** camera movement per clip.

## 📦 Use the dataset

```python
import json, urllib.request

url = "https://raw.githubusercontent.com/freeaiprompts/free-ai-prompts/main/data/prompts.json"
data = json.load(urllib.request.urlopen(url))

christmas = [p for p in data["prompts"] if "christmas" in p["categories"]]
print(len(christmas), "Christmas prompts")
print(christmas[0]["prompt"])
```

Each prompt has: `id`, `title`, `slug`, `type`, `categories`, `tools`, `prompt`, `description`, `tips`, `url`.
Ideas: a Telegram/Discord prompt bot, a "prompt of the day" widget, a VS Code snippet pack, or a mobile app.

## 🌍 Website & languages

Prefer browsing with previews? The same collection — with before/after images, a one-click *Copy for ChatGPT / Gemini / Midjourney* button and a prompt builder for the `[brackets]` — is available in 8 languages (English, German, French, Portuguese, Spanish, Hindi, Thai and Chinese) at **[FreeAIPrompts.net](https://freeaiprompts.net)**.

## 🤝 Contributing

New prompts, fixes and translations are welcome! Read [CONTRIBUTING.md](CONTRIBUTING.md), then open a pull request or use the [new prompt issue form](../../issues/new/choose).

## ⚠️ Responsible use

- Only upload photos of yourself or people who agreed to it.
- Don't use these prompts to impersonate real people or create misleading content.
- Follow the terms of the AI tool you use. AI results can be wrong — check facts before you rely on them.

## 📄 License

[MIT](LICENSE) — free for personal and commercial use. Attribution is appreciated but not required.

<div align="center">

If this collection helped you, please ⭐ **star the repo** so more people can find it.

</div>
