def choose_type(task_type):
    match task_type:
        case 1:
            return "from itertools import product\n" \
                   "words = list(product('letters', repeat=amount))\n" \
                   "print(*words[number-1])\n"
        case 2:
            return "letters = ''\n" \
                   "cnt = 0\n" \
                   "for x1 in letters:\n" \
                   "\tfor x2 in letters:\n" \
                   "\t\tfor x3 in letters:\n" \
                   "\t\t\tr = x1 + x2 + x3\n" \
                   "\t\t\tif r.count('letter') == amount:\n" \
                   "\t\t\t\tcnt += 1\n"
        case _:
            return "no such type"
