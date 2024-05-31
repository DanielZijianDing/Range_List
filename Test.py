import unittest
from Range_List import range_list

class TestFunction(unittest.TestCase):
    def test_1(self):
        X = range_list()
        X.add(10, 30, 1)
        X.add(20, 40, 1)
        X.add(10, 40, -2)
        self.assertEqual(X.result(), [[10.0, -1], [20.0, 0], [30.0, -1], [40.0, 0]])
    def test_2(self):
        X = range_list()
        X.add(10, 30, 1)
        X.add(20, 40, 1)
        X.add(10, 40, -1)
        X.add(10, 40, -1)
        self.assertEqual(X.result(), [[10.0, -1], [20.0, 0], [30.0, -1], [40.0, 0]])
    def test_3(self):
        X = range_list()
        X.set(10, 30, 1)
        X.add(20, 40, 1)
        X.set(10, 40, -1)
        X.add(10, 40, -1)
        self.assertEqual(X.result(), [[10.0, -2], [40.0, 0]])

if __name__ == '__main__':
    #import time
    #start = time.time()
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
    #print(f'runtime: {time.time() - start:.20f}')