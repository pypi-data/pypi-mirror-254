def choose_type(task_type):
    match task_type:
        case 1:
            return "arrMaxLen = []\n" \
                   "for n in range(4, 1000):\n" \
                   "\ts = '1' + '2' * n\n" \
                   "\twhile '12' in s or '322' in s or '222' in s:\n" \
                   "\t\tif '12' in s:\n" \
                   "\t\t\ts = s.replace('12', '2', 1)\n" \
                   "\t\tif '322' in s:\n" \
                   "\t\t\ts = s.replace('322', '21', 1)\n" \
                   "\t\tif '222' in s:\n" \
                   "\t\t\ts = s.replace('222', '3', 1)\n" \
                   "\tarrMaxLen.append(len(s))\n"
        case 2:
            return "arrMaxSum = []\n" \
                   "summa = 0\n" \
                   "for n in range(4, 1000):\n" \
                   "\ts = '1' + '2' * n\n" \
                   "\twhile '12' in s or '322' in s or '222' in s:\n" \
                   "\t\tif '12' in s:\n" \
                   "\t\t\ts = s.replace('12', '2', 1)\n" \
                   "\t\tif '322' in s:\n" \
                   "\t\t\ts = s.replace('322', '21', 1)\n" \
                   "\t\tif '222' in s:\n" \
                   "\t\t\ts = s.replace('222', '3', 1)\n" \
                   "\tfor i in range(len(s)):\n" \
                   "\t\tsumma = summa + int(s[i])\n" \
                   "\tarrMaxSum.append(summa)\n" \
                   "\tsumma = 0\n"
