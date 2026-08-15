🪨📄✂️ Rock-Paper-Scissors-Lizard-Spock

A terminal-based Rock-Paper-Scissors game — extended to the 5-option Rock-Paper-Scissors-Lizard-Spock variant, with best-of-N matches and persistent stats.

Features
🖐 Full Rock-Paper-Scissors-Lizard-Spock rule set (5 choices instead of 3)
🏆 Best-of-3 / 5 / 7 match format — first to majority round wins takes the match
📊 Persistent stats — total matches played and match win/loss record saved to stats.json, shown on launch
🛡 Input validation — typos or invalid choices just re-prompt instead of crashing
Rules

Each choice beats exactly two others:

Choice	Beats
Rock	Scissors, Lizard
Paper	Rock, Spock
Scissors	Paper, Lizard
Lizard	Paper, Spock
Spock	Rock, Scissors

Win logic is driven by a single lookup dictionary (RULES) rather than a long if/elif chain — this is what makes the game logic scale cleanly from classic 3-choice RPS to the 5-choice variant without rewriting anything, just extending the rule map.

Example
🪨📄✂️ Welcome to Rock-Paper-Scissors-Lizard-Spock!
Matches played: 2 (You: 1  |  Computer: 1)

1. Play a match
2. Quit
> 1
Best of how many rounds? (3/5/7): 3

Match started — first to 2 round wins takes it!

--- Round 1 ---
Choose (rock/paper/scissors/lizard/spock): spock
You chose spock, I chose rock.
✅ Spock beats rock. You win this round!
Score — You: 1  |  Computer: 0

Possible Improvements
Track per-choice stats (which choice wins most often for the player)
Add a "best of" streak/tournament mode across multiple matches
GUI or web version with clickable icons instead of typed input
AI opponent that adapts based on player's most frequent choice
Author

Built by Kirithik as part of a personal Python mini-projects collection.