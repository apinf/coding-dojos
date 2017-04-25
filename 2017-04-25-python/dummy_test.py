import unittest


class DummyTest(unittest.TestCase):
    def testDummy(self):
        self.assertEquals(2, 1+1)


if __name__ == '__main__':
    unittest.main()
