import re

def credit_card_check(card_number):
    # Define the regex pattern for initial validation
    pattern = r"""
    ^           # its first value of nummber of cards                    
    (?:4|5|6)                     
    (\d{3}                         
    (?:-\d{4}){3}|\d{15})           
    $                               
    """
    
    repeated_digits = r"(\d)(\1{3,})"
    card_pattern = re.compile(pattern, re.VERBOSE)
    
  
    if card_pattern.match(card_number) and not re.search(repeated_digits, card_number.replace("-", "")):
        return "Valid"
    else:
        return "Invalid"


N = int(input("")) ## Read the input 

if 0 < N < 100:
 
    card_numbers = [input() for _ in range(N)] ### read the input each line of input
    

    for card in card_numbers:
        print(f"{credit_card_check(card)}")
else:
    print("Max cards are 100 ONLY ")