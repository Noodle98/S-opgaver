import os
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
#print(str(emp))


# Opgave:
# Tilføj en magisk funktion til klassen Dog så "huge_dog > tiny_dog" interpreteres på en fornuftig måde.

class Dog:
    def __init__(self, size):
        self.size = size

    def __gt__(self, other):
        return self.size > other.size


huge_dog = Dog(80)
tiny_dog = Dog(25)
#print(type(huge_dog))

# Uncomment this in order to test your solution!
#if huge_dog > tiny_dog:
    #print("You solved the exercise :)")



# Eksempel:
# Kør programmet og leg med koden
a_string = "abc"   # string
#print(f"{a_string=}     {type(a_string)=}")
a_tuple = ("abc",)   # tuple  (kommaet er afgørende!)
#print(f"{a_tuple=}     {type(a_tuple)=}")
also_a_string = ("abc")   # tuple  (kommaet er afgørende!)
#print(f"{also_a_string=}     {type(also_a_string)=}")
#print()

#for s in a_string:
    #print("String", s)
#for t in a_tuple:
    #print("Tuple", t)



# Eksempel:
# Kør programmet og leg med koden
names = ["Klaus", "Dorte", "Hans"]
ages= [18, 20, 15]
zipped = zip(names, ages)
print(f"{zipped=}")
print(f"{type(zipped)=}")
#for item in zipped:
    #print(f"{item=}   {type(item)=}")


# Eksempel:
# Kør programmet og leg med koden
#for i, j, k in zip(range(4,23), "abc", ["One", "Two", "Three", "Four"]):
    #print(i, j, k, end="           ")


# Opgave:
# Tilføj en for løkke med 2 iteratorer, som udprinter "a 10   b 12   c 23   d 41"
letters = ["a", "b", "c", "d"]
numbers = [10, 12, 23, 41, 56, 58]
#for i, j in zip(letters, numbers):
    #print(i, j, end="        ")


# Eksempel:
# Kør programmet og leg med koden
class Dummy:

    def __init__(self, a_, b_):
        self.a = a_
        self.b = b_

    def __repr__(self):
        return f"{self.a=} {self.b=}"


dummy1 = Dummy(999, 3)
dummy2 = Dummy(777, 5)
dummies = [dummy1, dummy2]
#rint("before", dummies)
dummies.sort(key=lambda x: x.a, reverse=False)
#print("after ", dummies)



# Opgave:
# Forklar hvad der sker i den følgende kodelinje.
#print((lambda x: x * 3)(5))
#Lambda funktionen kalder x*3, og tager så (5) som argument, hvilket gør x til 5. Og 5x3 = 15, så derfor bliver der printet 15.


# Eksempel:
# Kør programmet og leg med koden
def infinite_sequence():
    num = 0
    while True:
        yield num
        num += 1


gen = infinite_sequence()
#print(next(gen))
#print(next(gen))
#for some_iterator in [3, 12, 4]:
    #print("in a for loop", next(gen))



current_dir = os.getcwd()
#print(f'{current_dir = }')


