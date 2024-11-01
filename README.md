# 8-Puzzle Solver

This project implements an agent to solve the classic **8-puzzle game** using both informed and uninformed search algorithms. It was completed as **Assignment 1** for the Artificial Intelligence course in the Computer and Systems Engineering program at Alexandria University.

[![GUI Demo](https://img.youtube.com/vi/kAQtM2uQznk/0.jpg)](https://youtu.be/kAQtM2uQznk)

## Overview

The 8-puzzle game involves a 3x3 board with 8 numbered, movable tiles and an empty space (represented as `0`). The objective is to reach the goal state, where all tiles are arranged in ascending order from `0` to `8`, by sliding tiles into the empty space. The agent uses various search algorithms to explore possible moves and identify the sequence that leads to the goal state with minimal cost.

## Features

- **Graphical User Interface (GUI)** to visualize the solution steps and path cost
  - Screenshots of the interface can be found [here](https://ibb.co/vcyzxq2) and [here](https://ibb.co/0Fk0ynt).
  - Full video demo on [YouTube](https://youtu.be/kAQtM2uQznk)
- **Configurable Initial States**: Start the puzzle from any randomized configuration.
- **Performance Analysis**: Measures nodes expanded, search depth, and path cost for each algorithm.

## Search Algorithms Implemented

1. **Breadth-First Search (BFS)** - Explores all nodes level by level to ensure an optimal solution.
2. **Depth-First Search (DFS)** - Searches paths to the deepest level before backtracking.
3. **Iterative Deepening DFS (IDDFS)** - Combines depth-limited DFS with progressive deepening for guaranteed solution within a set limit.
4. **A\*** - Utilizes heuristics to estimate the cost to the goal and prioritize efficient paths.

## Heuristics for A* Search

1. **Manhattan Distance**  
   Sum of the absolute differences between each tile’s coordinates and their goal positions.

2. **Euclidean Distance**  
   Straight-line distance between each tile’s position and its goal position.

## Project Structure

- **GUI Implementation**: Displays the initial and goal states and traces each move made by the search algorithm.
- **Algorithms**: Contains implementations of BFS, DFS, IDDFS, and A* with the Manhattan and Euclidean heuristics.
- **Performance Metrics**: Reports the path to goal, total moves (path cost), nodes expanded, search depth, and run time for each algorithm.

## Usage

1. Set the initial state of the puzzle board.
2. Run the program to see the solution steps, generated path, and performance metrics.

## License

This project was developed as an educational exercise. Please refer to the course guidelines and academic integrity policies if adapting any part of this code.
