# Python code​​​​​​‌‌​‌‌​‌​​​‌​​​‌​‌​​​​‌‌‌‌ below
hexNumbers = {
    '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
    'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15
}

# Converts a string hexadecimal number into an integer decimal
# If hexNum is not a valid hexadecimal number, returns None
def hexToDec(hexNum):

    for char in hexNum:
        if char not in hexNumbers:
            return None
    
    if len(hexNum)==1:
        result = ((hexNumbers[hexNum[0]])*(16**0))
        return result
    
    if len(hexNum)==2:
        result = (((16**1)*(hexNumbers[hexNum[0]]))+((hexNumbers[hexNum[1]])*(16**0)))
        return result
    
    if len(hexNum)==3:
        result = (((16**2)*(hexNumbers[hexNum[0]]))+((16**1)*(hexNumbers[hexNum[1]]))+((hexNumbers[hexNum[2]])*(16**0)))
        return result
    
    if len(hexNum)==4:
        result = (((16**3)*(hexNumbers[hexNum[0]]))+((16**2)*(hexNumbers[hexNum[1]]))+((16**1)*(hexNumbers[hexNum[2]]))+((hexNumbers[hexNum[3]])*(16**0)))
        return result
    

print(hexToDec('B2A5'))
print(hexToDec('B2A'))
print(hexToDec('B2'))
