# Assigment - 11
# question-1
print("Answer-1")
class Animal :
    legs = 4
    eyes = 2
    def animal_attribute(self):
        print("Animal walk with %d legs" % self.legs)
        print("Animal saw with %d eyes" % self.eyes)

class Tiger(Animal) :
    smart = "Intelligent"
    def tiger_attribute(self):
        print("Tigers are %s" % self.smart)


tiger = Tiger()
tiger.animal_attribute()

tiger.legs = 5
tiger.animal_attribute()

tiger.tiger_attribute()

# question-2
print("Answer-2")
class A:
    def f(self):
        return self.g()

    def g(self):
        return 'A'

class B(A):
    def g(self):
        return 'B'

a = A()
b = B()
print a.f(), b.f()
print a.g(), b.g()

# question-3
print("Answer-3")
class Cop:
    name = "Shivani"
    age = 21
    work_experience = 3
    designation = "Administrator"

    def add(self):
        print("%s with age %d having work experience of %d is working as an %s" % (self.name, self.age, self.work_experience, self.designation))
    def display(self):
        print(self.name,self.age,self.work_experience,self.designation)
    def update(self,name,age,work_experience,designation):
        print("Myself..... :")
        print("%s with age %d having work experience of %d is working as an %s" % (name, age, work_experience, designation))

class Mission(Cop):
    def add_mission_details(self):
        print("hello Mission....")
        m_obj.update("Laddu",23,5,"Lawyer")

cop_ob = Cop()
m_obj = Mission()

cop_ob.add()
cop_ob.display()
cop_ob.update("Shinu",22,4,"Administrator")

m_obj.add_mission_details()

# question-4
print("Answer-4")
class Shape:
    length = 5
    breadth = 5
    def Area(self):
        area = (self.length * self.breadth)
        print(area)

class Rectangle(Shape):
    def AOR(self):
        print("Area of rectangle is : ")
        rect_obj.Area()

class Square(Shape):
    def AOS(self):
        print("Area of square is : ")
        sqr_obj.Area()
s= Shape()
rect_obj = Rectangle()
sqr_obj = Square()

rect_obj.AOR()
sqr_obj.AOS()

