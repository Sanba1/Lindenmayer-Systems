import numpy as np
from matplotlib import pyplot as plt

def LindIter(System, N):
    if System == "Koch":
        LindenmayerString = "S"
    elif System == "Sierpinski":
        LindenmayerString = "A"

    rules = {"S": "SLSRSLS", "L": "L", "R": "R", "A": "BRARB", "B": "ALBLA", "D": "DLDDRDL"}

    def LindString(start):
        output = ''
        for letter in start:
            LindenmayerString = rules[letter]
            output += LindenmayerString
        return output

    for i in range(N):
        LindenmayerString = LindString(LindenmayerString)

    return LindenmayerString

def turtleGraph(LindenmayerString,N):
    turtleCommands = []
    if LindenmayerString[0] == "S":
        kochCommands = {"S": (1/3 ** N), "L": (np.pi / 3), "R": (-2*np.pi/3)}
        for letter in LindenmayerString[:]:
            LindenmayerString = kochCommands[letter]
            turtleCommands.append(LindenmayerString)

    elif LindenmayerString[0] == "A" or "B":
        sierpinskiCommands = {"A": (1/2**N), "B": (1/2**N), "L": (np.pi/3), "R": (-np.pi/3)}
        for letter in LindenmayerString[:]:
            LindenmayerString = sierpinskiCommands[letter]
            turtleCommands.append(LindenmayerString)
    turtleCommands = np.array(turtleCommands)
    return turtleCommands


def turtlePlot(turtleCommands):
    coords = np.array([[0, 0]])
    lenght = np.array([turtleCommands[0], 0])
    angle = np.array([[1, 0], [0, 1]])

    for i in range(len(turtleCommands)):
        if i % 2 != 0:  # as indexes start from 0, the odd indexes are the angles
            directionMatrix = np.array([[np.cos(turtleCommands[i]), -np.sin(turtleCommands[i])], [np.sin(turtleCommands[i]), np.cos(turtleCommands[i])]])
            angle = np.dot(directionMatrix, angle)

        else:
            newCoords = [np.add(coords[-1], np.dot(angle, lenght))]
            coords = np.append(coords, newCoords, axis=0)
        xcoords = [x[0] for x in coords]  # plotting the first column of the coordintes for the x-axis
        ycoords = [x[1] for x in coords]  # plotting the second column of the coordinated for the y-axis
    plt.plot(xcoords, ycoords)  # creating the graph for the line plot
    plt.show()  # show the plot
# in next iteration new coordinates are made from the previous coordinates


def Main():
    while True:
        # The options are printed
        print("\n1.Choose the type of Lindenmayer system and the number of iterations\n2.Generate plot\n3.Quit\n")
        option = int(input("Enter your option: "))
        # The choice made must be an integer, and we give it some conditions thorugh if-statements.
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
