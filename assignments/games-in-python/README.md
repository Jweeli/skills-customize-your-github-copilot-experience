```markdown
# 📘 Assignment: Hangman (Games in Python)

## 🎯 Objective

Build a playable Hangman word-guessing game in Python to practice string handling, loops, conditionals, and user input.

## 📝 Tasks

### 🛠️ Core: Build the Hangman Game

#### Description
Implement the core Hangman gameplay: word selection, guess processing, progress display, and win/lose conditions.

#### Requirements
Completed program should:

- Randomly select a word from the provided word list or `starter-code.py`.
- Prompt the player for single-letter guesses and validate input (letters only, single character).
- Reveal correctly guessed letters in a `_ _ a _ _` style display.
- Track and display the number of incorrect guesses remaining.
- Prevent repeated guesses from decrementing remaining attempts.
- End the game when the word is fully guessed or attempts are exhausted and show a clear win/lose message.


### 🛠️ Enhancements (Optional)

#### Description
Add optional features to improve user experience and replayability.

#### Suggestions

- Add ASCII-art hangman stages that update with each wrong guess.
- Support difficulty levels (e.g., Easy/Medium/Hard) that adjust allowed attempts or word pools.
- Allow whole-word guesses as a bonus action.
- Persist simple high scores or wins in a local file.

## 🔧 Starter Files

- `starter-code.py` — starter scaffold and sample word list.

## ✅ Submission

- Provide a working `.py` file runnable with Python 3.8+.
- Include brief usage instructions at the top of your file or a short `USAGE` section in this README.

```
