import math

def measurements():

    programOn = True
    subTotal = 0

    program_continue = input("Do you want to keep a running total of your measurements? 1 for yes, 2 for no: ");

    feet = input("Enter feet portion of distance: ");
    inch = input("Enter inches portion of distance: ");
    subTotal += (feet + (inch/12))
    
    while(programOn):

        program_continue = input("Do you want to keep adding to your running total? 1 for yes, 2 for no: ");
        
        if (program_continue == 1):
            feet = input("Enter feet portion of distance: ");
            inch = input("Enter inches portion of distance: ");
            subTotal += (feet + (inch/12))
        elif (program_continue == 2):
            print subTotal
            total = subTotal
            programOn = False
            return total
        else:
            program_continue = input("ERROR!!! Do you want to keep adding to your running total? 1 for yes, 2 for no: ");

measurements()
