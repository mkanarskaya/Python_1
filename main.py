with open("numbers.txt", 'w') as file:
    numbers = list(range(10 ** 7 + 1))
    numbers[1] = 0
    for i in numbers:
        if i > 1:
            for j in range(i+i, len(numbers), i):
                numbers[j] = 0
    numbers = list(set(numbers))
    numbers.sort()
    file.write('{}\n'.format(numbers))
