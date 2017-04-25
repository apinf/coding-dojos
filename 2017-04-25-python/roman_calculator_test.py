# -*- coding: utf-8 -*-
import unittest


dictionary = {
 'I': 1,
 'II': 2,
 'III': 3,
}

reverseDictionary = {
  1: "I",
  2: "II",
  3: "III",
  4: "IV",
  5: "V",
}

def calculate(statement):
    parts = statement.split('+')
    firstNumber = dictionary[parts[0]]
    secondNumber = dictionary[parts[1]]
    answer = firstNumber + secondNumber 
    return reverseDictionary[answer]

class RomanCalculatorTest(unittest.TestCase):
    def testSumsIandIequalsII(self):
        expected = calculate('I + I')
        self.assertEquals(expected, 'II')
    def testSumsIandIIequalsII(self):
        expected = calculate('I + I')
        self.assertEquals(expected, 'II')
    def testSumsIIandIIequalsIV(self):
        expected = calculate('II + II')
        self.assertEquals(expected, 'IV')
    def testSumsIIandIIIequalsV(self):
        expected = calculate('II + III')
        self.assertEquals(expected, 'V')

if __name__ == '__main__':
    unittest.main()
