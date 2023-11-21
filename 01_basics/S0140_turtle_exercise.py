"""
Opgave "Tom the Turtle":

Som altid skal du læse hele opgavebeskrivelsen omhyggeligt, før du begynder at løse opgaven.

Kopier denne fil til din egen løsningsmappe. Skriv din løsning ind i kopien.

Funktionen "demo" introducerer dig til alle de kommandoer, du skal bruge for at interagere med Tom i de følgende øvelser.

Kun hvis du er nysgerrig og elsker detaljer:
    Her er den fulde dokumentation for turtle graphics:
    https://docs.python.org/3.3/library/turtle.html

Del 1:
    Skriv en funktion "square", som accepterer en parameter "length".
    Hvis denne funktion kaldes, får skildpadden til at tegne en firkant med en sidelængde på "længde" pixels.

Del 2:
     Færdiggør funktionen "visible", som skal returnere en boolsk værdi,
     der angiver, om skildpadden befinder sig i det synlige område af skærmen.
     Brug denne funktion i de følgende dele af denne øvelse
     til at få skildpadden tilbage til skærmen, når den er vandret væk.

Del 3:
    Skriv en funktion "many_squares" med en for-loop, som kalder square gentagne gange.
    Brug denne funktion til at tegne flere firkanter af forskellig størrelse i forskellige positioner.
    Funktionen skal have nogle parametre. F.eks:
        antal: hvor mange firkanter skal der tegnes?
        størrelse: hvor store er firkanterne?
        afstand: hvor langt væk fra den sidste firkant er den næste firkant placeret?

Del 4:
    Skriv en funktion, der producerer mønstre, der ligner dette:
    https://pixabay.com/vectors/spiral-square-pattern-black-white-154465/

Del 5:
    Skriv en funktion, der producerer mønstre svarende til dette:
    https://www.101computing.net/2d-shapes-using-python-turtle/star-polygons/
    Funktionen skal have en parameter, som påvirker mønsterets form.

Del 6:
    Opret din egen funktion, der producerer et sejt mønster.
    Senere, hvis du har lyst, kan du præsentere dit mønster på storskærmen for de andre.

Når dit program er færdigt, skal du skubbe det til dit github-repository.
Send derefter denne Teams-meddelelse til din lærer: <filename> færdig
Fortsæt derefter med den næste fil.
"""

import turtle  # this imports a library called "turtle". A library is (someone else's) python code, that you can use in your own program.

# Del 2:
def visible(turtle_name):  # returns true if both the x- and y-value of the turtle's position are between -480 and 480
    # you will need this: x-value: turtle_name.position()[0]
    # and this:           y-value: turtle_name.position()[1]
    x = turtle_name.position()[0]
    y = turtle_name.position()[1]
    if (x <= 480 and x >= -480) and (y <= 480 and y >= -480):
        return True
    else:
        return False



def demo():  # demonstration of basic turtle commands
    tom = turtle.Turtle()  # create an object named tom of type Turtle
    print(type(tom))
    tom.speed(1)  # fastest: 10, slowest: 1
    for x in range(8):  # do the following for x = 0, 1, 2, 3, 4, 5, 6, 7
        tom.forward(50)  # move 50 pixels
        tom.left(45)  # turn 45 degrees left
        print(f'Tom is now at {tom.position()}, x-value: {tom.position()[0]=:.2f}, y-value: {tom.position()[1]=:.2f}')
    tom.penup()  # do not draw while moving from now on
    tom.forward(100)
    tom.pendown()  # draw while moving from now on
    tom.pencolor("red")  # draw in red
    tom.right(90)  # turn 90 degrees right
    tom.forward(120)
    tom.right(-90)  # turning -90 degrees right is the same as turning +90 degrees left
    tom.forward(120)
    tom.home()  # return to the original position in the middle of the window
    turtle.done()  # keeps the turtle window open after the program is done


#demo()
# Del 1:
def square(length):
    tom = turtle.Turtle()
    tom.speed(1)
    tom.pendown()
    for x in range(4):
        tom.forward(length)
        tom.left(90)
    tom.penup()
    turtle.done()

# square(150)

# Del 3:
def many_squares(amount, length, distance):
    tom = turtle.Turtle()
    tom.speed(1)
    for number in range(amount):
        for sides in range(4):
            tom.pendown()
            tom.forward(length)
            tom.left(90)
        tom.penup()
        tom.forward(length)
        tom.forward(distance)
    tom.home()
    turtle.done()

# many_squares(4, 50, 30)

# Del 4:
def spiral_square_pattern(spiral_distance, amount):
    tom = turtle.Turtle()
    tom.speed(1)
    tom.right(90)
    tom.pendown()
    current_size = spiral_distance * 2
    for number in range(amount):
        tom.forward(current_size)
        current_size = current_size + spiral_distance
        tom.left(90)
    turtle.done()

# spiral_square_pattern(5, 20)

# Del 5:
""" 
Jeg ved godt den ikke virker ordenligt,
Men jeg kan ikke finde ud af hvordan man får den til at virke som den skal.
Jeg går ud fra at jeg skal dividere 360 eller 180 (grader) med hvor mange spidser der skal være.
Men uanset hvordan jeg prøver bliver resultatet ikke som jeg ønsker det.
"""
def star_polygons(points, length):
    tom = turtle.Turtle()
    tom.speed(5)
    tom.pendown()
    angle = 180 - (360 / points)
    for x in range(points):
        tom.forward(length)
        tom.right(angle)
    turtle.done()

#star_polygons(7, 100)

# Del 6:
def outwards_square_pattern(length, size):
    tom = turtle.Turtle()
    tom.speed(5)
    amount = size * 4
    spiral_distance = length * 2
    for squares in range(amount):
        tom.pendown()
        for sides in range(4):
            tom.forward(length)
            tom.left(90)
        tom.penup()
        tom.left(90)
        tom.forward(spiral_distance)
        spiral_distance = spiral_distance + length
    turtle.done()

outwards_square_pattern(40, 10)