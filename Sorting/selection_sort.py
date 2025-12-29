"""
Selection Sort: select the minimum and swap
every ith iteration, we will find ith min, and move it to ith position by swapping that specific positioned element
Ex: 
34 56 23 4 26 16 
--> step 1: found minimum at index 3, swap(arr[3], arr[0])
4 56 23 34 26 16
--> step 2: found minimum at index 5, swap(arr[5], arr[1])
4 16 23 34 26 56
--> step 3: found minimum at index 2, swap(arr[2], arr[2])
4 16 23 34 26 56
--> step 4: found minimum at index 4, swap(arr[4], arr[3])
4 16 23 26 34 56
--> step 5: found minimum at index 4, swap(arr[4], arr[4])
4 16 23 26 34 56
"""
def selection_sort(n, list_of_integers):
    
    for i in range(n):
        # considering ith position is having the minimum value
        min_index = i
        # finding the minimum value's index
        for j in range(i, n):
            if list_of_integers[j] < list_of_integers[min_index]:
                min_index = j
        # swapping the minimum values index with ith index value
        temp = list_of_integers[min_index]
        list_of_integers[min_index] = list_of_integers[i]
        list_of_integers[i] = temp
        print(list_of_integers)

if __name__ == '__main__':
    n = int(input("Enter the length of the array to be sorted: "))
    nums = list(map(int, input(f"Enter space separated {n} integers: ").split()))
    selection_sort(n, nums)
    
        