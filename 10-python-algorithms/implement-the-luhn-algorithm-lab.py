def verify_card_number(card_number):
    # 1. Handle and remove dashes and spaces from the card number
    cleaned_card = card_number.replace("-", "").replace(" ", "")
    
    # Check if the remaining string contains only digits
    if not cleaned_card.isdigit():
        return "INVALID!"
        
    total_sum = 0
    # Reverse the digits to easily process starting from the right (1-based or 0-based index)
    digits = [int(char) for char in cleaned_card[::-1]]
    
    for i, digit in enumerate(digits):
        if i % 2 == 1:
            doubled = digit * 2
            if doubled > 9:
                doubled -= 9
            total_sum += doubled
        else:
            total_sum += digit

    if total_sum % 10 == 0:
        return "VALID!"
    else:
        return "INVALID!"