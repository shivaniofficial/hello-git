# Assignment-3
#import statements :;
from collections import deque

# question-1 list with user efined inputs
list1 = raw_input("Enter the elements : ").split(",")
print(list1)

# question-2 adding another list to above list
list2 = ['google','appple','facebook','microsoft','tesla']
final_list = list1 + list2
print(final_list)

# question-3 count the no. of times an object occurs in final_list
print(final_list.count('google'))

#question-4 create a list with numbers and sort it in ascending order.
list3 = [32,88,98,56,23,11,74]
list3.sort()
print(list3)

# question-5 merging and sorting of arrays
A = [1,2,3,4,5]
B = [6,7,8,9,10]
C = A + B
C.sort()
print(C)

# question-6 stack and queue operations on list
print("Stack Operations")
stack = [1,2,3]
stack.append(6)
stack.append(7)
print(stack)
stack.pop()
print(stack)
stack.pop()
print(stack)

print("Queue operations : ")
queue = deque([1,2,3])
queue.append(4)
queue.append(5)
print(queue)
queue.popleft()
print("hello world")
print(queue)
queue.popleft()
print(queue)