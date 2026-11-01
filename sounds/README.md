# Animal sounds

Recorded animal sounds for Habre's Nepali (`kids.html`). When an animal has a file here, the game plays it after the animal's name. When it doesn't, Habre says the animal's sound word with his own voice (*myaau myaau*, *bhau bhau*…). Nothing breaks if a file is missing.

## Only use sounds you may use

Use only sounds that are **CC0 / public domain**, or that are your own recordings. Check the licence on each sound's own page, write it in `SOUNDS-LICENSES.md` (one row per file), and keep a screenshot of the licence page. Do not use sounds licensed non-commercial (CC BY-NC), BBC Sound Effects, or xeno-canto recordings if you will sell the game. The files in this folder are public once the repo is public, so CC0 or your own recordings are the safe choice.

## Adding a sound

1. Download the sound as **OGG** (small, and plays in every browser the game supports). Save it here, named after the animal's word in the game: `biralo.ogg` for the cat, `kukur.ogg` for the dog, `gai.ogg` for the cow. The names are the romanized words in `ANIMAL_FX` in `kids.html`.
2. Add a line for it to `manifest.json`:

```json
{
  "biralo": {
    "f": "biralo.ogg",
    "ms": 2500,
    "title": "Little Meow of a Cat #1",
    "by": "Joseph Sardin",
    "src": "https://bigsoundbank.com/little-meow-of-a-cat-s0494.html",
    "lic": "CC0"
  }
}
```

- `f`: the file name in this folder.
- `ms`: how many milliseconds to play before fading out (use this to cut a long recording short; 2500 to 3500 suits a small child). The clip starts from its beginning.
- `title`, `by`, `src`, `lic`: shown on the grown-ups' **Sound credits** page.
- `vol` (optional, 0 to 1): quieter or louder than the usual 0.9.

3. Reload the game. Tap the animal on a learn card to hear it. Under **For grown-ups > Voice and sound**, "Animal sounds" turns all of this on or off.

Keep each clip short (a few seconds) and the folder small: every file is downloaded by the child's device the first time it plays.
