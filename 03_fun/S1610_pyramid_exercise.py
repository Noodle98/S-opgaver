"""Opgave "Number pyramid"

Som altid skal du læse hele opgavebeskrivelsen omhyggeligt, før du begynder at løse opgaven.

Denne øvelse er en valgfri udfordring for de fremragende programmører blandt jer.
Du behøver absolut ikke at løse denne øvelse for at fortsætte med succes.

Kopier denne fil til din egen løsningsmappe. Skriv din løsning ind i kopien.

Se de første 93 sekunder af denne video: https://www.youtube.com/watch?v=NsjsLwYRW8o

Skriv en funktion "pyramid", der producerer de tal, der er vist i videoen.
Funktionen har en parameter "lines", der definerer, hvor mange talrækker der skal produceres.
Funktionen udskriver tallene i hver række og også deres sum.

I hovedprogrammet kalder du funktionen med fx 7 som argument.

Tilføj en mere generel funktion pyramid2.
Denne funktion har som andet parameter "firstline" en liste med pyramidens øverste rækkens tallene.

I hovedprogrammet kalder du pyramid2 med fx 10 som det første argument
og en liste med tal efter eget valg som andet argument.
Afprøv forskellige lister som andet argument.

Hvis du ikke aner, hvordan du skal begynde, kan du åbne S1620_pyramid_help.py og starte derfra

Når dit program er færdigt, skal du skubbe det til dit github-repository.
Send derefter denne Teams-meddelelse til din lærer: <filename> færdig
Fortsæt derefter med den næste fil."""
def pyramid(lines):
    all_numbers_lists = [[1, 1]]
    new_number = 1
    for line in range(lines):
        new_number += 1
        new_line = []
        numbers = all_numbers_lists[-1]
        for x in range(len(numbers)):
            #print(f"number spotted: {numbers[x]}")
            try:
                if numbers[x] + numbers[x+1] == new_number:
                    new_line.append(numbers[x])
                    #print(numbers[x])
                    new_line.append(new_number)
                    #print(numbers[x] + 1)
                else:
                    new_line.append(numbers[x])
            except IndexError:
                new_line.append(numbers[x])
        all_numbers_lists.append(new_line)


        #print(new_line)
    for list in all_numbers_lists:
        print(list)
pyramid(7)