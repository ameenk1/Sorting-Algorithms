#MUHAMMAD AMEEN KASHIF G21097717

import random # required for the random number generator only
import time

count = 0 #comparison count for sorting methods

def GenerateNumbers(size):
    minValue = 100000 #minimum value of an element inside the array
    maxValue = 999999 #maximum value of an element inside the array
    array = []
    while len(array) < size:
        randomGenerate =random.randint(minValue,maxValue)
        if randomGenerate not in array:
            array.append(randomGenerate)
    return array

def SelectionSort(array):
    
    global count
    max = len(array)
    
    for i in range (max):
        min = i;
        for j in range(i + 1, max):
            count += 1 # adds one to each comparison made
            if array[j] < array[min]:
                min = j

        array[i], array[min] = array[min], array[i]

def MergeSort(array):

    global count
    if len(array) > 1:
        #defining the variables required to divide the numbers for sorting
        middle = len(array) // 2  #Getting the middle value for the sorting proccess
        leftSide = array[:middle] # values before the middle gets seperated 
        rightSide = array[middle:]

        MergeSort(leftSide)
        MergeSort(rightSide)

        i = j = k = 0
        
        while i < len(leftSide) and j < len(rightSide):# ensures that there are values to sort from
            count += 1
            if leftSide[i] < rightSide[j]:
                array[k] = leftSide[i]
                i += 1
            else:
                array[k] = rightSide[j]
                j += 1
            k += 1

        # Copy any remaining elements from leftSide
        while i < len(leftSide):
            array[k] = leftSide[i]
            i += 1
            k += 1

        # Copy any remaining elements from rightSide
        while j < len(rightSide):
            array[k] = rightSide[j]
            j += 1
            k += 1

def QuickSort(array, low, high):
    global count
    if low< high:
        i = low
        j = high
        pivot = array[low]

        
        while i <= j: #ensuring the code runs till the moment they cross
            count += 1
            while i <= j and array[i] <= pivot:
                i += 1
            while i <= j and array[j] > pivot:
                j -= 1
            #i and j swap
            if i < j:
                array[i], array[j] = array[j], array[i]
        #pivot swap
        array[low], array[j] = array[j], array[low]

        #sorting the sub arrays 
        QuickSort(array, low, j-1)
        QuickSort(array, j+1, high)
        
# writing the sorted arrays into a file
def sortArrayFile(file, sortedArray, arraySize, sortType):
    print(f"Array of size {arraySize} ({sortType} Sort):", file=file)
    print(sorted_array, file=file)
    print("\n", file=file)

def sortArrayFile(sortedArray, arraySize, sortType):
    filename = f"{sortType}_sorted_arrays.txt"
    with open(filename, "a") as file:
        print(f"Array of size {arraySize} ({sortType} Sort):", file=file)
        print(sortedArray, file=file)
        print("\n", file=file)
    
            
#SCreating array & copies to maintain data intergrity  
arrayOneHundred = GenerateNumbers(100)
arrayOneThousand = GenerateNumbers(1000)
arrayTenThousand = GenerateNumbers(10000)

SelectionArrayOneHundred = arrayOneHundred.copy()
SelectionArrayOneThousand = arrayOneThousand.copy()
SelectionArrayTenThousand = arrayTenThousand.copy()

MergeArrayOneHundred = arrayOneHundred.copy()
MergeArrayOneThousand = arrayOneThousand.copy()
MergeArrayTenThousand = arrayTenThousand.copy()

QuickArrayOneHundred = arrayOneHundred.copy()
QuickArrayOneThousand = arrayOneThousand.copy()
QuickArrayTenThousand = arrayTenThousand.copy()


#selection Sort
print("------------------------------------\n       Selection Sort Timings \n------------------------------------")
startTime = time.time()
SelectionSort(SelectionArrayOneHundred)
endTime = time.time()
timeTaken = (endTime - startTime) * 1000 
print(f"Array of size 100: {timeTaken} milliseconds")
print(f"Total comparison count: {count}")

count = 0  # Reset count for each sort
startTime = time.time()
SelectionSort(SelectionArrayOneThousand)
endTime = time.time()
timeTaken = (endTime - startTime) * 1000 
print(f"Array of size 1000: {timeTaken} milliseconds")
print(f"Total comparison count: {count}")

count = 0  
startTime = time.time()
SelectionSort(SelectionArrayTenThousand)
endTime = time.time()
timeTaken = (endTime - startTime) * 1000 
print(f"Array of size 10,000: {timeTaken} milliseconds")
print(f"Total comparison count: {count}")

#Merge Sort
print("------------------------------------\n       Merge Sort Timings \n------------------------------------")
count = 0
startTime = time.time()
MergeSort(MergeArrayOneHundred)
endTime = time.time()
timeTaken = (endTime - startTime) * 1000 
print(f"Array of size 100: {timeTaken} milliseconds")
print(f"Total comparison count: {count}")

count = 0
startTime = time.time()
MergeSort(MergeArrayOneThousand)
endTime = time.time()
timeTaken = (endTime - startTime) * 1000 
print(f"Array of size 1000: {timeTaken} milliseconds")
print(f"Total comparison count: {count}")

count = 0
startTime = time.time()
MergeSort(MergeArrayTenThousand)
endTime = time.time()
timeTaken = (endTime - startTime) * 1000 
print(f"Array of size 10,000: {timeTaken} milliseconds")
print(f"Total comparison count: {count}")

#Quick Sort

print("------------------------------------\n       Quick Sort Timings \n------------------------------------")
count = 0
startTime = time.time()
QuickSort(QuickArrayOneHundred, 0, len(QuickArrayOneHundred)-1)
endTime = time.time()
timeTaken = (endTime - startTime) * 1000 
print(f"Array of size 100: {timeTaken} milliseconds")
print(f"Total comparison count: {count}")

count = 0
startTime = time.time()
QuickSort(QuickArrayOneThousand, 0, len(QuickArrayOneThousand)-1)
endTime = time.time()
timeTaken = (endTime - startTime) * 1000 
print(f"Array of size 1000: {timeTaken} milliseconds")
print(f"Total comparison count: {count}")

count = 0
startTime = time.time()
QuickSort(QuickArrayTenThousand, 0, len(QuickArrayTenThousand)-1)
endTime = time.time()
timeTaken = (endTime - startTime) * 1000 
print(f"Array of size 10,000: {timeTaken} milliseconds")
print(f"Total comparison count: {count}")

#Sorted array to text file
sortArrayFile(SelectionArrayOneHundred,  100, "Selection")
sortArrayFile(SelectionArrayOneThousand, 1000, "Selection")
sortArrayFile(SelectionArrayTenThousand, 10000, "Selection")

sortArrayFile(MergeArrayOneHundred,  100, "Merge")
sortArrayFile(MergeArrayOneThousand, 1000, "Merge")
sortArrayFile(MergeArrayTenThousand, 10000, "Merge")

sortArrayFile(QuickArrayOneHundred,  100, "Quick")
sortArrayFile(QuickArrayOneThousand, 1000, "Quick")
sortArrayFile(QuickArrayTenThousand, 10000, "Quick")
