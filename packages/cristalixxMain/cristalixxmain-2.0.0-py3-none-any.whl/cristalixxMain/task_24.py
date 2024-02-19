def choose_type(task_type):
    match task_type:
        case 1:
            return "s = open('*file').readline()\n" \
                   "cnt = 0, arr = []\n" \
                   "for i in range(len(s) - 1):\n" \
                   "\tif s[i] <= s[i + 1]:\n" \
                   "\t\tcnt += 1\n" \
                   "\telif s[i] > s[i + 1]:\n" \
                   "\t\tarr.append(cnt)\n" \
                   "\t\tcnt = 1\n" \
                   "print(max(arr))\n"
        case 2:
            return "s = open('*file').readline()\n" \
                   "cnt = 0, arr = []\n" \
                   "s = s.replace('some letters', 'some numbers')\n" \
                   "for i in range(len(s)):\n" \
                   "\tif s[i] == '1':\n" \
                   "\t\tcnt = 1\n" \
                   "\t\tfor j in range(i + 1, len(s)):\n" \
                   "\t\t\tif s[j] == '1':\n" \
                   "\t\t\t\tcnt += 1\n" \
                   "\t\t\telse:\n" \
                   "\t\t\t\tarr.append(cnt)\n" \
                   "\t\t\t\tbreak\n" \
                   "print(max(arr))"
        case 3:
            return "s = open('*file').readline()\n" \
                   "cnt = 0, arr = []\n" \
                   "s = s.replace('some letters combinations', '*')\n" \
                   "s = s.replace('some letters combinations', '*')\n" \
                   "s = s.replace('some letters combinations', '*')\n" \
                   "for i in range(len(s)):\n" \
                   "\tif s[i] != '*':\n" \
                   "\t\tcnt += 1\n" \
                   "\tif s[i] == '*':\n" \
                   "\t\tarr.append(cnt)\n" \
                   "\t\tcnt = 0\n" \
                   "print(max(arr))\n"
        case _:
            return "no such type"
