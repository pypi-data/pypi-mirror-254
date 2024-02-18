def print_prog():
    print(
        """
import re

def extract_info(text):
    names = re.findall(r'\b[A-Z][a-z]+\b', text)
    emails = re.findall(r'\b[A-Za-z0-9]+@[A-Za-z0-9]+\.[A-Z|a-z]{2,}\b', text)
    phone_numbers = re.findall(r'[0-9]+', text)
    return names, emails, phone_numbers

text = ''' Jyohuguvyghjkl's email is jyo@gmail.com and her number is +9392821338 '''
names, emails, phone_numbers = extract_info(text)

print("Names:", names)
print("Emails:", emails)
print("Phone numbers:", phone_numbers)
"""
    )
