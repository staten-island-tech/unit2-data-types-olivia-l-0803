def factors(n):
    for i in range(1, n + 1):
        if n % i == 0:
            yield i 
        
# the % gives us a remainder. this checks if the remainder is 0 to see if it is a factor
""" print(list(factors(10)))
print(list(factors(89)))
print(list(factors(57))) """

def oddOrEven(x):
    if x % 2 == 0:
        yield "even"
    else:
        yield "odd"

""" print(list(oddOrEven(10)))
print(list(oddOrEven(8978)))      
print(list(oddOrEven(6887)))  

 """

def greatfactor(x, y):
    listFactors = []
    for i in range(1, x + 1):
        if x % 1 == 0 and y % i == 0:
            yield i 
            listFactors.append(i)
    gcf = len(listFactors)
    yield listFactors[gcf - 1]
    

def primey(n):
    factors(n)
    if len(list(factors(n))) == 2:
        print("This is a prime number!")
    else:
        x = list(factors(n))
        print(f"This is not a prime number. The factors are {x}.")

Answer1 = input("Welcome to my calculator! Would you like to find factors, find the greatest common factors, or determine if something is a prime number? ")

if Answer1 == "factors" or "Factors" or "factor" or "Factor":
    num = int(input("What number would you like to find the factors of? "))
    factors(num)
    print(f" The factors are{list(factors(num))}")
elif Answer1 == "greatest common factors" or "Greatest common factors" or "greatest common factor" or "Greatest common factor" or "gcf" or "GCF":
    num1 = int(input("What is the first number? "))
    num2 = int(input("What is the second number? "))
    greatfactor(num1, num2)
    print(f"The greatest common factor is {list(greatfactor(num1, num2))}. ")
elif Answer1 == "prime" or "Prime" or "prime number" or "Prime number":
    num3 = int(input("What number would you like to check? "))
    primey(num3)
