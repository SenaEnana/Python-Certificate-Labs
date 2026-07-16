# Implement the Bisection Method
# The bisection method, also known as the binary search method, uses a binary search to find the roots of a real-valued function. 
# It works by narrowing down an interval where the square root lies until it converges to a value within a specified tolerance.

# For example, if the tolerance is 0.01, the bisection method will keep halving the interval until the 
# difference between the upper and lower bounds is less than or equal to 0.01.

# In this lab, you will implement a function that uses the bisection method to find the square root of a number.

# Objective: Fulfill the user stories below and get all the tests to pass to complete the lab.

# User Stories:

# You should define a function named square_root_bisection with three parameters:

# The number for which you want to find the square root.
# The tolerance being the acceptable error margin for the result. You should set a default tolerance value.
# The maximum number of iterations to perform. You should set a default number of iterations.
# The square_root_bisection function should:

# Raise a ValueError with the message Square root of negative number is not defined in real numbers if the number passed to the function is negative.
# For numbers 0 and 1, print the message: The square root of [number] is [number] and return the number itself as the square root.
# For any other positive number, print the approximate square root with the message: The square root of [square_target] is approximately [root] and return the computed root value.
# If no value meets the tolerance condition, print a failure message: Failed to converge within [maximum] iterations and return None.
# Note: You cannot import any module for this lab.

# Tests:
# Waiting:1. You should not import any module.
# Waiting:2. You should have a function named square_root_bisection.
# Waiting:3. Your square_root_bisection function should have three parameters.
# Waiting:4. You should set a default value for the tolerance and the maximum number of iterations.
# Waiting:5. Your square_root_bisection function should raise a ValueError with the message Square root of negative number is not defined in real numbers when the number passed to the function is negative.
# Waiting:6. square_root_bisection(0) should return 0.
# Waiting:7. square_root_bisection(0) should print The square root of 0 is 0.
# Waiting:8. square_root_bisection(0.001, 1e-7, 50) should return a number between 0.03162267660168379 and 0.031622876601683794.
# Waiting:9. square_root_bisection(0.001, 1e-7, 50) should print The square root of 0.001 is approximately X, where X is a number between 0.03162267660168379 and 0.031622876601683794.
# Waiting:10. square_root_bisection(0.25, 1e-7, 50) should return a number between 0.4999999 and 0.5000001.
# Waiting:11. square_root_bisection(0.25, 1e-7, 50) should print The square root of 0.25 is approximately X, where X is a number between 0.4999999 and 0.5000001.
# Waiting:12. square_root_bisection(1) should return 1.
# Waiting:13. square_root_bisection(1) should print The square root of 1 is 1.
# Waiting:14. square_root_bisection(81, 1e-3, 50) should return a number between 8.999 and 9.001.
# Waiting:15. square_root_bisection(81, 1e-3, 50) should print The square root of 81 is approximately X, where X is a number between 8.999 and 9.001.
# Waiting:16. square_root_bisection(225, 1e-3, 100) should return a number between 14.999 and 15.001.
# Waiting:17. square_root_bisection(225, 1e-3, 100) should print The square root of 225 is approximately X, where X is a number between 14.999 and 15.001.
# Waiting:18. square_root_bisection(225, 1e-5, 100) should return a number between 14.99999 and 15.00001.
# Waiting:19. square_root_bisection(225, 1e-5, 100) should print The square root of 225 is approximately X, where X is a number between 14.99999 and 15.00001.
# Waiting:20. square_root_bisection(225, 1e-7, 100) should return a number between 14.9999999 and 15.0000001.
# Waiting:21. square_root_bisection(225, 1e-7, 100) should print The square root of 225 is approximately X, where X is a number between 14.9999999 and 15.0000001.
# Waiting:22. square_root_bisection(225, 1e-7, 10) should return None.
# Waiting:23. square_root_bisection(225, 1e-7, 10) should print Failed to converge within 10 iterations.

# Tests:
# Passed:1. You should not import any module.
# Passed:2. You should have a function named square_root_bisection.
# Passed:3. Your square_root_bisection function should have three parameters.
# Passed:4. You should set a default value for the tolerance and the maximum number of iterations.
# Passed:5. Your square_root_bisection function should raise a ValueError with the message Square root of negative number is not defined in real numbers when the number passed to the function is negative.
# Passed:6. square_root_bisection(0) should return 0.
# Passed:7. square_root_bisection(0) should print The square root of 0 is 0.
# Passed:8. square_root_bisection(0.001, 1e-7, 50) should return a number between 0.03162267660168379 and 0.031622876601683794.
# Passed:9. square_root_bisection(0.001, 1e-7, 50) should print The square root of 0.001 is approximately X, where X is a number between 0.03162267660168379 and 0.031622876601683794.
# Passed:10. square_root_bisection(0.25, 1e-7, 50) should return a number between 0.4999999 and 0.5000001.
# Passed:11. square_root_bisection(0.25, 1e-7, 50) should print The square root of 0.25 is approximately X, where X is a number between 0.4999999 and 0.5000001.
# Passed:12. square_root_bisection(1) should return 1.
# Passed:13. square_root_bisection(1) should print The square root of 1 is 1.
# Passed:14. square_root_bisection(81, 1e-3, 50) should return a number between 8.999 and 9.001.
# Passed:15. square_root_bisection(81, 1e-3, 50) should print The square root of 81 is approximately X, where X is a number between 8.999 and 9.001.
# Passed:16. square_root_bisection(225, 1e-3, 100) should return a number between 14.999 and 15.001.
# Passed:17. square_root_bisection(225, 1e-3, 100) should print The square root of 225 is approximately X, where X is a number between 14.999 and 15.001.
# Passed:18. square_root_bisection(225, 1e-5, 100) should return a number between 14.99999 and 15.00001.
# Passed:19. square_root_bisection(225, 1e-5, 100) should print The square root of 225 is approximately X, where X is a number between 14.99999 and 15.00001.
# Passed:20. square_root_bisection(225, 1e-7, 100) should return a number between 14.9999999 and 15.0000001.
# Passed:21. square_root_bisection(225, 1e-7, 100) should print The square root of 225 is approximately X, where X is a number between 14.9999999 and 15.0000001.
# Passed:22. square_root_bisection(225, 1e-7, 10) should return None.
# Passed:23. square_root_bisection(225, 1e-7, 10) should print Failed to converge within 10 iterations