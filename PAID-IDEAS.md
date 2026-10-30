# Ideas for the paid version

Ideas for what a paid version of Habre's Nepali (`kids.html`) could include. Nothing here is built yet. For lessons taken out of the free game that might come back as paid content, see `SHELVED.md`.

## Better analytics that grown-ups can see at any time

- A progress view that's always up to date and easy to reach, not only the current grown-ups' page.
- Ideas to explore:
  - time played and streaks over days and weeks
  - words learned over time
  - the words a child keeps getting wrong
  - progress by trip and by level
  - a weekly summary
- **Free version today:** the grown-ups' page shows stars, games played, a topic-by-level table, journey and story progress, flashcard baskets and "Words to practise".

## More control over flashcards

- Grown-ups (or children) make their own flashcard sets: choose the words, name the set, and maybe add their own words and pictures.
- **Free version:** flashcards stay as the built-in categories only (one deck for each topic in play, plus story words and tricky words).
- **Grown-ups' deck:** the free game had one set a grown-up builds by ticking words on the grown-ups' page. It was shelved on 2026-10-30 (see `SHELVED.md`). The code is a starting point for making your own sets, and words already ticked are kept.

## Replay every story

- **Paid:** replay any story at any time.
- **Free:** replay only the first 5 stories the child reads. Any story still plays once, the first time its stop is reached on the path.
- On the path as it is now, a child's first 5 stories would be:
  - *Bagaichama* and *Paani paryo* (the garden)
  - *Haraeko biralo* and *Bhok lagyo!* (the farm village)
  - *Bazaar ma* (the market)
- **Free version today:** any story stop already passed can be replayed by tapping it, so all 11 stories on the path can be replayed.
- **To work out:**
  - Count the first 5 per player, by the order each child read them.
  - Decide what a locked replay shows: a lock and a short "replay with Habre Plus" note behind the grown-ups' gate, so children aren't asked to buy anything.
  - Decide whether the 4 stories that aren't on the path (*Habre ko bihana*, *Habreko janmadin*, *Daktarkahaa*, *Schoolma*) become paid-only.

## Paid maps

Built on the `habre-plus` branch (local, not pushed): two maps shaped like the free one, each 10 sections of 10 words (7 new, 3 already seen). They open once the free map is finished. Every word is listed in the README's Habre Plus section.
- 🌊 **The water map:** river → rice fields → Phewa Lake → fishing village → beach → coral reef → across the sea → deep sea → treasure island → frozen sea.
- ☁️ **The sky map:** roof → weather → treetops → above the clouds → airport → paragliding over Pokhara → night sky → sun and planets → rocket launch → far out in space.

Still to add:
- Stories along each map.
- A Nepali speaker's check of the new words.
- Ideas for more maps: Kathmandu (the big city), Chitwan (jungle safari), a mountain trek, the fair.

## Also sketched on the `habre-plus` branch

- A real person reading the words and stories.
- A weekly report for grown-ups (this overlaps with the analytics idea above).
