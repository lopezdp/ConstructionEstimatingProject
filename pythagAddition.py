import math

def pythagAddition():

    programOn = True
    aSide = 0
    bSide = 0
    cSide = 0

    subTotal = 0

    program_continue = input("Do you want to keep a running total of measurements that calculate "
                             "the C side of a Triangle? 1 for yes, 2 for no: ");

    if (program_continue == 1):
        print " "
        feet = input("Enter feet portion of distance A: ");
        inch = input("Enter inches portion of distance A: ");
        aSide = (float(feet) + (float(inch)/12))

        print " "
        feet = input("Enter feet portion of distance B: ");
        inch = input("Enter inches portion of distance B: ");
        bSide = (float(feet) + (float(inch)/12))

        cSide = math.sqrt(aSide **2 + bSide **2)

        subTotal += cSide        

        print " "
        print "The Length of you C side using Pythagorean Theorem is: ", cSide
        print "Your current subTotal is: ", subTotal

    elif (program_continue == 2):
        print " "
        total = subTotal
        print "Your measurement in FEET is: ", total
        meters = total * 0.3048
        print "Your measurement in METERS is: ", meters
        programOn = False
        return total

    else:
        print " "
        program_continue = input("ERROR!!! Do you want to keep adding to your running total? 1 for yes, 2 for no: ");

    while(programOn):
        print " "
        program_continue = input("Do you want to keep adding to your running total? 1 for yes, 2 for no: ");

        if (program_continue == 1):
            print " "
            feet = input("Enter feet portion of distance A: ");
            inch = input("Enter inches portion of distance A: ");
            aSide = (float(feet) + (float(inch)/12))

            print " "
            feet = input("Enter feet portion of distance B: ");
            inch = input("Enter inches portion of distance B: ");
            bSide = (float(feet) + (float(inch)/12))

            cSide = math.sqrt(aSide **2 + bSide **2)

            subTotal += cSide        

            print " "
            print "The Length of you C side using Pythagorean Theorem is: ", cSide
            print "Your current subTotal is: ", subTotal

        elif (program_continue == 2):
            print " "
            total = subTotal
            print "Your measurement in FEET is: ", total
            meters = total * 0.3048
            print "Your measurement in METERS is: ", meters
            programOn = False
            return total

        else:
            print " "
            program_continue = input("ERROR!!! Do you want to keep adding to your running total? 1 for yes, 2 for no: ");

pythagAddition()
