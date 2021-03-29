#!python3
# Volume Calculator
# Feel free to rename your variables


def title():
    # Will display a title screen
    # input parameters: none needed
    # output parameters: None
    # Author: Copper
    # Modified:
    print("==========Title Screen==========")

def instructions():
    # Will display instructions
    # input parameters: none needed
    # output parameters: None
    # Author:
    # Modified:
    print("Calculate Area of Circle --- 1")
    print("Calculate Perimeter of Regular Polygon --- 2")
    print("Calculate Surface Area of Cylinder ---3")
    print("Calculate Volume of Cone --- 4")
    print("Exit --- 5")
    print("==================================")

def getParams(shape):
    # Will create a list of questions to be asked depending on the shape.
    # These will be asked so that the user can enter in appropriate values
    # input parameter: string 
    # output parameter: return a list containing the prompts for each shape:
    # example: ["Enter the radius:","Enter the slant height:","Enter the height:"]
    prompts = []
    if shape == "Circle":
        prompts.append(("Enter the Radius: "))
    elif shape == "Regular Polygon":
        prompts.append(("Enter the Number of Sides: "))
        prompts.append(("Enter the Sides Length: "))
    elif shape == "Cylinder":
        prompts.append(("Enter the Height: "))
        prompts.append(("Enter the Radius: "))
    elif shape == "Cone":
        prompts.append(("Enter the Height: "))
        prompts.append(("Enter the Radius: "))

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

def cycle_area(l):
    print("Area of Circle is : ", end = "")
    return l[0] * l[1]

def regular_polygon_perimeter(l):
    print("Perimeter of Regular Polygon is : ", end = "")
    return l[0] * l[1]

def cylinder_surface_area(l):
    print("Surface Area of Cylinder is : ", end = "")
    return cylinder_surface_area([l[1]]) * 2 + l[0] * l[1] * 2 * math.pi

def cone_volume(l):
    print("Volume of Cone is : ", end = "")
    return circle_area([l[0]]) * l[1] * 1/3

def main():
    # main block of code that will run your program and control program flow
    # You will need to include a while loop to keep repeating the commands until
    # the user chooses to exit
    shape_list = ["Circle", "Regular Polygon", "Cylinder", "Cone"]
    title()
    instructions()
    option = int(input())
    while option != 5:
        shape = shape_list[option - 1]
        input_list = getInputs(getParams(shape))
        if option == 1:
            print(cycle_area(input_list))
        elif option == 2:
            print(regular_polygon_perimeter(input_list))
        elif option == 3:
            print(cylinder_surface_area(input_list))
        elif option == 3:
            print(cone_volume(input_list))
        title()
        instructions()
        option = int(input())
main()
