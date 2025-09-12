bill = float(input("How much was your bill? "))
answer = float(input("Please rate your service from 1-10: ")) 
tip = 0

if answer < 3:
    print("Lets tip 0%.")
    tip = bill * 0
    total = bill + tip 
    print("You tipped " + tip + ". Your total is " + total)
elif answer < 5:
    print("Lets tip 10%.")
    tip = bill * .1
    total = bill + tip 
    print("You tipped " + tip + ". Your total is " + total)
elif answer < 7:
    print("Lets tip 15%.")
    tip = bill * .15
    total = bill + tip 
    print("You tipped " + tip + ". Your total is " + total)
elif answer < 9:
    print("Lets tip 20%.")
    tip = bill * 0.2
    total = bill + tip 
    print("You tipped " + tip + ". Your total is " + total)
elif answer < 10:
    print("Yay! Lets tip 25%.")
    tip = bill * .25
    total = bill + tip 
    print("You tipped " + tip + ". Your total is " + total)
elif answer > 10 or answer <= 0:
    print("I hope you slip on a banana peel and break both your legs.")