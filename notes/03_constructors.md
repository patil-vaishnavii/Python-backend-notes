# OOPS Conecpt : Constructors & Destructors

------------------------------------Constructors--------------------------------------------------
# 1. Consturctors
- A constructor is a special method that is automatically called whenever an object is created.

In Python,the constructor is written as:

__init__()

It's main purpose is to initialize(assign values to) the object's attributes.

def __init__(self,name,roll,marks):
    self.name = name
    self.roll = roll
    self.marks = marks

## Real-Life Analogy

Imagine buying a new phone.

As soon as we turn it on for the first time:
- Language is selected.
- Time is set.
- Initial settings are configured.

We don't have to manually call a "setup" function - it happens automatically.
Similarly,when an object is created ,the constructor automatically initializes it.

## Syntax

class class_name:
      def __init__(self):
          print("Constructor is called.")

//creating an object

obj = class_name()

// Output

Constructor is called.

Notice that we never called __init__() ourselves.Python called it automatically.

## Why do we need a Constructor?

🔴 Without a Constructor:

class Student:
      pass

s1 = student()

s1.name = "Vaishnavi"
s1.age = 21

That is, Every object has to be assigned values seperately.

🟢 With a constructor:

class Student:
      def __init__(self,name,age):
        self.name = name
        self.age = age

s1 = Student("Vaishnavi",21)

Everything can be initialized in one step.

------------------------------------Types of Constructors--------------------------------------------------
## Types
Python mainly has two types.

1. Default Constructor
2. Parameterized Constructor

### 1. Default Construtor
 - It takes only self.

class Student:
  def __init__(self):
    print("Student Created.")
s1 = Student()

// Output

Student Created.


### 2. Parameterized Constructor

- It accepts additional values.

class Student:
    def __init__(self,name,age):
      self.name = name
      self.age = age

s1 = student("Vaishnavi",21)

print(s1.name)
print(s1.age)

//Output

Vaishnavi
21

----------------------------------------Destructors--------------------------------------------------

# 2. Destructors
- A destructor is a special method that is automatically called when an object is about to be destroyes(removed from memory.)

in Python,it is written as:

__del__()


It is mainly used to clean up resources,such as:
- Closing files. 
- Closing databases connections.
- Releasing memory or other resources.

## Real life analogy

Suppose leaving a classroom,

Before leaving, we:
- Switch off the lights.
- Close the windows.
- Lock the door.

The cleanup happens before we leave.

A destructor works the same way --> It performs cleanup before the project is removed.

## Syntax

class Student:
    def __init__(self):
        print("Object Created.")

    def __del__(self):
        print("Object Destroyed.")

s1 = Student()

del s1

// Output

Object Created.
Object Destroyed.

-------------------------------------------Some Imp Quetions for Interview--------------------------------------------------

Q1. What is a constructor?
--> A constructor is a special method(__init__) that is automatically called when an object is created to initialize its attributes.

Q2. Can a class have multiple constructors in Python?
--> Not in the traditional sense. Python does not support constructor overloading directly. We can use default arguments or *args/**kwargs to achieve similar behaviour.

Q3. Is calling __init__() mandatory?
--> No. If you don't define one, Python provides a default construtor automatically.

Q4. What is a destructor?
--> A destructor(__del__) is a special method that is called when an object is about to be destroyed, mainly for cleanup tasks.

---------------------------------------------------------SUMMARY------------------------------------------------------------

- __init__() --> Constructor(runs automatically when an object is created).
- Initializes object attributes.
- Types: Default and Parameterized constructors.

- __del__() --> Destructor(used for cleanup before object destruction).
-self refers to current object.