class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __str__(self):
        return f'name={self.name = }, salary={str(self.salary)}'




# Eksempel:
# Kør programmet og leg med koden
list_comprehension_with_1_if = [i * i if i > 5 else i for i in range(10)]
#print(list_comprehension_with_1_if)

list_comprehension_with_2_if = [i * i if i > 5 else i for i in range(10) if i%2 == 0]
#print(list_comprehension_with_2_if)

# Opgave:
# Ændr den følgende kode. Brug en inline if.
# Programmets output skal være: [0, 3, 14, 9, 28, 15, 42, 21, 56, 27, 70, 33, 84, 39, 98, 45]

example_list = [i * 7 if i%2 == 0 else i * 3 for i in range(16)]
#print(example_list)

x = [1, 2, 3]
x_squared = (x_i**2 for x_i in x)
#print(x_squared)

# Eksempel:
# Kør programmet og leg med koden
list_comprehension_1 = [i * i for i in range(13) if i > 5]  # if statement controls for which values of i an element is added to the list
#print(f'{list_comprehension_1 = }')
list_comprehension_2 = [i * i if i > 7 else i + 1000 for i in range(13) if i > 5]  # the first if statement (ternary if) controls what is added to the list (provided the second if statement is true)
#print(f'{list_comprehension_2 = }')

# In 7
# Opgave:
# Skab denne liste med comprehension: [10, 15, 20, 25, 30, 35]
list_comprehension_3 = [i * 5 for i in range(8) if i > 1]
print(list_comprehension_3)

# In 8
# Opgave:
# Skab denne liste med comprehension: [0, 1, 2, 3, 40, 41, 42, 43, 44, 45]
# Brug "if" i din løsning!
list_comprehension_4 = [i + 36 if i > 3 else i for i in range(10)]
print(list_comprehension_4)

# In 9
# Opgave:
# Skab denne dictionary med comprehension: {3: 33, 4: 44, 5: 55, 6: 66}
dict_comprehension_1 = {i: i * 11 for i in range(7) if i > 2}
print(dict_comprehension_1)

emp = Employee("Jonas", 500000)
print(str(emp))


# Opgave:
# Tilføj en magisk funktion til klassen Dog så "huge_dog > tiny_dog" interpreteres på en fornuftig måde.

class Dog:
    def __init__(self, size):
        self.size = size

    def __int__(self):
        return self.size


huge_dog = Dog(80)
tiny_dog = Dog(25)
print(huge_dog)

# Uncomment this in order to test your solution!
#if huge_dog > tiny_dog:
#    print("You solved the exercise :)")