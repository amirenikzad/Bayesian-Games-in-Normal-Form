
# Bayesian Games in Normal Form

## Overview
Bayesian Games are a type of game theory model where players make decisions based on incomplete information about other players. Unlike classical games, where all information is common knowledge, Bayesian games involve situations where players possess private information (also known as types). This uncertainty is modeled using probability distributions over different possible states.

### Normal Form
In the context of normal form Bayesian games, the game is represented in a matrix where each player chooses strategies simultaneously without knowing the strategies chosen by the others. The payoffs depend not only on the chosen strategies but also on the types of the players.

---
![Bayesian Games in Normal Form](https://github.com/user-attachments/assets/99b54874-6532-4542-bdfa-f679d68d3683)

## Code Overview

### Tech Stack
- **Python**: Core programming language.
- **Tkinter**: Used for creating the GUI (Graphical User Interface).
- **Pillow (PIL)**: For handling images in the application.

### Code Functionality
The code creates an interactive graphical interface to simulate a Bayesian game in normal form. The user can input different values, representing the nature of the game and strategies of two players (p1 and p2), and observe the calculated payoffs.

Key components:
- **Nature Probabilities**: The code allows users to define "nature" probabilities, which represent uncertainty in the game.
- **Payoff Calculation**: Payoffs are calculated based on user inputs for each player's strategies and the nature probabilities.
- **Interactive Matrix**: The interface is set up as a grid where users can input and modify values, and the results update dynamically.

### How It Works
1. **Entry Widgets**: Users input strategy values for each player and nature probabilities.
2. **Dynamic Calculation**: When values are updated, the payoffs for each possible outcome are recalculated and displayed in real-time.
3. **Graphical Interface**: Tkinter is used to create a visual representation of the Bayesian game in a matrix form, providing an easy-to-use interface for experimenting with different inputs.

### Example Interface
The GUI provides labeled entries for player strategies, payoff outcomes, and nature values. The payoffs are updated based on the current inputs, and results are displayed dynamically in matrix form.

---

## How to Run

1. Ensure you have Python installed on your machine.
2. Install the required libraries:
    ```bash
    pip install tkinter pillow
    ```
3. Run the script:
    ```bash
    python BayesianGames.py
    ```

The GUI will launch, allowing you to interact with the Bayesian game model.

---
