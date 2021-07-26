# Imports:
from graphics import GraphWin, Circle, Line, Point, Text, color_rgb
from math import cos, sin, pi

# Constants (for easy tuning)
WINDOW_WIDTH = 900
WINDOW_HEIGHT = 900
GRAPH_RADIUS = 430
VERTEX_RADIUS = 18
LINES_WIDTH = 2

BACKGROUNDCOLOR = color_rgb(219,219,219)
FILLCOLOR = color_rgb(205,255,255)

# Classes/Functions:
class Vertex:
    def __init__(self, label, xPos, yPos):
        self.label = label
        self.xPos = xPos
        self.yPos = yPos

def construct_vertex(vertexNumber, totalVertices):
    radialPos = 2 * pi * vertexNumber / totalVertices
    xPos = cos(radialPos)*GRAPH_RADIUS + WINDOW_WIDTH/2
    yPos = sin(radialPos)*GRAPH_RADIUS + WINDOW_HEIGHT/2
    return Vertex(vertexNumber, xPos, yPos)
        

# Code:
print("===============================================================")
print("NOTE:\n")

print("This program generates the data for and then displays circulant")
print("graphs. All you need to tell it is what the size of the graph")
print("and edge-lengths are. The output is customizeable via the")
print("variables in all-caps at the top of the code, assuming you have")
print("python installed.")
print("===============================================================")
print("\n")

graphSize = None
while graphSize is None:
    try:
        graphSize = int(input("Type the size of the circulant graph: "))
    except ValueError:
        print("That was not a valid input. Please input a number.")


gettingEdges = True
lengthSet = list   # To appease PyCharm (and other IDE's which don't understand non-optional try:except: statements)
while gettingEdges:
    lengthInput = input("Enter the list of edge-lengths, separated by commas (ex. '1,2,3'): ")
    lengthSet = lengthInput.split(",")
    
    gettingEdges = False
    for i in range(len(lengthSet)):
        try:
            lengthSet[i] = int(lengthSet[i])
        except ValueError:
            print("Edge number " + str(i + 1) + " is not a valid input. Please input only numbers.")
            gettingEdges = True
            break


print("Generating Data...")
edgeSet = []
vertexSet = []
for i in range(graphSize):
    vertexSet.append(construct_vertex(i, graphSize))

lengthSet.sort()
for length in lengthSet:
    for i in range(graphSize):
        newEdge = (i, (i + length) % graphSize)
        edgeSet.append(newEdge)


print("Displaying Graphics...")
graphName = "Embedding of C" + str(graphSize) + "(" + str(lengthSet)[1:-1] + ")"
window = GraphWin(graphName, WINDOW_WIDTH, WINDOW_HEIGHT)
window.setBackground(BACKGROUNDCOLOR)

for edge in edgeSet:
    vertexA = vertexSet[edge[0]]
    vertexB = vertexSet[edge[1]]
    pointA = Point(vertexA.xPos, vertexA.yPos)
    pointB = Point(vertexB.xPos, vertexB.yPos)
    edgeLine = Line(pointA, pointB)

    edgeLine.setWidth(LINES_WIDTH)
    edgeLine.draw(window)

for vertex in vertexSet:
    vtPoint = Point(vertex.xPos,vertex.yPos)
    vtCircle = Circle(vtPoint, VERTEX_RADIUS)
    labelText = Text(vtPoint, str(vertex.label + 1))

    vtCircle.setFill(FILLCOLOR)
    vtCircle.setWidth(LINES_WIDTH)
    vtCircle.draw(window)

    labelText.setStyle("bold")
    labelText.draw(window)

print("Click the window to stop the program...")
window.getMouse()