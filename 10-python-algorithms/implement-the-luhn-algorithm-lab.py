def verify_card_number(card_number):
    cleaned_card = card_number.replace("-", "").replace(" ", "")

    if not cleaned_card.isdigit():
        return "INVALID!"
        
    total_sum = 0
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