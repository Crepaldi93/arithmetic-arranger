test_1 = ['3801 - 2', '123 + 49']

test_2 = ['1 + 2', '1 - 9380']

test_3 = ['3 + 855', '3801 - 2', '45 + 43', '123 + 49']

test_4 = ['11 + 4', '3801 - 2999', '1 + 2', '123 + 49', '1 - 9380']

test_5 = ['3 + 855', '988 + 40']

test_6 = ['32 - 698', '1 - 3801', '45 + 43', '123 + 49', '988 + 40']


def arithmetic_arranger(problems, show_answers=False):


    # Variable where the problems are to be arranged later

    arranged_problems = ""

    # Lists where operands, operands' lenght, operators and results are to be put in in order to be organised

    top_operands = []

    bottom_operands = []

    operators = []

    widths = []

    results = []


    length = len(problems)

    # Returns Error message if the "problems" list has more than 5 elements

    if length > 5:
        return "Error: Too many problems."


    # Splits list elements into numbers and operations

    for problem in problems:
        parts = problem.split()
        number_one = parts[0]
        number_two = parts[2]
        operator = parts[1]


        # Returns Error message if operators are other than + or -

        if operator not in "+-":
            return "Error: Operator must be '+' or '-'."


        # Returns Error message if number_1 or number_2 are not integers

        try:
            number_1 = int(number_one)
            number_2 = int(number_two)

        except ValueError:
            return "Error: Numbers must only contain digits."


        # Returns Error message if any of the operands has more than four digits

        if len(number_one) > 4 or len(number_two) > 4:
            return "Error: Numbers cannot be more than four digits."


        # Sets the value of wid to the length of the longer operand

        width = max(len(number_one), len(number_two))


        # Right align the operands

        number_one = number_one.rjust(width)

        number_two = number_two.rjust(width)


        # Calculates the result of the operations

        if operator == "+":
            result = str(int(number_one) + int(number_two))

        else:
            result = str(int(number_one) - int(number_two))


        # Appends data to lists in order to organise the strings

        top_operands.append(number_one)

        bottom_operands.append(number_two)

        operators.append(operator)

        widths.append(width)

        results.append(result)

    # Line 1

    line_1 = ""

    for num in top_operands:
        line_1 = line_1 + "  " + num + "    "


    # Line 2

    line_2 = ""

    for index, value in enumerate(bottom_operands):
        line_2 = line_2 + operators[index] + " " + value + "    "


    # Line 3

    line_3 = ""

    for num in widths:
        line_3 = line_3 + (2 + num)*"-" + "    "

    # Line 4

    line_4 = ""


    for ind, val in enumerate(results):
        line_4 = line_4 + val.rjust(2 + widths[ind]) + "    "


    # Arranges lines

    if show_answers == True:
        arranged_problems = line_1.rstrip() + "\n" + line_2.rstrip() + "\n" + line_3.rstrip() + "\n" + line_4.rstrip()

    else:
        arranged_problems = line_1.rstrip() + "\n" + line_2.rstrip() + "\n" + line_3.rstrip()


    # return arranged_problems

    print(arranged_problems)


arithmetic_arranger(test_1)

arithmetic_arranger(test_2)

arithmetic_arranger(test_3)

arithmetic_arranger(test_4)

arithmetic_arranger(test_5, True)

arithmetic_arranger(test_6, True)
















    # return arranged_problems
