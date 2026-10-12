import datetime
import time
import random
import string
import math

def dir_operation():
    while True:
        

        print("Exploring Modules Attributes:")
        print("-------------------------------")
        print("1. Dir For Datetime Module")
        print("2. Dir For Time Module")
        print("3. Dir For Random Module")   
        print("4. Dir For String Module")
        print("5. Dir For Math Module")
        print("6. Back To Main Menu")
        print("-------------------------------")
        
        choice = int(input("Enter Your choice Between (1-6): "))
        
        if choice == 1:
            dt = dir(datetime)
            print(f"Dir For Datetime Module : {dt}")
            
        elif choice == 2:
            tm = dir(time)
            print(f"Dir For Time Module : {tm}")
            
        elif choice == 3:
            rm = dir(random)
            print(f"Dir For Random Module :- {rm}")
            
        elif choice == 4:
            sm = dir(string)
            print(f"Dir For String Module : {sm}")
            
        elif choice == 5:
            mm = dir(math)
            print(f"Dir For Math Module : {mm}")
            
        elif choice == 6:
         break
        
        else:
            print("Invalid Choice ")
            
    