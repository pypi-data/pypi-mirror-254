def convert_to_system(number, base):
    letters = '0123456789ABCDEF'
    new = ''

    while number > 0:
        number, remainder = divmod(number, base)
        new = letters[remainder] + new

    return new


def digit_action(number, action):
    match action:
        case 'sum':
            number = str(number)
            summa = 0
            for digit in number:
                summa += int(digit)
            return summa
        case 'mult':
            number = str(number)
            mult = 1
            for digit in number:
                mult *= int(digit)
            return mult
        case _:
            return "404 action"
