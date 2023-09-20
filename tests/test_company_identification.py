
import unittest
from scripts import company_identification

class TestCompanyIdentification(unittest.TestCase):

    def setUp(self):
        self.company_identification = company_identification.CompanyIdentification()

    def test_identify_companies(self):
        companies = self.company_identification.identify_companies('data/companies.csv')
        self.assertIsInstance(companies, list)
        self.assertGreater(len(companies), 0)

    def test_identify_biggest_companies(self):
        companies = self.company_identification.identify_companies('data/companies.csv')
        biggest_companies = self.company_identification.identify_biggest_companies(companies)
        self.assertIsInstance(biggest_companies, list)
        self.assertGreater(len(biggest_companies), 0)

if __name__ == '__main__':
    unittest.main()

