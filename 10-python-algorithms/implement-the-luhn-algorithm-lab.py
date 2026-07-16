def verify_card_number(card_number):
    # 1. Handle and remove dashes and spaces from the card number
    cleaned_card = card_number.replace("-", "").replace(" ", "")
    
    # Check if the remaining string contains only digits
    if not cleaned_card.isdigit():
        return "INVALID!"
        
