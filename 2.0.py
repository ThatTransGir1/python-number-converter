import pyfiglet, sys, os, platform, re
from colorama import Fore as color

# basic intro function for the program
def intro(txt, author, url):
  intro = color.GREEN + pyfiglet.figlet_format(txt)
  credit = "\n" + color.LIGHTMAGENTA_EX + "Created by " + author + " on " + url + color.RESET + "\n"
  return print(intro + credit)


intro("Converter", "ThatTransGir1", "https://github.com/thattransgir1")

# checks if inputed number is a valid decimal
Dec = re.compile(r'[0-9]{7}[\S\D\W]{1}[0-9]+$')

# checks if inputed number is valid binary
Bin = re.compile('[^01]')

# checks if inputed number is a valid hexadecimal
Hex = re.compile(r'\s--([0-9a-fA-F]+)(?:--)?\s')

hexCovTbl = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}

# binary to decimal convert function
def binaryToDecimal(n):
  # checks if the inputed string is valid binary
  if Bin.match(str(n)) == False:
    return "Input must be a binary number string [0-1]"
  digits = []
  placeVal = 1
  decVal = 0
  digits = list(n)
  for i in range(len(digits)):
    decVal += placeVal * int(digits[len(digits) - i - 1])
    placeVal *= 2
  return decVal

# decimal to binary convert function
def decimalToBinary(n):
  # checks if the inputed string is a valid decimal
  if Dec.match(str(n)) == False:
    return "Input must be a decimal number string [0-9]"
  if (int(n) <= 1):
    return n
  binVal = ''
  decRem = int(n)
  while decRem > 0:
    binVal = str(decRem % 2) + binVal
    decRem = decRem // 2
  return binVal

# decimal to hexadecimal convert function
def decimalToHexadecimal(n):
  # checks if the inputed string is valid hexadecimal
  if Hex.match(str(n)) == False:
    return "Input must be a decimal number string [0-9]"
  n = int(n)
  while(n > 0):
        remainder = n % 16
        hexa = hexCovTbl[remainder] + hexa
        n = n // 16
  return hexa
def hexadecimalToDecimal(n):
  # checks if the inputed string is valid hexadecimal
  if Hex.match(str(n)) == False:
    return "Input must be a hexadecimal number string [0-F]"
  dec = int(n, 16)
  return dec
# the programs main prompt
prompt = input(color.LIGHTCYAN_EX + "\n1. Binary to Decimal\n2. Decimal to Binary\n3. Binary to Hexadecimal\n4. Hexadecimal to Binary\n5. Decimal to Hexadecimal\n6. Hexadecimal to Decimal\n7. Close\n: " + color.RESET)

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
  print(color.LIGHTCYAN_EX + "Original Binary number: " + color.GREEN + bin + color.LIGHTCYAN_EX + " Decimal: " + color.GREEN + str(dec) + color.RESET)

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
  print(color.LIGHTCYAN_EX + "Original Decimal number: " + color.GREEN + dec + color.LIGHTCYAN_EX + " Binary: " + color.GREEN + str(bin) + color.RESET)
if prompt == "3":
  # checks the OS and runs a diffrent clear command if it's windows
  if platform.system == "Windows":
    os.system("cls")
  # clears the terminal
  os.system("clear")
  conv = input(color.MAGENTA + "Enter the Decimal number you would like to convert below\n: " + color.RESET)
  dec = conv
  hex = decimalToHexadecimal(conv)
  print(color.LIGHTCYAN_EX + "Original Decimal number: " + color.GREEN + dec + color.LIGHTCYAN_EX + " Hexadecimal: " + color.GREEN + str(hex) + color.RESET)
if prompt == "4":
  # checks the OS and runs a diffrent clear command if it's windows
  if platform.system == "Windows":
    os.system("cls")
  # clears the terminal
  os.system("clear")
  
# Exits the program.
if prompt == "7":
  sys.exit(color.RED + "Closing Program")

# checks if the "prompt" variable is greater than 3 and if it is closes the program.
if prompt == int(prompt)<4:
  sys.exit(color.RED + "Please restart the program and choose a valid option [1-3]")