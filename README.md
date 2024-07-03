# Football Game Simulator

This repository contains a simple text-based football game simulator written in Python. The game allows you to play either a half (4 drives) or a full game (8 drives) against an opponent. You can choose between two difficulty levels: Easy or Hard.

## Gameplay

### Objective
The goal of the game is to outscore your opponent by strategically choosing plays (either passing or running) to gain yards and eventually score touchdowns or field goals.

### Mechanics
- **Drive Structure**: Each drive consists of up to 4 downs to move the ball a total of 75 yards down the field.
- **Play Options**: 
  - **Pass Plays**: Choose from a variety of pass plays like slants, hail mary, etc., each with different potential gains.
  - **Run Plays**: Opt for running plays such as inside run, quarterback sneak, etc., with varying yardage potential.
- **Outcome Determination**: After each play call, the game determines the success based on a success rate. There's also a chance of turnovers (interceptions or fumbles) which could end your drive.
- **Opponent Score**: After your drive, the opponent may also score based on the game difficulty chosen (Easy or Hard).

### Winning
- The game concludes after all drives are completed.
- The team with the higher score wins. If scores are tied, the game results in a tie.

## Getting Started

### Prerequisites
- Python 3.x
- `coolconsole` library (for colored console output)

### Installation
1. Clone this repository to your local machine.
2. Install the required dependencies:
   ```bash
   pip install coolconsole
   ```

### Running the Game
1. Navigate to the cloned repository directory.
2. Run the game script:
   ```bash
   python football_game.py
   ```
3. Follow the on-screen prompts to choose the game duration (half or full game) and difficulty level (Easy or Hard).

## Authors
- Tanish Gupta

## License
This project is licensed under the MIT License - see the LICENSE.md file for details.

## Acknowledgments
- This game was inspired by a passion for football and text-based simulations.
- Hat tip to anyone whose code was used or who provided inspiration.

---

Feel free to customize and expand upon this game as you see fit! Happy gaming! 🏈