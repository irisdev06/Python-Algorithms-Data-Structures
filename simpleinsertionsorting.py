def insertion_sort(list):
    for i in range(1, len(list)):
        j = i 
        while list[j - 1] > list[j] and j > 0:
            list[j  - 1], list[j] = list[j], list[j - 1]
            j -= 1
            print(list)

list = [2, 5, 6, 1, 3, 4]
insertion_sort(list)
