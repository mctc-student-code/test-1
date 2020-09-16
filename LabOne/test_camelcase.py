import camelcase
from unittest import TestCase

class TestCamelCase(TestCase):
    def test_camelcase_sentence(self):

        #Checks for empty space inbetween sentence and correct capitilization
        self.assertEqual('helloWorld', camelcase.convertSentence('Hello World'))

        #Test if userInput starts, ends, or even just had empty space between words.
        self.assertEqual('helloWorld', camelcase.convertSentence('    Hello   World   '))
        
        '''
        #Checks for special characters, this is already taken care of by the method
        self.assertEqual('', camelcase.convertSentence('%$#%&^%'))

        #Method already checks for empty string
        self.assertEqual('', camelcase.convertSentence(''))
        '''