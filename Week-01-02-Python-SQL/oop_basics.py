"""
Object-Oriented Programming Basics

This module demonstrates:
- Class definitions and objects
- Attributes and methods
- Constructors (__init__)
- Inheritance
- Polymorphism
- Encapsulation
- Special methods (dunder methods)
"""

# ============================================================================
# BASIC CLASS DEFINITION
# ============================================================================

print("=" * 60)
print("OBJECT-ORIENTED PROGRAMMING BASICS")
print("=" * 60)

class Person:
    """A class to represent a person."""

    # Class variable (shared by all instances)
    population = 0

    def __init__(self, name, age):
        """Initialize a person object.

        Args:
            name: Person's name
            age: Person's age
        """
        # Instance variables
        self.name = name
        self.age = age
        Person.population += 1

    def introduce(self):
        """Return introduction string."""
        return f"Hi, I'm {self.name} and I'm {self.age} years old"

    def have_birthday(self):
        """Increment age by one year."""
        self.age += 1
        return f"{self.name} is now {self.age} years old"

    def __str__(self):
        """Return string representation of person."""
        return f"Person({self.name}, {self.age})"

    def __repr__(self):
        """Return official string representation."""
        return f"Person('{self.name}', {self.age})"

# Create objects
print("\nCreating objects:")
person1 = Person("Alice", 28)
person2 = Person("Bob", 35)
person3 = Person("Charlie", 42)

print(f"{person1.introduce()}")
print(f"{person2.introduce()}")
print(f"{person3.introduce()}")

print(f"Total population: {Person.population}")

# Accessing and modifying attributes
print(f"\nBefore birthday: {person1}")
print(person1.have_birthday())
print(f"After birthday: {person1}")

# ============================================================================
# ATTRIBUTES AND METHODS
# ============================================================================

print("\n" + "=" * 60)
print("ATTRIBUTES AND METHODS")
print("=" * 60)

class BankAccount:
    """A class to represent a bank account."""

    def __init__(self, account_number, owner, balance=0):
        """Initialize bank account.

        Args:
            account_number: Account number
            owner: Account owner name
            balance: Initial balance (default: 0)
        """
        self.account_number = account_number
        self.owner = owner
        self.balance = balance
        self.transaction_history = []

    def deposit(self, amount):
        """Deposit money to account."""
        if amount > 0:
            self.balance += amount
            self.transaction_history.append(f"Deposit: ${amount}")
            return f"Deposited ${amount}. New balance: ${self.balance}"
        return "Deposit amount must be positive"

    def withdraw(self, amount):
        """Withdraw money from account."""
        if amount > self.balance:
            return "Insufficient funds"
        if amount > 0:
            self.balance -= amount
            self.transaction_history.append(f"Withdrawal: ${amount}")
            return f"Withdrew ${amount}. New balance: ${self.balance}"
        return "Withdrawal amount must be positive"

    def get_balance(self):
        """Return current balance."""
        return self.balance

    def print_history(self):
        """Print transaction history."""
        print(f"\nTransaction history for {self.owner}:")
        for transaction in self.transaction_history:
            print(f"  - {transaction}")

# Using BankAccount
print("\nBankAccount example:")
account = BankAccount("ACC001", "Alice", 1000)
print(account.deposit(500))
print(account.withdraw(200))
print(account.withdraw(2000))  # Insufficient funds
account.print_history()

# ============================================================================
# INHERITANCE
# ============================================================================

print("\n" + "=" * 60)
print("INHERITANCE")
print("=" * 60)

# Base class
class Animal:
    """Base class for animals."""

    def __init__(self, name, age):
        """Initialize animal."""
        self.name = name
        self.age = age

    def speak(self):
        """Make sound (to be overridden)."""
        return f"{self.name} makes a sound"

    def describe(self):
        """Describe the animal."""
        return f"{self.name} is {self.age} years old"

# Derived classes (subclasses)
class Dog(Animal):
    """Dog class inheriting from Animal."""

    def __init__(self, name, age, breed):
        """Initialize dog.

        Args:
            name: Dog's name
            age: Dog's age
            breed: Dog's breed
        """
        super().__init__(name, age)  # Call parent constructor
        self.breed = breed

    def speak(self):
        """Override speak method."""
        return f"{self.name} barks: Woof!"

    def fetch(self):
        """Dog-specific method."""
        return f"{self.name} is fetching"

class Cat(Animal):
    """Cat class inheriting from Animal."""

    def __init__(self, name, age, indoor=True):
        """Initialize cat."""
        super().__init__(name, age)
        self.indoor = indoor

    def speak(self):
        """Override speak method."""
        return f"{self.name} meows: Meow!"

    def scratch(self):
        """Cat-specific method."""
        return f"{self.name} is scratching the furniture"

# Using inheritance
print("\nInheritance example:")
dog = Dog("Rex", 5, "Labrador")
cat = Cat("Whiskers", 3)

print(dog.describe())
print(dog.speak())
print(dog.fetch())

print("\n" + cat.describe())
print(cat.speak())
print(cat.scratch())

# ============================================================================
# POLYMORPHISM
# ============================================================================

print("\n" + "=" * 60)
print("POLYMORPHISM")
print("=" * 60)

# Polymorphism: Different classes, same interface
animals = [
    Dog("Buddy", 4, "Golden Retriever"),
    Cat("Mittens", 2),
    Animal("Unknown", 1)
]

print("\nPolymorphism example - calling speak() on different types:")
for animal in animals:
    print(f"  {animal.speak()}")

# ============================================================================
# ENCAPSULATION
# ============================================================================

print("\n" + "=" * 60)
print("ENCAPSULATION (Private/Protected Attributes)")
print("=" * 60)

class Student:
    """Student class with encapsulation."""

    def __init__(self, name, student_id):
        """Initialize student.

        Args:
            name: Student's name
            student_id: Student ID
        """
        self.name = name
        self._student_id = student_id  # Protected (single underscore)
        self.__gpa = 4.0  # Private (double underscore)
        self.__courses = []  # Private

    def add_course(self, course):
        """Add course to student's schedule."""
        self.__courses.append(course)
        return f"Added {course}"

    def get_courses(self):
        """Get list of courses."""
        return self.__courses.copy()  # Return copy, not reference

    def set_gpa(self, gpa):
        """Set GPA with validation."""
        if 0 <= gpa <= 4.0:
            self.__gpa = gpa
            return f"GPA set to {gpa}"
        return "Invalid GPA value"

    def get_gpa(self):
        """Get current GPA."""
        return self.__gpa

    def __calculate_grade_point(self, course):
        """Private method - not accessible outside class."""
        return len(course) * 0.5  # Dummy calculation

# Using encapsulation
print("\nEncapsulation example:")
student = Student("John", "STU001")
print(student.add_course("Python"))
print(student.add_course("SQL"))
print(f"Courses: {student.get_courses()}")
print(f"GPA: {student.get_gpa()}")

print(student.set_gpa(3.8))
print(f"Updated GPA: {student.get_gpa()}")

# Name mangling for private attributes
print(f"\nProtected attribute (accessible): {student._student_id}")
print(f"Private attribute (name mangled): {student._Student__gpa}")
# Note: student.__gpa would raise AttributeError (not directly accessible)

# ============================================================================
# SPECIAL METHODS (DUNDER METHODS)
# ============================================================================

print("\n" + "=" * 60)
print("SPECIAL METHODS (Dunder Methods)")
print("=" * 60)

class Rectangle:
    """Rectangle class with special methods."""

    def __init__(self, width, height):
        """Initialize rectangle."""
        self.width = width
        self.height = height

    def __str__(self):
        """Return user-friendly string."""
        return f"Rectangle ({self.width} x {self.height})"

    def __repr__(self):
        """Return technical string."""
        return f"Rectangle({self.width}, {self.height})"

    def __eq__(self, other):
        """Check equality (==)."""
        return (self.width == other.width and
                self.height == other.height)

    def __lt__(self, other):
        """Check less than (<)."""
        return self.area() < other.area()

    def __add__(self, other):
        """Add two rectangles."""
        return Rectangle(self.width + other.width,
                        self.height + other.height)

    def __mul__(self, factor):
        """Multiply rectangle dimensions."""
        return Rectangle(self.width * factor, self.height * factor)

    def __len__(self):
        """Return perimeter when len() is called."""
        return 2 * (self.width + self.height)

    def area(self):
        """Calculate area."""
        return self.width * self.height

# Using special methods
print("\nSpecial methods example:")
rect1 = Rectangle(5, 3)
rect2 = Rectangle(5, 3)
rect3 = Rectangle(4, 6)

print(f"str(): {str(rect1)}")
print(f"repr(): {repr(rect1)}")

print(f"\nEquality: rect1 == rect2: {rect1 == rect2}")
print(f"Less than: rect1 < rect3: {rect1 < rect3}")

print(f"\nAddition: rect1 + rect3: {rect1 + rect3}")
print(f"Multiplication: rect1 * 2: {rect1 * 2}")

print(f"\nlen() (perimeter): {len(rect1)}")
print(f"Area: {rect1.area()}")

# ============================================================================
# CLASS AND STATIC METHODS
# ============================================================================

print("\n" + "=" * 60)
print("CLASS AND STATIC METHODS")
print("=" * 60)

class Temperature:
    """Temperature conversion class."""

    # Class variable
    celsius_to_fahrenheit_factor = 9/5
    fahrenheit_offset = 32

    def __init__(self, celsius):
        """Initialize with temperature in Celsius."""
        self.celsius = celsius

    @staticmethod
    def from_fahrenheit(fahrenheit):
        """Create Temperature from Fahrenheit (doesn't need instance)."""
        celsius = (fahrenheit - 32) * 5/9
        return Temperature(celsius)

    @classmethod
    def absolute_zero_celsius(cls):
        """Class method to return absolute zero in Celsius."""
        return cls(-273.15)

    def to_fahrenheit(self):
        """Convert to Fahrenheit."""
        return (self.celsius * self.celsius_to_fahrenheit_factor +
                self.fahrenheit_offset)

    def __str__(self):
        """String representation."""
        return f"{self.celsius}°C = {self.to_fahrenheit():.2f}°F"

# Using static and class methods
print("\nStatic and class methods example:")
temp1 = Temperature(0)
print(f"Freezing point: {temp1}")

temp2 = Temperature.from_fahrenheit(68)  # Static method
print(f"Room temperature: {temp2}")

temp3 = Temperature.absolute_zero_celsius()  # Class method
print(f"Absolute zero: {temp3}")

# ============================================================================
# COMPOSITION
# ============================================================================

print("\n" + "=" * 60)
print("COMPOSITION (Object Composition)")
print("=" * 60)

class Engine:
    """Engine class."""

    def __init__(self, horsepower):
        """Initialize engine."""
        self.horsepower = horsepower

    def start(self):
        """Start engine."""
        return f"Engine started with {self.horsepower}hp"

class Car:
    """Car class with composition."""

    def __init__(self, make, model, engine):
        """Initialize car.

        Args:
            make: Car manufacturer
            model: Car model
            engine: Engine object (composition)
        """
        self.make = make
        self.model = model
        self.engine = engine

    def start(self):
        """Start the car."""
        engine_status = self.engine.start()
        return f"{self.make} {self.model}: {engine_status}"

# Using composition
print("\nComposition example:")
v8_engine = Engine(400)
car = Car("Ford", "Mustang", v8_engine)
print(car.start())

# ============================================================================
# PRACTICAL EXAMPLE
# ============================================================================

print("\n" + "=" * 60)
print("PRACTICAL EXAMPLE - Library System")
print("=" * 60)

class Book:
    """Represents a book in the library."""

    def __init__(self, title, author, isbn, year):
        """Initialize book."""
        self.title = title
        self.author = author
        self.isbn = isbn
        self.year = year
        self.borrowed_by = None

    def __str__(self):
        """String representation."""
        status = f"(Borrowed by {self.borrowed_by})" if self.borrowed_by else "(Available)"
        return f"{self.title} by {self.author} {status}"

class Member:
    """Represents a library member."""

    def __init__(self, name, member_id):
        """Initialize member."""
        self.name = name
        self.member_id = member_id
        self.books_borrowed = []

    def borrow_book(self, book):
        """Borrow a book."""
        if book.borrowed_by is None:
            book.borrowed_by = self.name
            self.books_borrowed.append(book.title)
            return f"{self.name} borrowed '{book.title}'"
        return f"Book '{book.title}' is already borrowed"

    def return_book(self, book):
        """Return a borrowed book."""
        if book.borrowed_by == self.name:
            book.borrowed_by = None
            self.books_borrowed.remove(book.title)
            return f"{self.name} returned '{book.title}'"
        return f"This book wasn't borrowed by {self.name}"

# Using the library system
print("\nLibrary system example:")
book1 = Book("Python Basics", "John Smith", "123456", 2023)
book2 = Book("Data Science", "Jane Doe", "234567", 2022)

member = Member("Alice Johnson", "M001")

print(book1)
print(member.borrow_book(book1))
print(book1)
print(member.borrow_book(book2))
print(f"Books borrowed: {member.books_borrowed}")
print(member.return_book(book1))
print(book1)

# ============================================================================
# SUMMARY
# ============================================================================

print("\n" + "=" * 60)
print("SUMMARY")
print("=" * 60)
print("""
OOP Concepts:

1. CLASSES AND OBJECTS:
   - Classes are blueprints; objects are instances
   - __init__() is the constructor
   - self refers to the instance

2. ATTRIBUTES AND METHODS:
   - Attributes: Data stored in objects
   - Methods: Functions defined in classes
   - Class variables: Shared across all instances
   - Instance variables: Unique to each object

3. INHERITANCE:
   - Child class inherits from parent class
   - super() calls parent class methods
   - Method overriding: Replace parent method

4. POLYMORPHISM:
   - Different objects respond to same method call differently
   - Based on the type of the object

5. ENCAPSULATION:
   - Single underscore: Protected (convention)
   - Double underscore: Private (name mangling)
   - Getter/setter methods control access

6. SPECIAL METHODS (Dunder Methods):
   - __init__(): Constructor
   - __str__(): String representation
   - __repr__(): Official representation
   - __eq__(), __lt__(), etc.: Comparison
   - __add__(), __mul__(), etc.: Operators
   - __len__(): Length

7. CLASS AND STATIC METHODS:
   - @classmethod: Works with class, not instance
   - @staticmethod: Doesn't need class or instance

8. COMPOSITION:
   - Has-a relationship (composition)
   - vs. Is-a relationship (inheritance)
   - Object contains other objects

Best Practices:
- Use meaningful class and method names
- Keep classes focused on one responsibility
- Use inheritance for logical hierarchies
- Prefer composition over inheritance
- Use encapsulation to hide implementation
- Document classes with docstrings
- Avoid deep inheritance hierarchies (>3 levels)
""")
