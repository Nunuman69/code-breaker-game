# Code Breaker Game

This is a Python-based implementation of the classic logic game **Code Breaker**.

## 🎯 Objective
The game challenges the player to guess a randomly generated 4-digit secret code (digits from 1 to 8, with possible repetitions). After each guess, the game provides feedback using:
- **X**: Correct digit in the correct position
- **O**: Correct digit in the wrong position

The goal is to crack the code within **10 attempts**.

## 🧠 Features
- Configurable code length, digit range, and max attempts
- Clear input validation with helpful error messages
- Feedback logic prioritizing exact matches (`X`) over partial matches (`O`)
- Full game history stored and displayed round-by-round
- Modular and object-oriented design using a single class: `CodeBreakerGame`

## 🗂️ File
- `CodeBreakerGame.py`: Main game script containing class definition and gameplay loop

## ▶️ How to Run
Make sure you have Python 3 installed. Then run:
```bash
python CodeBreakerGame.py
