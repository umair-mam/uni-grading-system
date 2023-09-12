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
            print ("Integer REQUIRED")# if input is not integer, print error message
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
            print("Enter a valid response!")# if input is not valid, print error message
            



# Function to print the histogram
def printHistogram():
        """
            The `printHistogram` function prints the histogram with the outcomes and the corresponding number of outcomes.
        """
        print("-----------------------------------------------------------------")
        print("Histogram")
        print("Progress",progress,":","*"*progress)
        print("Trailer",trailer,":","*"*trailer)      
        print("Retriever",retriever,":","*"*retriever)      
        print("Excluded",excluded,":","*"*excluded)
        print("""
        """)
        print(total_outcomes,"outcomes in total.")      
        print("-----------------------------------------------------------------")



# Function to read and print the file
def readAndPrintFile():
    """
        The `readAndPrintFile` function reads and prints the file. 
    """
    with open("Part 03 Outputs.txt","r") as file:
        output_file = file.read()
        print("\n")
        print("Part 03:")
        print (output_file)

    


# Initializing variables        
progress = 0
trailer = 0
retriever = 0
excluded = 0
total_outcomes = 0
staff_preference = "y" #initialized to "y", Used to store the user's preference for continuing or quitting.
progressionDataList = [] #is an empty list that will be used to store the progression outcomes for each student



# Keep looping until staff enters 'q' to quit
while staff_preference == "y":
        # In each iteration, the `checkInput` function is called to get the user input for credit values.
        credit_at_pass = checkInput("What is your credit at pass: ")
        credit_at_defer = checkInput("What is your credit at defer: ")
        credit_at_fail = checkInput("What is your credit at fail: ")

        progressionValueList = [credit_at_pass, credit_at_defer, credit_at_fail]
        
        # Check if total credit is equal to 120
        if credit_at_pass + credit_at_defer + credit_at_fail != 120:
            print("Total incorrect") # if total credit is not equal to 120, print error message
            staff_preference = checkPreference()# ask staff whether to continue or quit
            if staff_preference == "q":
                printHistogram() # if staff enters 'q', print the histogram and break the loop
                break
            
        else:
            #Check credit values to determine progression outcome
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
                outcome = "Do not Progress–module retriever"
                print(outcome)
                retriever += 1
        
            progressionValueList.append(outcome)
            progressionDataList.append(progressionValueList)
            
            print("\n")
            staff_preference = checkPreference()
            
            if staff_preference == 'q': # If the user decides to quit, the `printHistogram` and `readAndPrintFile` functions are called to print the histogram and the results in the file, respectively.
                printHistogram()
                
                print("Part 02:")
                for oneItem in progressionDataList:
                    values = str(oneItem[0:3]) # The `values` variable is used to store the credit values for each student.
                    values = values.replace("[","")
                    values = values.replace("]","")
                    
                    
                    
                    with open("Part 03 Outputs.txt","w")as file: # Writing the results to file
                    
                        for oneItem in progressionDataList:
                            values = str(oneItem[0:3]) #values reps items from progressionValueList
                            values = values.replace("[","") 
                            values = values.replace("]","")
                            print(oneItem[-1],"-",values)
                            file.write(oneItem[-1])
                            file.write("-")
                            file.write(f"{values}\n")# The progression outcome and credit values are written to the file.
                            
                            
                        file.close() # The file is closed after writing.

                        break

readAndPrintFile()
                    
    

