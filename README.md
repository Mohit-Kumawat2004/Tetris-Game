# 🎮 Tetris Game in Python 🎮

Welcome to the **Tetris Game** built with **Python** 🐍! This game uses **Pygame** for graphics and provides an interactive, fun way to play the classic **Tetris**. The game logic is implemented using Python classes and functions, with blocks falling from the top and the player rotating and moving them to complete lines.

## 🛠️ Features:
- **Block Movement**: Move and rotate the blocks using keyboard inputs ⬆️⬇️⬅️➡️.
- **Speed Control**: Speed of falling blocks increases as the game progresses 🕹️.
- **Scoring System**: Earn points for every line completed 💯.
- **Game Over**: The game ends when blocks stack up to the top of the screen ⚰️.
  
## 📂 File Descriptions:

- **`block.py`**: Contains the block shapes and their rotation logic 🧩.
- **`blocks.py`**: Manages the different shapes and types of blocks that can fall in the game 🔲.
- **`colors.py`**: Defines the colors for each block, making the game visually appealing 🌈.
- **`game.py`**: Contains the game logic and control mechanisms for gameplay 🏁.
- **`grid.py`**: Responsible for the grid where the blocks fall and lines are cleared 🟥🟩🟦.
- **`main.py`**: The entry point for the game that initializes the game window and loop 🖥️.
- **`position.py`**: Handles the positioning and collision detection of blocks 🧭.

## 🖼️ Output Images:

1. **Tetris Gameplay**  
   ![Gameplay](https://github.com/Mohit-Kumawat2004/Tetris-Game/blob/main/Output%20Images/In-Game%202.png)

2. **Tetris Game About**  
   ![About Game Over](https://github.com/Mohit-Kumawat2004/Tetris-Game/blob/main/Output%20Images/About.png)

3. **Tetris Block Shapes**  
   ![Block Shapes](https://github.com/Mohit-Kumawat2004/Tetris-Game/blob/main/Output%20Images/UI.png)

## 📅 Recent Updates:
- **Last Week**:
    - **`block.py`**: Improved block rotation logic 🔄.
    - **`blocks.py`**: Added new block shapes to diversify gameplay 🧩.
    - **`colors.py`**: Updated color palette to make the game more vibrant 🌈.
    - **`game.py`**: Fixed issues with line clearing and added sound effects 🎶.
    - **`grid.py`**: Optimized grid rendering for smoother gameplay 🕹️.
    - **`main.py`**: Added difficulty levels for increased challenge 🎮.
    - **`position.py`**: Enhanced collision detection and block placement accuracy 🔒.

## ⚙️ Installation Instructions:
1. **Clone the Repository**:
    ```bash
    git clone https://github.com/your-username/tetris-game-python.git
    ```

2. **Install Dependencies**:
    - Install the required libraries, including **Pygame**:
    ```bash
    pip install pygame
    ```

3. **Run the Game**:
    ```bash
    python main.py
    ```

## 🎮 Controls:
- **Move Left**: Press the **Left Arrow** key ⬅️.
- **Move Right**: Press the **Right Arrow** key ➡️.
- **Rotate**: Press the **Up Arrow** key ⬆️.
- **Move Down**: Press the **Down Arrow** key ⬇️.
- **Pause**: Press **P** to pause the game ⏸️.

## 🏆 Scoring System:
- **Line Cleared**: You earn points for every line cleared. More lines = higher score! 💥
- **Combo**: Clear multiple lines at once for bonus points ✨.
- **Game Over**: The game ends when the blocks stack up to the top of the screen ⚰️.

## 💡 How to Play:
1. Blocks fall from the top of the grid.
2. Use the arrow keys to move the blocks into place.
3. Complete horizontal lines to clear them and earn points.
4. The game speeds up as you progress — can you keep up? ⏳

## 📑 Contributing:
We welcome contributions! If you’d like to contribute, follow these steps:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-name`).
3. Commit your changes (`git commit -am 'Add feature'`).
4. Push to your branch (`git push origin feature-name`).
5. Create a new Pull Request.

## 📝 License:
This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.
