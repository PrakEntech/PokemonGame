# Pokémon Battle Game

Welcome to the Pokémon Battle Game! This game allows you to engage in a strategic turn-based battle between various Pokémon. The gameplay involves choosing your Pokémon, selecting their moves, and battling against a rival Pokémon with the aim of defeating them by reducing their HP to zero.

## Table of Contents

- [Features](#features)
- [Game Mechanics](#game-mechanics)
- [Installation](#installation)
- [How to Play](#how-to-play)
- [Pokémon Data](#pokémon-data)

## Features

- **Multiple Pokémon**: Play with a selection of 20 Pokémon from different types (Fire, Water, Grass, Electric, Rock).
- **Move Sets**: Each Pokémon has a unique set of moves with various power, accuracy, and additional effects like recoil, burn, or flinch.
- **Type Advantage**: Battle outcomes can be influenced by type advantages, adding a layer of strategy.
- **Randomized Battles**: Pokémon are selected randomly for you and your rival, making each game unique.

## Game Mechanics

- **Turn-Based Combat**: The game is turn-based, where you and your rival Pokémon take turns to attack.
- **Type Advantage**: Certain Pokémon types have advantages or disadvantages against others, affecting the damage dealt.
- **Random Effects**: Moves may have additional effects such as causing the opponent to flinch or your Pokémon to suffer recoil damage.

## Installation

To play the Pokémon Battle Game, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/PrakEntech/PokemonGame.git
   ```
2. **Navigate to the Game Directory**:
   ```bash
   cd PokemonGame
   ```
3. **Run the Game**:
   ```bash
   python3 game.py
   ```

## How to Play

1. **Starting the Game**: Run the game script to start.
2. **Main Menu**: Choose from the following options:
   - **0**: Start a new game.
   - **1**: List all available Pokémon.
   - **2**: Exit the game.
3. **Select Pokémon**: After starting a new game, you and your rival will be randomly assigned three Pokémon each.
4. **Battle**: Choose your Pokémon and attack moves strategically to defeat your rival's Pokémon.
5. **Win Condition**: The game ends when all three of either player's Pokémon are defeated.

## Pokémon Data

The Pokémon data is stored in the `pokemondata.py` file and includes the following Pokémon:

- **Fire Type**: Charizard, Infernape, Magmortar, Moltres
- **Water Type**: Blastoise, Gyarados, Greninja, Suicune
- **Grass Type**: Venusaur, Leafeon, Decidueye, Ferrothorn
- **Electric Type**: Raikou, Manectric, Electivire, Zapdos
- **Rock Type**: Tyranitar, Lycanroc, Gigalith, Rhyperior

Each Pokémon has attributes such as speed, HP, current HP, type, and moves. Moves are defined by their power, accuracy, PP (power points), and any special effects.

---

Enjoy your Pokémon battles!
