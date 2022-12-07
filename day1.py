
max = []

with open('input1.txt', 'r') as f:
    Sum = 0
    for line in f:
        cal = line.strip()
        # check if line is empyty
        if not cal.strip():
            # line is empty
            if len(max) >= 3:
                if max[2] < Sum:
                    max[2] = Sum
                    max.sort(reverse=True)
            else:
                max.append(Sum)
                max.sort(reverse=True)
            Sum = 0
        else:
            Sum += int(cal)
    print('Top 3: ', max)
    print('Total: ', sum(max))