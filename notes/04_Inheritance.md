# Inheritance

- Inheritance is a feature in OOP where one class acquires the properties and methods of another class.
- It allows us to reuse existing code instead of writing it again.

## Real life Analogy

Suppose a Parent and a Child.

The child inherts:
- Eye color.
- hair color.

But the child also has their own unique qualities.

Similarly,
A child class inherits the propertirs and methods of the parent class and can also have its own additional features.

## Why do we use inheritance?

🔴 Without Inheritance:

class Dog:
  def eat(self):
    print("Eating")

class Cat:
  def eat(self):
    print("Eating")

The same eat() method is repeated.

🟢 With inheritance:

class Animal:
  def eat(self):
    print("Eating")

class Dog(Animal):
  pass

class Cat(Animal):
  pass

Now both Dog and Cat automatically get the eat() method.

### Parent Class(Base Class)
The class whose properties are inherited.

Example:

class Animal:
  def eat(self):
    print("Eating")

Here, Animal is the Parent Class.

### Child Class (Derived Class)
The class that inherits from another class.

Syntax:

  class ChildClass(ParentClass):
    pass

Example:

  class Dog(Animal):
    pass

Dog is the Child Class.

### Example

class Animal:
  def eat(self):
    print("Animal is eating.")

class Dog(Animal):
  pass

dog = Dog()

dog.eat()

//Output

Animal is eating

Notice that Dog doesn't have an eat() method,but it inherited it from Animal.

### Child Class with its Own Method

A child class can have additional methods.

class Animal:

    def eat(self):
        print("Animal is eating")


class Dog(Animal):

    def bark(self):
        print("Dog is barking")


dog = Dog()

dog.eat()
dog.bark()

//Output

Animal is eating
Dog is barking

The Dog class has:
- Inherited method --> eat()
- Own method -->

## The super() Keyword
- super() is used to access the parent class.
- It is commonly used to call the parent's constructor or methods.

* Why do we need it?
- Suppose the parent constructor initializes some common data.
- Instead of writing the same code again in the child class,we can simply call the parent's constructor using super().

## Example
class Animal:

    def __init__(self, name):
        self.name = name


class Dog(Animal):

    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def display(self):
        print("Name :", self.name)
        print("Breed:", self.breed)


dog = Dog("Moti", "Golden Retriever")
dog.display()

// Output
Name : Moti
Breed : Golden Retriver

Without super(),we would have to write:

self.name = name

again in the child class.

## Method Overriding
- Method Overriding means a child class provides its own implementation of a method that already exits in the parent class.

class Animal:
    def sound(self):
        print("Animal makes sound")

class Dog(Animal):
    def sound(self):
        print("Dog barks.")

dog = Dog()
dog.sound()

// Output

Dog barks.

Here,the child's sound() method overrides the parent's version.

## Types of Inheritance

### 1. Single Inheritance

One Parent --> One Child

### 2. Multiple Inheritance

- One Child inherits from multiple Parents.

### 3. Multilevel Inheritance


