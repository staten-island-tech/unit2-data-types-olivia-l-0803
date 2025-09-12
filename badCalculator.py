def factors(n):
    for i in range(1, n + 1):
        if n % i == 0:
            yield i 
        
# the % gives us a remainder. this checks if the remainder is 0 to see if it is a factor
print(list(factors(10)))
print(list(factors(89)))
print(list(factors(57)))

def oddOrEven(x):
    if x % 2 == 0:
        yield "even"
    else:
        yield "odd"

print(list(oddOrEven(10)))
print(list(oddOrEven(8978)))      
print(list(oddOrEven(6887)))  

 
def gcf(x, y):
    for i in range(1, min(x, y) + 1):
        if x % i == 0 and y % i == 0:
            yield i


print(gcf(25, 100))
