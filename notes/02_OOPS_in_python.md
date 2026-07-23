# OOP in Python

## Defination
 
Object-Oriented Programming(OOP) is a programming paradigm where we represent real-world    things as objects,and these objects are created using classes.
Instead of writing only functions,we create objects that contain both data(attributes) and behaviour(methods).

## Real life analogy

Suppose there is a Car,

Every Car has:
- Color
- Brand
- Speed

And every car can:
- Start
- Stop
- Accelerate

Here,
Car --> Class
Your Car (PORSCHE)--> Object
Color, Brand --> Attributes
Start(),Stop()--> Methods (functions)

## Why do we use OOP?

Without OOP:
- Code becomes repetitive.
- Difficult to manage.
- Hard to use.

With OOP:
- Code is reusable.
- Easy to maintain.
- Easy to expand.
- Models real-world applications.

----------------------------------------------------1.Classes & Objects-----------------------------------------------------------

# 1. Classes & Objects
-----------------------------------------Class-------------------------------------
## Class
- A class is a blueprint or template for creating objects.
- It tells Python what properties and behaviours an object should have.

## Real-life Analogy
To understand it better,take an example of building blueprint.

A building blueprint isn't an actual building.
It only describes how a building should be made.

Similarly,
A class isn't an object.
It is only a DESIGN.

## Syntax

class class_name:
        #code

## Example

from one of the previous example,

class Car:
      #code

Here,Car is only a blueprint,nothing has been created yet.

-----------------------------------------Objects-------------------------------------
## Objects

- An Object is an actual instance of a class.
- It occupies memory and can use all the properties and methods defined inside the class.

## Real-Life Analogy

A house blueprint --> class
An actual house --> Object

One building can create many houses.
Similarly,
One class can create many objects.

## Syntax

object_name = class_name()

## Example

car1 = Car()
car2 = Car()

Here,Now we have two different objects.

## Creating Attributes and Methods
Input:-
                                                    Output:
class car:                                            Car started!

      def start(self):
        print("Car started!")

car1 = Car()
car1.start()

## What is  self?
- self represents the current object.

Whenever we call -->  car1.start()

Python automatically sends

self = car1

So, car1.start() internally becomes --> Car.start(car1)

That's why every instance method must have 'self' as its first parameter.

-----------------------------------------SUMMARY-------------------------------------

OOP --> Programming using objects.
Class --> Blueprint or template.
Object --> Instance of a class.
Attibutes --> variables that describe an object.
Methods --> Functions that define an object's behaviour.

self --> Refers to current object.
