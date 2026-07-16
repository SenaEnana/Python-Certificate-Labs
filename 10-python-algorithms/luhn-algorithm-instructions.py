# Implement the Luhn Algorithm
# The Luhn algorithm, also known as the "modulus 10" or "mod 10" algorithm, 
# is a simple checksum formula used to validate a variety of identification numbers, like credit card numbers. 
# These are the steps to validate a number using the Luhn algorithm:

# Starting from the right, and excluding the rightmost digit (the check digit), double the value of every other digit.
# If the result of doubling a digit is greater than 9, sum the digits to get a single digit. Alternatively, 
# you can subtract 9 from the result.
# Take the sum of all the digits including the check digit.
# If the sum of all the digits is a multiple of 10, then the number is valid; else it is not valid.
# For example, consider the number 453914881. The steps to validate it using the Luhn algorithm are:

# Example Code
# Account number      4   5   3   9   1   4   8   8   1 
# Double every other  4  10   3  18   1   8   8  16   1 
# Sum 2-char digits   4   1   3   9   1   8   8   7   1 
# Then sum all numbers, 4 + 1 + 3 + 9 + 1 + 8 + 8 + 7 + 1 = 42.
# Since 42 is not a multiple of 10, the number is invalid.
# In this lab, you will build a credit card validator using the Luhn algorithm.

# Objective: Fulfill the user stories below and get all the tests to pass to complete the lab.

# User Stories:

# You should define a function named verify_card_number that takes a string of digits (representing a card number) 
# and verifies whether it is valid according to the Luhn algorithm.

# Within the verify_card_number function:

# You should handle any dashes or spaces that may be present in the card number passed to it.
# Return VALID! if the card number is valid; otherwise, return INVALID!.
# When you complete the project, you should see the following messages depending on the input:

# Card Number	Message
# 453914889	VALID!
# 4111-1111-1111-1111	VALID!
# 1234 5678 9012 3456	INVALID!

