# Exercise 23 (and Solution)
#
# Given two .txt files that have lists of numbers in them, find the numbers that are overlapping.
# One .txt file has a list of all prime numbers under 1000, and the other .txt file has a list of
# happy numbers up to 1000.
#
# (If you forgot, prime numbers are numbers that can’t be divided by any other number.
# And yes, happy numbers are a real thing in mathematics - you can look it up on Wikipedia.
# The explanation is easier with an example, which I will describe below.)

with open("primenumbers.txt", "r") as prime_nums, open("happynumbers.txt", "r") as happy_nums:
    primes = prime_nums.read().split()
    happys = happy_nums.read().split()
    overlap = [i for i in primes if i in happys]

print(overlap)