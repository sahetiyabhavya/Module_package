

def file_operation():
    
    while True:

        print("")
        print("---------------------")
        print("File Operation")
        print("1. Create a New File")
        print("2. Read a File")
        print("3. Write in File")
        print("4. Append to File")
        print("5. Exit")
        print("---------------------")
        
        choice = int(input("Enter Your Choice Between (1-6): "))
        
        if choice == 1:
            try:
                with open("work.txt", "x") as file:
                    print("File Created Successfully")  
            except :
                print("File Already Exists") 
        elif choice == 2:
            with open("work.txt", "r") as file:
                
                content = file.read()
                print(f"File Content : {content}")
        elif choice == 3:
            with open("work.txt", "w") as file:
                content = input("Enter Content To Write: ")
                file.write(content)
                print("Content Written Successfully")
        
        elif choice == 4:
            with open("work.txt", "a") as file:
                content = input("Enter Content To Append: ")
                for i in content:
                    file.write(i)
                file.write("\n")
                print("Content Appended Successfully")

        elif choice == 5:
            break
        
        else:
            print("Invalid Choice")
            

            