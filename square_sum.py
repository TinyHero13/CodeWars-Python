"""Complete the square sum function so that it squares each number passed into it and then sums the results together.
For example, for [1, 2, 2] it should return 9 because 1^2 + 2^2 + 2^2 = 9."""
import random, unittest

"""lst = []
for i in range(6):
    lst.append(random.randint(0,22))
"""

def square_sum(numbers):
    sum = 0
    for i in numbers:
        multi = i * i
        sum += multi
    return sum

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(square_sum([0, 3, 4, 5]), 50)

if __name__ == '__main__':
    unittest.main()