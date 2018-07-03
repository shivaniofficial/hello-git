# Assignment-4
from collections import Counter

# tuple with different data types
tpl_1 = ("Python", True, 3.8, 5)

#length of tuple :
print(len(tpl_1))
#maximum element of tuple
print(max(tpl_1))
#minimum elememt of tuple
print(min(tpl_1))

#product of tuple
tpl_2 = (5,8,6.2,8,7)
result = 1
for x in tpl_2:
    result = result * x
print(result)

# creation of sets
my_set1 = set(input("Enter the elements in set 1 : "))
print(my_set1)
my_set2 = set(input("Enter the elements in set 2 : "))
print(my_set2)

# difference of two sets
# method-1
print("Difference of sets : ")
difference = (my_set1 - my_set2)
print(difference)
# method-2
print("Another method of difference : ")
print(my_set1.difference(my_set2))

# comparison of sets

if (my_set1 > my_set2):
    print("set 1 is greater")
else:
    print("Set 2 is greater")

#intersection of two sets
print("Intersection of two sets :")
inter_set = my_set1 & my_set2
print(inter_set)

# dictionary to store name and marks of students by user input

list_name = input("enter names seperated by commas : ")
list_value = list(input("enter the marks of the corresponding students: "))
final_dictionary = dict(zip(list_name,list_value))
print(final_dictionary)

# sorting of dictionary
print("sorting")
srt = sorted(final_dictionary.values())
print(srt)

#counting no. of occurance of each alphabet in word
print("word = MISSISSIPPI")
word = "MISSISSIPPI"
d = Counter(word)
print(d)