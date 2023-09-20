
import unittest
from scripts import data_preprocessing

class TestDataPreprocessing(unittest.TestCase):

    def setUp(self):
        self.data_preprocessor = data_preprocessing.DataPreprocessor()

    def test_clean_data(self):
        raw_data = {"name": ["Company1 ", " Company2", "Company3"], "sector": [" IT", "Healthcare ", " Finance"]}
        expected_output = {"name": ["Company1", "Company2", "Company3"], "sector": ["IT", "Healthcare", "Finance"]}
        self.assertEqual(self.data_preprocessor.clean_data(raw_data), expected_output)

    def test_split_data(self):
        data = {"name": ["Company1", "Company2", "Company3", "Company4", "Company5"], "sector": ["IT", "Healthcare", "Finance", "Retail", "Manufacturing"]}
        train_data, test_data = self.data_preprocessor.split_data(data, test_size=0.2)
        self.assertEqual(len(train_data), 4)
        self.assertEqual(len(test_data), 1)

if __name__ == '__main__':
    unittest.main()
