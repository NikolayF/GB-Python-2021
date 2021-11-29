factorial_number = 4
factorial_list = []

def iterator_count(num):
    count = 1
    while count < num + 1:
        factorial_list.append(count)
        if count == num + 1:
            break
        yield count
        count += 1

for el in iterator_count(factorial_number):
    print(el)

