
import unittest
from scripts.lead_generation import LeadGeneration

class TestLeadGeneration(unittest.TestCase):

    def setUp(self):
        self.lead_gen = LeadGeneration()

    def test_generate_leads(self):
        leads = self.lead_gen.generate_leads()
        self.assertIsNotNone(leads)
        self.assertIsInstance(leads, list)

    def test_filter_leads(self):
        leads = ['Company1', 'Company2', 'Company3']
        filtered_leads = self.lead_gen.filter_leads(leads)
        self.assertIsNotNone(filtered_leads)
        self.assertIsInstance(filtered_leads, list)

if __name__ == '__main__':
    unittest.main()

