"""
1 set a variable to store the absolute square difference of two elements 
2 a for loop to iterate at the same time over each pair of elements
3 get the square absolute difference of these two elements
4 return the  average of the square differences of both lists
"""

first_list = [1, 2, 3]
second_list = [4, 5, 6]
square_difference = 0
total = 0

for first_element, second_element in zip(first_list,second_list):
    square_difference = abs(first_element - second_element) ** 2
    total += square_difference
return (total/len(second_list))