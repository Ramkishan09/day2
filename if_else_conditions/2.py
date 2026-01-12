# Variables & Data Types (int, float, str, bool)

# Swap the values of two variables without using a third variable. → Intermediate
# Take user input for name (str), age (int), height (float), and print them with their data types. → Beginner
# Convert a float to int and observe what happens (truncation). → Beginner
# Check if a number is even or odd using boolean. → Beginner
# Take a temperature in Celsius (float) and convert it to Fahrenheit. → Beginner
# Create variables of different types and print their types using type(). → Beginner
# Take a string input and convert it to uppercase/lowercase. → Beginner
# Check if a given year is a leap year (use boolean logic). → Intermediate
# Calculate the area of a circle given radius (float) and print with 2 decimal places. → Beginner
# Take two boolean inputs and demonstrate AND, OR, NOT operations. → Beginner
# Store a person's details (name str, age int, is_student bool) and print a sentence. → Beginner
# Take an integer input and check if it's positive, negative, or zero. → Beginner
# Convert a string representing a number to int/float and perform addition. → Intermediate
# Create a boolean variable for "is_raining" and print appropriate message. → Beginner
# Calculate BMI given weight (float) and height (float), and print the result. → Beginner

# Lists, Tuples, Sets, Dictionaries

# Create a list of numbers and find its sum, max, min. → Beginner
# Append, remove, and insert elements in a list. → Beginner
# Create a tuple of fruits and try to modify it (observe immutability). → Beginner
# Convert a list to a tuple and vice versa. → Beginner
# Create a set of numbers and add/remove elements (observe no duplicates). → Beginner
# Find intersection and union of two sets. → Intermediate
# Create a dictionary of student names and scores, then add/update entries. → Beginner
# Iterate over a dictionary and print keys and values. → Beginner
# Count frequency of elements in a list using a dictionary. → Intermediate
# Remove duplicates from a list using a set. → Intermediate
# Create a list of tuples with (name, age) and sort by age. → Intermediate
# Unpack a tuple into variables. → Beginner
# Check if a key exists in a dictionary. → Beginner
# Merge two dictionaries. → Intermediate
# Create a shopping list (list) and remove bought items. → Beginner
# Store coordinates as tuples in a list and calculate distances. → Advanced
# Use a set to find unique words in a sentence. → Intermediate
# Create a phonebook dictionary and search for contacts. → Intermediate
# Reverse a list without using reverse(). → Intermediate
# Find common elements in two lists using sets. → Intermediate

# Conditional Statements (if-else)

# Check if a number is positive, negative, or zero. → Beginner
# a=int(input("Enter the number here for number test:"))
# if a==0:
#     print("The Number is zero")
# elif a>0:
#     print("The number is positive i.e. ",a)
# else:
#     print("The number is negative i.e", a)
# Find the largest of three numbers. → Beginner
# a = int(input("Enter the number here for Max number test: "))
# b = int(input("Enter the number here for Max number test: "))
# c = int(input("Enter the number here for Max number test: "))

# numbers = [a, b, c]
# print("The largest number is:", max(numbers))

# Determine if a character is a vowel or consonant. → Beginner
# Check if a person is eligible to vote (age >= 18). → Beginner
# age=int(input("Enter the voter age here: "))
# if age==18 or age>18:
#     print("Voter is eligible for the voting , voter age is",age)
# else:
#     print("Voter is not eligible for the voting. The age is",age)



# Determine if a triangle is valid given three sides. → Intermediate
# Simple calculator: take two numbers and operator (+,-,*,/), perform operation. → Intermediate
# Check if a string is palindrome (ignore case). → Intermediate
# Determine the season based on month input. → Intermediate
# Check if a number is prime. → Intermediate
# Find if a year is leap year using nested if. → Intermediate
# Traffic light simulator: input color and print action (go, wait, stop). → Beginner
# BMI category: underweight, normal, overweight, obese. → Intermediate
# Login system: check username and password (hardcoded). → Intermediate
# Determine odd/even and positive/negative. → Beginner
# Find day of week (1-7) and print name. → Beginner
# Check if a character is uppercase, lowercase, digit, or special. → Intermediate
# Discount calculator: based on amount, apply different discounts. → Intermediate
# Rock-paper-scissors game logic (single round). → Intermediate

# Loops (for, while)

# Print numbers from 1 to 10 using for and while. → Beginner
# Calculate sum of first N natural numbers. → Beginner
# Print multiplication table of a given number. → Beginner
# Count down from 10 to 1 and print "Blast off!". → Beginner
# Find factorial of a number. → Intermediate
# Print Fibonacci series up to N terms. → Intermediate
# Reverse a number using while loop. → Intermediate
# Check if a number is Armstrong (sum of cubes of digits). → Intermediate
# Print all even numbers between 1 and 50. → Beginner
# Guess the number game (computer generates random, user guesses with hints). → Advanced
# Print star pattern (triangle) using nested loops. → Intermediate
# Sum of digits of a number. → Intermediate
# Find prime numbers up to N. → Intermediate
# Keep asking for input until user enters "quit". → Intermediate
# Calculate average of numbers entered by user (stop on negative). → Intermediate
# Print all factors of a number. → Intermediate
# Simple menu-driven program (loop until exit). → Advanced
# Count vowels in a string. → Intermediate
# Generate multiplication tables from 1 to 10. → Intermediate
# Simulate a login with limited attempts (3 tries). → Intermediate

# You can now use these problems progressively: start with Beginner to build confidence, move to Intermediate for deeper understanding, and tackle Advanced ones to challenge yourself further!2.5sFastwith all of this give me the more questions on advance level min count topic wise 30Here are additional advanced-level practice problems for each of the four topics. These are designed to be genuinely challenging, requiring deeper understanding, combination of multiple concepts (variables/data types + collections + conditionals + loops), handling edge cases, efficiency considerations, or creative problem-solving.
# I’ve provided exactly 30 advanced problems per topic (120 total), all marked as Advanced.
# Variables & Data Types (int, float, str, bool) – 30 Advanced Problems

# Implement variable swapping for three variables in a cycle without using extra space.
# Safely convert a string to float/int with error handling and default value if invalid.
# Simulate fixed-point arithmetic using integers to avoid floating-point precision issues.
# Parse a complex string like "True, 42, 3.14, hello" into corresponding bool, int, float, str types.
# Implement a custom string formatting function similar to f-strings using only basic operations.
# Detect and handle overflow when adding two large integers represented as strings.
# Convert Roman numerals to integer and vice versa with full validation.
# Implement arbitrary-precision addition for very large numbers given as strings.
# Create a type-checking function that distinguishes between int, float, str, bool even when values overlap (e.g., "True" vs True).
# Simulate boolean logic gates (AND, OR, XOR, NAND) using only arithmetic operations on integers.
# Parse and evaluate a simple arithmetic expression string without using eval().
# Implement scientific notation parsing (e.g., "1.23e-4") into float.
# Handle Unicode string normalization and compare strings ignoring accents.
# Implement a custom base conversion (base 2 to base 36) for large integers as strings.
# Detect floating-point precision errors by comparing two floats with epsilon.
# Create a truthy/falsy evaluator that mimics Python’s behavior for custom objects (simulated).
# Implement integer square root using only bit operations (no math library).
# Parse time strings in various formats (12-hour, 24-hour, with/without seconds) into structured data.
# Simulate enum-like behavior using constants and type checking.
# Implement a safe type coercion system that logs warnings on lossy conversions.
# Convert a float to its exact fractional representation as string (e.g., 0.1 → "1/10").
# Handle signed zero, infinity, and NaN in float operations manually.
# Implement string compression count (e.g., "aaabbc" → "a3b2c1") and decompression.
# Create a dynamic variable naming system using dictionaries to simulate forbidden behavior.
# Implement bit-level manipulation to pack/unpack multiple bools into a single int.
# Parse and validate IPv4 addresses from strings.
# Implement a custom delimiter-based CSV line parser handling quoted fields.
# Simulate complex numbers using two floats and overload basic operations (as functions).
# Convert between little-endian and big-endian byte representations of integers.
# Implement a robust password strength checker using multiple boolean conditions and scoring.

# Lists, Tuples, Sets, Dictionaries – 30 Advanced Problems

# Implement a sparse matrix using nested dictionaries and support addition.
# Flatten a deeply nested list of arbitrary depth into a single list.
# Find all subsets of a list that sum to a target value (subset sum problem).
# Implement an LRU Cache using OrderedDict or manual doubly linked list + dict.
# Detect and remove cycles in a list of objects referencing each other (using dict for seen).
# Group anagrams from a list of strings using dictionary with sorted tuple keys.
# Implement a trie (prefix tree) using nested dictionaries for word storage and search.
# Find the longest consecutive sequence in an unsorted list using sets efficiently.
# Implement a priority queue using a list and manual heap operations.
# Merge k sorted lists into one sorted list efficiently.
# Rotate a 2D matrix (list of lists) in-place 90 degrees clockwise.
# Find all pairs in a list with a given difference using sets.
# Implement a disjoint set union (DSU) with path compression and union by rank.
# Count inversions in a list using modified merge sort (list manipulation).
# Implement a frequency stack that pops the most frequent element.
# Find the maximum depth of nested lists/tuples.
# Serialize and deserialize a nested structure (lists, tuples, dicts) to/from string.
# Implement a graph using adjacency list (dict of lists) and perform DFS/BFS.
# Find all duplicate subtrees in a binary tree represented as nested tuples.
# Implement a bloom filter using sets or bit manipulation for approximate membership.
# Solve the N-Queens problem and store board states as lists/tuples.
# Implement a Sudoku solver using backtracking with 2D list.
# Find the kth largest element in an unsorted list without sorting fully.
# Implement a dictionary that supports version history (undo/redo operations).
# Detect if two lists form a valid anagram of each other using counters.
# Implement topological sort on a DAG represented as dict of lists.
# Find the maximum product subarray in a list (Kadane’s variant).
# Implement a min/max stack that supports O(1) peek for min/max using auxiliary structures.
# Solve word ladder problem using BFS with sets and queues.
# Implement a memory-efficient set for storing billions of integers using bit arrays.

# Conditional Statements (if-else) – 30 Advanced Problems

# Implement a decision tree evaluator for a complex rule set (nested ifs with multiple conditions).
# Solve the 3-SAT problem for small instances using backtracking and conditionals.
# Determine if a point lies inside a convex polygon given coordinates (ray casting with edge cases).
# Implement FizzBuzzBuzz variant with multiple divisible conditions and custom rules.
# Validate a date (day, month, year) considering leap years and all edge cases.
# Determine the winner in a rock-paper-scissors-lizard-spock tournament (complex rules).
# Classify a triangle by sides and angles (scalene, isosceles, right, obtuse, etc.) with floating-point tolerance.
# Implement a tax calculator with progressive brackets and multiple condition tiers.
# Determine if four points form a square (distance + diagonal checks).
# Solve the Josephus problem using conditional elimination logic.
# Validate and classify chess moves for a given piece (e.g., knight) on an 8x8 board.
# Implement a credit score classifier with multiple weighted conditions.
# Determine if a string matches a simplified regex pattern (e.g., "a*b+c").
# Solve the knapsack 0/1 problem using recursion with conditionals (small input).
# Classify network packets based on multiple header fields (simulated).
# Determine the type of IPv4 address (unicast, multicast, broadcast, etc.).
# Implement a vending machine state machine with coin and selection conditions.
# Solve the stable marriage problem for small pairs using preference checks.
# Determine if a number is a valid Luhn algorithm credit card number.
# Implement a parser for simple boolean expressions with operators and parentheses.
# Determine the zodiac sign and Chinese zodiac combination based on birth date.
# Solve the 8-puzzle solvability check (inversion count parity).
# Implement a flight fare calculator with multiple conditions (age, class, baggage, season).
# Determine if a graph is bipartite using coloring with conditionals.
# Implement a simple AI for tic-tac-toe (check winning/blocking moves).
# Validate and parse cron expression for scheduling (minute, hour, etc.).
# Determine if a hand of cards contains poker combinations (flush, straight, etc.).
# Implement a loan eligibility checker with multiple financial and demographic conditions.
# Solve the egg dropping puzzle for minimum trials in worst case.
# Implement a complex discount engine with overlapping rules (e.g., buy 2 get 1, loyalty, coupon).

# Loops (for, while) – 30 Advanced Problems

# Implement matrix multiplication using triple nested loops with proper bounds.
# Solve the traveling salesman problem using backtracking loops (small cities).
# Generate all permutations of a list using recursive loops.
# Implement Conway’s Game of Life simulation on a grid with toroidal boundaries.
# Find the longest palindromic substring using nested loops (expand around center).
# Implement sieve of Eratosthenes optimized with segmented approach.
# Simulate a Turing machine for simple operations using while loops.
# Generate all combinations of k elements from n using iterative loops.
# Implement Floyd’s cycle detection in a linked list (simulated with list).
# Solve the longest increasing subsequence using dynamic programming loops.
# Implement a loop-based parser for balanced parentheses with multiple types ([]{}()).
# Simulate a CPU instruction cycle with fetch-decode-execute loop.
# Generate Pascal’s triangle up to n rows and find element at position.
# Implement Rabin-Karp string search with rolling hash in a loop.
# Solve the stock buy/sell problem for maximum profit with multiple transactions.
# Implement iterative deepening depth-first search (IDDFS) on a graph.
# Generate all prime numbers up to n using wheel factorization loop.
# Simulate a banking queue system with multiple tellers using event loops.
# Implement big integer multiplication using Karatsuba algorithm recursively/iteratively.
# Solve the maximum subarray sum using divide-and-conquer with loops.
# Generate mazes using randomized depth-first search with backtracking loops.
# Implement iterative fast Fourier transform (FFT) for power-of-2 lengths.
# Simulate particle movement in a grid with collision handling loops.
# Solve the word break problem using dynamic programming loops.
# Implement a loop-based interpreter for a simple stack-based language (like Forth).
# Generate all magic squares of order n using constraint loops.
# Implement longest common subsequence using 2D DP table loops.
# Simulate a multi-threaded task scheduler using round-robin loop.
# Solve the edit distance (Levenshtein) problem using DP loops.
# Implement a loop-driven cellular automaton for Langton’s ant with large grid.

