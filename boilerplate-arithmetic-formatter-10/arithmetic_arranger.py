def arithmetic_arranger(problems, show_answers=False):
    
    if len(problems) > 5:
        return "Error: Too many problems."

    arranged_problems = {"top": [], "bottom": [], "line": [], "result": []}

    for problem in problems:
        
        operands = problem.split()

        if len(operands) != 3:
            return "Error: Invalid problem format."

        num1, operator, num2 = operands

        if not num1.isdigit() or not num2.isdigit():
            return "Error: Numbers must only contain digits."

        if operator not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."

        if len(num1) > 4 or len(num2) > 4:
            return "Error: Numbers cannot be more than four digits."

        max_width = max(len(num1), len(num2)) + 2

        formatted_num1 = num1.rjust(max_width)
        formatted_num2 = operator + num2.rjust(max_width - 1)

        line = '-' * max_width

        arranged_problems["top"].append(formatted_num1)
        arranged_problems["bottom"].append(formatted_num2)
        arranged_problems["line"].append(line)

        if show_answers:
            if operator == '+':
                result = str(int(num1) + int(num2))
            else:
                result = str(int(num1) - int(num2))
            result = result.rjust(max_width)
            arranged_problems["result"].append(result)

    arranged_problems_output = (
        "    ".join(arranged_problems["top"]) + "\n" +
        "    ".join(arranged_problems["bottom"]) + "\n" +
        "    ".join(arranged_problems["line"])
    )
    
    if show_answers:
        arranged_problems_output += "\n" + "    ".join(arranged_problems["result"])

    return arranged_problems_output


problems2 = ["45 + 10", "99 - 456", "8181 + 8182", "123 - 111"]
print(arithmetic_arranger(problems2, True))