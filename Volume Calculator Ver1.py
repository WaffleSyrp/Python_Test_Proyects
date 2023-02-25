import math


def proceed():
    print("Would you like to continue?")
    print("(Answer with YES or NO)")
    blueamogus = input("")
    if blueamogus == "YES" or blueamogus == "yes" or blueamogus == "Y" or blueamogus == "y":
        sussy_calc()
    elif blueamogus == "NO" or blueamogus == "no" or blueamogus == "N" or blueamogus == "n":
        quit()
    else:
        print("Invalid input. Please try again")
        proceed()#


def sussy_calc():
    print("Please enter your desired process:")
    amogus = input("")
    if amogus == "Volume" or amogus == "volume" or amogus == "VOLUME":
        print("You selected VOLUME")
        print("Keep in mind that this calculator is only equipped to find the volume of a:")
        print("CUBE, RECTANGULAR PRISM, a PYRAMID, a SPHERE, and a CYLINDER")
        print("Please enter the type of shape you want to find the volume for:")
        redamogus = input("")
        if redamogus == "CUBE" or redamogus == "Cube" or redamogus == "cube":
            print("You selected CUBE")
            print("Please enter the length of any edge")
            print("DO NOT INSERT LETTERS ONLY NUMBERS")
            sussyred1 = float(input(""))
            print("ANSWER:")
            print(sussyred1 ** 3)
        elif redamogus == "RECTANGULAR PRISM" or redamogus == "Rectangular Prism" or redamogus == "Rectangular prism" or redamogus == "rectangular prism":
            print("You selected RECTANGULAR PRISM")
            print("Please enter it's length")
            print("DO NOT INSERT LETTERS ONLY NUMBERS")
            sussyred1 = float(input(""))
            print("Please enter it's with")
            print("DO NOT INSERT LETTERS ONLY NUMBERS")
            sussyred2 = float(input(""))
            print("Please enter it's height")
            print("DO NOT INSERT LETTERS ONLY NUMBERS")
            sussyred3 = float(input(""))
            print("ANSWER:")
            print(sussyred1 * sussyred2 * sussyred3)
        elif redamogus == "SPHERE" or redamogus == "Sphere" or redamogus == "sphere":
            print("You selected SPHERE")
            print("Do you have the radius or diameter of the sphere?")
            sussyred1 = input("")
            if sussyred1 == "RADIUS" or sussyred1 == "Radius" or sussyred1 == "radius":
                print("Please enter the radius")
                print("DO NOT INSERT LETTERS ONLY NUMBERS")
                sussyred2 = float(input(""))
                sussyred3 = sussyred2 ** 3
                print("ANSWER:")
                print(4.188790205 * sussyred3)
            elif sussyred1 == "DIAMETER" or sussyred1 == "Diameter" or sussyred1 == "diameter":
                print("Please enter the diameter")
                print("DO NOT INSERT ANY LETTERS ONLY NUMBERS")
                sussyred2 = float(input(""))
                sussyred3 = sussyred2 / 2
                sussyred4 = sussyred3 ** 3
                print("ANSWER:")
                print(4.188790205 * sussyred4)
            else:
                print("Invalid input. Please try again")
                pass
        elif redamogus == "CYLINDER" or redamogus == "Cylinder" or redamogus == "cylinder":
            print("You selected CYLINDER")
            print("Please enter the height")
            print("DO NOT INSERT LETTERS ONLY NUMBERS")
            sussyred1 = float(input(""))
            print("Do you have the radius or diameter of the cylinder?")
            sussyred2 = input("")
            if sussyred2 == "RADIUS" or sussyred2 == "Radius" or sussyred2 == "radius":
                print("Please enter the radius")
                print("DO NOT INSERT LETTERS ONLY NUMBERS")
                sussyred3 = float(input(""))
                sussyred4 = sussyred3 ** 2
                sussyred5 = sussyred4 * sussyred1
                print("ANSWER:")
                print(math.pi * sussyred5)
            elif sussyred2 == "DIAMETER" or sussyred2 == "Diameter" or sussyred2 == "diameter":
                print("Please enter the diameter")
                print("DO NOT INSERT LETTERS ONLY NUMBERS")
                sussyred3 = float(input(""))
                sussyred4 = sussyred3 / 2
                sussyred5 = sussyred4 ** 2
                sussyred6 = sussyred5 * sussyred1
                print("ANSWER:")
                print(math.pi * sussyred6)
            else:
                print("Invalid input. Please try again")
                pass
        elif redamogus == "PYRAMID" or redamogus == "Pyramid" or redamogus == "pyramid":
            print("You selected PYRAMID")
            print("Does the pyramid have a square base?")
            print("(Answer with YES or NO)")
            sussyred1 = input("")
            if sussyred1 == "YES" or sussyred1 == "Yes" or sussyred1 == "y" or sussyred1 == "Y":
                print("Please the base's length")
                sussyred2 = float(input(""))
                print("Please enter the pyramid's height")
                sussyred3 = float(input(""))
                sussyred4 = (sussyred2*2)*sussyred3
                print("ANSWER:")
                print(sussyred4/3)
            elif sussyred1 == "NO" or sussyred1 == "No" or sussyred1 == "n" or sussyred1 == "N":
                print("Please enter the base's length")
                print("DO NOT INSERT LETTERS ONLY NUMBERS")
                sussyred2 = float(input(""))
                print("Please enter the base's with")
                print("DO NOT INSERT LETTERS ONLY NUMBERS")
                sussyred3 = float(input(""))
                print("Please enter the pyramid's height")
                print("DO NOT INSERT LETTERS ONLY NUMBERS")
                sussyred4 = float(input(""))
                sussyred5 = sussyred4 * sussyred3 * sussyred2
                print("ANSWER:")
                print(sussyred5/3)
            else:
                print("Invalid input. Please try again")
        else:
            print("Invalid input. Please try again")
            pass
    elif amogus == "PERIMETER" or amogus == "Perimeter" or amogus == "perimeter":
        print("You selected PERIMETER")
        print(
            "Keep in mind that this calculator is only equipped to find the perimeter of a:")
        print("SQUARE, a RECTANGLE, a TRIANGLE and CIRCLE")
        print("Please enter the type of shape you want to find the perimeter for:")
        sussyred1 = input("")
        if sussyred1 == "SQUARE" or sussyred1 == "Square" or sussyred1 == "square":
            print("You selected SQUARE")
            print("Please enter the length of any side of the square")
            print("DO NOT INSERT LETTERS ONLY NUMBERS")
            sussyred2 = float(input(""))
            print("ANSWER:")
            print(sussyred2 * 4)
        elif sussyred1 == "RECTANGLE" or sussyred1 == "Rectangle" or sussyred1 == "rectangle":
            print("You selected RECTANGLE")
            print("Please enter the length")
            print("DO NOT INSERT LETTERS ONLY NUMBERS")
            sussyred2 = float(input(""))
            sussyred3 = sussyred2 * 2
            print("Please enter the with")
            print("DO NOT INSERT LETTERS ONLY NUMBERS")
            sussyred4 = float(input(""))
            sussyred5 = sussyred4 * 2
            print("ANSWER:")
            print(sussyred3 + sussyred5)
        elif sussyred1 == "TRIANGLE" or sussyred1 == "Triangle" or sussyred1 == "triangle":
            print("You selected TRIANGLE")
            print("Is the triangle equilateral?")
            print("(Answer with Yes or No")
            sussyred2 = input("")
            if sussyred2 == "YES" or sussyred2 == "Yes" or sussyred2 == "y" or sussyred2 == "Y":
                print("Please enter the length of any side")
                print("DO NOT INSERT LETTERS ONLY NUMBERS")
                sussyred3 = float(input(""))
                print("ANSWER:")
                print(sussyred3 * 3)
            elif sussyred2 == "NO" or sussyred2 == "No" or sussyred2 == "n" or sussyred2 == "N":
                print("Please enter the length of the first side")
                print("DO NOT INSERT LETTERS ONLY NUMBERS")
                sussyred3 = float(input(""))
                print("Please enter the length of the second side")
                print("DO NOT INSERT LETTERS ONLY NUMBERS")
                sussyred4 = float(input(""))
                print("Please enter the length of the third side")
                print("DO NOT INSERT LETTERS ONLY NUMBERS")
                sussyred5 = float(input(""))
                print("ANSWER:")
                print(sussyred5 + sussyred4 + sussyred3)
            else:
                print("Invalid input. Please try again")
                pass
        elif sussyred1 == "CIRCLE" or sussyred1 == "Circle" or sussyred1 == "circle":
            print("You selected CIRCLE")
            print("Do you have the radius or diameter of the circle?")
            sussyred2 = input("")
            if sussyred2 == "RADIUS" or sussyred2 == "Radius" or sussyred2 == "radius":
                print("Please enter the radius")
                print("DO NOT INSERT LETTERS ONLY NUMBERS")
                sussyred3 = float(input(""))
                print("ANSWER:")
                print(6.283185307 * sussyred3)
            elif sussyred2 == "DIAMETER" or sussyred2 == "Diameter" or sussyred2 == "diameter":
                print("Please enter the diameter")
                print("DO NOT INSERT LETTERS ONLY NUMBERS")
                sussyred3 = float(input(""))
                sussyred4 = sussyred3 / 2
                print("ANSWER:")
                print(6.283185307 * sussyred4)
            else:
                print("Invalid input. Please try again")
                pass
        else:
            print("Invalid input. Please try again")
    elif amogus == "Amogus" or amogus == "amogus" or amogus == "AMOGUS":
        print("I wanna have seccs with amogus so bad omg")
    elif amogus == "AREA" or amogus == "Area" or amogus == "area":
        print("You selected AREA")
        print(
            "Keep in mind that this calculator is only equipped to find the area of a:")
        print("SQUARE, a RECTANGLE, a TRIANGLE, a CIRCLE and a TRAPEZOID")
        print("Please enter the type of shape you want to find the area for")
        sussyred1 = input("")
        if sussyred1 == "SQUARE" or sussyred1 == "Square" or sussyred1 == "square":
            print("You selected SQUARE")
            print("Please enter the length of any side of the square")
            print("DO NOT INSERT LETTERS ONLY NUMBERS")
            sussyred2 = float(input(""))
            print("ANSWER:")
            print(sussyred2 ** 2)
        elif sussyred1 == "RECTANGLE" or sussyred1 == "Rectangle" or sussyred1 == "rectangle":
            print("You selected RECTANGLE")
            print("Please enter the length")
            print("DO NOT INSERT LETTERS ONLY NUMBERS")
            sussyred2 = float(input(""))
            print("Please enter the with")
            print("DO NOT INSERT LETTERS ONLY NUMBERS")
            sussyred3 = float(input(""))
            print("ANSWER:")
            print(sussyred2 * sussyred3)
        elif sussyred1 == "TRIANGLE" or sussyred1 == "Triangle" or sussyred1 == "triangle":
            print("You selected TRIANGLE")
            print("Please enter the height")
            print("DO NOT INSERT LETTERS ONLY NUMBERS")
            sussyred2 = float(input(""))
            print("Please enter the length of the triangle's base")
            print("DO NOT INSERT LETTERS ONLY NUMBERS")
            sussyred3 = float(input(""))
            sussyred4 = sussyred3 * sussyred2
            print("ANSWER:")
            print(sussyred4 / 2)
        elif sussyred1 == "CIRCLE" or sussyred1 == "Circle" or sussyred1 == "circle":
            print("You selected CIRCLE")
            print("Do you have the radius or diameter of the circle?")
            sussyred2 = input("")
            if sussyred2 == "RADIUS" or sussyred2 == "Radius" or sussyred2 == "radius":
                print("Please enter the radius")
                print("DO NOT INSERT LETTERS ONLY NUMBERS")
                sussyred3 = float(input(""))
                sussyred4 = sussyred3 ** 2
                print("ANSWER:")
                print(math.pi * sussyred4)
            elif sussyred2 == "DIAMETER" or sussyred2 == "Diameter" or sussyred2 == "diameter":
                print("Please enter the diameter")
                print("DO NOT INSERT LETTERS ONLY NUMBERS")
                sussyred3 = float(input(""))
                sussyred4 = sussyred3 / 2
                sussyred5 = sussyred4 ** 2
                print("ANSWER:")
                print(math.pi * sussyred5)
            else:
                print("Invalid input. Please try again")
                pass
        elif sussyred1 == "TRAPEZOID" or sussyred1 == "Trapezoid" or sussyred1 == "trapezoid":
            print("You selected TRAPEZOID")
            print("Please enter the trapezoid's first base")
            print("DO NOT INSERT LETTERS ONLY NUMBERS")
            sussyred2 = float(input(""))
            print("Please enter the trapezoid's second base")
            print("DO NOT INSERT LETTERS ONLY NUMBERS")
            sussyred3 = float(input(""))
            print("Please enter the trapezoid's height")
            print("DO NOT INSERT LETTERS ONLY NUMBERS")
            sussyred4 = float(input(""))
            sussyred5 = (sussyred2 + sussyred3) / 2
            print("ANSWER:")
            print(sussyred5 * sussyred4)
        else:
            print("Invalid input. Please try again")
    else:
        print("Invalid input. Please try again")
        pass


print("Hello! Welcome to my AREA, PERIMETER and VOLUME calculator")
print("Please enter CONTINUE to begin, or QUIT to exit")
BlueAmogus = input("")
if BlueAmogus == "QUIT" or BlueAmogus == "quit":
    quit()
elif BlueAmogus == "CONTINUE" or BlueAmogus == "continue":
    sussy_calc()
else:
    print("Invalid input. Please try again")
    proceed()
print("Would you like to continue?")
print("(Answer with YES or NO)")
greenamogus = input("")
while greenamogus == "YES" or greenamogus == "yes" or greenamogus == "y" or "Y":
    sussy_calc()
    proceed()
quit()
