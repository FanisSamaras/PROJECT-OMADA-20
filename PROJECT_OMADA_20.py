import joblib as jb
import tkinter as tk
import numpy as np
np.set_printoptions(threshold=np.inf)
def main():
    while True:
        print(" 1.ΠΡΟΣΘΕΣΗ ΠΙΝΑΚΩΝ \n 2.ΠΟΛΛΑΣΙΑΣΜΟΣ ΠΙΝΑΚΩΝ \n 3.ΕΞΟΔΟΣ")
        epilog = int(input(">>>"))
        if epilog == 3:break
        elif epilog == 2:mult()
        elif epilog == 1:add()
        else:
            print("ΔΙΑΛΕΞΕ ΜΕΤΑΞΥ 1 2 3")
            continue
def mult():
    while True:
        dia1 = input("ΔΩΣΕ ΤΙΣ ΔΙΑΣΤΑΣΕΙΣ ΤΟΥ ΠΡΩΤΟΥ ΠΙΝΚΑ(π.χ. m*n-> m,n):")
        dia2 = input("ΔΩΣΕ ΤΙΣ ΔΙΑΣΤΑΣΕΙΣ ΤΟΥ ΔΕΥΤΕΡΟΥ ΠΙΝΚΑ(π.χ. j*k-> j,k):")
        if "," in dia1:
            diam,dian = dia1.split(",")
        elif "." in dia1:
            diam,dian = dia1.split(".")
        if "," in dia2:
            diaj,diak = dia2.split(",")
        elif "." in dia2:
            diaj,diak = dia2.split(".")
        if dian != diaj:
            print("ΑΥΤΟΣ Ο ΠΟΛΛΑΠΛΑΣΙΑΣΜΟΣ ΔΕΝ ΜΠΟΡΕΙ ΝΑ ΓΙΝΕΙ")
            continue
        else:
            break
    diam = int(diam)
    dian = int(dian)
    diaj = int(diaj)
    diak = int(diak)

    p1 = np.random.randint(0,9,size=(diam,dian))
    p2 = np.random.randint(0,9,size=(diaj,diak))

    mul = np.matmul(p1,p2)
    print(mul)
def add():
    while True:
        dia1 = input("ΔΩΣΕ ΤΙΣ ΔΙΑΣΤΑΣΕΙΣ ΤΟΥ ΠΡΩΤΟΥ ΠΙΝΚΑ(π.χ. m*n-> m,n):")
        dia2 = input("ΔΩΣΕ ΤΙΣ ΔΙΑΣΤΑΣΕΙΣ ΤΟΥ ΔΕΥΤΕΡΟΥ ΠΙΝΚΑ(π.χ. j*k-> j,k):")
        if "," in dia1:
            diam,dian = dia1.split(",")
        elif "." in dia1:
            diam,dian = dia1.split(".")
        if "," in dia2:
            diaj,diak = dia2.split(",")
        elif "." in dia2:
            diaj,diak = dia2.split(".")
        if (dian == diak) and (diam == diaj):
            break
        else:
            print("ΑΥΤΗ Η ΠΡΟΣΘΕΣΗ ΔΕΝ ΓΙΝΕΤΑΙ")
            continue
    diam = int(diam)
    dian = int(dian)
    diaj = int(diaj)
    diak = int(diak)
    
    p3 = np.random.randint(0,9,size=(diam,dian))
    p4 = np.random.randint(0,9,size=(diaj,diak))

    pros = np.add(p3,p4)
    print(pros)

main()