# 🌌 The Last Signal

A sci-fi mystery choose-your-own-adventure game with **6 distinct endings**, persistent stats, and a twist mechanic that recontextualizes the entire story depending on your choices — plus a **hidden feature** that remembers your decisions across playthroughs.

## The Premise

You wake up in a sealed room with no memory. A blinking console says you have three paths to choose from. Every path reveals a different layer of what's actually happening — and each ending changes how you understand the story that came before it.

## Features

- 🌀 **3 Starting Paths** — Trust the signal, Break the console, or Ignore it completely
- 🎭 **6 Unique Endings** — 2 GOOD, 2 BAD, 2 TWIST endings, each revealing something new about the premise
- 📊 **Persistent stats** — playthroughs, endings unlocked tracked in `stats.json` across sessions
- 🔄 **Hidden memory mechanic** — if you pick "Ignore it → Stay still" multiple times across different runs, the game *remembers* and injects a meta line like "This is the 3rd time you've chosen to do nothing" — genuinely only works if you replay that branch
- ✨ **Slow-printed text** — story text types out character-by-character for atmosphere
- 🛡 **Input validation** — invalid choices just re-prompt, never crash

## The Endings (Spoiler-Free Tones)

| Ending | Tone | Path |
|--------|------|------|
| **Glitch in the System** | 🌀 TWIST | Trust the Signal → Smash Screens |
| **The Operator** | 🌀 TWIST | Trust the Signal → Keep Walking |
| **The Awakened** | 🏆 GOOD | Break Console → Search for Others |
| **Lost Forever** | 💀 BAD | Break Console → Run Alone |
| **The Loop** | 💀 BAD | Ignore It → Stay Still (3+ times) |
| **Break the Loop** | 🏆 GOOD | Ignore It → Scream and Fight |

## Example Playthrough

```
🌌 THE LAST SIGNAL
============================================================
Playthroughs: 2  |  Endings found: 3/6

1. Begin
2. Quit
> 1

You wake up on a cold floor. No memory of how you got here.
A console on the wall blinks red text:
  "SIGNAL RECEIVED. 3 PATHS DETECTED. CHOOSE."

  1. Trust the signal, follow its instructions
  2. Break the console, go your own way
  3. Ignore it. Sit. Wait.

> 3

You wait. The countdown on the console hits zero.
Nothing explodes. The room simply... resets.

(This is the 1st time you've chosen to do nothing.)

  1. Stay still. Wait again.
  2. Scream and fight against the reset

> 2

Right as the reset takes hold, you refuse. You scream, fight, push back
against the exact moment you always used to stay still.
The loop stutters — and breaks. You're the first version of you to ever get this far.

============================================================

🏆 GOOD ENDING
✨ New ending discovered! (4/6 found)
```

## Project Structure

```
choose_your_own_adventure/
├── game.py       # story tree, choice logic, stats tracking
├── stats.json     # auto-created, tracks playthroughs + endings seen
└── README.md
```

## Design Details

**Why this is more than a text adventure:**
- Story is **pure data** (`STORY` dict) — adding new branches means no code changes, just extending the dict
- **Persistent replay value** — the loop-counting mechanic actually requires multiple sessions to fully appreciate; it's not just flavor, it changes the text mid-game
- **Twist endings** that reframe the premise (e.g. "The Operator" suggests you were never trapped *in* the simulation, you were running *it*)
- **Clean separation** between game logic (`play()`, `get_choice()`) and story content — story could be reloaded from a JSON file later without refactoring

## Possible Improvements

- Load story from external JSON instead of hardcoding it (scales to much larger games)
- Add **inventory/items** that unlock or block certain choices (e.g. finding a keycard early opens a path later)
- **Randomized branches** — some choices lead to random sub-paths, not deterministic ones
- **Dialogue trees** instead of narrator-only text (NPCs you meet in some endings)
- Web version with a visual choice UI

## Author

Built by **Kirithik** as part of a personal Python mini-projects collection.