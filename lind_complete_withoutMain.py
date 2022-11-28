import numpy as np
from matplotlib import pyplot as plt
import math as math

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

    elif LindenmayerString[0] == "A":
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
turtlePlot(turtleGraph("SLSRSLSLSLSRSLSRSLSRSLSLSLSRSLS",2))
