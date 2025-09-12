bill = int(input("How much was your bill? "))
answer = int(input("Please rate your service from 1-10: "))
tip = 0

def calculate_tip(perctenage):
    tip = bill * perctenage
    total = bill + tip
    print("You tipped: ")
    print(tip)
    print("Your total is: ")
    print(total)


if answer < 3:
    print("Lets tip 0%.")
    calculate_tip(0)
elif answer < 5:
    print("Lets tip 10%.")  
    calculate_tip(.1)
elif answer < 7:
    print("Lets tip 15%.")
    calculate_tip(.15)
elif answer < 9:
    print("Lets tip 20%.")
    calculate_tip(.2)
elif answer < 10:
    print("Yay! Lets tip 25%.")
    calculate_tip(.25)
elif answer > 10 or answer <= 0:
    print("I hope you slip on a banana peel and break both your legs.")



