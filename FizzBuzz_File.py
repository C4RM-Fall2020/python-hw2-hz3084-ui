import numpy as np

def FizzBuzz(start, finish):

    nums = np.arange(start, finish + 1, dtype=object)

    fizz = (nums.astype(int) % 3 == 0)
    buzz = (nums.astype(int) % 5 == 0)

    nums[fizz & ~buzz] = "fizz"
    nums[buzz & ~fizz] = "buzz"
    nums[fizz & buzz] = "fizzbuzz"

    return nums.tolist()
