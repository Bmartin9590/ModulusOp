## Write a program to print 1 to 30 but skip all the numbers that are divisible by 5
## For Loop
''' 1. Figure out how we can skip the numbers divisible by 5, which would be by the "remainder" or modulus opertation. Anything divisible by 5 would have no remainder (0).
2. We will use a "for loop" so we won't have to incement the equation
3. The "for loop" will need a range because 30 is the number we are counting to (have to use 31 so 30 runs thru the loop)
4. We then create an if statement where the modulus equation takes place
5. The equation has to include "not equal to" so that the numbers with a "0" remainder (divisible by 5) aren't printed
6. Create a print statement so the solution with show in the console '''

for i in range(31):
    if i % 5 != 0:
        print(i)