import unittest
from solution import GameOfLife


class TestGameOfLife(unittest.TestCase):

    def setUp(self):
        # Test seed looks like this:
        # _X_
        # _X_
        # _X_
        self.game = GameOfLife("test_seed.txt")

    # Test read_seed_file
    def test_read_seed_file(self):
        print("Testing read_seed_file")
        expected_seed = [[0, 1, 0], [0, 1, 0], [0, 1, 0]]
        self.assertEqual(self.game.read_seed_file("test_seed.txt"), expected_seed)

        # Test whether the lengths of rows and columns are correct
        self.assertEqual(self.game.n_rows, 3)
        self.assertEqual(self.game.n_cols, 3)

    # Test count_live_neighbours for various cells in the seed
    def test_count_live_neighbours(self):
        print("Testing count_live_neighbours for various cells in the seed")
        # (0,0) should have 2 live neighbours
        self.assertEqual(self.game.count_live_neighbours(0, 0), 2)

        # (0,1) should have 1 live neighbor
        self.assertEqual(self.game.count_live_neighbours(0, 1), 1)

        # (1,1) should have 2 live neighbours
        self.assertEqual(self.game.count_live_neighbours(1, 1), 2)

        # (2,2) should have 2 live neighbours
        self.assertEqual(self.game.count_live_neighbours(2, 2), 2)

        # (1,0) should have 3 live neighbours
        self.assertEqual(self.game.count_live_neighbours(1, 0), 3)

    # Test update_cell_state for various cells
    def test_update_cell_state(self):
        print("Testing update_cell_state for various cells")
        # Test update_cell_state for live cells
        # A live cell with 2 live neighbours should survive
        self.assertEqual(self.game.update_cell_state(1, 2), 1)

        # A live cell with less than 2 live neighbours should die
        self.assertEqual(self.game.update_cell_state(1, 1), 0)

        # A live cell with more than 3 live neighbours should die
        self.assertEqual(self.game.update_cell_state(1, 4), 0)

        # Test update_cell_state for dead cells
        # A dead cell with exactly 3 live neighbours should become alive
        self.assertEqual(self.game.update_cell_state(0, 3), 1)

        # A dead cell with less than 3 live neighbours should remain dead
        self.assertEqual(self.game.update_cell_state(0, 2), 0)

        # A dead cell with more than 3 live neighbours should remain dead
        self.assertEqual(self.game.update_cell_state(0, 4), 0)

    # Test simulate for generations 1, 2 and 3 to check if the game is working as expected
    def test_simulate(self):
        print("Testing simulate for 1st generation")
        expected_generation_1 = [[0, 0, 0], [1, 1, 1], [0, 0, 0]]
        self.game.simulate(1)
        self.assertEqual(self.game.current_generation, expected_generation_1)

        print("Testing simulate for 2nd generation")
        expected_generation_2 = [[0, 1, 0], [0, 1, 0], [0, 1, 0]]
        self.game.simulate(1)
        self.assertEqual(self.game.current_generation, expected_generation_2)

        print("Testing simulate for 3rd generation")
        # Test simulation for 3rd generation
        expected_generation_3 = [[0, 0, 0], [1, 1, 1], [0, 0, 0]]
        self.game.simulate(1)
        self.assertEqual(self.game.current_generation, expected_generation_3)


if __name__ == "__main__":
    unittest.main()
