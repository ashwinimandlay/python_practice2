# greatest number finder function
def greatest_number(numbers):
    max = numbers[0]
    for number in numbers:
        if number > max:
            max = number
    return max


# shadow built in warning means it is already defined
# in the python