
from package import dt_operation, random_operation
from package import mathematical_op
from package import random_operation
from package import file_operation
from package import uuid_generation
from package import dir_operation



def main():
    while True:
        print("=====================================")
        print("Welcome To Modules And Package ")
        print("=====================================")
        
        print("-- Select An Option --")
        print("1. Datetime And Time Operations")
        print("2. Mathemathical Operation ")
        print("3. Random Data Generation ")
        print("4. Generate Unique Identifiers (UUID) ")
        print("5. File Operation ")
        print("6. Explore Modules Attributes  ")
        print("7. Exit")
        print("=====================================")
        
        
        choice = int(input("Enter Your Choice Between (1-7): "))
        print()
        
        if choice == 1:
            dt_operation()
        elif choice == 2:
            mathematical_op()
        elif choice == 3:
            random_operation()
        elif choice == 4:
            uuid_generation()
        elif choice == 5 :
            file_operation()
        elif choice == 6 :
            dir_operation()
        elif choice == 7:
            print("Thank You")
            break
        else :
            print("Invalid choice")
            
            
if __name__ == "__main__" :
    main()