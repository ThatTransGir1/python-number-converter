import os, pyfiglet
from colorama import Fore as color

intro = color.GREEN + pyfiglet.figlet_format('Converter') + color.RESET
print(intro)
print(color.LIGHTMAGENTA_EX +
      'Created by ThatTransGir1 on https://github.com/thegamershollow' +
      color.RESET + '\n')

#decimal to binary function
def decimalToBinary(n):
  return bin(n).replace("0b", "")


#binary to decimal function
def binaryToDecimal(n):
  return int(n, 2)


#hexadecimal to binary
def hexadecimalToBinary(n):
  res = bin(int(n, 16)).zfill(8)
  return (res)


# binary to hexadecimal
def binaryToHexadecimal(n):
  num = int(n, 2)
  hex_num = hex(num)
  return (hex_num)


# decimal to hexadecimal
def decimalToHexadecimal(n):
  hexa = hex(n)
  return (hexa)


# Driver code
if __name__ == '__main__':
  # input prompt
  prompt = input(
    'Choose the option that you want:\n1. Binary to Hexadecimal\n2. Decimal to Hexadecimal\n3. Decimal to Binary\n4. Binary to Decimal\n5. Hexadecimal to Binary\n6. Hexadecimal to Decimal\n: '
  )
  if prompt == '1':
    os.system('clear')
    convPrompt = input('Binary Number: ')
    print('Binary to Hex')
    print(binaryToHexadecimal(convPrompt))
  if prompt == '2':
    os.system('clear')
    convPrompt = input('Decimal Number: ')
    convPrompt = int(convPrompt)
    print('Decimal to Hex')
    print(decimalToHexadecimal(convPrompt))
  if prompt == '3':
    os.system('clear')
    convPrompt = input('Decimal Number: ')
    convPrompt = int(convPrompt)
    print('Decimal to Binary')
    print(decimalToBinary(convPrompt))
  if prompt == '4':
    os.system('clear')
    convPrompt = input('Binary Number: ')
    print('Binary to Decimal')
    print(binaryToDecimal(convPrompt))
  if prompt == '5':
    os.system('clear')
    convPrompt = input('Hexadecimal Number: ')
    print('Hexadecimal to Binary')
    print(hexadecimalToBinary(convPrompt))
  if prompt == '6':
    os.system('clear')
    convPrompt = input('Hexadecimal Number: ')
    print('Hexadecimal to Decimal')
    print(hexadecimalToBinary(convPrompt))
