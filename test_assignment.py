import unittest
from assignment import load_movie_data, add_profit_column, print_min_and_max_profit

class TestMovieProfitAnalysis(unittest.TestCase):

    def setUp(self):
        self.sample_data = [
            ["2023-01-01", "Sample Movie 1", 100000, 200000],
            ["2023-01-02", "Sample Movie 2", 150000, 100000],
            ["2023-01-03", "Sample Movie 3", 120000, 300000],
        ]

    def test_add_profit_column(self):
        add_profit_column(self.sample_data)
        expected_profits = [100000, -50000, 180000]
        for i, row in enumerate(self.sample_data):
            self.assertEqual(row[-1], expected_profits[i])

    def test_min_and_max_profit(self):
        add_profit_column(self.sample_data)
        min_profit_movie = min(self.sample_data, key=lambda x: x[-1])
        max_profit_movie = max(self.sample_data, key=lambda x: x[-1])
        
        self.assertEqual(min_profit_movie[1], "Sample Movie 2")
        self.assertEqual(max_profit_movie[1], "Sample Movie 3")

if __name__ == "__main__":
    unittest.main()