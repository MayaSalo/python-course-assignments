import math
import sys

radius = float(sys.argv[1])

area = math.pi*radius**2
circumference = 2*math.pi*radius

print("The area of the circle is: ", area)
print("The circumference of the circle is: ",circumference)
