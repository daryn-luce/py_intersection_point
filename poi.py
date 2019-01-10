import math

def findSlope(line):
	return (line["y2"] - line["y1"]) / (line["x2"] - line["x1"])
	
def findB(line, m):
	return (line["y1"] - (m * line["x1"]))
	

def findY(m1, m2, b1, b2):
	xA = m2 - m1
	xB = b1 - b2
	x = xB / xA
	y1 = m1 * x + b1
	y2 = m2 * x + b2
	if y1 == y2:
		return "POI ! " , x,y1
	else:
		return "fail" , x,y1


first_points = {
	"x1": 192,
	"y1": -112,
	"x2": 343,
	"y2": 7
	}
second_points = {
	"x1": 654,
	"y1": -58,
	"x2": 787,
	"y2": 93
	}
slopeA = findSlope(first_points)
slopeB = findSlope(second_points)
y_interceptA = findB(first_points,slopeA)
y_interceptB = findB(second_points,slopeB)


# first_points["x1"] = input("First point, first line 'x,y'")
# print(first_points["x1"])
# print(first_points["y1"])
# aSecond = input("Second point, first line 'x,y'") 
# bFirst = input("First point, second line 'x,y'") 
# bSecond = input("Second point, second line 'x,y'") 
# aFirstx, aFirsty = aFirst.split(",")
# aSecondx, aSecondy = aSecond.split(",")
# bFirstx, bFirsty = bFirst.split(",")
# bSecondx, bSecondy = bSecond.split(",")


print("Line 1 y =" , slopeA, "x +" , y_interceptA)
print("Line 2 y =" , slopeB, "x +" , y_interceptB)

print(findY(slopeA,slopeB,y_interceptA,y_interceptB))
