# Pertemuan 8
# linearsearch
def linear_search(keyword, data):
    for i in range(len(data)):
        if str(data[i]).lower() == keyword.lower():
            print(f"Keyword {keyword} has found at index {i}")
            return i
    print(f"Keyword {keyword} not found")
    return -1
data = [23, 3, 4, 78, 9, 10, 32]
keyword = input("Input Keyword:")
linear_search(keyword, data)

# BinerSearch
def bubble_sort(keyword, data):
    for i in range(len(data)):
        for j in range(len(data) - i - 1):
            if str(data[j]).lower() > str(data[j+1]).lower():
                data[j], data[j+1] = data[j+1], data[j]
    return binary_search(keyword, data)

def binary_search(keyword, data):
    left = 0
    right = len(data) - 1

    while left <= right:
        mid = (left + right) // 2
        if str(data[mid]).lower() > keyword.lower():
            right = mid - 1
        elif str(data[mid]).lower() < keyword.lower():
            left = mid + 1
        else:
            print(data)
            print(f"Keyword {keyword} has been found at index {mid}")
            return mid

    print(f"Keyword {keyword} not found")
    return -1

data = [23, 3, 4, 78, 9, 10, 32]
keyword = input("Input keyword: ")
bubble_sort(keyword, data)

# Tugas 1
def linear_search(keyword, data):
    for i in range(len(data)):
        if str(data[i]).lower() == keyword.lower():
            print(f"Keyword {keyword} has found at index {i}")
            return i
    print(f"Keyword {keyword} not found")
    return -1

data = ['R 2477 SR', 'R 1234 DJ', 'R 7015 LP', 'R 0201 RR', 
        'R 3304 DA', 'R 2401 SK', 'R 2103 RT', 'R 1708 RI', 'R 1111 SR',
          'R 4987 LH']
keyword = input("Input keyword: ")
linear_search(keyword, data)

# Tugas 2
def bubble_sort(keyword, data):
    for i in range(len(data)):
        for j in range(len(data) - i - 1):
            if str(data[j]).lower() > str(data[j+1]).lower():
                data[j], data[j+1] = data[j+1], data[j]
    return binary_search(keyword, data)

def binary_search(keyword, data):
    left = 0
    right = len(data) - 1

    while left <= right:
        mid = (left + right) // 2
        if str(data[mid]).lower() > keyword.lower():
            right = mid - 1
        elif str(data[mid]).lower() < keyword.lower():
            left = mid + 1
        else:
            print(data)
            print(f"Keyword {keyword} has been found at index {mid}")
            return mid

    print(f"Keyword {keyword} not found")
    return -1

data = [20103023, 20103002, 20103019, 20103001, 20103017, 20103005, 20103011, 20103003, 20103009, 20103021, 20103006, 20103015, 20103013, 20103007]
keyword = input("Input keyword: ")
bubble_sort(keyword, data)

# Tugas 3
def bubble_sort(keyword, data):
    for i in range(len(data)):
        for j in range(len(data) - i - 1):
            if str(data[j]).lower() > str(data[j+1]).lower():
                data[j], data[j+1] = data[j+1], data[j]
    return binary_search(keyword, data)

def binary_search(keyword, data):
    left = 0
    right = len(data) - 1

    while left <= right:
        mid = (left + right) // 2
        if str(data[mid]).lower() > keyword.lower():
            right = mid - 1
        elif str(data[mid]).lower() < keyword.lower():
            left = mid + 1
        else:
            print(data)
            print(f"Keyword {keyword} has been found at index {mid}")
            return mid

    print(f"Keyword {keyword} not found")
    return -1

data = [17, 2, 15, 7, 72, 31, 12, 57, 63, 71, 23, 92, 1 ]
keyword = input("Input keyword: ")
bubble_sort(keyword, data)