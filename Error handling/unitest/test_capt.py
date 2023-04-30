import unittest
import capt

class Testcap(unittest.TestCase):
    def test_one_word(self):
        text='python'
        result=capt.capt_text(text)
        self.assertEqual(result,'Python')
    
    def test_multiple_word(self):
        text='Monty python'
        result=capt.capt_text(text)
        self.assertEqual(result,'Monty Python')

if __name__=='__main__':
    unittest.main( )
