while True:
    # The options are printed
    print("\n1.Choose the type of Lindenmayer system and the number of iterations\n2.Generate plot\n3.Quit\n")
    
    # The input is first put into a temp file to troubleshoot whatever the user inputted. It will check if its an int or random inputs.
    temp = input("Enter your option: ")
    
    # This attempts to check if it is an integer
    try:
        option = int(temp)
    except:
        # We do not want anything that isnt an integer in the main menu
        print("\nInput is not an integer")
        option = 4  # Because it is not an integer, we still have to initialize option, we chose 4 as a random integer that isnt one of the options
        
    
    # Hard cases for each option
    valid = 0
    
    # Option 1 is the system choices and iterations
    if option == 1:

        # We initialize the "failsafe"  where if valid is not 0, a problem has occurred.
        valid = 0

        # Runs a loop if the question is not fulfilled using the valid varible, in this case, type of Lindermayer system
        while (valid == 0):
            
            # Unlike valid, this is a specific case of error that is solved with the variable "problem" to solve if there was no previous load data.
            problem = 0
            # Attempt to remember previous choice, if a problem occurs, ignore oldSystem.
            try:
                oldSystem = System
            except:
                problem = 1
            
            # A temp file to hold whatever the user inputted again.
            temp = input(
                "\nChoose the type of Lindenmayer system:\n 1.Koch System\n 2.Sierpinski System\nTo cancel, type 'cancel'\n\nEnter your option: ")

            # Added a cancel feature if the user ever chooses to.
            if temp == 'cancel':
                valid = 1
                break

            # Filters through different possible cases of answers. If the answer is satisfactory, make valid = 1.
            try:
                systemChoice = int(temp)
            except ValueError:
                print("\nPlease enter an integer option.")
                # Similarly to the "option" variable, we want to make sure it is none of the options because we still need to initialize the variable.
                systemChoice = 0
            
            # Selects the different choices available, 1 for Koch, 2 for Sierpinski
            if systemChoice == 1:
                System = "Koch"
                break
            elif systemChoice == 2:
                System = "Sierpinski"
                break
            else:
                # Either they wrote random gibberish or they did not input 1 or 2
                print("Please select between option 1 or 2.")

        # Similar system as the previous question, but asking iterations
        while (valid == 0):
            
            # Temp file things, still handles errors and makes it idiot proof
            temp = input("\nHow many iterations would you like? (To cancel, type 'cancel'): ")

            # Cancel function will reinput the previous choice, therefore keeping it as a "saved" load
            if temp == 'cancel':
                if problem != 1:
                    
                    # Will input the old input if there was any, defined by problem variable. If problem occurs, skip process 
                    System = oldSystem
                # Valid will return to main menu
                valid = 1
                break
            
            # This is similar to problem, but for iterations
            iterprob = 0

            try:
                N = int(temp)
            except ValueError:
                print("\nPlease enter an integer option.")
                iterprob = 1

            # iterprob will determine if there is an invalid input and will ignore these if statements
            if iterprob == 0:
                if N <= 0:
                    print("The number of iterations must be positive.")
                    
                # We cannot handle these many iterations, even 9 is occassionally too much for some systems. Therefore we limited it to 9.
                elif N > 9:
                    print('\nThe number of iterations is limited to 9 to prevent excessive runtime. Please try again.')

            # Prints out the final "load" of the loading data process, prints out what was chosen, the menu screen will reappear
                else:
                    print(
                        f'\nYou have chosen {System} as your Lindenmayer system and chosen {N} iterations.')
                    #Unlike the other valid, this just brings it back to the main menu safely.
                    valid = 1
    
    # Option 2 is plotting the graph using turtle
    if option == 2:
        valid = 1
        
        # We check if it is possible to make a graph, if not, there were no previous "load" of data.
        try:
            # At this point, it is shown how every function in the whole program should run, and what inputs should be used for each of them
            turtlePlot(turtleGraph(LindIter(System, N), N))
        except:
            print("\nLindenmayer System not chosen.")

    # Option 3 to end the program
    if option == 3:
        print("\nGoodbye!")
        break
    
    # This makes sure that the input is acceptable (1, 2 or 3) and ignores everything else. Valid is to make sure that if option 1 was chosen, it will still print correct statements.
    if valid == 0:
        print("\nPlease select between option 1, 2 or 3.")
