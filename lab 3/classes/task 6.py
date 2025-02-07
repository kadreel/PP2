class PrimeFilter:
    def __init__(self, numbers):
        self.numbers = numbers

    def is_prime(self, num):
        if num < 2:                                                                 #1 can't be prime, that's obvious
            return False
        for i in range(2, int(num**0.5) + 1):                                       #ngl I googled the formula
            if num % i == 0:
                return False
        return True

    def filter_primes(self):
        prime_numbers = list(filter(lambda x: self.is_prime(x), self.numbers))      #lambda starts the loop, filter only returns the numbers that get true from is_prime, list turns prime_numbers into a list made out of filtered stuff
        return prime_numbers

# EXAMPLE:

numbers = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33]
prime_filter = PrimeFilter(numbers)
print(f"Prime numbers in the list: {prime_filter.filter_primes()}")                 #Output: Prime numbers in the list: [3, 5, 7, 11, 13, 17, 19, 23, 29, 31]