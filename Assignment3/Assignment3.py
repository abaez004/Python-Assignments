#Angel Baez 9:30 AM Lab Assignment #3

#gets input from the user and validates using exception handling
def collatz_input():
    try:
        n = int(input("Enter a positive integer for n: "))
        if n > 0:
            return n
        else:
            print("Your value must be a positive integer")
    except ValueError:
        print("You must enter a valid positive integer")
    
#prints collatz conjecture of n
def collatz_conjecture(n):
    if n == 1:
        print(n)
        return
    elif n % 2 == 0:
        print(n)
        collatz_conjecture(n//2)
    else:
        print(n)
        collatz_conjecture(3*n+1)

#used to get and verify input for prime_factor and prime_less_than
def prime_factor_input():
    try:
        n = int(input("Enter an integer: "))
        if n > 1:
            return n
        else:
            print("You must enter an integer greater than 0")
    except ValueError:
        print("You must enter a valid positive integer")
        
#returns true if the n1 is prime, false otherwise
def is_prime(n1,n2):
    if n2 == 1:
        return True
    elif n1 % n2 == 0:
        return False
    else :
        return is_prime(n1, n2 - 1)

def prime_factor(n1, n2):
    if n2 == 1:
        return
    elif n1 % n2 == 0 and is_prime(n2, n2//2):
        print(n2, " ")
        prime_factor(n1, n2-1)
    else:
        prime_factor(n1, n2-1)

#prints all prime numbers less than or equal to n1
def prime_less_than(n1):
    if n1 < 2:
        return
    elif is_prime(n1,n1//2):
        print(n1)
        prime_less_than(n1 - 1)
    else:
        prime_less_than(n1 - 1)

        
n = collatz_input()
collatz_conjecture(n)

try:
    a = int(input("Enter a number:"))
    b = int(input("Enter a number:"))
    print(a/b)
except ValueError:
    print("Please enter a valid value for a and b")
except ZeroDivisionError:
    print("Error, divide by zero")
except:
    print("Something unexpected happened")

n1 = prime_factor_input()
print("The prime factors of", "n1", "are: ")
prime_factor(n1, n1)

n2 = prime_factor_input()
print("The prime numbers less than or equal to", "n2", "are: ")
prime_less_than(n2)

