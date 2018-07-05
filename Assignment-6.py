# Assignment-6
# taking input from the user and print it on the screen :
i = 0
list = []
while (i<10):
    user_input = int(input("enter a number : "))
    list.append(user_input)
    i = i+1
print("the numbers you entered are : " + str(list))

# infinite loop :
shiv = 1
while shiv:
    print("hello!!!!")

# question-3 :
print("\n\n\nprevious list was : " + str(list))
new_list = []
for each in list:
    sqr = each*each
    new_list.append(sqr)
print("Square of element is : " + str(new_list))

#question-4 :
print("\n")
final_list = [1,2,3,"shivani","laddu","shinu",1.11,1.22,1.33]
int_list = []
str_list = []
flt_list = []
for every in final_list:
    if type(every) == int:
        int_list.append(every)
    elif type(every) == str:
        str_list.append(every)
    elif type(every) == float:
        flt_list.append(every)
print("int list :" + str(int_list))
print("string list :" + str(str_list))
print("float " + str(flt_list))


# question-5 :
print("\n")
odd_list = []
even_list =[]
for i in range(1,101):
    if (i%2) == 0:
        even_list.append(i)
    else:
        odd_list.append(i)
print("list of odd elements is : " + str(odd_list))
print("list of even elements is : " + str(even_list))


# question-6 (printing the pattern) :
print("\n")
num = 4
for i in range(1,4):
    for j in range(1,i+1):
        print("*",end=" ")
    print()


# question-7 :
print("\n")
list_name = input("enter keys of the dictionary separated by ',' : ")
list_value = input("enter the values of the corresponding keys : ")
final_dictionary = dict(zip(list_name,list_value))
print(final_dictionary)
print("keys corresponding to their values : \n")
for k,v in final_dictionary.items():
    print (k,v)


# searching and deletion from list :

print("\nPrevious list you made was : ")
print(list)
number = int(input("enter the element you want to delete from the list : "))
if number in list:
    a = list.index(number)
    del list[a-1]
    print(list)
else:
    print("Element not found!!")
