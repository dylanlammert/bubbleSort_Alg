import random


# bubble sort function
def bubble_alg(array):
    for i in range(n):
        for j in range(0, n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
            
# size of the array
n = 10
# generate n number of random numbers for the array
random_numbers = [random.randint(1,100) for x in range (n)]
print("\n")
print("Unsorted " + str(n) + " numbers")
print(random_numbers)
print("\n")
bubble_alg(random_numbers)
print("Sorted " + str(n) + " numbers")
print(random_numbers)

