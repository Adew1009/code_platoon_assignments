# Big O Answers

## Snippet 1 -
### Big O: O(n)
### Explanation: The for loop goes through all numbers therefore it will be O(n)
```python
def largest(array, value):
  for item in array:
    if item > value:
      return False
  return True 
```


## Snippet 2 -
### Big O: O(n)
### Explanation: It will be O of N since the for loops are not nested. I think it would actually be O(2n)

```python
def info_dump(customers):
  
  print('Customer Names:')
  for customer in customers: 
    print(customer['name'])
  
  print('Customer Locations:')
  for customer in customers: 
    print(customer['country'])
  
```

## Snippet 3 -
### Big O: O(1)
### Explanation: this is direct access and it doenst matter how large the array is to the 

```python
def first_element_is_red(array):
  return array[0] == 'red' 
```

## Snippet 4 -
### Big O: O(n^2)
### Explanation: Nested for loop of the same array

```python
def duplicates(array):
  for index1, item1 in enumerate(array):
    for index2, item2 in enumerate(array):
      if index1 == index2:
        continue
      if item1 == item2:
        return True
  return False
``` 

## Snippet 5 -
### Big O:
### Explanation": The code above contains two nested loops, one iterating over the words list and the other iterating over the endings list. Let's denote the length of the words list as m and the length of the endings list as n. Since the loops are nested, the time complexity is the product of the iterations of both loops. In other words, it's O(m * n). In this specific case, if the lengths of the words and endings lists are both m and n, respectively, then the time complexity would be O(m * n).

```python
words = ['chocolate', 'coconut', 'rainbow']
endings = ['cookie', 'pie', 'waffle']

for word in words:
  for ending in endings:
    print(word + ending)

```

## Snippet 6 -
### Big O: O(n)
### Explanation: The for loop of the array pushes it to O(n)

```python
numbers = [1,2,3,4,5,6,7,8,9,10]

def print_array(array):
  for item in array:
    print(item)

```

## Snippet 7 -
### Big O: O(n^2)
### Explanation:The provided code implements the Insertion Sort algorithm. Let's denote the length of the input array arr as n. In the worst-case scenario, where the array is initially in reverse order, the inner while loop will execute the maximum number of times for each element. In this case, the number of comparisons and swaps increases quadratically with the size of the array. The time complexity of Insertion Sort is O(n^2) in the worst-case scenario, where n is the number of elements in the array. This is because, for each element, the algorithm may need to compare and swap it with all previous elements in the sorted portion of the array.

```python
# this is insertion sort
def insertionSort(arr): 
  for i in range(1, len(arr)): 
    key = arr[i] 
    j = i-1
    while j >=0 and key < arr[j] : 
      arr[j+1] = arr[j] 
      j -= 1
    arr[j+1] = key 
```

## Snippet 8 -
### Big O: O(n^2)
### Explanation: The provided code is implementing the Selection Sort algorithm. Let's denote the length of the input list my_list as n. In the worst-case scenario, the outer loop will iterate n times, and for each iteration of the outer loop, the inner loop will iterate n - i times, where i is the current iteration of the outer loop. The time complexity of Selection Sort is O(n^2) in all cases, as it always has to compare and possibly swap each element with every other element in the list. Therefore, it performs (n * (n - 1)) / 2 comparisons in the worst case, which simplifies to O(n^2).

```python
for i in range(len(my_list)):
  min_idx = i
  for j in range(i+1, len(my_list)):
      if my_list[min_idx] > my_list[j]:
          min_idx = j

  my_list[i], my_list[min_idx] = my_list[min_idx], my_list[i]
```
