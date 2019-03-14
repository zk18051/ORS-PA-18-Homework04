"""
===================   TASK 2   ====================
* Name: Even and Odd Numbers
*
* Write a script that will populate list with as
* many elemens user defines. For taken number
* of elements the script should take the input from
* user for each element. You should expect that user
* will always provide integer numbers. At the end,
* script should print how many even and odd numbers
* were present in list.
*
*
* Note: Please describe in details possible cases
* in which your solution might not work.
===================================================
"""

def main():
    number = input('Enter a number:')
    number_of_odd= 0
    number_of_even=0
    for i in number:
        if i%2==0:
            i=i+1
            number_of_even=i
        if int(number[i])%2!=0:
            i=i+1
            number_of_odd=i

    print('Number of odd is '+number_of_odd)

main()


#Ne znam, nesto ne kontam.