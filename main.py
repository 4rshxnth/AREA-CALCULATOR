def area_calculator():
    # Display a welcome message
    print("-----Welcome to Area Calculator-----")
    
    while True:
        # Display menu options
        print("Choose which Area you need to Calculate")
        print("\n1.Square")
        print("2.Rectangle")
        print("3.Circle")
        print("4.Exit")

        # Get user choice
        select = int(input("\nWhat Shape Do You Want to Check the Area For : "))

        if select == 1:
            # Calculate the area of a square
            side = float(input("Enter the Side : "))
            area = side ** 2
            print("The Area of the Square is", area)  
            
        elif select == 2:
            # Calculate the area of a rectangle (CORRECTION NEEDED: was using addition instead of multiplication)
            length = float(input("Enter the Length : "))
            breadth = float(input("Enter the Breadth : "))
            area = length * breadth  # Fixed incorrect calculation
            print("The Area of the Rectangle is", area)

        elif select == 3:
            # Calculate the area of a circle
            radius = float(input("Enter the Radius : "))
            area = 3.14 * radius ** 2
            print("The Area of the Circle is", area)
            
        elif select == 4:
            # Exit the program
            print("Exit Successfully")
            break  # Ensure the loop stops when the user chooses to exit
        else:
            # Handle invalid input
            print("Error Occurred: Invalid Selection")

# Run the area calculator function
area_calculator()
