# Taken from internet, RE works for following format
#     ^           # matches the start of string
#     (\d{3})     # area code is 3 digits (e.g. '800')
#     \D*         # optional separator is any number of non-digits
#     (\d{3})     # trunk is 3 digits (e.g. '555')
#     \D*         # optional separator
#     (\d{4})     # rest of number is 4 digits (e.g. '1212')
#     \D*         # optional separator
#     (\d*)       # extension is optional and can be any number of digits
#     $           # end of string

import re
phonePattern = re.compile(r'^\D*(\d{3})\D*(\d{3})\D*(\d{4})\D*(\d*)$')
while(1):
  s=input("Enter phone number : ")
  if (phonePattern.match(s)):
    print("Valid number.")
    break
  else:
    print("Invalid number. Try again")