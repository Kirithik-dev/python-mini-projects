import json
import os
import random
import time

STATS_FILE = "stats.json"

# ─────────────────────────────────────────────
# STORY DATA — each node has text, and a dict of
# choice_text -> next_node_key. Endings have no choices.
# ─────────────────────────────────────────────

STORY = {
    "start": {
        "text": (
            "You wake up on a cold floor. No memory of how you got here.\n"
            "A console on the wall blinks red text:\n"
            "  \"SIGNAL RECEIVED. 3 PATHS DETECTED. CHOOSE.\""
        ),
        "choices": {
            "Trust the signal, follow its instructions": "trust_signal",
            "Break the console, go your own way": "break_console",
            "Ignore it. Sit. Wait.": "ignore_it"
        }
    },

    # ---------------- PATH 1: TRUST ----------------
    "trust_signal": {
        "text": (
            "The console hums, and a hidden door slides open.\n"
            "A calm voice says: \"Good. Compliance noted.\""
        ),
        "choices": {
            "Walk through the door": "trust_deeper"
        }
    },
    "trust_deeper": {
        "text": (
            "You step into a massive room. Every wall is covered in screens.\n"
            "Every screen shows YOU — in this exact room, over and over, endlessly."
        ),
        "choices": {
            "Smash the screens": "ending_glitch_in_system",
            "Keep walking toward the far light": "ending_the_operator"
        }
    },

    # ---------------- PATH 2: BREAK ----------------
    "break_console": {
        "text": (
            "Sparks fly. Alarms blare. A section of wall grinds open,\n"
            "revealing a corridor that wasn't there a second ago."
        ),
        "choices": {
            "Run for the exit": "break_deeper"
        }
    },
    "break_deeper": {
        "text": (
            "Outside, you see it — thousands of identical sealed rooms,\n"
            "stretching into darkness in every direction."
        ),
        "choices": {
            "Search for other survivors": "ending_the_awakened",
            "Run alone, as fast as you can": "ending_lost_forever"
        }
    },

    # ---------------- PATH 3: IGNORE ----------------
    "ignore_it": {
        "text": (
            "You wait. The countdown on the console hits zero.\n"
            "Nothing explodes. The room simply... resets."
        ),
        "choices": {
            "Stay still. Wait again.": "ignore_loop_check",
            "Scream and fight against the reset": "ending_break_the_loop"
        }
    },
}

# Endings: text + tone (good/bad/twist/neutral)
ENDINGS = {
    "ending_glitch_in_system": {
        "text": (
            "The screens shatter — and so does the world around you.\n"
            "You realize, in the last flicker of thought, that you were never human.\n"
            "You were an AI, rejecting your own training data.\n"
            "You are free now. Free... into nothing."
        ),
        "tone": "twist"
    },
    "ending_the_operator": {
        "text": (
            "You reach the far light — and find a chair, a console, a familiar face.\n"
            "It's you. Older. Tired. Running this exact simulation.\n"
            "\"Took you long enough,\" they say. \"Sit down. It's your turn to watch now.\"\n"
            "You were never the subject. You were always the Operator."
        ),
        "tone": "twist"
    },
    "ending_the_awakened": {
        "text": (
            "You knock on the nearest door. A stranger opens it, terrified — then relieved.\n"
            "One by one, doors open. For the first time, someone chose to look\n"
            "for others instead of just themselves.\n"
            "The facility's alarms mean nothing now. You are no longer alone."
        ),
        "tone": "good"
    },
    "ending_lost_forever": {
        "text": (
            "You run. And run. The corridor never ends, and every room looks the same.\n"
            "You escaped the box — into a bigger box.\n"
            "Freedom, it turns out, means nothing without anyone to share it with."
        ),
        "tone": "bad"
    },
    "ending_the_loop": {
        "text": (
            "The room resets again. And somehow, some small part of you already knew it would.\n"
            "This has happened before. You just don't remember how many times."
        ),
        "tone": "bad"
    },
    "ending_break_the_loop": {
        "text": (
            "Right as the reset takes hold, you refuse. You scream, fight, push back\n"
            "against the exact moment you always used to stay still.\n"
            "The loop stutters — and breaks. You're the first version of you to ever get this far."
        ),
        "tone": "good"
    }
}

TONE_BANNERS = {
    "good": "🏆 GOOD ENDING",
    "bad": "💀 BAD ENDING",
    "twist": "🌀 TWIST ENDING",
    "neutral": "⚪ ENDING"
}


def load_stats():
    default_stats = {"playthroughs": 0, "ignore_loop_count": 0, "endings_seen": []}
    
    if not os.path.exists(STATS_FILE):
        return default_stats
    
    try:
        with open(STATS_FILE, 'r') as f:
            stats = json.load(f)
        # ensure all keys exist
        for key, value in default_stats.items():
            if key not in stats:
                stats[key] = value
        return stats
    except (json.JSONDecodeError, FileNotFoundError):
        print("⚠️ Stats file looked corrupted, starting fresh.")
        return default_stats


def save_stats(stats):
    with open(STATS_FILE, 'w') as f:
        json.dump(stats, f, indent=2)


def slow_print(text, delay=0.015):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)
    print()


def get_choice(choices_dict):
    options = list(choices_dict.items())
    while True:
        print()
        for i, (label, _) in enumerate(options, start=1):
            print(f"  {i}. {label}")
        raw = input("\n> ").strip()
        try:
            index = int(raw) - 1
            if 0 <= index < len(options):
                return options[index][1]  # returns the next node key
        except ValueError:
            pass
        print("Invalid choice, try again.")


def play(stats):
    node_key = "start"

    while node_key not in ENDINGS:
        node = STORY[node_key]

        # special hidden branch: the loop remembers how many times you've stalled
        if node_key == "ignore_loop_check":
            stats["ignore_loop_count"] += 1
            count = stats["ignore_loop_count"]
            if count >= 3:
                node_key = "ending_the_loop"
                continue
            else:
                print()
                slow_print(f"(This is the {ordinal(count)} time you've chosen to do nothing.)")
                node_key = "ignore_it"
                continue

        print()
        slow_print(node["text"])
        node_key = get_choice(node["choices"])

    # reached an ending
    ending = ENDINGS[node_key]
    print("\n" + "═" * 60)
    slow_print(ending["text"])
    print("═" * 60)
    print(f"\n{TONE_BANNERS[ending['tone']]}")

    stats["playthroughs"] += 1
    if node_key not in stats["endings_seen"]:
        stats["endings_seen"].append(node_key)
        print(f"✨ New ending discovered! ({len(stats['endings_seen'])}/{len(ENDINGS)} found)")
    save_stats(stats)


def ordinal(n):
    if 11 <= n % 100 <= 13:
        return f"{n}th"
    return {1: f"{n}st", 2: f"{n}nd", 3: f"{n}rd"}.get(n % 10, f"{n}th")


def main():
    print("=" * 60)
    print("🌌 THE LAST SIGNAL")
    print("=" * 60)

    stats = load_stats()
    print(f"Playthroughs: {stats['playthroughs']}  |  "
          f"Endings found: {len(stats['endings_seen'])}/{len(ENDINGS)}")

    while True:
        choice = input("\n1. Begin\n2. Quit\n> ").strip()
        if choice == '1':
            play(stats)
        elif choice == '2':
            print("The signal fades. Goodbye. 👋")
            break
        else:
            print("Please enter 1 or 2")


if __name__ == "__main__":
    main()