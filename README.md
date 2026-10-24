# Chiya Pasal

A small browser game for learning romanized Nepali. You run a tea stall (*chiya pasal*) in Kathmandu, and every customer talks to you in Nepali.

**Play it in your browser: https://lighting8282.github.io/chiya-pasal/**

**For children: [Habre's Nepali](https://lighting8282.github.io/chiya-pasal/kids.html)**, a picture-and-voice version with Habre the red panda. Kids tap big pictures to hear Nepali words in 18 topics (animals, wild animals, birds, reptiles and frogs, sea animals, bugs, colours, counting to 20, big numbers up to 100, family, food, body, clothes, things at home, nature, vehicles, feelings and everyday sayings), then play "find it" games for stars. Each topic has three levels: *Sajilo* (easy, 2 choices), *Thikka* (medium, 3 choices) and *Gaaro* (hard, 4 choices, counting to 20, listen-only). Each child gets their own player profile with their own stars. Voices use the browser's own speech: Microsoft Edge has Nepali voices, and Chrome reads the Devanagari with its Hindi voice. The ⚙ button lets a grown-up pick the voice and speed.

## How to play

Play online at the link above, or download `index.html` and open it in any modern browser. There is no build step and nothing to install.

- **Greetings and small talk.** Pick the right reply, e.g. *"Tapai lai kasto cha?"* → *"Malai sanchai cha."*
- **Orders.** Read *"Malai dui plate momo chahiyo"*, put the right food on the tray, then press **Linus!** ("here you go").
- **Paying.** When a customer asks *"Kati bhayo?"* ("How much?"), add up the menu prices and pick the total in Nepali.
- **Stock questions.** *"Thukpa cha?"* → *Cha* (yes) or *Chaina* (no), depending on today's menu.

### Mausam (weather)

Open **Mausam** from the header at any time for a weather practice round, or reach day 6, when the weather starts changing at the stall. The window shows the sky (sun, heat, clouds, rain, snow, cold, wind or fog) and customers ask:

- *"Aaja mausam kasto cha?"* ("What's the weather like today?"): look outside and pick the matching sentence, e.g. *"Aaja paani pardai cha."*
- Yes/no questions like *"Ghaam lagyo?"* ("Is it sunny?"): answer *Ho* (yes) or *Hoina* (no).
- Reports from around Nepal like *"Mustang ma hawa chaldai cha"* ("It's windy in Mustang"): pick the matching weather picture.

On cold or wet days customers order more hot drinks. On hot days they want water.

### Pariwar (family)

Open **Pariwar** from the header to practise talking with your wife's family. Six relatives come to visit, each labelled with who they are (for example *sasu*, your mother-in-law). You:

- greet each one by the right name: *Aama* and *Buwa* for your parents-in-law, *Dai* for her elder brother, *Bhai* and *Bahini* for her younger siblings, and *dhog* for her grandparents;
- answer everyday questions such as *"Khana khanubhayo?"* ("Have you eaten?"), *"Ali aru khanus na"* (eat a little more → *"Pugyo"*, that's enough), *"Kahaa jaane?"* ("Where are you going?") and *"Bujhnubhayo?"* → *"Bujhina. Pheri bhannus na."* ("I didn't understand. Please say it again.");
- with your wife, use the familiar *timi* forms, e.g. *"Ma pani timilai maya garchhu"* ("I love you too").

After each answer a tip explains the custom behind it, such as when to use *hajur*, *tapai* or *timi*. The intro screen has a table of what to call each relative and what they call you (*jwain*, *bhinaju*). There is no timer in this round.

### Vishaya (picture topics)

Open **Vishaya** from the header to practise everyday words in 15 topics: animals, wild animals, birds, reptiles and frogs, sea animals, bugs, colours, body, clothes, things at home, nature, vehicles, feelings, fruit, and sayings people use today (including slang such as *khatra* and *dami*). A neighbour's child shows you a picture and asks *"Yo ke ho?"* ("What is this?") to name in Nepali, or asks *"… dekhaunus"* ("please show me …") and you pick the picture. Each topic opens with word cards you can tap to hear.

### Voices

Every line in the game can be read aloud. The game turns the romanized text into Devanagari and speaks it with a Nepali voice installed on your device, or a Hindi voice if there is no Nepali one. Microsoft Edge has Nepali voices built in. On Android, install Nepali in Google's text-to-speech settings. Tap 🔊 in a speech bubble to hear the line again, or tap a word to hear just that word. Settings lets you turn voices off, pick a voice and change the speed.

Tap any word in a speech bubble to see its meaning and Devanagari spelling. Peeking costs that customer's tip (*baksis*).

## Learning design

- New vocabulary comes in over six days: numbers, foods, counting words (*cup, gilas, plate, wota*), polite phrases, and on day 6 the weather. Each day opens with a card of the new words. Day 7 onward is review.
- Every word has a mastery level (0 to 5). Correct answers without peeking raise it, mistakes lower it, and weaker words show up more often.
- The **Shabdakosh** (dictionary) lists every unlocked word with its mastery.
- **Settings** has a Relaxed mode (no patience timer) and a Show English mode.
- Progress is saved in the browser's `localStorage`.

## Limitations

- Prices are multiples of 10, because Nepali numbers from 11 to 99 are irregular and aren't taught yet.
- Romanized Nepali spelling varies between sources. The game uses common forms such as *dhanyabaad*, *chhito* and *bhetaula*.

## Project layout

The kids' game is a separate single file, `kids.html`. The main game lives in one file, `index.html`, which GitHub Pages serves from the `main` branch: styles, vocabulary data (`VOCAB`, `ITEMS`, `CHATS`), the step generators, and the game loop.
