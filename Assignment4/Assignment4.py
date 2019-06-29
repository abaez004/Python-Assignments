#Angel Baez 9:30 AM Lab Assignment #4
import math

#prints whether or not the user entered number is a perfect number
def perfect_number():
    try:
        n = int(input("Enter a positive integer for n: "))
        if n < 0:
            print("Your value must be a positive integer")
            return
        divisors = n - 1
        sum = 0
        while(divisors > 0):
            if(n % divisors) == 0:
                sum += divisors
            divisors = divisors - 1    
        if(sum == n):
            print(n, "is a perfect number")
        else:
            print(n, "is not a perfect number")
    except ValueError:
        print("You must enter a valid positive integer")
    except:
        print("Please enter a valid input")
    

#prints all positive divisors for a number entered by the user
def positive_divisors():
    x = "c"
    while x != "" :
        try:
            n = int(input("Enter a positive integer for n: "))
            divisors = n
            while(divisors > 0):
                if(n % divisors) == 0:
                    print(divisors)
                divisors = divisors - 1
        except ValueError:
            print("You must enter a valid positive integer")
        except:
            print("Please enter a valid input")
        finally:
            x = input("Would you like to continue? (Press Enter to exit) ")

#verifies whether three coordinates entered by user create a triangle
def is_triangle(): 
    x = "n"
    while x != "":
        try:
            x1 = float(input("Enter coordinates for the first point x value: "))
            y1 = float(input("Enter coordinates for the first point y value: "))
            x2 = float(input("Enter coordinates for the second point x value: "))
            y2 = float(input("Enter coordinates for the second point y value: "))
            x3 = float(input("Enter coordinates for the third point x value: "))
            y3 = float(input("Enter coordinates for the third point y value: "))
            s1 = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
            s2 = math.sqrt((x1 - x3)**2 + (y1 - y3)**2)
            s3 = math.sqrt((x2 - x3)**2 + (y2 - y3)**2)
            if (s1 < s2 + s3) and (s2 < s1 + s3) and (s3 < s1 + s2):
                print("You have entered a triangle!")
            else:
                print("This is not a triangle")
        except ValueError:
            print("Please enter valid coordinates")
        except:
            print("Please enter valid coordinates")
        finally:
            x = input("Would you like to continue? (Press Enter to exit) ")

#returns true if the n1 is prime, false otherwise
def is_prime(n1,n2):
    if n1 == 1:
        return False
    elif n2 == 1:
        return True
    elif n1 % n2 == 0:
        return False
    else :
        return is_prime(n1, n2 - 1)

#prints all prime numbers between n1 and n2
def prime_numbers():
    x = "n"
    while x != "":
        n1 = int(input("Enter a number for the lower bound: "))
        n2 = int(input("Enter a number for the upper bound: "))
        n3 = n2
        while n3 >= n1:
            if is_prime(n3, n3 - 1):
                print(n3)
            n3 = n3 - 1
        x = input("Would you like to continue? (Press Enter to exit) ")

#computes how many ways to seat n2 people out of n1
def people_table():
    x = "n"
    while x != "":
        n1 = int(input("How many people are there?: "))
        n2 = int(input("How many of them would you like to seat?: "))
        try:
            combination = (math.factorial(n1))/(math.factorial(n2)* math.factorial(n1-n2))
            print("There are", int(combination), "ways to seat", n2, "out of", n1, "people")
        except ValueError:
            print("There must be more people than you want to seat, make sure your inputs are valid!")
        x = input("Would you like to continue? (Press Enter to exit) ")
        
print("\nPERFECT NUMBER FUNCTION")
perfect_number()
print("\nPOSITIVE DIVISORS FUNCTION")
positive_divisors()
print("\nIS TRIANGLE FUNCTION")
is_triangle()
print("\nPRIME NUMBERS FUNCTION")
prime_numbers()
print("\nPEOPLE SEATED AT A TABLE FUNCTION")
people_table()

