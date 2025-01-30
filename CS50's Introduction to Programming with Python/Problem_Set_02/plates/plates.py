def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # must start with at least two letters, contain a maximum of 6 characters and a minimum of 2.
    if s[0:2].isalpha() == False or not (2 <= len(s) <= 6):
        return False

    # no periods, spaces, or punctuation marks are allowed
    invalid_inputs = ["!", ",", ".", "?", " "]
    for char in s:
        if char in invalid_inputs:
            return False

    #Numbers cannot be used in the middle of a plate; they must come at the end.
    # Iterate over each character once digit is found, slice it and evaluate.
    i = 0
    while i < len(s):
        if s[i].isdigit():
            if not s[i:].isdigit():
                return False
            else:
                break
        i += 1


    #The first number used cannot be a ‘0’. Append numbers to a list and check first element in the list.
    list_numbers = []
    for char in s:
        if char.isdigit():
            list_numbers.append(char)
            if list_numbers and list_numbers[0] == "0":
                return False


    else:
        return True


main()
