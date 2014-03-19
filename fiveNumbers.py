#add the list of five numbers

def total (fiveNumbers):
    total = fiveNumbers[0]
    fiveNumbers = fiveNumbers[1:]
    for item in fiveNumbers:
        total = total + item
    return (total)