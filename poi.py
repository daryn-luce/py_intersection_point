import pygame
import os

background_color = (255,255,255)
width, height = 800,800
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('POI Map')

def findSlope(line):
	return (int(line["y2"]) - int(line["y1"])) / (int(line["x2"]) - int(line["x1"]))
	
def findB(line, m):
	return (int(line["y1"]) - (m * int(line["x1"])))
	

def findY(m1, m2, b1, b2):
    xA = m2 - m1
    xB = b1 - b2
    x = xB / xA
    y1 = m1 * x + b1
    y2 = m2 * x + b2
    if y1 == y2:
        return y1

def newCords(x,y):
    y = -y
    x_zero = width / 2
    y_zero = height / 2
    return (int(x + x_zero), int(y + y_zero))
    
    
class Line():
    def __init__(self, point1, point2, color,thick):
        self.x1, self.y1 = point1
        self.x2, self.y2 = point2
        self.color = color
        self.thick = thick
        
    def display(self):
        pygame.draw.line(screen,self.color, (self.x1,self.y1),(self.x2,self.y2), self.thick)

LinesX = int(width / 10)
LinesY = int(height / 10)
x_inc = width / LinesX
y_inc = height / LinesY
x1w = 0
y1w = (height / 2) + y_inc
y2w = (height / 2) - y_inc
y1h = 0
x1h = (width / 2) + x_inc
x2h = (width / 2) - x_inc
x_gridLines = []
y_gridLines = []

xBaseLine = Line((width / 2, 0), (width / 2 , height), (128,128,128), 2)
yBaseLine = Line((0, height / 2), (width, height / 2), (128,128,128), 2)

for n in range(LinesX):
    thick = 1
    x1w = x1w + x_inc
    x_line = Line((int(x1w),int(y1w)),(int(x1w),int(y2w)), (128,128,128),thick)
    x_gridLines.append(x_line)
for n in range(LinesY):
    thick = 1
    y1h = y1h + y_inc
    y_line = Line((int(x1h),int(y1h)),(int(x2h),int(y1h)), (128,128,128),thick)
    y_gridLines.append(y_line)
    
first_points = {
	"x1": 0,
	"y1": 0,
	"x2": 0,
	"y2": 0
	}
second_points = {
	"x1": 0,
	"y1": 0,
	"x2": 0,
	"y2": 0
	}
running = True
while running:
    screen.fill(background_color)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
        if event.type == pygame.MOUSEBUTTONDOWN:
            
            pygame.draw.line(screen,(128,128,128), (width / 2,0), (width / 2,height), 1)
            pygame.draw.line(screen,(128,128,128), (0, height / 2), (width, height / 2), 1)
            os.system('cls||clear')
            aFirst = input("First point, first line 'x,y': ")
            aSecond = input("Second point, first line 'x,y': ") 
            bFirst = input("First point, second line 'x,y': ") 
            bSecond = input("Second point, second line 'x,y': ") 

            first_points["x1"], first_points["y1"] = aFirst.split(",")
            first_points["x2"], first_points["y2"] = aSecond.split(",")
            second_points["x1"], second_points["y1"] = bFirst.split(",")
            second_points["x2"], second_points["y2"] = bSecond.split(",")


            slopeA = findSlope(first_points)
            slopeB = findSlope(second_points)
            y_interceptA = findB(first_points,slopeA)
            y_interceptB = findB(second_points,slopeB)
            poi = findY(slopeA,slopeB,y_interceptA,y_interceptB)
            print("\nPoint of Intercet is at x{}, y{}".format(poi,poi))
            pygame.draw.line(screen,(191,255,0), newCords(int(first_points["x1"]),int(first_points["y1"])), newCords(int(first_points["x2"]),int(first_points["y2"])), 2)
            pygame.draw.line(screen,(0,191,255), newCords(int(second_points["x1"]),int(second_points["y1"])), newCords(int(second_points["x2"]),int(second_points["y2"])), 2)
            pygame.draw.circle(screen,(255,0,0), (newCords(poi,poi)),5, 1)
            # pygame.draw.line(screen,(191,255,0), (192,-112), (343,7), 2)
            # pygame.draw.line(screen,(0,191,255), (654,-58), (787,93), 2)


            # print("Line 1 y =" , slopeA, "x +" , y_interceptA)
            # print("Line 2 y =" , slopeB, "x +" , y_interceptB)

            print("\nPoint of Intercet is at x{}, y{}".format(poi,poi))
    for line in x_gridLines:
        line.display()
    
    for line in y_gridLines:
        line.display()
    xBaseLine.display()
    yBaseLine.display()
    pygame.display.flip()