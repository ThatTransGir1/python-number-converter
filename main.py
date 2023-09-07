import pyfiglet, sys, os, platform
from colorama import Fore as color

# checks the OS and runs a diffrent clear command if it's windows
if platform.system == "Windows":
  os.system("cls")
else:
  #clears the terminal
  os.system("clear")

# basic intro function for the program
def intro(txt, author, url):
  intro = color.GREEN + pyfiglet.figlet_format(txt)
  credit = "\n" + color.LIGHTMAGENTA_EX + "Created by " + author + " on " + url + color.RESET + "\n"
  return print(intro + credit)

intro("Converter", "ThatTransGir1", "https://github.com/thattransgir1")

# checks if inputed number is a valid base (10 or 2 for this converter)
def baseCheck(num_string, base):
    for single_char in num_string:
        if int(single_char) >= int(base):
            return False
    return True

# binary to decimal convert function
def binaryToDecimal(n):
  # checks if the inputed string is valid binary
  if baseCheck(n,2) == False:
    return sys.exit(print(color.RED + "Input must be a binary number string [0-1]"))
  # creates an empty list 'digits'
  digits = []
  # sets the 'placeVal' variable to 1
  placeVal = 1
  # sets the 'decVal' variable to 0
  decVal = 0
  # splits the string 'n' and puts into the 'digits' list
  digits = list(n)
  # iterates through each digit in the 'digit' list
  for i in range(len(digits)):
    decVal += placeVal * int(digits[len(digits) - i - 1])
    placeVal *= 2
    # prints the power of 2 that was multiplied
    print(color.LIGHTCYAN_EX + "Power of 2: " + color.GREEN + str(placeVal) + color.RESET)
    # prints the solution of above
    print(color.LIGHTCYAN_EX + "Answer: " + color.GREEN + str(decVal) + "\n")
  return decVal

# decimal to binary convert function
def decimalToBinary(n):
  # checks if the inputed string is a valid decimal
  if baseCheck(n,10) == False:
    return sys.exit(print(color.RED + "Input must be a decimal number string [0-9]"))
  if (int(n) <= 1):
    return n
  # creates an empty string
  binVal = ''
  # sets 'decRem' to n as an integer
  decRem = int(n)
  # while 'decRem' is greater than 0 
  while decRem > 0:
    # divides the 'decRem' variable by 2 to get the remainder
    binVal = str(decRem % 2) + binVal
    # divides the 'decRem' variable by 2 to get the quotient
    decRem = decRem // 2
    # prints the remainder
    print(color.LIGHTCYAN_EX + "Remainder: " + color.GREEN + str(binVal) + color.RESET)
    # prints the quotient
    print(color.LIGHTCYAN_EX + "Quotient: " + color.GREEN + str(decRem) + color.RESET+ "\n")
  return binVal
# the begining prompt
prompt = input(color.LIGHTRED_EX + "\nType a number corrasponding to an option below [1-3]." + color.LIGHTCYAN_EX + "\n\n1. Binary to Decimal\n2. Decimal to Binary\n3. Close\n: " + color.RESET)

# converts the inputed binary into decimal and prints the output
if prompt == "1":
  # checks the OS and runs a diffrent clear command if it's windows
  if platform.system == "Windows":
    os.system("cls")
  # clears the terminal
  os.system("clear")
  # asks for a binary(base2) number that will be converted into decimal(base10)
  conv = input(color.MAGENTA + "Enter the Binary number you would like to convert below\n: " + color.RESET)
  bin = conv
  dec = binaryToDecimal(conv)
  # prints the output from the decimal to binary conversion
  print(color.LIGHTCYAN_EX + "Original Binary: " + color.GREEN + bin + color.LIGHTCYAN_EX + "\nSolution: " + color.LIGHTGREEN_EX + str(dec) + color.RESET)

# converts the inputed decimal into binary and prints the output
if prompt == "2":
  # checks the OS and runs a diffrent clear command if it's windows
  if platform.system == "Windows":
    os.system("cls")
  # clears the terminal
  os.system("clear")
  # asks for a binary(base2) number that will be converted into decimal(base10)
  conv = input(color.MAGENTA + "Enter the Decimal number you would like to convert below\n: " + color.RESET)
  dec = conv
  bin = decimalToBinary(conv)
  # prints the output from the decimal to binary conversion
  print(color.LIGHTCYAN_EX + "Original Decimal: " + color.GREEN + dec + color.LIGHTCYAN_EX + "\nSolution: " + color.LIGHTGREEN_EX + str(bin) + color.RESET)

# Exits the program.
if prompt == "3":
  sys.exit(color.RED + "Closing Program" + color.RESET)

# checks if the "prompt" variable is greater than 3 and if it is closes the program.
if prompt == int(prompt)>3:
  sys.exit(color.RED + "Please restart the program and choose a valid option [1-3]" + color.RESET)

