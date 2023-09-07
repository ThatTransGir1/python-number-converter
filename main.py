import pyfiglet, sys, os, platform, re
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

# checks if inputed number is a valid decimal
Dec = re.compile(r'[0-9]{7}[\S\D\W]{1}[0-9]+$')

# checks if inputed number is valid binary
Bin = re.compile('[^01]')

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
    print(color.LIGHTCYAN_EX + "Ans: " + color.GREEN + str(decVal))
    placeVal *= 2
    print(color.LIGHTCYAN_EX + "" + color.GREEN + str(placeVal) + color.RESET)
  return decVal

# decimal to binary convert function
def decimalToBinary(n):
  # checks if the inputed string is a valid decimal
  if Dec.match(str(n)) == False:
    return "Input must be a decimal number string [0-9]"
  if (int(n) <= 1):
    return n
  # creates an empty string
  binVal = ''
  # sets decRem to n as an integer
  decRem = int(n)
  # while decRem is greater than 0 
  while decRem > 0:
    binVal = str(decRem % 2) + binVal
    print(color.LIGHTCYAN_EX + "Remainder: " + color.GREEN + str(binVal) + color.RESET)
    decRem = decRem // 2
    print(color.LIGHTCYAN_EX + "" + color.GREEN + str(decRem) + color.RESET)
  return binVal

prompt = input(color.LIGHTCYAN_EX + "\n1. Binary to Decimal\n2. Decimal to Binary\n3. Close\n: " + color.RESET)

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
  print(color.LIGHTCYAN_EX + "Original Binary: " + color.GREEN + bin + color.LIGHTCYAN_EX + "\nSolution: " + color.GREEN + str(dec) + color.RESET)

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
  print(color.LIGHTCYAN_EX + "Original Decimal: " + color.GREEN + dec + color.LIGHTCYAN_EX + "\nSolution: " + color.GREEN + str(bin) + color.RESET)

# Exits the program.
if prompt == "3":
  sys.exit(color.RED + "Closing Program" + color.RESET)

# checks if the "prompt" variable is greater than 3 and if it is closes the program.
if prompt == int(prompt)<3:
  sys.exit(color.RED + "Please restart the program and choose a valid option [1-3]" + color.RESET)