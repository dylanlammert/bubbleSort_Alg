import matplotlib.pyplot as plt
import random


# bubble sort function
def bubble_alg(array):
    for i in range(n):
        for j in range(0, n - i - 1):
            # placing values on a bar chart
            plt.bar(plotvalues, random_numbers)
            plt.pause(.000001)
            plt.clf()
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
            
# size of the array
n = 50
plotvalues = list(range(1, n + 1))
# print(plotvalues)
    
# generate n number of random numbers for the array
random_numbers = [random.randint(1,100) for x in range (n)]
print("\n")
print("Unsorted " + str(n) + " numbers")
print(random_numbers)
print("\n")
bubble_alg(random_numbers)
print("Sorted " + str(n) + " numbers")
print(random_numbers)

