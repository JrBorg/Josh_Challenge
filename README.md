# Josh_Challenge
*Credit Card Validator*

This script is designed to validate credit card numbers according to a set of criteria. The following functions are included:

validate_credit_card_number
This function takes a string argument card_number and validates it according to the following rules:

Any hyphens or spaces in the card_number string are removed.
The card_number must be exactly 16 digits long and only contain digits.
The card_number must start with 4, 5, or 6.
The card_number cannot have 4 or more consecutive repeated digits.
The card_number must have groups of 4 digits separated by hyphens or be a 16-digit number.
If the card_number meets all of these criteria, the function returns the string 'Valid'. If it fails to meet any of these criteria, the function returns the string 'Invalid'.

