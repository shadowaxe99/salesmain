
import unittest
from scripts.email_generation import EmailGenerator

class TestEmailGeneration(unittest.TestCase):

    def setUp(self):
        self.email_generator = EmailGenerator()

    def test_generate_email(self):
        ceo_name = "John Doe"
        company_name = "Big Corp"
        email = self.email_generator.generate_email(ceo_name, company_name)
        self.assertIn(ceo_name, email)
        self.assertIn(company_name, email)

    def test_send_email(self):
        ceo_email = "john.doe@bigcorp.com"
        email_content = "Dear John Doe, ..."
        self.assertTrue(self.email_generator.send_email(ceo_email, email_content))

if __name__ == '__main__':
    unittest.main()

