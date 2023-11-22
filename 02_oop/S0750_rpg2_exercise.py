"""opgave: Objektorienteret rollespil, del 2 :

Som altid skal du læse hele øvelsesbeskrivelsen omhyggeligt, før du begynder at løse opgaven.

Byg videre på din løsning af del 1.

Opfind to nye klasser, som arver fra klassen Character. For eksempel Hunter og Magician.
Dine nye klasser skal have deres egne ekstra metoder og/eller attributter.
Måske overskriver de også metoder eller attributter fra klassen Character.

Lad i hovedprogrammet objekter af dine nye klasser (dvs. rollespilfigurer) kæmpe mod hinanden,
indtil den ene figur er død. Udskriv, hvad der sker under kampen.

I hver omgang bruger en figur en af sine evner (metoder). Derefter er det den anden figurs tur.
Det er op til dig, hvordan dit program i hver tur beslutter, hvilken evne der skal bruges.
Beslutningen kan f.eks. være baseret på tilfældighed eller på en smart strategi

Opgradering 1:
Hver gang en figur bruger en af sine evner, skal du tilføje noget tilfældighed til den anvendte evne.

Opgradering 2:
Lad dine figurer kæmpe mod hinanden 100 gange.
Hold styr på resultaterne.
Prøv at afbalancere dine figurers evner på en sådan måde, at hver figur vinder ca. halvdelen af kampene.

Hvis du går i stå, kan du spørge google, de andre elever eller læreren (i denne rækkefølge).

Når dit program er færdigt, skal du skubbe det til dit github-repository.
Send derefter denne Teams-besked til din lærer: <filename> done
Fortsæt derefter med den næste fil."""
import random

class Character:
    def __init__(self, name, max_health, _current_health, attackpower):
        self.name = name
        self.max_health = max_health
        self._current_health = _current_health
        self.attackpower = attackpower

    def __repr__(self):
        return f"name: {self.name}. max health: {self.max_health}. current health: {self.get_current_health()}. attackpower: {self.attackpower}"

    def get_current_health(self):
        return self._current_health

    def set_current_health(self, x):
        self._current_health = x

    def get_hit(self, damage):
        self.set_current_health(self.get_current_health() - damage)

    def get_healed(self, heal):
        if self.get_current_health() + heal > self.max_health:
            self.set_current_health(self.max_health)
        else:
            self.set_current_health(self.get_current_health() + heal)
    def hit(self, other_object):
        damage = self.attackpower
        other_object.get_hit(damage)
        print(f"{self.name} hit {other_object.name} for {damage} damage")


class Healer(Character):
    def __init__(self, name, max_health, _current_health, attackpower, healpower):
        super().__init__(name, max_health, _current_health, attackpower)
        self.attackpower = 0
        self.healpower = healpower

    def __repr__(self):
        return f"name: {self.name}. max health: {self.max_health}. current health: {self.get_current_health()}. healpower: {self.healpower}"

    def heal(self, other_object):
        heal = self.healpower
        other_object.get_healed(heal)


class Hunter(Character):
    def __init__(self, name, max_health, _current_health, attackpower, pet_damage, hit_chance):
        super().__init__(name, max_health, _current_health, attackpower)
        self.pet_damage = pet_damage
        self.hit_chance = 10

    def __repr__(self):
        return f"name: {self.name}. max health: {self.max_health}. current health: {self.get_current_health()}. attackpower: {self.attackpower}. pet damage: {self.pet_damage}"

    def shoot(self, other_object):
        damage = self.attackpower
        hit_chance_value = round(random.randrange(1, 100))
        if hit_chance_value <= self.hit_chance:
            other_object.get_hit(damage)
            print(f"{self.name} shot {other_object.name} for {damage} damage.")
        else:
            print(f"{self.name} missed a clear shot on {other_object.name}, yikes!")




    def pet_attack(self, other_object):
        damage = self.pet_damage
        other_object.get_hit(damage)
        print(f"{self.name}'s pet bit {other_object.name} for {damage} damage.")

    def increase_hit_chance(self):
        self.hit_chance = 90

class Mage(Character):
    def __init__(self, name, max_health, _current_health, attackpower, spellpower):
        super().__init__(name, max_health, _current_health, attackpower)
        self.attackpower = 0
        self.spellpower = spellpower
        self.shield = 0

    def __repr__(self):
        return f"name: {self.name}. max health: {self.max_health}. current health: {self.get_current_health()}. spellpower: {self.spellpower}"

    def icebolt(self):
        damage = self.spellpower
