#!python3
# Volume Calculator
# Feel free to rename your variables

import math
def title():
    # Will display a title screen
    # input parameters: none needed
    # output parameters: None
    # Author: Copper
    # Modified:
    # title
    print("===========Title Screen============")

def instructions():
    # Will display instructions
    # input parameters: none needed
    # output parameters: None
    # Author:
    # Modified:
   print("Calculate Area of Rectangle --- 1")
   print("Calculate Perimeter of Triangel --- 2")
   print("Calculate Surface Area of Cube --- 3")
   print("Calculate Volum of Cylinder --- 4")
   print("Exit --- 5")
   print("===============================")


def getParams(shape):
    # Will create a list of questions to be asked depending on the shape.
    # These will be asked so that the user can enter in appropriate values
    # input parameter: string 
    # output parameter: return a list containing the prompts for each shape:
    # example: ["Enter the radius:","Enter the slant height:","Enter the height:"]
    prompts = []
    if shape == "Rectangle":
        prompts.append(("Enter the width: "))
        prompts.append(("Enter the Height: "))
    elif shape == "Triangle":
        prompts.append(("Enter the First Length: "))
        prompts.append(("Enter the Second Length: "))
        prompts.append(("Enter the Third Length: "))
    elif shape == "Cube":
        prompts.append(("Enter the Side of Length: "))
    elif shape == "Cylinder":
        prompts.append(("Enter the Radius: "))
        prompts.append(("Enter the Height: "))


    return prompts

def getInputs(questions):
    # Will prompt the user for inputs for the shape they.
    # These will be asked so that the user can enter in appropriate values
    # It will turn all the input data into a list
    # input parameter: list containing the prompts/questions
    # output parameter: return a list containing all the measurements of the shape
    measurements = []
    for q in questions:
        measurements.append(int(input(q)))
    
    return measurements

def rectangle_area (l):
    print("Area of Rectangle is :", end = "")
    return l[0]*l[1]

def tangle_primieter (l):
    print("Primieter of Triangle is :", end = "")
    return l[0]+l[1]+l[2]

def cube_surface_area (l):
    print("Surface Area of Cube is :", end = "")
    return (l[0]^2)*6

def cylinder_volum (l):
    print("Volum of Cylinder is :", end = "")
    return math.pi * (l[1]^2) *l[2]

def main():
    # main block of code that will run your program and control program flow
    # You will need to include a while loop to keep repeating the commands until
    # the user chooses to exit
    shape_list = ["Rectangle","Triangle","Cube","Cylinder"]
    title()
    instructions()
    option = int(input())
    while option!= 9:
        if option == 1:
            print(rectangle_area(input_list))
        elif option == 2:
            print(triangle_perimeter(input_list))
        elif option == 3:
            print(cube_surface_area(input_list))
        elif option == 4:
            print(cylinder_volum(input_list))
main()
