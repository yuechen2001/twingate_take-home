class GameOfLife:
    def __init__(self, seed_file):
        self.seed = self.read_seed_file(seed_file)
        self.current_generation = self.seed
        self.generation_count = 0
        self.n_rows = len(self.seed)
        self.n_cols = len(self.seed[0])

    def reset(self):
        self.current_generation = self.seed
        self.generation_count = 0

    def simulate(self, n):
        for _ in range(n):
            new_grid = [[0] * self.n_cols for _ in range(self.n_rows)]
            for row in range(self.n_rows):
                for col in range(self.n_cols):
                    # Update status of the cell in the new generation based on number of live neighbours
                    live_neighbours = self.count_live_neighbours(row, col)
                    current_state = self.current_generation[row][col]
                    new_grid[row][col] = self.update_cell_state(
                        current_state, live_neighbours
                    )

            self.current_generation = new_grid.copy()
            self.generation_count += 1
            print("Generation", self.generation_count, ":")
            self.print_grid(self.current_generation)

    # Count the number of live neighbours for a given cell
    def count_live_neighbours(self, row, col):
        grid = self.current_generation
        directions = [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1),
            (1, 1),
            (-1, -1),
            (1, -1),
            (-1, 1),
        ]
        live_neighbours = 0

        for row_direction, col_direction in directions:
            new_row, new_col = row + row_direction, col + col_direction
            # Check if the neighbour is within the grid
            if 0 <= new_row < self.n_rows and 0 <= new_col < self.n_cols:
                live_neighbours += grid[new_row][new_col]

        return live_neighbours

    # Update the state of the cell based on the number of live neighbours
    def update_cell_state(self, current_state, live_neighbours):

        # Transition 1, 2, 3 applies to live cells
        if current_state == 1:
            if live_neighbours < 2 or live_neighbours > 3:
                return 0
            else:
                return 1
        # Transition 4 applies to dead cells
        else:
            if live_neighbours == 3:
                return 1
            else:
                return 0

    # Helper function to print the grid in terms of "X" for live cells and "_" for dead cells
    def print_grid(self, grid):
        for row in grid:
            print("".join(["X" if cell else "_" for cell in row]))
        print()

    # Helper function to read the seed file and convert it into a 2D list of 1s and 0s
    def read_seed_file(self, file_name):
        with open(file_name, "r") as file:
            lines = file.readlines()

        seed = []
        for line in lines:
            row = [1 if cell == "X" else 0 for cell in line.strip()]
            seed.append(row)

        return seed


if __name__ == "__main__":
    game = GameOfLife("seed.txt")

    print("Seed State (Generation 0):")
    game.print_grid(game.seed)

    print("10 Generations:")
    game.simulate(10)
