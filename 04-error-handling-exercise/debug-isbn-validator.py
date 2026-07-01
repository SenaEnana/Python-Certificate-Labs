def validate_isbn(isbn, length):
    # Fix: Corrected len() to check string length of isbn instead of len(isbn, length)
    if len(isbn) != length:
        print(f'ISBN-{length} code should be {length} digits long.')
        return
        
    # Fix: Rectified off-by-one errors & out-of-bounds index errors
    # The check digit calculation requires only the first (length - 1) digits.
    main_digits = isbn[0:length-1]
    given_check_digit = isbn[length-1]
    
    # Fix: Added a try-except block to gracefully catch characters that aren't numbers 
    # while parsing the main digits list.
    try:
        main_digits_list = [int(digit) for digit in main_digits]
    except ValueError:
        print('Invalid character was found.')
        return

    # Calculate the check digit from other digits
    if length == 10:
        expected_check_digit = calculate_check_digit_10(main_digits_list)
    else:
        expected_check_digit = calculate_check_digit_13(main_digits_list)
        
    # Check if the given check digit matches with the calculated check digit
    if given_check_digit == expected_check_digit:
        print('Valid ISBN Code.')
    else:
        print('Invalid ISBN Code.')

def calculate_check_digit_10(main_digits_list):
    digits_sum = 0
    for index, digit in enumerate(main_digits_list):
        digits_sum += digit * (10 - index)
    result = 11 - digits_sum % 11
    if result == 11:
        expected_check_digit = '0'
    elif result == 10:
        expected_check_digit = 'X'
    else:
        expected_check_digit = str(result)
    return expected_check_digit

def calculate_check_digit_13(main_digits_list):
    digits_sum = 0
    for index, digit in enumerate(main_digits_list):
        if index % 2 == 0:
            digits_sum += digit * 1
        else:
            digits_sum += digit * 3
    result = 10 - digits_sum % 10
    if result == 10:
        expected_check_digit = '0'
    else:
        expected_check_digit = str(result)
    return expected_check_digit

def main():
    user_input = input('Enter ISBN and length: ')
    
    # Fix: Handle IndexError if a comma isn't provided
    try:
        values = user_input.split(',')
        isbn = values[0]
        length_str = values[1]
    except IndexError:
        print('Enter comma-separated values.')
        return

    # Fix: Handle ValueError if length isn't a valid integer
    try:
        length = int(length_str)
    except ValueError:
        print('Length must be a number.')
        return

    # Fix: Corrected IndentationErrors inside the conditional blocks
    if length == 10 or length == 13:
        validate_isbn(isbn, length)
    else:
        print('Length should be 10 or 13.')

# Important: The requirement states to comment out the main() call in global space 
# so the test suites can execute without waiting on an input block.
# main()

## the above is the answer to the following code and it asks to debug the code because
## if you run this or the below code you will get an error so the lab is to fix the error using exception handling

# def validate_isbn(isbn, length):
#     if len(isbn, length) != length:
#         print(f'ISBN-{length} code should be {length} digits long.')
#         return
#     main_digits = isbn[0:length]
#     given_check_digit = isbn[length]
#     main_digits_list = [int(digit) for digit in main_digits]
#     # Calculate the check digit from other digits
#     if length == 10:
#         expected_check_digit = calculate_check_digit_10(main_digits_list)
#     else:
#         expected_check_digit = calculate_check_digit_13(main_digits_list)
#     # Check if the given check digit matches with the calculated check digit
#     if given_check_digit == expected_check_digit:
#         print('Valid ISBN Code.')
#     else:
#         print('Invalid ISBN Code.')
# def calculate_check_digit_10(main_digits_list):
#     # Note: You don't have to fully understand the logic in this function.
#     digits_sum = 0
#     # Multiply each of the first 9 digits by its corresponding weight (10 to 2) and sum up the results
#     for index, digit in enumerate(main_digits_list):
#         digits_sum += digit * (10 - index)
#     # Find the remainder of dividing the sum by 11, then subtract it from 11
#     result = 11 - digits_sum % 11
#     # The calculation result can range from 1 to 11.
#     # If the result is 11, use 0.
#     # If the result is 10, use upper case X.
#     # Use the value as it is for other numbers.
#     if result == 11:
#         expected_check_digit = '0'
#     elif result == 10:
#         expected_check_digit = 'X'
#     else:
#         expected_check_digit = str(result)
#     return expected_check_digit
# def calculate_check_digit_13(main_digits_list):
#     # Note: You don't have to fully understand the logic in this function.
#     digits_sum = 0
#     # Multiply each of the first 12 digits by 1 and 3 alternately (starting with 1), and sum up the results
#     for index, digit in enumerate(main_digits_list):
#         if index % 2 == 0:
#             digits_sum += digit * 1
#         else:
#             digits_sum += digit * 3
#     # Find the remainder of dividing the sum by 10, then subtract it from 10
#     result = 10 - digits_sum % 10
#     # The calculation result can range from 1 to 10.
#     # If the result is 10, use 0.
#     # Use the value as it is for other numbers.
#     if result == 10:
#         expected_check_digit = '0'
#     else:
#         expected_check_digit = str(result)
#     return expected_check_digit
# def main():
#     user_input = input('Enter ISBN and length: ')
#     values = user_input.split(',')
#     isbn = values[0]
#     length = int(values[1])
#     if length == 10 or length == 13:
#     validate_isbn(isbn, length)
#     else:
#     print('Length should be 10 or 13.')

# main()