import unittest
from solution import GameOfLife


class TestGameOfLife(unittest.TestCase):

    def setUp(self):
        # Test seed looks like this:
        # _X_
        # _X_
        # _X_
        self.game = GameOfLife("test_seed.txt")

    # Test count_live_neighbors for various cells in the seed
    def test_count_live_neighbors(self):
        print("Test count_live_neighbors for various cells in the seed")
        # (0,0) should have 2 live neighbors
        self.assertEqual(self.game.count_live_neighbors(self.game.seed, 0, 0), 2)

        # (0,1) should have 1 live neighbor
        self.assertEqual(self.game.count_live_neighbors(self.game.seed, 0, 1), 1)

        # (1,1) should have 2 live neighbors
        self.assertEqual(self.game.count_live_neighbors(self.game.seed, 1, 1), 2)

        # (2,2) should have 2 live neighbors
        self.assertEqual(self.game.count_live_neighbors(self.game.seed, 2, 2), 2)

        # (1,0) should have 3 live neighbors
        self.assertEqual(self.game.count_live_neighbors(self.game.seed, 1, 0), 3)

    # Test update_cell_state for various cells
    def test_update_cell_state(self):
        print("Test update_cell_state for various cells")
        # Test update_cell_state for live cells
        # A live cell with 2 live neighbors should survive
        self.assertEqual(self.game.update_cell_state(1, 2), 1)

        # A live cell with less than 2 live neighbors should die
        self.assertEqual(self.game.update_cell_state(1, 1), 0)

        # A live cell with more than 3 live neighbors should die
        self.assertEqual(self.game.update_cell_state(1, 4), 0)

        # Test update_cell_state for dead cells
        # A dead cell with exactly 3 live neighbors should become alive
        self.assertEqual(self.game.update_cell_state(0, 3), 1)

        # A dead cell with less than 3 live neighbors should remain dead
        self.assertEqual(self.game.update_cell_state(0, 2), 0)

        # A dead cell with more than 3 live neighbors should remain dead
        self.assertEqual(self.game.update_cell_state(0, 4), 0)

    # Test simulate for 1st generation
    def test_simulate(self):
        print("Test simulate for 1st generation")
        # Test simulation for 2nd generation
        expected_generation_2 = [[0, 0, 0], [1, 1, 1], [0, 0, 0]]
        self.game.simulate(1)
        self.assertEqual(self.game.current_generation, expected_generation_2)


if __name__ == "__main__":
    unittest.main()
