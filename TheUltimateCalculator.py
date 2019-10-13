# The Ultimate Calculator by Rainverm38
# You can find more info at: https://github.com/Rainverm38/TheUltimateCalculator

import math

menu = 1
while menu == 1:
    print('Welcome to the ultimate calculator! To get started, please select an option from the following list:')
    print('0) Exit')
    print('1) Simplifing the discriminant of a quadratic')
    print('2) Solve for the \'x\' value of a quadratic')
    print()
    operation = float(input('Please insert an operation from the list: '))
    
    if operation == 1:
        a = 1
        print('Selected: 1) simplifing the discriminant of a quadratic')
        while a == 1:
            a = int(input('Insert \'a\' value: '))
            b = int(input('Insert \'b\' value: '))
            c = int(input('Insert \'c\' value: '))
            print()
            ans = (b**2) - (4*a*c)

            if ans > 0:
                print('There Are 2 Real Solutions, The Answer is: ', ans)
            elif ans == 0:
               print('There Is 1 Real Solution, The Answer is: ', ans)
            elif ans < 0:
                print('There Are 2 Imaginary Solutions, The Answer is: ', ans)
    
            print('The equation is: ', b, '^2 - 4(', a, ')', '(', c, ') = ', ans)
            print()
            exit = input('Press enter to continue calculating discriminants or type \'x\' to return to the menu: ')
            if exit == 'x':
                a = 0
                print()
            else:
                a = 1
    elif operation == 2:
        b = 1
        print('Selected: 2) Solve for the \'x\' value of a quadratic')
        while b == 1:
            a = int(input('Insert \'a\' value: '))
            b = int(input('Insert \'b\' value: '))
            c = int(input('Insert \'c\' value: '))
            print()

            d = (b**2) - (4*a*c)
            
            if d > 0:
                bPlus = (-b + math.sqrt(d)) / (2 * a)
                bMinus = (-b - math.sqrt(d)) / (2 * a)
                print('There Are 2 Real Solutions, The X Values Are: ', bPlus, bMinus)
            elif d == 0:
               bPlus = (-b + math.sqrt(d)) / (2 * a)
               print('There Is 1 Real Solution, The Answer is: ', bPlus)
            elif d < 0:
                print('There Are 2 Imaginary Solutions, I Can\'t Calculate Those Yet.')
                print('The value of the discriminant is: ', d)
            else:
                print('If you are somehow seeing this, I am very, very broken.')
            
            print()
            exit = input('Press enter to continue calculating discriminants or type \'x\' to return to the menu: ')
            if exit == 'x':
                b = 0
                print()
            else:
                b = 1
            
    elif operation == 0:
        exit()