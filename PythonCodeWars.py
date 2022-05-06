# Create a function that takes a Roman numeral as its argument and returns its value as a numeric decimal integer.
# You don't need to validate the form of the Roman numeral.
def roman_to_int(roman):
    roman = roman.upper()
    roman_dict = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    int_val = 0
    for i in range(0,len(roman)):
        if i+1 < len(roman) and roman_dict[roman[i]] < roman_dict[roman[i+1]]:
            int_val -= roman_dict[roman[i]]
        else:
            int_val += roman_dict[roman[i]]
        return int_val
        
# Write a function that accepts an array of 10 integers (between 0 and 9), 
# that returns a string of those numbers in the form of a phone number.   
def create_phone_number(n):
    return "({}{}{}) {}{}{}-{}{}{}{}".format(*n)

#Your goal in this kata is to implement a difference function, which subtracts one list from another and returns the result.
#It should remove all values from list a, which are present in list b keeping their order.
def array_dif(a, b):
    return [x for x in a if x not in b]

#Take 2 strings s1 and s2 including only letters from ato z. 
#Return a new sorted string, the longest possible, containing distinct letters - each taken only once - coming from s1 or s2.
def longest(a1, a2):
    return "".join(sorted(set(a1 + a2)))


