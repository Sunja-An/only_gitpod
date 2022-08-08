import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from CSV_manager import Sample

while True:
# Case 1 : 부조리인 경우, Case 2: 부조리가 아닌 경우
    try:
        case = int(input("What is the Case ?(1 or 2) :"))

    except:
        print("Wrong Data. Try again.\n")
        continue

    if case == 1:
        True_Data = input("Write the positive comment : ")
        True_Data.replace(",", "")
        sp = Sample('admin',True_Data,'True','00:00:00') # object
        sp.insert()
        print(sp.show_data())
    
    elif case == 2:
        False_Data = input("Write the negative comment: ")
        False_Data.replace(",", " ")
        sp = Sample('admin',False_Data,'False','00:00:00') # object
        sp.insert()
        print(sp.show_data())
    
    elif case == 0:
        sp.close()
        break

    else:
        print("Wrong value. Try Again.\n")