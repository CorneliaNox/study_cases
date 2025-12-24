def print_result(calculation):
    symbols_p34 = "+-*/"
    new_calculation = ""
    for i in calculation:
        if i in symbols_p34:
            new_calculation = new_calculation + " " + i + " "
        else:
            new_calculation = new_calculation + i
    return new_calculation
