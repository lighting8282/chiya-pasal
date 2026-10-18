# Chiya Pasal

A small browser game for learning romanized Nepali. You run a tea stall (*chiya pasal*) in Kathmandu, and every customer talks to you in Nepali.

## How to play

Open `chiya_pasal.html` in any modern browser. There is no build step and nothing to install.

- **Greetings and small talk.** Pick the right reply, e.g. *"Tapai lai kasto cha?"* → *"Malai sanchai cha."*
- **Orders.** Read *"Malai dui plate momo chahiyo"*, put the right food on the tray, then press **Linus!** ("here you go").
- **Paying.** When a customer asks *"Kati bhayo?"* ("How much?"), add up the menu prices and pick the total in Nepali.
- **Stock questions.** *"Thukpa cha?"* → *Cha* (yes) or *Chaina* (no), depending on today's menu.

Tap any word in a speech bubble to see its meaning and Devanagari spelling. Peeking costs that customer's tip (*baksis*).

## Learning design

- New vocabulary comes in over five days: numbers, foods, counting words (*cup, gilas, plate, wota*) and polite phrases. Each day opens with a card of the new words. Day 6 onward is review.
- Every word has a mastery level (0 to 5). Correct answers without peeking raise it, mistakes lower it, and weaker words show up more often.
- The **Shabdakosh** (dictionary) lists every unlocked word with its mastery.
- **Settings** has a Relaxed mode (no patience timer) and a Show English mode.
- Progress is saved in the browser's `localStorage`.

## Limitations

- Prices are multiples of 10, because Nepali numbers from 11 to 99 are irregular and aren't taught yet.
- Romanized Nepali spelling varies between sources. The game uses common forms such as *dhanyabaad*, *chhito* and *bhetaula*.

## Project layout

Everything lives in one file, `chiya_pasal.html`: styles, vocabulary data (`VOCAB`, `ITEMS`, `CHATS`), the step generators, and the game loop.
