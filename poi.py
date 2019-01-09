#Y = 2.0x - 3.0
#Y = -0.5x - 7.0

lineAxOne = 192
lineAyOne = -112
lineAxTwo = 343
lineAyTwo = 7

lineBxOne = 654
lineByOne = -58
lineBxTwo = 787
lineByTwo = 93

def Slope(x1,y1,x2,y2):
	return (y2 - y1) / (x2 - x1)
	
	
def Yintercept(x, y ,m):
	return (y - m * x)
	
def findX(m1,m2,b1,b2):
	xA = m2 - m1
	xB = b1 - b2
	return xB / xA
	
def findY(m1,m2,b1,b2):
	x = findX(m1,m2,b1,b2)
	y1 = m1 * x + b1
	y2 = m2 * x + b2
	if y1 == y2:
		return "POI ! " , x,y1
	else:
		return "fail" , x,y1


	
slpLineA = Slope(lineAxOne, lineAyOne, lineAxTwo, lineAyTwo)
slpLineB = Slope(lineBxOne, lineByOne, lineBxTwo, lineByTwo)

yIntLineA = Yintercept(lineAxOne, lineAyOne, slpLineA)
yIntLineB = Yintercept(lineBxOne, lineByOne, slpLineB)	
	
print("y = " ,slpLineA , "x + " ,yIntLineA)
print("y = " ,slpLineB , "x + " ,yIntLineB)

print(findY(slpLineA,slpLineB,yIntLineA,yIntLineB))