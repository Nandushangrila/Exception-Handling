def check_age_parity():
    """
    Prompts the user for their age, validates the input, 
    and checks if the age is even or odd.
    """
    while True:
        age_input = input("Please enter your age: ")
        try:
            age = int(age_input)
           
            if age <= 0:
                print("Error: Age must be a positive integer. Please try again.")
                continue 
            
            break
        except ValueError:
            print("Error: Invalid input. Please enter a numerical age.")
           

    if age % 2 == 0:
        parity_status = "even"
    else:
        parity_status = "odd"

   
    print(f"You entered the age: {age}")
    print(f"The age {age} is an {parity_status} number.")

if __name__ == "__main__":
    check_age_parity()
