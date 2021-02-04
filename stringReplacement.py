"""
Trolls are attacking your comment section!

A common way to deal with this situation is to remove all of the vowels from the trolls' comments, neutralizing the threat.

Your task is to write a function that takes a string and return a new string with all vowels removed.

For example, the string "This website is for losers LOL!" would become "Ths wbst s fr lsrs LL!".
"""

import unittest

def disemvowel(string):
    for i in "aeiouAEIOU": 
        string = string.replace(i,'')
    return string

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(disemvowel("This website is for losers LOL!"),"Ths wbst s fr lsrs LL!")

if __name__ == '__main__': 
    unittest.main() 