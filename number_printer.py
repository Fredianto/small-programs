def is_prime(n):
    """Check if a number is prime."""
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


numbers = list(range(1, 101))


numbers.reverse()

result = []

for num in numbers:
   
    if is_prime(num):
        continue
    
  
    if num % 15 == 0:  
        result.append("FooBar")
    elif num % 3 == 0: 
        result.append("Foo")
    elif num % 5 == 0:  
        result.append("Bar")
    else:
        result.append(str(num))


print(", ".join(result))
