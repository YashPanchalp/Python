
def octal_to_decimal(octal):
    decimal = 0
    power = 0
    while octal > 0:
        remainder = octal % 10
        decimal += remainder * (8 ** power)
        octal //= 10
        power += 1
    return decimal
    
def decimal_to_hexadecimal(decimal):
    if decimal == 0:
        return "0"
    
    hex_digits = "0123456789ABCDEF"
    hexadecimal = ""
    
    while decimal > 0:
        remainder = decimal % 16
        hexadecimal = hex_digits[remainder] + hexadecimal
        decimal //= 16
    
    return hexadecimal


def octal_to_hexadecimal(octal):
    # octal to decimal
    decimal = octal_to_decimal(octal)
    
    # decimal to hexadecimal
    hexadecimal = decimal_to_hexadecimal(decimal)
    
    return hexadecimal

# Example usage
octal_number = int(input("Enter an octal number: "))
hexadecimal_number = octal_to_hexadecimal(octal_number)
print(f"The hexadecimal representation is: {hexadecimal_number}")
