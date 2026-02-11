# Turtle Race Game

A fun, interactive Python game built using the `turtle` graphics library. Place your bet and watch the turtles race!

## 🎮 How it Works

1.  **Place Your Bet**: When the game starts, a popup will ask you to bet on a turtle color (`red`, `orange`, `yellow`, `green`, `blue`, or `purple`).
2.  **The Race**: Six turtles line up at the starting position and race across the screen.
3.  **Randomized Movement**: Each turtle moves forward by a random distance (0-10 pixels) in each step, making the outcome unpredictable!
4.  **Winner**: The first turtle to cross the finish line (x-coordinate 230) is declared the winner.
5.  **Result**: The game prints the winning color and whether you won or lost your bet to the console.

## 🚀 Getting Started

### Prerequisites

- Python 3.x
- `turtle` module (standard library)

### Running the Game

Simply run the `main.py` script:

```bash
python main.py
```

## 🛠️ Implementation Details

- **Visuals**: Uses the `turtle` module for rendering animations and the game window.
- **Logic**: Implements a simple game loop that continues until a turtle crosses the finish line.
- **Randomness**: Utilizes the `random` module to decide turtle speed.
