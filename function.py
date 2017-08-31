# Function for checking the divisibility
# Notice the indentation after function declaration
# and if and else statements
def checkDivisibility(a, b):
    if a % b == 0 :
        print "a is divisible by b"
    else:
        print "a is not divisible by b"
#Driver program to test the above function
a = raw_input("Enter a: ")
b = raw_input("Enter b: ")
checkDivisibility(int(a), int(b))