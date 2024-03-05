# Game of Life Solution! 

## Setting up 

1. Download the zipped files to your local device. 
2. Unzip the files into a new folder.
3. Open your favourite code editor. Using the terminal, `cd` into the folder above and move on to the next step! 

## Simulate
To simulate the Game of Life, use the following command in your terminal: 
```
python solution.py
```
To run the tests, use the following command in your terminal:
```
python -m unittest tests.py
```

## Documentations 
I wrote GameOfLife as a Python class, and here are the descriptions of important attributes and methods: 
### Attributes 
- `seed`: The starting state of the Game of Life, as given in the instructions. 
- `current_generation`: The current state of the Game of Life. 
### Methods
- `simulate(n)`: The main function that generates a new generation from the old generation. The function will run n number of times to simulate n rounds of the Game of Life.
- `count_live_neighbours(row, col)`: This function takes in the (row, column) coordinates of the current cell, and count the number of live neighbours that are around it, as statetd in the instructions. 
- `update_cell_state(row, col, live_neighbours)`: This function takes in the (row, column) coordinates of the current cell, and the number of live neighbours around it. It checks the state of the current cell, and updates its next state based on the number of live neighbours and its current state. 
- `print_grid(grid)`: This helper function takes in the current state of the grid, converts '1' to 'X' and '0' to '_', and prints the grid of the current generation. 
- `read_seed_file`: This helper function helps to read the seed file given,  converts 'X' to '1' and '0' to '_', and stores the starting state of the Game of Life. 
