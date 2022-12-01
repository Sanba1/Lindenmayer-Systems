"""
Please enjoy the Lindenmayer System Program, which we worked on as our exam project. We chose this project because it seemed intriguing and was a good way to use some of the programming skills we have learnt in this semester.
Lindenmayer system was created to simulate natural systems like the Sierpinski triangle and the Koch curve

what this program does is that it first asks you to choose which Lindenmayer system you want to perform.
It will then ask the number of iterations.
However, there is a limit to the number of iterations that can be put in for the function to work as higher number of iterations take a lot of time to compute.
You will then have the opportunity to map the system using the program. This will display the specified Lindenmayer system's plot.
We have also made it as user-friendly as much as possible.
We have also used try-except to deal with possible errors.

Enjoy

By: Dhruva Sakhare, Lawrence Ryan and Santosh Balaji

"""


import numpy as np
from matplotlib import pyplot as plt


'''
The LindIter(System, N) function uses the arguments System and N to compute the Lindenmayer String after N iterations.
It uses the "rules" dictionary to convert the symbols, for example it converts S to SLSRSLS.
We have used another function LindString(string) inside LindIter(System, N), which translates the symbols according to rules.
Then we finaly do the steps for N iterations.

System: The type of system the user wants to compute.
N: The number of iterations.
'''
def LindIter(System, N):
    if System == "Koch":
        LindenmayerString = "S"  # the first letter of Koch System
    elif System == "Sierpinski":
        LindenmayerString = "A"  # the first letter of Sierpinski System

    rules = {"S": "SLSRSLS", "L": "L", "R": "R", "A": "BRARB", "B": "ALBLA", "D": "DLDDRDL"}

    def LindString(string):
        output = ''
        for letter in string:
            LindenmayerString = rules[letter]  # Translates according to rules.
            output += LindenmayerString
        return output

    for i in range(N):  # Iterates N times.
        LindenmayerString = LindString(LindenmayerString)

    return LindenmayerString


'''
The turtleGraph(LindenmayerString,N) function determines the plot commands from the Lindenmayer String, which was computed by LindIter(System, N).
It does this by translating the string into commands based on the commands dictionary, which is unique to the system.

LindenmayerString: The Lindmayer String computed before.
N: The number of iterations.
'''

def turtleGraph(LindenmayerString,N):
    turtleCommands = []
    if LindenmayerString[0] == "S":  # As S is always the first letter of Koch system.
        kochCommands = {"S": (1/3 ** N), "L": (np.pi / 3), "R": (-2*np.pi/3)}  # commands
        for letter in LindenmayerString[:]:
            LindenmayerString = kochCommands[letter]
            turtleCommands.append(LindenmayerString)

    elif LindenmayerString[0] == "A" or "B":  # As the first letter of Sierpinski system can be A or B.
        sierpinskiCommands = {"A": (1/2**N), "B": (1/2**N), "L": (np.pi/3), "R": (-np.pi/3)}  # commands
        for letter in LindenmayerString[:]:
            LindenmayerString = sierpinskiCommands[letter]
            turtleCommands.append(LindenmayerString)
    turtleCommands = np.array(turtleCommands)
    return turtleCommands


'''
The turtlePlot(turtleCommands) uses the commands computed in turtleGraph(LindenmayerString,N) to plot the final graph.

turtleCommands: An array of numbers which signify the distance and angle the "turtle" should move to plot the graph. Computed by turtleGraph(LindenmayerString,N).
'''
def turtlePlot(turtleCommands):
    coords = np.array([[0, 0]])  # Starting from the origin (0,0).
    lenght = np.array([turtleCommands[0], 0])  # The first lenght is the first Letter in the string.
    angle = np.array([[1, 0], [0, 1]])

    for i in range(len(turtleCommands)):
        if i % 2 != 0:  # as indexes start from 0, the odd indexes are the angles
            directionMatrix = np.array([[np.cos(turtleCommands[i]), -np.sin(turtleCommands[i])], [np.sin(turtleCommands[i]), np.cos(turtleCommands[i])]])
            angle = np.dot(directionMatrix, angle)  # Using the formula from the Projects documentation.

        else:
            newCoords = [np.add(coords[-1], np.dot(angle, lenght))]  # Using the formula from the Projects documentation to find the next coordinate.
            coords = np.append(coords, newCoords, axis=0)
        xcoords = [x[0] for x in coords]  # plotting the first column of the coordinates for the x-axis
        ycoords = [x[1] for x in coords]  # plotting the second column of the coordinated for the y-axis
    plt.plot(xcoords, ycoords)  # creating the graph
    plt.show()  # show the plot
    # in next iteration new coordinates are made from the previous coordinates

'''
Finally, our main script :)
First it prints the options and then the user can select the option they want.
The user inputs the type of system and number of iterations they want and then they can select to plot a graph for the same.
'''
def Main():
    while True:
        # The options are printed
        print("\n1.Choose the type of Lindenmayer system and the number of iterations\n2.Generate plot\n3.Quit\n")
        option = int(input("Enter your option: "))
        # The choice made must be an integer, and we give it some conditions through if-statements.
        # Also, there is an if-statement in order to prevent error.
        valid = 0
        if option == 1:

            # Attempt to get a valid number, valid is the condition that there is a valid input
            valid = 0

            # Runs a loop if the question is not fulfilled using the valid varible, in this case, type of Lindermayer system
            while (valid == 0):

                temp = input("\nChoose the type of Lindenmayer system:\n 1.Koch System\n 2.Sierpinski System \nEnter your option: ")

                # Filters through different possible cases of answers. If the answer is satisfactory, make valid != 0
                try:
                    systemChoice = int(temp)
                except ValueError:
                    print("Please enter an integer option.")

                if systemChoice == 1:
                    System = "Koch"
                    valid = 1
                elif systemChoice == 2:
                    System = "Sierpinski"
                    valid = 1
                else:
                    print("Please select between option 1 or 2.")

            valid = 0

            # Similar system as the previous question, asking iterations
            while (valid == 0):

                temp = input("How many iterations would you like? : ")

                try:
                    N = int(temp)
                except ValueError:
                    print("Please enter an integer option.")

                if N <= 0:
                    print("The number of iterations must be positive.")
                elif N > 9:
                    print('The number of iterations is limited to 9, as to prevent excessive runtime.')

                # Prints out the final "load" of the loading data process, prints out what was chosen, the menu screen will reappear
                else:
                    print(
                        f'\nYou have chosen {System} as your Lindenmayer system and chosen {N} number of iterations\n')
                    valid = 1

        if option == 2:
            # At this point, it is shown how every function in the whole program should run, and what inputs should be used for each of them
            turtlePlot(turtleGraph(LindIter(System, N), N))

        if option == 3:
            print("Goodbye")
            break
        elif valid == 0:
            print("Please select between option 1, 2 or 3.")


Main()
