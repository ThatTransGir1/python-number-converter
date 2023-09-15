import pyfiglet, sys, os, platform
from colorama import Fore as color

#* checks the OS and runs a diffrent clear command if it's windows
if platform.system == "Windows":
  os.system("cls")
else:
  #* clears the terminal
  os.system("clear")


#* basic intro function for the program
def intro(txt, author, url):
  intro = color.GREEN + pyfiglet.figlet_format(txt)
  credit = "\n" + color.LIGHTMAGENTA_EX + "Created by " + author + " on " + url + color.RESET + "\n"
  return print(intro + credit)


intro("Converter", "ThatTransGir1", "https://github.com/thattransgir1")

#* dictionary of decimal to binary converted numbers
hexListD = {
  0: '0',
  1: '1',
  2: '2',
  3: '3',
  4: '4',
  5: '5',
  6: '6',
  7: '7',
  8: '8',
  9: '9',
  10: 'A',
  11: 'B',
  12: 'C',
  13: 'D',
  14: 'E',
  15: 'F'
}
hexListH = {
  '0': 0,
  '1': 1,
  '2': 2,
  '3': 3,
  '4': 4,
  '5': 5,
  '6': 6,
  '7': 7,
  '8': 8,
  '9': 9,
  'A': 10,
  'B': 11,
  'C': 12,
  'D': 13,
  'E': 14,
  'F': 15
}


#* binary to decimal convert function
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
    print(color.LIGHTCYAN_EX + "Power of 2: " + color.GREEN + str(placeVal) +
          color.RESET)
    #* prints the solution of above
    print(color.LIGHTCYAN_EX + "Answer: " + color.GREEN + str(decVal) + "\n")
  return decVal


#* decimal to binary convert function
def decimalToBinary(n):
  if (int(n) <= 1):
    return n
  #* creates an empty string
  binVal = ''
  #* sets 'decRem' to n as an integer
  decRem = int(n)
  #* while 'decRem' is greater than 0
  while decRem > 0:
    #* divides the 'decRem' variable by 2 to get the remainder
    binVal = str(decRem % 2) + binVal
    #* divides the 'decRem' variable by 2 to get the quotient
    decRem = decRem // 2
    #* prints the remainder
    print(color.LIGHTCYAN_EX + "Remainder: " + color.GREEN + str(binVal) +
          color.RESET)
    #* prints the quotient
    print(color.LIGHTCYAN_EX + "Quotient: " + color.GREEN + str(decRem) +
          color.RESET + "\n")
  return binVal


# hexadecimal to decimal convert function
def hexadecimalToDecimal(n):
  decimal = 0
  length = len(n) - 1
  for digit in n:
    decimal += hexListH[digit] * 16**length
    length -= 1
  return decimal


#* decimal to hexadecimal convert function
def decimalToHexadecimal(n):
  hexadecimal = ''
  while (n > 0):
    remainder = n % 16
    hexadecimal = hexListD[remainder] + hexadecimal
    n = n // 16
  return hexadecimal


#* restart prompt
def restart():
  p = input(color.LIGHTCYAN_EX + "Restart the Program?" + color.LIGHTRED_EX +
            " [Y/N]\n: ")
  if p == "y" or p == "Y":
    os.system("python3 2.0.py")


#* the begining prompt
prompt = input(
  color.LIGHTRED_EX + "\nType a number corrasponding to an option below" +
  color.LIGHTRED_EX + " [1-7]." + color.LIGHTCYAN_EX +
  "\n\n1. Binary to Decimal\n2. Decimal to Binary\n3. Hexadecimal to Decimal\n4. Decimal to Hexadecimal\n5. Binary to Hexadecimal\n6. Hexadecimal to Binary\n7. Close\n: "
  + color.RESET)

#* converts the inputed binary into decimal and prints the output
if prompt == "1":
  #* checks the OS and runs a diffrent clear command if it's windows
  if platform.system == "Windows":
    os.system("cls")
  #* clears the terminal
  os.system("clear")
  #* asks for a binary(base2) number that will be converted into decimal(base10)
  conv = input(color.MAGENTA +
               "Enter the Binary number you would like to convert below\n: " +
               color.RESET)
  Bin = conv
  Dec = binaryToDecimal(conv)
  #* prints the output from the decimal to binary conversion
  print(color.LIGHTCYAN_EX + "Original Binary: " + color.GREEN + Bin +
        color.LIGHTCYAN_EX + "\nSolution: " + color.LIGHTGREEN_EX + str(Dec) +
        color.RESET)
  restart()

# converts the inputed decimal into binary and prints the output
if prompt == "2":
  #* checks the OS and runs a diffrent clear command if it's windows
  if platform.system == "Windows":
    os.system("cls")
  #* clears the terminal
  os.system("clear")
  #* asks for a binary(base2) number that will be converted into decimal(base10)
  conv = input(color.MAGENTA +
               "Enter the Decimal number you would like to convert below\n: " +
               color.RESET)
  Dec = conv
  Bin = decimalToBinary(conv)
  #* prints the output from the decimal to binary conversion
  print(color.LIGHTCYAN_EX + "Original Decimal: " + color.GREEN + Dec +
        color.LIGHTCYAN_EX + "\nSolution: " + color.LIGHTGREEN_EX + str(Bin) +
        color.RESET)
  restart()

#* converts inputed hexadecimal into decimal and prints the output
if prompt == "3":
  if platform.system == "Windows":
    os.system("cls")
  os.system("clear")
  conv = input(
    color.MAGENTA +
    "Enter the Hexadecimal number you would like to convert below\n: " +
    color.RESET)
  Hex = conv
  Dec = hexadecimalToDecimal(conv)
  print(color.LIGHTCYAN_EX + "Original Hexadecimal: " + color.GREEN + Hex +
        color.LIGHTCYAN_EX + "\nSolution: " + color.LIGHTGREEN_EX + str(Dec) +
        color.RESET)
  restart()

#* converts inputed decimal into hexadecimal and prints the output
if prompt == "4":
  if platform.system == "Windows":
    os.system("cls")
  os.system("clear")
  conv = input(color.MAGENTA +
               "Enter the Decimal number you would like to convert below\n: " +
               color.RESET)
  Dec = conv
  Hex = decimalToHexadecimal(int(conv))
  print(color.LIGHTCYAN_EX + "Original Hexadecimal: " + color.GREEN + Dec +
        color.LIGHTCYAN_EX + "\nSolution: " + color.LIGHTGREEN_EX + str(Hex) +
        color.RESET)
  restart()

#* converts the inputed binary into hexadecimal
if prompt == "5":
  if platform.system == "Windows":
    os.system("cls")
  os.system("clear")
  conv = input(color.MAGENTA +
               "Enter the Binary number you would like to convert below\n: " +
               color.RESET)
  Bin = conv
  Dec = binaryToDecimal(conv)
  Hex = decimalToHexadecimal(int(Dec))
  print(color.LIGHTCYAN_EX + "Original Binary: " + color.GREEN + Bin +
        color.LIGHTCYAN_EX + "\nSolution: " + color.LIGHTGREEN_EX + str(Hex) +
        color.RESET)
  restart()

#* converts the inputed binary into hexadecimal
if prompt == "6":
  if platform.system == "Windows":
    os.system("cls")
  os.system("clear")
  conv = input(
    color.MAGENTA +
    "Enter the Hexadecimal number you would like to convert below\n: " +
    color.RESET)
  Hex = conv
  Dec = hexadecimalToDecimal(conv)
  Bin = decimalToBinary(Dec)
  print(color.LIGHTCYAN_EX + "Original Binary: " + color.GREEN + Hex +
        color.LIGHTCYAN_EX + "\nSolution: " + color.LIGHTGREEN_EX + str(Bin) +
        color.RESET)
  restart()

#* Exits the program.
if prompt == "7":
  sys.exit(color.RED + print("Closing Program") + color.RESET)

#* checks if the "prompt" variable is greater than 3 and if it is closes the program.
if int(prompt) == int(prompt) > 7:
  sys.exit(
    print(color.RED + "Please restart the program and choose a valid option " +
          color.LIGHTGREEN_EX + "[1-7]" + color.RESET))
