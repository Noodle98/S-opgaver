"""Opgave: Objektorienteret rollespil, del 1 :

Som altid skal du læse hele opgavebeskrivelsen omhyggeligt, før du begynder at løse opgaven.

Kopier denne fil til din egen løsningsmappe. Skriv din løsning ind i kopien.

Definer en klasse "Character" med attributterne "name", "max_health", "_current_health", "attackpower".
_current_health skal være en privat attribut, det er ikke meningen at den skal kunne ændres udefra i klassen.

Tilføj en konstruktor (__init__), der accepterer klassens attributter som parametre.
Tilføj en metode til udskrivning af klasseobjekter (__repr__).

Tilføj en metode "hit", som reducerer _current_health af en anden karakter med attackpower.
Eksempel: _current_health=80 og attackpower=10: et hit reducerer _current_health til 70.

Metoden hit må ikke ændre den private attribut _current_health i en (potentielt) fremmed klasse.
Derfor definerer vi en anden metode get_hit, som reducerer _current_health for det objekt, som den tilhører, med attackpower.

Hvis du er gået i stå, kan du spørge google, de andre elever eller læreren (i denne rækkefølge).
Hvis du ikke aner, hvordan du skal begynde, kan du åbne S0720_rpg1_help.py og starte derfra.

Når dit program er færdigt, skal du skubbe det til dit github-repository
og sammenlign det med lærerens løsning i S0730_rpg1_solution.py

Send derefter denne Teams-besked til din lærer: <filename> færdig
Fortsæt derefter med den næste fil."""
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


class Healer(Character):
    def __init__(self, name, max_health, _current_health, attackpower, healpower):
        super().__init__(name, max_health, _current_health, attackpower)
        self.attackpower = 0
        self.healpower = healpower

    def heal(self, other_object):
        heal = self.healpower
        other_object.get_healed(heal)



warrior1 = Character("Zíva", 200, 200, 50)
print(warrior1)
warrior2 = Character("Nuddeldreng", 170, 170, 25)
print(warrior2)
warrior1.hit(warrior2)
warrior2.hit(warrior1)
print(warrior1)
print(warrior2)
druid1 = Healer("Noodlegrill", 140, 140, 0, 30)
druid1.heal(warrior2)
print(warrior2)



