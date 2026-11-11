# Contributing

Thanks for helping make this the most useful free prompt collection on GitHub! 🎉

## Adding a prompt

1. **Test it first** on at least one AI tool and note which one.
2. Add it to the right file in [`prompts/`](prompts/) using the same format:
   - `## Title` (max ~60 characters)
   - one or two sentences describing the result
   - `**Works with:**` and `**Type:**`
   - the prompt inside a ```` ```text ```` block
   - up to 4 short tips
3. Add the same prompt to [`data/prompts.json`](data/prompts.json) with the next free `id`.
4. Run the check locally:

   ```bash
   python scripts/validate.py
   ```

5. Open a pull request.

## Prompt quality rules

- Write in clear English; be specific (lighting, camera, style, aspect ratio).
- Use `[square brackets]` for parts the user should replace — keep each one short.
- Photo prompts that use an uploaded picture must say **"keep the face exactly the same"**.
- No prompts for real celebrities, copyrighted characters, adult content or deception.
- No affiliate links or promotional links inside prompts.

## Fixes and translations

Typos, better wording and translations are very welcome — open a PR or an issue.

## Code of conduct

Be kind and constructive. Harassment or spam in issues and pull requests will be removed.
