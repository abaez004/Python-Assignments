#Angel Baez 9:30 AM This is the updated version
import math

minutes = 42;
seconds = 42;
totalTime = minutes * 60 + seconds;
print("The total time is:", totalTime);

radius = 6;
radius2 = 4;
volume = 4 / 3 * math.pi * (math.pow(radius,3));
volume2 = 4 / 3 * math.pi * (math.pow(radius2,3));
print("The volume of the sphere with radius 6 is:", volume);
print("The volume of the sphere with radius 4 is:", volume2);

farenheit = -40;
fToC = (farenheit - 32) * 5/9;
print("-40 degrees farenheit to celsius is:", fToC);
celsius = -40;
cToF = (celsius * 9/5) + 32;
print("-40 degrees celsius to farenheit is:", cToF);

a_str = input("Enter the value for a:");
a_int = int(a_str);
rPrism = a_int * 2 * a_int * 3 * a_int;
cube = math.pow(a_int, 3);
print("The prism can fit: ", rPrism//cube, "cubes");
