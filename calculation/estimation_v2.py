def estimation(calculation):
    while calculation.find("(") > 0:
        calculation = is_there_brackets(calculation)

    if calculation.find("+") > 0 or calculation.find("-") >= 0:
        result = priority_4(calculation)
    elif calculation.find("*") > 0 or calculation.find("/") > 0:
        result = priority_3(calculation)
    elif calculation.find("^") > 0:
        result = priority_2(calculation)
    else:
        return int(calculation)
    return result

def is_there_brackets(calculation):
    if "(" in calculation:
        index_1 = calculation.find("(")
        index_2 = calculation.find(")")
        result = estimation(calculation[index_1+1:index_2])
        new_calculation = calculation[:index_1]+str(result)+calculation[index_2+1:]
        return new_calculation
    else:
        return calculation

def priority_4(calculation):
    if calculation.find("+") > 0:
        index = calculation.find("+")
        number_1 = estimation(calculation[:index])
        number_2 = estimation(calculation[index+1:])
        result = number_1 + number_2
    elif calculation.find("-") >= 0:
        index = calculation.find("-")
        if index == 0:
            result = estimation(calculation[index+1:]) * (-1)
        elif not calculation[index-1].isdigit():
            if calculation.find("^") > 0:
                result = priority_2(calculation)
            elif calculation.find("*") > 0 or calculation.find("/") > 0:
                result = priority_3(calculation)
        else:
            number_1 = estimation(calculation[:index])
            number_2 = estimation(calculation[index+1:])
            result = number_1-number_2
    return result

def priority_3(calculation):
    if calculation.find("*") > 0:
        index = calculation.find("*")
        number_1 = estimation(calculation[:index])
        number_2 = estimation(calculation[index+1:])
        result = number_1 * number_2
    elif calculation.find("/") > 0:
        index = calculation.find("/")
        number_1 = estimation(calculation[:index])
        number_2 = estimation(calculation[index+1:])
        result = number_1 / number_2 if number_2 != 0 else print("Делить на 0 нельзя")
    return result

def priority_2(calculation):
    index = calculation.find("^")
    number_1 = estimation(calculation[:index])
    number_2 = estimation(calculation[index+1:])
    result = number_1**number_2
    return result
