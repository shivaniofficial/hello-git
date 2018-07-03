# Assignment-5
# leap year
year = int(input("Enter the year you want to check : "))
if (year%4 ==0):
    print("Leap Year.")
else:
    print("Not a leap year.")

# square or rectangle :
length = int(input("Enter the value of length :"))
breadth = int(input("Enter the value of breadth : "))
if length == breadth :
    print("Dimensions are of a square.")
else:
    print("Dimensions are of a rectangle.")

#oldest and youngest of people :
p1 = int(input("Enter the age of first person : "))
p2 = int(input("Enter the age of second person : "))
p3 = int(input("Enter the age of third person : "))

oldest_person = max(p1,p2,p3)
print("oldest person is with age : " + str(oldest_person))

young_person = min(p1,p2,p3)
print("youngest person is with age : " + str(young_person))

#prize distribution :
your_input = int(input("Enter your points : "))
if (your_input > 200):
    print("please enter value upto 200.")
else:
    if (your_input >= 1 and your_input <= 50):
        print("Sorry! No prize this time.")
    elif(your_input >=51 and your_input <= 150):
        print("Congratulations! You won a Wooden Dog!")
    elif(your_input >= 151 and your_input <= 180):
        print("Congratulations! You won a Book!")
    elif(your_input >= 181 and your_input <= 200):
        print("Congratulations! You won chocolates!")
    else:
        print("Invalid Input!!!")

# discount

items = int(input("enter the quantity please : "))
cost = items * 100
if cost > 1000:
    dis = cost-(cost/10)
    print("you only have to pay " + str(dis))
else:
    print("Sorry no discount this time!!!")