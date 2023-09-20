
import unittest
from scripts import model_training

class TestModelTraining(unittest.TestCase):

    def setUp(self):
        self.model_trainer = model_training.ModelTrainer()

    def test_train_lead_generation_model(self):
        data = self.model_trainer.load_data('data/leads.csv')
        model = self.model_trainer.train_lead_generation_model(data)
        self.assertIsNotNone(model)

    def test_train_company_identification_model(self):
        data = self.model_trainer.load_data('data/companies.csv')
        model = self.model_trainer.train_company_identification_model(data)
        self.assertIsNotNone(model)

if __name__ == '__main__':
    unittest.main()

