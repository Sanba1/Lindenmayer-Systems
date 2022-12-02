while True:
    # The options are printed
    print("\n1.Choose the type of Lindenmayer system and the number of iterations\n2.Generate plot\n3.Quit\n")
    temp = input("Enter your option: ")

    try:
        option = int(temp)
    except:
        print("\nInput is not an integer")
        option = 4  #redo
    # The choice made must be an integer, and we give it some conditions thorugh if-statements.
    # Also, there is an if-statement in order to prevent error.
    valid = 0
    if option == 1:

        # Attempt to get a valid number, valid is the condition that there is a valid input
        valid = 0

        # Runs a loop if the question is not fulfilled using the valid varible, in this case, type of Lindermayer system
        while (valid == 0):

            problem = 0
            # Attempt to remember previous choice, if a problem occurs, ignore
            try:
                oldSystem = System
            except:
                problem = 1

            temp = input(
                "\nChoose the type of Lindenmayer system:\n 1.Koch System\n 2.Sierpinski System\nTo cancel, type 'cancel'\n\nEnter your option: ")

            # Added a cancel feature if the user ever chooses to
            if temp == 'cancel':
                valid = 1
                break

            # Filters through different possible cases of answers. If the answer is satisfactory, make valid != 0
            try:
                systemChoice = int(temp)
            except ValueError:
                print("\nPlease enter an integer option.")
                systemChoice = 0

            if systemChoice == 1:
                System = "Koch"
                break
            elif systemChoice == 2:
                System = "Sierpinski"
                break
            else:
                print("Please select between option 1 or 2.")

        # Similar system as the previous question, asking iterations
        while (valid == 0):

            temp = input("\nHow many iterations would you like? (To cancel, type 'cancel'): ")

            # Cancel function will reinput the previous choice, therefore keeping it as a "saved" load
            if temp == 'cancel':
                if problem != 1:
                    System = oldSystem
                valid = 1
                break

            iterprob = 0

            try:
                N = int(temp)
            except ValueError:
                print("\nPlease enter an integer option.")
                iterprob = 1

            # We limited it to this specific range to keep it runnable on a potato if desired
            if iterprob == 0:
                if N <= 0:
                    print("The number of iterations must be positive.")
                elif N > 9:
                    print('\nThe number of iterations is limited to 9, as to prevent excessive runtime.')

            # Prints out the final "load" of the loading data process, prints out what was chosen, the menu screen will reappear
                else:
                    print(
                        f'\nYou have chosen {System} as your Lindenmayer system and chosen {N} iterations.')
                    valid = 1

        # The program will bring up the main menu again, asking the 3 possible options

    # Option 2 is plotting the graph using turtle
    if option == 2:
        valid = 1
        try:
            # At this point, it is shown how every function in the whole program should run, and what inputs should be used for each of them
            turtlePlot(turtleGraph(LindIter(System, N), N))
        except:
            print("\nLindenmayer System not chosen.")

    # Option 3 to end the program
    if option == 3:
        print("\nGoodbye!")
        break
    if valid == 0:
        print("\nPlease select between option 1, 2 or 3.")
