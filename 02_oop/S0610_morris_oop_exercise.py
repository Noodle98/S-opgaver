"""
Opgave "Morris The Miner" (denne gang objekt orienteret)

Som altid skal du læse hele opgavebeskrivelsen omhyggeligt, før du begynder at løse opgaven.

Kopier denne fil til din egen løsningsmappe. Skriv din løsning ind i kopien.

Omskriv din oprindelige Morris-kode til en objektorienteret version.

Definer en klasse Miner med attributter som sleepiness, thirst osv.
og metoder som sleep, drink osv.
Opret Morris og initialiser hans attributter ved at kalde konstruktoren for Miner:
morris = Miner()

Hvis du går i stå, så spørg google, de andre elever eller læreren (i denne rækkefølge).

Når dit program er færdigt, skal du skubbe det til dit github-repository.
Send derefter denne Teams-meddelelse til din lærer: <filename> færdig
Fortsæt derefter med den næste fil."""
class Miner():
    sleepiness = 0
    thirst = 0
    hunger = 0
    whisky = 0
    gold = 0
    turn = 0

    def __repr__(self):
        return f"Dead: {self.dead()}. Gold: {self.gold}. Turn: {self.turn}"
    def sleep(self):
        self.sleepiness -= 10
        self.thirst += 1
        self.hunger += 1

    def mine(self):
        self.sleepiness += 5
        self.thirst += 5
        self.hunger += 5
        self.gold += 5

    def eat(self):
        self.sleepiness += 5
        self.thirst -= 5
        self.hunger -= 20
        self.gold -= 2

    def buy_whisky(self):
        self.sleepiness += 5
        self.thirst += 1
        self.hunger += 1
        self.whisky += 1
        self.gold -= 1

    def drink(self):
        self.sleepiness += 5
        self.thirst -= 15
        self.hunger -= 1
        self.whisky -= 1

    def dead(self):
        return self.sleepiness > 100 or self.thirst > 100 or self.hunger > 100

    def play(self):
        while not self.dead() and self.turn < 1000:
            self.turn += 1
            if self.sleepiness > 80:
                self.sleep()
            elif self.thirst > 80 and self.whisky < 1:
                self.buy_whisky()
            elif self.thirst > 80 and self.whisky > 0:
                self.drink()
            elif self.hunger >= 85:
                self.eat()
            else:
                self.mine()

morris = Miner()
morris.play()
print(morris)