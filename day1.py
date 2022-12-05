
max = 0
elf = 0

with open('input1.txt', 'r') as f:
    sum = 0
    for line in f:
        cal = line.strip()
        # check if line is empyty
        if not cal.strip():
            # line is empty
            if sum > max:
                max = sum
            elf += 1
            sum = 0
        else:
            sum += int(cal)
    print('Max Calories: ', max)
    print('Elf:', elf)