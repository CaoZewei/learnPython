import re

phoneNumberRegex = re.compile(r'\d{3}-\d{3}-\d{4}')

text = 'my number is 415-555-4234 and 123-523-5341'

phone = phoneNumberRegex.search(text)
print(phone)
print('phone number:'+phone.group())