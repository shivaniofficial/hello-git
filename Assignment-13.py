# Assignment-13

# question-1 (name and handle the exception)
#a=3
# if a<4:
#    a=a/(a-3)
#     print(a)
# Error-1 = IndentationError
# Error-2 = ZeroDivisionError
print("\nAnswer 1\n")
a = 3
try:
    if a<4:
        a=a/(a-3)
        print(a)
except:
    a = a/1
    print("Error corrected now a is %d" %a)



# question-2 (name and handle the exception)
# error is: IndexError
print("\nAnswer 2\n")
l = [1,2,3]
try:
    print(l[3])
except:
    print("Index is out of range.")




# question-3 "output of the code"
# answer : in this we ourself have generated the error using the "raise" and type of that error is "NameError"
# when error occur it will simply go to exception block and print "An exception"
# then raise is called which in turn generates the NameError represented as "" Hi there
#try:
#    raise NameError("Hi there")  # Raise Error
#except NameError:
#    print "An exception"
#    raise  # To determine whether the exception was raised or not




# question-4 : Function which returns a/b
# answer :  1 = -5.0
# answer :  2 = a/b result in 0
print("\nAnswer 4\n")
def AbyB(a , b):
	try:
		c = ((a+b) / (a-b))
	except ZeroDivisionError:
		print "a/b result in 0"
	else:
		print c

# Driver program to test above function
# 1
AbyB(2.0, 3.0)
# 2
AbyB(3.0, 3.0)




# question-5 : handling import,value and index error :
# ImportError
print("\nAnswer 5\n")
try:
    raise ImportError
except :
    print("Importing is not correct!!!")
# ValueError
try:
    raise ValueError
except :
    print("value is not correct!!!")
# IndexError
try:
    raise IndexError
except :
    print("Index is not correct!!!")


# question-6
print("\nAnswer 6\n")
def AgeTooSmallError():
    age = int(input("please enter the age : "))
    if age < 18:
        print("Age is too small!!!")
        try:
          raise AgeTooSmallError()
        except :
            AgeTooSmallError()
    else:
        print("You are welcomed!!!")
AgeTooSmallError()
