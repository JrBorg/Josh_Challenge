import sys
import re

def validate_credit_card_number(card_number):
    # Remove any hyphens or spaces from the card number
    card_number = re.sub(r'[-\s]', '', card_number)

    # Check that the card number is exactly 16 digits long and only contains digits
    if not re.match(r'^\d{16}$', card_number):
        return 'Invalid'

    # Check that the card number starts with 4, 5, or 6
    if not re.match(r'^[456]', card_number):
        return 'Invalid'

    # Check that the card number does not have 4 or more consecutive repeated digits
    if re.search(r'(\d)\1{3}', card_number):
        return 'Invalid'

    # Check that the card number has groups of 4 digits separated by hyphens or is a 16-digit number
    if re.match(r'^\d{4}(-\d{4}){3}$', card_number) or re.match(r'^\d{16}$', card_number):
        return 'Valid'

    # If none of the above conditions are met, the card number is invalid
    return 'Invalid'

if __name__ == '__main__':
    num_cards = int(sys.argv[1])
    card_numbers = sys.argv[2:]

    # Check each credit card number and print the result
    for card_number in card_numbers:
        if re.search(r'\s', card_number):
            print('Invalid')
        else:
            print(validate_credit_card_number(card_number))