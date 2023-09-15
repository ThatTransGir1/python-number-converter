# Python Based Number Converter

This is a python based Binary(base2) to decimal(base10) converter.

It uses custom functions for the calculations instead of the built-in functions.

## Code Overview

## The Functions
### Binary to Decimal Conversion
```python:
def binaryToDecimal(n):
  #* creates an empty list 'digits'
  digits = []
  #* sets the 'placeVal' variable to 1
  placeVal = 1
  #* sets the 'decVal' variable to 0
  decVal = 0
  #* splits the string 'n' and puts into the 'digits' list
  digits = list(n)
  #* iterates through each digit in the 'digit' list
  for i in range(len(digits)):
    decVal += placeVal * int(digits[len(digits) - i - 1])
    placeVal *= 2
    #* prints the power of 2 that was multiplied
    print(color.LIGHTCYAN_EX + "Power of 2: " + color.GREEN + str(placeVal) + color.RESET)
    #* prints the solution of above
    print(color.LIGHTCYAN_EX + "Answer: " + color.GREEN + str(decVal) + "\n")
  return decVal
```

```python:

