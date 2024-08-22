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

| Pokémon   | Speed | HP  | Type     | Moves                                                                                                                                                          |
|-----------|-------|-----|----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Charizard | 100   | 245 | Fire     | 1. Flare Blitz (Power: 90, Accuracy: 70, PP: 2) - Recoil: 33%                                                                                                  |
|           |       |     |          | 2. Dragon Rage (Power: 0.4, Accuracy: 90, PP: 5)                                                                                                               |
|           |       |     |          | 3. Wing Attack (Power: 60, Accuracy: 90, PP: 3)                                                                                                                |
|           |       |     |          | 4. Fire Fang (Power: 65, Accuracy: 85, PP: 5) - Burned: 30%                                                                                                    |
| Infernape | 108   | 242 | Fire     | 1. Mach Punch (Power: 40, Accuracy: 90, PP: 5)                                                                                                                 |
|           |       |     |          | 2. Flame Wheel (Power: 60, Accuracy: 90, PP: 5) - Burned: 10%                                                                                                  |
|           |       |     |          | 3. Fire Spin (Power: 35, Accuracy: 85, PP: 4)                                                                                                                  |
|           |       |     |          | 4. Acrobatics (Power: 55, Accuracy: 90, PP: 3)                                                                                                                 |
| Magmortar | 83    | 240 | Fire     | 1. Hyper Beam (Power: 90, Accuracy: 70, PP: 1)                                                                                                                 |
|           |       |     |          | 2. Fire Punch (Power: 75, Accuracy: 90, PP: 4) - Burned: 10%                                                                                                   |
|           |       |     |          | 3. Ember (Power: 40, Accuracy: 100, PP: 5)                                                                                                                     |
|           |       |     |          | 4. Lava Plume (Power: 80, Accuracy: 80, PP: 4) - Burned: 30%                                                                                                   |
| Leafeon   | 95    | 223 | Grass    | 1. Leaf Blade (Power: 90, Accuracy: 70, PP: 2)                                                                                                                 |
|           |       |     |          | 2. Synthesis (Power: 0, Accuracy: 100, PP: 4) - Regen: 33%                                                                                                     |
|           |       |     |          | 3. Quick Attack (Power: 40, Accuracy: 100, PP: 5)                                                                                                              |
|           |       |     |          | 4. Magical Leaf (Power: 60, Accuracy: 90, PP: 2)                                                                                                               |
| Decidueye | 70    | 245 | Grass    | 1. Sucker Punch (Power: 70, Accuracy: 90, PP: 3)                                                                                                               |
|           |       |     |          | 2. Razor Leaf (Power: 55, Accuracy: 95, PP: 3) - Critical Hit: 12.5%                                                                                           |
|           |       |     |          | 3. Peck (Power: 35, Accuracy: 90, PP: 5)                                                                                                                       |
|           |       |     |          | 4. Leafage (Power: 40, Accuracy: 90, PP: 4)                                                                                                                    |
| Venusaur  | 80    | 249 | Grass    | 1. Petal Blizzard (Power: 90, Accuracy: 70, PP: 1)                                                                                                             |
|           |       |     |          | 2. Tackle (Power: 40, Accuracy: 90, PP: 5)                                                                                                                     |
|           |       |     |          | 3. Vine Whip (Power: 45, Accuracy: 90, PP: 5)                                                                                                                  |
|           |       |     |          | 4. Take Down (Power: 90, Accuracy: 85, PP: 2)                                                                                                                  |
| Greninja  | 122   | 235 | Water    | 1. Water Pulse (Power: 60, Accuracy: 95, PP: 4)                                                                                                                |
|           |       |     |          | 2. Night Slash (Power: 70, Accuracy: 80, PP: 4)                                                                                                                |
|           |       |     |          | 3. Hydro Pump (Power: 90, Accuracy: 80, PP: 1)                                                                                                                 |
|           |       |     |          | 4. Quick Attack (Power: 40, Accuracy: 100, PP: 5)                                                                                                              |
| Gyarados  | 81    | 274 | Water    | 1. Twister (Power: 40, Accuracy: 100, PP: 5) - Flinch: 30%                                                                                                     |
|           |       |     |          | 2. Ice Fang (Power: 65, Accuracy: 95, PP: 4)                                                                                                                   |
|           |       |     |          | 3. Aqua Tail (Power: 90, Accuracy: 80, PP: 2)                                                                                                                  |
|           |       |     |          | 4. Blizzard (Power: 90, Accuracy: 70, PP: 2)                                                                                                                   |
| Blastoise | 78    | 247 | Water    | 1. Water Gun (Power: 40, Accuracy: 100, PP: 5)                                                                                                                 |
|           |       |     |          | 2. Bite (Power: 60, Accuracy: 90, PP: 4) - Flinch: 30%                                                                                                         |
|           |       |     |          | 3. Skull Bash (Power: 90, Accuracy: 90, PP: 2)                                                                                                                 |
|           |       |     |          | 4. Flash Cannon (Power: 80, Accuracy: 80, PP: 2)                                                                                                               |
| Moltres   | 90    | 290 | Fire     | 1. Gust (Power: 40, Accuracy: 100, PP: 5)                                                                                                                      |
|           |       |     |          | 2. Ancient Power (Power: 60, Accuracy: 90, PP: 4)                                                                                                              |
|           |       |     |          | 3. Incinerate (Power: 60, Accuracy: 90, PP: 2)                                                                                                                 |
|           |       |     |          | 4. Heat Wave (Power: 95, Accuracy: 80, PP: 1) - Burned: 10%                                                                                                   |
| Suicune   | 85    | 310 | Water    | 1. Extrasensory (Power: 80, Accuracy: 90, PP: 2) - Flinch: 10%                                                                                                 |
|           |       |     |          | 2. Surf (Power: 90, Accuracy: 90, PP: 2)                                                                                                                       |
|           |       |     |          | 3. Water Gun (Power: 40, Accuracy: 100, PP: 5)                                                                                                                 |
|           |       |     |          | 4. Facade (Power: 70, Accuracy: 90, PP: 2)                                                                                                                     |
| Ferrothorn| 20    | 258 | Grass    | 1. Metal Claw (Power: 50, Accuracy: 95, PP: 4)                                                                                                                 |
|           |       |     |          | 2. Power Whip (Power: 120, Accuracy: 80, PP: 2)                                                                                                                |
|           |       |     |          | 3. Knock Off (Power: 65, Accuracy: 90, PP: 3)                                                                                                                  |
|           |       |     |          | 4. Tackle (Power: 40, Accuracy: 100, PP: 5)                                                                                                                    |
| Raikou    | 115   | 290 | Electric | 1. Spark (Power: 65, Accuracy: 90, PP: 4)                                                                                                                       |
|           |       |     |          | 2. Zap Cannon (Power: 120, Accuracy: 80, PP: 1)                                                                                                                |
|           |       |     |          | 3. Thunder Shock (Power: 40, Accuracy: 100, PP: 5) - Flinch: 10%                                                                                               |
|           |       |     |          | 4. Extrasensory (Power: 80, Accuracy: 90, PP: 2)                                                                                                               |
| Manectric | 105   | 230 | Electric | 1. Thunder Fang (Power: 65, Accuracy: 90, PP: 4)                                                                                                               |
|           |       |     |          | 2. Spark (Power: 65, Accuracy: 90, PP: 4)                                                                                                                      |
|           |       |     |          | 3. Charge Beam (Power: 50, Accuracy: 90, PP: 4)                                                                                                                |
|           |       |     |          | 4. Shock Wave (Power: 60, Accuracy: 100, PP: 4)                                                                                                                |
| Electivire| 95    | 273        | Electric | 1. Thunder Punch (Power: 75, Accuracy: 95, PP: 4) - Paralyzed: 10%                                                                                             |
|           |       |               |          | 2. Low Kick (Power: 60, Accuracy: 100, PP: 5)                                                                                                                  |
|           |       |                |          | 3. Discharge (Power: 80, Accuracy: 100, PP: 3)                                                                                                                 |
|           |       |               |          | 4. Thunderbolt (Power: 90, Accuracy: 80, PP: 2)                                                                                                                |
| Zapdos    | 100   | 290        | Electric | 1. Thunder Shock (Power: 40, Accuracy: 100, PP: 5)                                                                                                             |
|           |       |     |            |          | 2. Drill Peck (Power: 80, Accuracy: 90, PP: 3)                                                                                                                 |
|           |       |     |            |          | 3. Agility (Power: 0, Accuracy: 100, PP: 3) - Speed Boost                                                                                                      |
|           |       |     |            |          | 4. Thunderbolt (Power: 90, Accuracy: 80, PP: 2)                                                                                                                |
| Tyranitar | 61    | 330       | Rock     | 1. Rock Slide (Power: 75, Accuracy: 90, PP: 4) - Flinch: 30%                                                                                                   |
|           |       |     |            |          | 2. Payback (Power: 50, Accuracy: 90, PP: 4)                                                                                                                    |
|           |       |     |            |          | 3. Bite (Power: 60, Accuracy: 90, PP: 4) - Flinch: 30%                                                                                                         |
|           |       |     |            |          | 4. Crunch (Power: 80, Accuracy: 100, PP: 3)                                                                                                                    |
| Lycanroc  | 82    | 272        | Rock     | 1. Stone Edge (Power: 100, Accuracy: 80, PP: 2)                                                                                                                |
|           |       |     |            |          | 2. Fire Fang (Power: 65, Accuracy: 95, PP: 4)                                                                                                                  |
|           |       |     |            |          | 3. Bite (Power: 60, Accuracy: 90, PP: 4) - Flinch: 30%                                                                                                         |
|           |       |     |            |          | 4. Thunder Fang (Power: 65, Accuracy: 90, PP: 4)                                                                                                               |
| Gigalith  | 25    | 308       | Rock     | 1. Smack Down (Power: 50, Accuracy: 100, PP: 5)                                                                                                                |
|           |       |     |            |          | 2. Rock Slide (Power: 75, Accuracy: 90, PP: 4) - Flinch: 30%                                                                                                   |
|           |       |     |            |          | 3. Explosion (Power: 100, Accuracy: 70, PP: 1)                                                                                                                 |
|           |       |     |            |          | 4. Earthquake (Power: 90, Accuracy: 90, PP: 2)                                                                                                                 |
| Rhyperior | 40    | 330       | Rock     | 1. Rock Wrecker (Power: 120, Accuracy: 70, PP: 1)                                                                                                              |
|           |       |     |            |          | 2. Bulldoze (Power: 60, Accuracy: 90, PP: 3)                                                                                                                   |
|           |       |     |            |          | 3. Stone Edge (Power: 100, Accuracy: 80, PP: 2)                                                                                                                |
|           |       |     |            |          | 4. Earthquake (Power: 90, Accuracy: 90, PP: 2)                                                                                                                 |


Each Pokémon has attributes such as speed, HP, current HP, type, and moves. Moves are defined by their power, accuracy, PP (power points), and any special effects.

---

Enjoy your Pokémon battles!
