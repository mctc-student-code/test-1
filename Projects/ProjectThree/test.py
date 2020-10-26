import validation
from unittest import TestCase

# class names use uppercase camel case
class TestValidation(TestCase):
    #Tests for extra spaces and title case
    def test_title_standardized(self):
        self.assertEqual('Here Is My Title', validation.standardize_title_format(" here is my title "))

    #Tests for extra spaces and title case with multiple inputs
    def test_artist(self):
        self.assertEqual('Jim Carter', validation.valid_artist(lambda x: "jim",lambda y: "carter"))
    
    #Tests for valid email
    def test_email(self):
        self.assertEqual('example@gmail.com', validation.valid_email(lambda x: " EXAMPLE@gmail.com"))

    #Tests for float more than 0
    def test_price(self):
        self.assertEqual(1, validation.valid_price(lambda x: 1))