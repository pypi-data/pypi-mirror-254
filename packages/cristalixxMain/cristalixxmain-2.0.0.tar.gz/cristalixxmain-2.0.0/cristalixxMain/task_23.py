def choose_type(task_type):
    match task_type:
        case 1:
            return "def f(x, y):\n" \
                   "\tif x > y:\n" \
                   "\t\treturn False\n" \
                   "\tif x == y:\n" \
                   "\t\treturn True\n" \
                   "\telse:\n" \
                   "\t\treturn f(x + number, y) + f(x + number, y)\n" \
                   "print(f(number1, number2) * f(number2, number3))\n"
        case 2:
            return "def f(x, y):\n" \
                   "\tif x > y or x == forbidden number:\n" \
                   "\t\treturn False\n" \
                   "\tif x == y:\n" \
                   "\t\treturn True\n" \
                   "\telse:\n" \
                   "\t\treturn f(x + number, y) + f(x + number, y)\n" \
                   "print(f(number1, number2) * f(number2, number3))\n"
