"""Analysis
    1. Set the function.
    1.1 Analyse if the number  is under 100 and multiple of 4; print.
    1.2 Analyse if the number is obove 100 and multiple of 4 and 400; print.
    4. Get the number and run the app.
"""

# -- Solution --

def leap_year(number):
    """ Checking if the number is multiple of 100, 400, and 4. 
        Also checking if the number is not multiple of 100 and 4.
    """    
    if (u_answer == 0):
        print(f"{u_answer} is NOT a leap-year.\n")
    elif ((u_answer % 100 == 0 and u_answer % 400 == 0) 
            or (u_answer % 4 == 0 and u_answer % 100 != 0)):
        print(f"{u_answer} is a leap-year.\n")
    else:
        print(f"{u_answer} is NOT a leap-year.\n")

while True:
    # Getting the number and running the app.
    try:
        u_answer = int(input("Write a number to know if it's leap-year or not: "))
        leap_year(u_answer)
        u_answer = input("Type 'Yes' if you want to try again or 'No' if you want to leave: ")
        if (u_answer.lower() == "yes") or (u_answer.lower() == "y"):
            continue
        else:
            print("Thanks for using our services.")
            break
    except ValueError:
        print("The input wasn't a integer number.\n")