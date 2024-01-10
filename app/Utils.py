from fractions import Fraction
import re


def convert_mixed_to_simple_fraction(mixed_fraction, servings: str = "1/1"):
    parts = mixed_fraction.split()
    print(parts)
    if len(parts) == 0:
        return 0

    whole_number, fraction = parts

    if len(parts) == 2 and whole_number != " " and fraction != " " and fraction != str(0):
        # Converting mixed fraction to a simple fraction
        simple_fraction = Fraction(int(whole_number) * int(fraction.split('/')[1]) + int(fraction.split('/')[0]), int(fraction.split('/')[1]))
        scaled_fraction = Fraction(int(str(simple_fraction).split('/')[0]), int(str(simple_fraction).split('/')[1])) * Fraction(int(str(servings).split('/')[0]), int(str(servings).split('/')[1]))
        return scaled_fraction
    else:
        print("Invalid mixed fraction format")
        return Fraction(int(whole_number), 1) * Fraction(int(str(servings).split('/')[0]), int(str(servings).split('/')[1]))


def extract_number(input_string: str):
    # Using regular expression to find the integer and fraction parts
    cleaned_string = input_string.strip()
    match = re.match(r'(\d+)(?:\s+(\d+/\d+))?', cleaned_string)

    if match:
        integer_part = match.group(1)
        fraction_part = match.group(2) if match.group(2) else '0'
        return f"{integer_part} {fraction_part}"
    else:
        print("No number found in the input string.")
        return " "


def extract_string(input_string: str):

    # Using regular expression to extract the string part
    match = re.match(r'\s*\d*\s*([\w\s,()]+)', input_string)

    if match:
        extracted_string = match.group(1)
        return extracted_string
    else:
        print("No match found.")


# print(convert_mixed_to_simple_fraction(extract_number("1 1/5 tablespoons low sodium soy sauce (plus additional to taste, divided)"),"2/2"))

# extract_string("1 tablespoons low sodium soy sauce (plus additional to taste, divided)")