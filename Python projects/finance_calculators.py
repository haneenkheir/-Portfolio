import math

# This programme allows the user to access two different financial calculators - an investment calculator and a home loan calculator 

# Display the options and prompt the user for a choice to run the calculator 
while True:
    print("Investment - calculates the amount of interest you'll earn on your investment")
    print("Bond - calculates the amount you'll have to pay on the home loan")

    user_selection = input("Enter either 'investment' or 'bond' from the menu above to proceed:")
    user_selection = user_selection.lower()
    user_selection = user_selection.strip()

    # Variables for investment calculator 
    amount_invested = 0 
    investment_interest_rate = 0 
    investment_years = 0 
    interest = " "

    # Variables for bond calculator 
    house_value = 0 
    bond_interest_rate = 0 
    number_months = 0 

# The investment calculator calculates simple or compound interest, based on the users choice the simple or compound calculation runs to give the user their final amount based on the values entered  
    
    if user_selection == "investment":
        while True:
            try:
                amount_invested = float(input("Enter the amount of money that you are depositing:"))
                investment_interest_rate = float(input("Enter the interest rate (without the % sign):"))
                investment_years = float(input("Enter the number of years you plan on investing:"))
                interest = input("Do you want to calculate simple or compound interest:")
                if interest.lower() not in ["simple", "compound"]:
                    print("Invalid interest type, please enter 'simple' or 'compound'")
                    continue
                break
            except ValueError:
                print("Invalid input. Please enter a valid number.")
             
        if interest.lower() == "simple":
            total_amount_simple = amount_invested * (1 + ((investment_interest_rate / 100) * investment_years))
            print(f"Total amount after simple interest: {total_amount_simple}")
            
        elif interest.lower() == "compound":
            total_amount_compound = amount_invested * math.pow((1 + (investment_interest_rate / 100)), investment_years)
            print(f"Total amount after compound interest: {total_amount_compound}")
            
        
  # This code runs when the user enters 'bond' which then calculates the monthly repayment amount based on the values entered for each variable
                      
    elif user_selection == "bond":
        while True:
            try:
                house_value = float(input("Enter the present value of the house:"))
                bond_interest_rate = float(input("Enter the investment rate:"))
                number_months = float(input("Enter the number of months that you plan to take to repay the bond:"))
                break
            except ValueError:
                print("Invalid input. Please enter a valid number.")
      
        monthly_interest_rate = (bond_interest_rate / 100) / 12
        bond_repayment_amount = (monthly_interest_rate * house_value) / (1 - (1 + monthly_interest_rate) ** (-number_months))
        print(f"Total amount to be repaid each month: {bond_repayment_amount}")

    else:
        print("Sorry, invalid input. Please enter 'investment' or 'bond'.")
        continue 
# This code gives the user an option of restarting the calculator and only shows after successful calculation 


    restart_choice = input("Do you wish to restart the calculator, enter Yes or No?: ")
    if restart_choice.lower() != "yes":
            print ("Exiting the calculator")
            break 