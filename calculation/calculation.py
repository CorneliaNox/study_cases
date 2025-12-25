import estimation_v2
import printing


def calculation(calculation):
        if calculation.isdigit():
            return calculation
        else:
            return estimation_v2.estimation(calculation)

def main():
    case_input = input("Введите пример: ")

    case = case_input.split()
    case = ''.join(case)

    if any(c.isalpha() for c in case):
        print("В примере есть буквы")
    else:
        result = calculation(case)
        print(printing.print_result(case), " = ", result)

main()