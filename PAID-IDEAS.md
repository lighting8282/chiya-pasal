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

## Future map ideas

Each map has the same shape as the free map: 10 sections of 10 words, and a Habre's Journey chapter in every section.

**Habre's adventures:** every map is a trip of its own. Habre is going around the world, and to many other places, to learn as much as he can, just like the child playing. Each map's story starts at home and stands alone, so the order doesn't matter: once the free map is finished, the child picks whichever open map they like. Trips that aren't holidays (school, helpers in town, the farming year) can be days out, and the most fantastical ones (the magic kingdom, the tiny world, inside the body) can be dreams.

**Postcards and souvenirs** (built for the free map; each paid map needs its own entry in `TRIP_ENDS`):
- **A postcard to Hajuraama** when a map is finished: a picture of the place and a short note from Habre, kept for grown-ups to see (and maybe in the game too).
- **A souvenir** from every map, such as a seashell from the water map or a model rocket from the sky map. Postcards go on a bulletin board and souvenirs in a glass case in Habre's living room, which gives the room a new purpose now that its lessons are shelved.

- 🌊 **Water**: built on the `habre-plus` branch.
- ☁️ **Sky**: built on the `habre-plus` branch.
- 🚀 **Space**: the sky map already ends with three space sections, so a space map could replace those or carry on from them.
- 🏙️ **City**: for example Kathmandu (temples, buses, shops, street food).
- 🏫 **School**: the classroom, the playground, lunch, books, sports day.
- 🎃 **Seasonal and holiday maps**, Nepali and American:
  - Nepali: Dashain, Tihar, Holi, Lhosar, Teej, Chhath, Nepali New Year
  - American: Halloween, Thanksgiving, Christmas, Easter, the Fourth of July
  - The free map's temple square already has the Tihar, Dashain and Holi side stories.
- Older ideas: Chitwan (jungle safari), a mountain trek, the fair.
- And more to come.

## Already sketched on the `habre-plus` branch (local, not pushed)

- New stories in every place.
- A real person reading the words and stories.
- A weekly report for grown-ups (this overlaps with the analytics idea above).
