# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion. 
# Any code taken from other sources is referenced within my code solution. 
# Student ID: w1987543 
 
# Date: 4/21/2023 

# Defining functions   
def checkInput(msg):
    """
        The `checkInput` function is used to validate user input.
        It checks if the user input is an integer and within the range of 0 to 120.
    """
    while True:
        try:
            get_credits = int(input(msg)) # get the input as integer
        except ValueError:
            print ("Integer REQUIRED") # if input is not integer, print error message
            continue
        if get_credits not in [0,20,40,60,80,100,120]: # if input is not within valid range, print error message
            print("Out of range")
            continue
        break  # if input is valid, break the loop and return the input value
    return get_credits



# Function to check whether staff wants to continue or quit
def checkPreference():
    """
        The `checkPreference` function prompts the user to enter whether they want to enter another set of data or quit and view the results.
        It checks if the user input is valid.
    """
    while True:
        print('\n')# print a newline
        staff_preference = input('''Would you like to enter another set of data?
Enter 'Y' to continue and 'Q' to quit and view results: ''')
        print('\n')
        
        if staff_preference.lower() in ["q", "y"]:# if input is valid (either q or y), return the lowercase input value 
            return staff_preference.lower()
        else:
            print("Enter a valid response!") # if input is not valid, print error message
            


# Initializing variables        
progress = 0
trailer = 0
retriever = 0
excluded = 0
total_outcomes = 0
staff_preference = "y" #initialized to "y", Used to store the user's preference for continuing or quitting.
studentData = {} # Initializing an empty dictionary to store student data


# Keep asking for input until staff preference is "q"
while staff_preference == "y":


        # Ask the user for the student ID
        student_id = input("Enter your student ID: ")


        # Check if the student ID is valid
        if len(student_id) != 8:
            print("Enter a valid ID")
            continue
        if student_id in studentData :
            print("ID already available")
            continue


        # Ask the user for the credit at pass, defer, and fail using the checkInput function
        credit_at_pass = checkInput("What is your credit at pass: ")
        credit_at_defer = checkInput("What is your credit at defer: ")
        credit_at_fail = checkInput("What is your credit at fail: ")
        credit_inputs = [credit_at_pass,credit_at_defer,credit_at_fail]

        
        # Check if the total credit value is incorrect
        if credit_at_pass + credit_at_defer + credit_at_fail != 120:
            print("Total incorrect")
            staff_preference = checkPreference()
            if staff_preference == "q":
                
                break
            
        else:
            
            # Check credit values to determine progression outcome
            total_outcomes += 1
            if credit_at_pass == 120:
                outcome = "Progress"
                print(outcome)
                progress += 1
                
            elif credit_at_pass == 100:
                outcome = "Progress(module trailer)"
                print(outcome)
                trailer += 1
                
            elif credit_at_fail >= 80:
                outcome = "Exclude"
                print(outcome)
                excluded += 1

            else:
                outcome ="Do not Progress–module retriever"
                print(outcome)
                retriever += 1
            credit_inputs.append(outcome)
            studentData[student_id] = credit_inputs

            print("\n")
            staff_preference = checkPreference()
            
            if staff_preference == 'q':

                # Print the final student data as a dictionary
                for key , value in studentData.items():
                    printing_data = str(value[0:3]) #values reps items from progressionValueList
                    printing_data = printing_data.replace("[","")
                    printing_data = printing_data.replace("]","")
                    print(key ,":",value[-1],"-", printing_data) # Print the student ID, progression outcome, and credit values
                break
            
        

    
