# 1. Write a function named sum_to that accepts a single integer, n, and returns the sum of the integers from 1 to n.
# Use enumerables, reduce
# For example:

# sum_to(6)  # returns 21
# sum_to(10) # returns 55

def sum_to(n):
    return print(n * (n + 1) // 2)

sum_to(6)


# 2. Write a function named largest that takes a list of numbers as an argument and returns the largest number in that list.

# For example:

# largest([1, 2, 3, 4, 0])  # returns 4
# largest([10, 4, 2, 231, 91, 54])  # returns 231

def largest(nums):
    largest_num = 0
    for num in nums:
        if num > largest_num:
            largest_num = num
    return print(largest_num)
    
    
largest([1, 2, 42, 4, 12])


# 3. Write a function named occurances that takes two string arguments as input and counts the number of occurances of the second string inside the first string.

# For example:

# occurances('fleep floop', 'e')   # returns 2
# occurances('fleep floop', 'p')   # returns 2
# occurances('fleep floop', 'ee')  # returns 1
# occurances('fleep floop', 'fe')  # returns 0

def occurances(str, sub):
    count = 0
    for i in range(len(str)):
        if str[i:].startswith(sub):
         count += 1
    return print(count)
    
occurances('fleep floop', 'e')
occurances('fleep floop', 'p')
occurances('fleep floop', 'ee')
occurances('fleep floop', 'fe')

# 4. Write a function named product that takes an arbitrary number of numbers, multiplies them all together, and returns the product.
# (HINT: Review your notes on *args).

# For example:

# product(-1, 4) # returns -4
# product(2, 5, 5) # returns 50
# product(4, 0.5, 5) # returns 10.0

def product(init, *nums):
    prod = init
    for num in nums:
        prod *= num
    return print(prod)

product(-1, 4)
product(2, 5, 5)
product(4, 0.5, 5)
    