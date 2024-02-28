# Linear Search
def linear_search_unsorted(arr, target):
    sort = sorted(arr)
    count = 0
    for num in sort:
        count +=1
        if num == target:
            return count, count
  

# Binary Search


def binary_search_unsorted(arr, target):
    sort =sorted(arr)
    count = 0
    left = 0
    right = len(arr)-1
    while left<=right:
        count +=1
        mid = (left+right) // 2
        if sort[mid] == target:
            return ([mid], count)
        elif sort[mid] < target:
            left = mid + 1
        elif sort[mid] > target:
            right = mid - 1

# Scenario 1 Test
unsorted_list = [42, 15, 7, 30, 22, 10, 18]

target_1 = 30
result_linear_search_1 = linear_search_unsorted(unsorted_list, target_1)
result_binary_search_1 = binary_search_unsorted(sorted(unsorted_list), target_1)
# print(f"Scenario 1 (Linear Search): Target {target_1} found at index {result_linear_search_1[0]} in {result_linear_search_1[1]} steps.")
# print(f"Scenario 1 (Binary Search): Target {target_1} found at index {result_binary_search_1[0]} in {result_binary_search_1[1]} steps.")
# print(linear_search_unsorted(unsorted_list, target_1))
# print(binary_search_unsorted(unsorted_list, target_1))

# print(unsorted_list[30])

# # **Scenario 2: Finding a Word in a Sorted List**

# You have a sorted list of words. Write two functions, one for linear search and one for binary search, to find a specific word in the list. Provide a return value that includes the answer and the number of steps the program took to encounter the answer.


# Linear Search
def linear_search_sorted_words(word_list, target_word):
    count = 0
    for index, word in enumerate(word_list):
        count += 1
        if word == target_word:
            return index, count
    return -1, count
       
# Binary Search
def binary_search_sorted_words(word_list, target_word):
   steps = 0
   left = 0
   right = len(word_list)-1
   while left<=right:
       steps +=1
       mid = (left + right) // 2
       if word_list[mid] == target_word:
           return mid, steps
       elif word_list[mid] < target_word:
           left = mid+1
       elif word_list[mid] > target_word:
           right = mid-1
   return -1, steps
           

# Scenario 2 Test
sorted_word_list = ['apple', 'banana', 'cherry', 'grape', 'orange', 'strawberry']
target_2 = 'orange'
result_linear_search_2 = linear_search_sorted_words(sorted_word_list, target_2)
result_binary_search_2 = binary_search_sorted_words(sorted_word_list, target_2)
# print(f"Scenario 2 (Linear Search): Target {target_2} found at index {result_linear_search_2[0]} in {result_linear_search_2[1]} steps.")
# print(f"Scenario 2 (Binary Search): Target {target_2} found at index {result_binary_search_2[0]} in {result_binary_search_2[1]} steps.")


# Linear Search
def linear_search_last_occurrence(arr, target_3):
    arr.sort()
    count = 0
    for index, element in enumerate(arr):
        count += 1
        if element == target_3:
            if arr[index+1] != target_3:
                return index, count# Your code here
    return -1, count

# Binary Search
def binary_search_last_occurrence(arr, target_3):
    arr.sort()
    print(arr)
    left = 0 
    right = len(arr) -1
    count = 0
    while left<=right:
        mid = (left+right) // 2
        if arr[mid] == target_3:
            print("target match")
            if arr[mid+1] != target_3:
                print("It Works")
                return mid, count
                print("It Works")
            elif arr[mid+1] == target_3:
                left = mid + 1
                print("Another 10")
        elif arr[mid] < target_3:
            left = mid + 1
        elif arr[mid] > target_3:
            right = mid-1
    return -1, count
    # Your

# Scenario 3 Test
occurrence_list = [5, 10, 15, 20, 10, 25, 30, 35, 10, 40]
target_3 = 10
result_linear_search_3 = linear_search_last_occurrence(occurrence_list, target_3)
result_binary_search_3 = binary_search_last_occurrence(sorted(occurrence_list), target_3)
print(f"Scenario 3 (Linear Search): Last occurrence of {target_3} found at index {result_linear_search_3[0]} in {result_linear_search_3[1]} steps.")
print(f"Scenario 3 (Binary Search): Last occurrence of {target_3} found at index {result_binary_search_3[0]} in {result_binary_search_3[1]} steps.")


## Evaluatioprint(n Criteria:

# - Correct implementation of linear and binary search algorithms for each scenario.
# - The functions should return both the answer and the number of steps taken.
# - Clarity and readability of the code. (DRY SRP)
# - Proper documentation and comments.

# **Note:** Analyze and discuss the efficiency of linear search and binary search based on the number of steps in each scenario.
