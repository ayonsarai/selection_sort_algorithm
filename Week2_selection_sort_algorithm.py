# Sarai Ayon
# 4/14/2024
# CS240 Data Structures and Algorithms
# Week2_insertion_sort_algorithm.py
# resource : https://www.youtube.com/watch?v=g-PGLbMth_g 


# Import List from typing module
from typing import List

# Define the selection_sort function that takes a list of integers as input and returns None as output 
def selection_sort(arr: List[int]) -> None:
    
    # Go through all array elements 
    for i in range(len(arr)):
        # Find the minimum element in remaining unsorted array
        min_idx = i
        # Go through the unsorted part of the array
        for j in range(i+1, len(arr)):
            # Update the index of the minimum element 
            if arr[min_idx] > arr[j]:
                # Update the index of the minimum element 
                min_idx = j 
                
        # Swap the found minimum element with the first element of the 'unsorted' part of the array
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

# Specify the file path to read the numbers from 
file_path = 'C:\\Users\\Sarai Ayon\\OneDrive - Whatcom Community College\\Spring 2024\\CS240 Database Structure & Algorithms\\Week 2 Linked List\\numbers.txt.txt'

# Read the numbers from the file and store them in a list 
with open(file_path, 'r') as f:
    # Convert the numbers to a list of integers 
    arr = [int(num) for num in f.read().split()]
   # Print the unsorted array
   
# Test the function
selection_sort(arr)
# Print the sorted array
print ("Sorted array is:", arr)

#HW Test What value is in position 7586?
#value_at_7586 = arr[7585]
#print("Value at position 7586 is:", value_at_7586)


