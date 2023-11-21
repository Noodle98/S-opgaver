"""
Opgave "Animals"

Som altid skal du læse hele opgavebeskrivelsen omhyggeligt, før du begynder at løse opgaven.

Kopier denne fil til din egen løsningsmappe. Skriv din løsning ind i kopien.

Alt, hvad du har brug for at vide for at løse denne opgave, finder du i cars_oop-filerne.

Definer en klasse ved navn Animal.
Hvert objekt i denne klasse skal have attributterne name (str), sound (str), height (float),
weight (float), legs (int), female (bool).
I parentes står data typerne, dette attributterne typisk har.

Tilføj til klassen meningsfulde metoder __init__ og __repr__.
Kald disse metoder for at oprette objekter af klassen Animal og for at udskrive dem i hovedprogrammet.

Skriv en klassemetode ved navn make_noise, som udskriver dyrets lyd i konsollen.
Kald denne metode i hovedprogrammet.

Definer en anden klasse Dog, som arver fra Animal.
Hvert objekt af denne klasse skal have attributterne tail_length (int eller float)
og hunts_sheep (typisk bool).

Tilføj til klassen meningsfulde metoder __init__ og __repr__.
Ved skrivning af konstruktoren for Dog skal du forsøge at genbruge kode fra klassen Animal.
Kald disse metoder for at oprette objekter af klassen Hund og for at udskrive dem i hovedprogrammet.

Kald metoden make_noise på Dog-objekter i hovedprogrammet.

Skriv en klassemetode ved navn wag_tail for Dog.
Denne metode udskriver i konsollen noget i stil med
"Hunden Snoopy vifter med sin 32 cm lange hale"
Kald denne metode i hovedprogrammet.

Skriv en funktion mate(mother, father). Begge parametre er af typen Dog.
Denne funktion skal returnere et nyt objekt af typen Dog.
I denne funktion skal du lave meningsfulde regler for den nye hunds attributter.
Hvis du har lyst, brug random numbers så mate() producerer tilfældige hunde.
Sørg for, at denne funktion kun accepterer hunde med det korrekte køn som argumenter.

I hovedprogrammet kalder du denne metode og udskriver den nye hund.

Når dit program er færdigt, skal du skubbe det til dit github-repository.
Send derefter denne Teams-meddelelse til din lærer: <filename> færdig
Fortsæt derefter med den næste fil."""
import random


class Animal:
    def __init__(self, name, sound, height, weight, legs, female):
        self. name = name
        self.sound = sound
        self.height = height
        self.weight = weight
        self.legs = legs
        self.female = female

    def __repr__(self):
        return f"name: {self.name}. sound: {self.sound}. height: {self.height} cm. weight: {self.weight} kg. legs: {self.legs}. female: {self.female}"

    def make_noise(self):
        print(f"{self.name} goes: {self.sound}")


class Dog(Animal):
    def __init__(self, name, sound, height, weight, legs, female, tail_length, hunts_sheep):
        super().__init__(name, sound, height, weight, legs, female)
        self.tail_length = tail_length
        self.hunts_sheep = hunts_sheep

    def __repr__(self):
        return f"name: {self.name}. sound: {self.sound}. height: {self.height} cm. weight: {self.weight} kg. legs: {self.legs}. female: {self.female}. tail length: {self.tail_length} cm. hunts sheep: {self.hunts_sheep}"

    def wag_tail(self):
        print(f"Hunden {self.name} vifter med sin {self.tail_length} cm lange hale, mens den siger {self.sound}")


def mate(mother, father):
    # Checks that mother and father are both dogs, and are of correct genders
    if type(mother) == Dog and mother.female == True and type(father) == Dog and father.female == False:
        print(f"Success! {mother.name} and {father.name} have mated!")
        # Makes 2 lists of female and male names for puppies
        possible_female_names = ["Tyranda", "Yrel", "Sylvanas", "Jaina", "Maiev"]
        possible_male_names = ["Saurfang", "Rexxar", "Anduin", "Thrall", "Illidan"]
        # gets a random gender
        female = bool(random.getrandbits(1))
        # assigns a random name to the puppy depending on gender
        name = ""
        if female == True:
            name = random.choice(possible_female_names)
        else:
            name = random.choice(possible_male_names)
        sound = "Woof!"
        legs = 4
        hunts_sheep = False
        # declares the other random attributes
        height = round(random.randrange(5, 20))
        weight = round(random.randrange(1, 3), 1)
        tail_length = round(random.randrange(1, 10))

        # Creates a new object with the variables
        puppy = Dog(name, sound, height, weight, legs, female, tail_length, hunts_sheep)
        return puppy


    else:
        print("Error, animals could not mate :(")


duck = Animal("ForDucksSake", "brap!", 30, 4, 2, True)
dog_father = Dog("Bob", "Woof!", 60, 15, 4, False, 15, False)
print(duck)
print(dog_father)
dog_father.wag_tail()
dog_mother = Dog("Anne", "Woof!", 50, 15, 4, True, 14, False)
new_dog = mate(dog_mother, dog_father)
print(new_dog)