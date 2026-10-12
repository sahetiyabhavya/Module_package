from datetime import datetime
import random
import string
import time
import math
from uuid import uuid4



def dt_operation():
    while True :
        
        print("----------------------------------")
        print("Datetime And Time Operations:")
        print("----------------------------------")
        print("1. Display Current Date And Time ")
        print("2. Calculate Difference Between Two Date/time ")
        print("3. Format Date Into Custom Format ")
        print("4. Stopwatch ")
        print("5. Countdown Timer")
        print("6. Back To Main Menu")
        print("----------------------------------")
        
        choice = int(input("Enter Your Choice Between (1-6): "))
        
        if choice == 1:
            now = datetime.now()
            print(f"Current Date And Time :- {now}")
            print()
            
        elif choice == 2:
            u1 = input("Enter The First Date (YYYY-MM-DD):- ")
            u2 = input("Enter The Second Date (YYYY-MM-DD):- ")
            
            u1 = datetime.strptime(u1, "%Y-%m-%d")
            u2 = datetime.strptime(u2, "%Y-%m-%d")
            
            print(f"Difference :- {abs(u2-u1)}")
            print()

            
        elif choice == 3:
            
            while True:    
                current = datetime.now()
                print("1. For Date")
                print("2. For Time ")
                print("3. Exit")
                print("--------------------------------")
                choice = int(input("Enter Your Choice (1-3) : "))
                
                if choice == 1:
                    print(current.strftime("%Y-%m-%d"))
                elif choice == 2:
                    print(current.strftime("%H-%M-%S"))
                elif choice == 3:
                    break
                else:
                    print("Invalid choice (1-3)")
                
        elif choice == 4:
            start = time.time()
            input("press Enter To Stop !")
            end = time.time()
            
            print(f"Time Stopped :- {end-start}")
            
        elif choice == 5 :
            count = int(input("Enter Number To Count "))
            
            while count>0:
                print(count)
                time.sleep(1)
                count-=1
                
            print("Time Up !")

        elif  choice == 6:
            break
        
        else:
            print("Invalid Choice (1-6)")
            
def mathematical_op():
    while True:
        print()      
        print("Mathematical Operation :")
        print("------------------------------")
        print("1. Calculate Factorial")
        print("2. Solve Compound Interest ")
        print("3. Trigonometric Calculation ")
        print("4. Area Of Geometric Shapes ")
        print("5. Back TO Main Menu")
        print("--------------------------------")
        
        choice = int(input("Enter An Choice Between (1-5): "))
        
        if choice == 1:
            num  = int(input("Enter The Number For Factoiral : ")) 
            print(math.factorial(num))

        elif choice == 2:
            amount = float(input("Enter A Amount : "))
            year  = int(input("Enter Year : "))
            rate = float(input("enter Interest rate : "))
            interest = amount *(1+rate/100)**year
            print(f"Compound Interest : {interest}")
            
        elif choice == 3:
             num = float(input("Enter The Number "))
             num = math.radians(num)
             
             print(f"This Value Is Sin :- {math.sin(num)}")
             print(f"This Value Is Cos :- {math.cos(num)}")
             
             
        elif choice == 4:
            
            while True:
                print("1. Area Of Circle ") 
                print("2. Area Of Triangle ") 
                print("3. Back To Main Menu ")
                print("===============================")
                c = int(input("Enter The Number Between (1-3):- "))
                
                if c == 1:
                    area = float(input("Enter A Number :- "))
                    area = math.radians(area)
                    
                    a = math.pi*area*area
                    print(f"Area Of Circle :- {a}")
                elif c == 2:
                    base = float(input("Enter Base Of Triangle :- "))
                    height = float(input("Enter Height Of Triangle :- "))
                    
                    a = 0.5*base*height
                    print(f"Area Of Triangle :- {a}")
                elif c == 3:
                    break
                else:
                    print("Invalid Choice (1-3)")


        elif choice == 5:
            break
        else:
            print("Invalid Choice (1-5)")
            
def random_operation():
    while True:
        print("Random Generating: ")
        print("----------------------------------")
        print("1. Generate Random Number")
        print("2. Generate Random List")
        print("3. Create Random Password")
        print("4. Generate Random OTP")
        print("5. Back To Main Menu")
        print("--------------------------------")
        
        choice = int(input("Enter Your Choice Between (1-5): "))
        
        if choice == 1:
            num = random.randint(1,100)
            print(f"Random Number : {num}")
            
        elif choice == 2:
            list1 = [10,20,30,85,74,96,41,52,63]
            random.shuffle(list1)
            print(f"Random List : {list1}")
        
        elif choice == 3:
            l = int(input("Enter Password lenth :"))
            value = string.ascii_letters + string.punctuation + string.digits
            password = "".join(random.choices(value,k=l))
            print(f"Generated Password : {password}")
            print()
            
        elif choice == 4:
            random_otp = random.randint(1000,9999)
            print(f"Random OTP : {random_otp}")
            
        elif choice == 5:
            break
        
        else:
            print("Invalid Choice!")
            
def uuid_generation():
    uu = uuid4()
    print(f"Generate UUID : {uu} ")
    
           
            