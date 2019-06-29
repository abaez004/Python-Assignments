#Angel Baez 9:30 AM Lab Assignment #2
import math

#converts minutes to milliseconds
def minutes_to_milliseconds(minutes):
    return minutes * 60000

#returns the average of 2 exams
def average_exam_scores(exam1, exam2):
    return (exam1 + exam2) / 2

#calculates the roots of an equation if they exist
def quadratic_equation(a, b, c):
    delta = b ** 2 - 4 * a * c
    x1 = (-1 * b + math.sqrt(delta)) / (2 * a)
    x2 = (-1 * b - math.sqrt(delta)) / (2 * a)
    return x1, x2

#converts kelvin to reaumur
def kelvin_to_reaumur(kelvin):
    return (kelvin - 273.15) * .8

#converts reaumur to celsius
def reaumur_to_celsius(reaumur):
    return reaumur * 1.25

#calculates how many marbles of radius n/4 fit inside a cube with side n
def calculate_marbles_cubes(n):
    sphere = 4 / 3 * math.pi * ((n/4) ** 3)
    cube = n ** 3
    return cube // sphere

#prints the first pattern of the art
def print_first_ascii():
    print("^ - ^ - ^^ - ^ - ^^ - ^ - ^^ - ^ - ^^")
    
#prints the second pattern of the art
def print_second_ascii():
    print("i        i        i        i        i")
    
#prints both patterns combined
def print_third_ascii():
    print_first_ascii()
    print_second_ascii()
    print_second_ascii()
    print_second_ascii()
    
#prints the entire art
def print_ascii_art():
    print_third_ascii()
    print_third_ascii()
    print_third_ascii()
    print_first_ascii()
    

minutes = int(input("Enter the number of minutes to be converted to milliseconds "))
print(minutes, " minute(s) in milliseconds is", minutes_to_milliseconds(minutes));

exam1 = float(input("Enter the grade for exam 1 "))
exam2 = float(input("Enter the grade for exam 2 "))
print("The average of ", exam1, " and ", exam2, " is: ", average_exam_scores(exam1, exam2))

a = int(input("Enter a value for a "))
b = int(input("Enter a value for b "))
c = int(input("Enter a value for c "))
root1, root2 = quadratic_equation(a, b, c)
print("The roots are ", root1, " and ", root2)

kelvin = int(input("Enter kelvin to be converted to reaumur "))
print(kelvin, "K = ", kelvin_to_reaumur(kelvin), "Re")
reaumur = int(input("Enter reaumur to be converted to reaumur "))
print(reaumur, "Re = ", reaumur_to_celsius(reaumur), "C")
        
n = int(input("Enter a size for n " ))
print(calculate_marbles_cubes(n), " marbles with radius ", n/4, " can fit inside a cube with side ", n)

print_ascii_art()


