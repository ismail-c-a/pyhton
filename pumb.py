
print("ENTER THE BELOW DETAILS")
print("-----------------------\n")
name=input("SALES MAN NAME:")
po = float(input("ENTER THE OPENING READ: "))
pc = float(input("ENTER THE CLOSING READ: "))

ps = pc - po

print("\n")
print("TOTAL SALES IN LTR: ", ps)
print("\n")
choice=input("PETROL or DIESEL(P/D):")
print("\n")
if choice=="P" or choice=="p":
                             option="ENTER TODAY'S PETROL RATE:"
                             feild="PETROL"
else:
                                   option="ENTER TODAY'S DIESEL RATE:"
                                   feild="DEISEL"

pr = float(input(option))

pt = ps * pr
print("\n")
print("*****************************************")
print("TOTAL SALES IN RS: ", pt)
print("*****************************************\n")

tp = input("DO YOU WISH TO TALLY HERE (y/n): ")

if tp == "y" or tp == "Y":
    print("\n\n")
    print("***ENTER DETAILS***")
    cash = float(input("CASH IN OFFICE: "))
    totalcash = float(input("CASH IN YOU'R HAND: "))
    cr = float(input("CREDIT: "))
    ph = float(input("UPI: "))
    sw = float(input("SWIPING CARD: "))
    test = float(input("TEST: "))
    other = float(input("OTHER: "))
    total = ph + sw + cash + cr+test+totalcash

    my_money= cash+totalcash 

    grand = total - pt

    print("TOTAL =", total)
    print("-----------------------")
    print("\n\n\n")
    print("***TODAY'S DETAILS***")
    print("\n")
    print("SALES MAN:",name)
    print("FEILD:",feild)
    print("OPENING =", po)
    print("CLOSING =", pc)
    print("SALES LTR =", ps)
    print("SALES CASH =", pt)
    print("UPI =", ph)
    print("SWIPING =", sw)
    print("CREDIT =", cr)
    print("OTHER =", other)
    print("OFFICE CASH+YOUR HAND CASH=",my_money)
    print("TOTAL YOU HAVE =", total)
    print("\n")
    
    if grand > 0:
        print("SHORT = +", grand)
    elif grand < 0:
        print("SHORT = ", grand)
    else:
        print("SHORT = ", grand)
    print("\n\n")
    print("Thank you!")

else:
    print("\n\n")
    print("SALES MAN:",name)
    print("OPENING =", po)
    print("CLOSING =", pc)
    print("SALES LTR =", ps)
    print("SALES CASH =", pt)
    print("\n\n")
    print("Thank you!")
